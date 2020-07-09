#!/usr/bin/env python

# File: filter-instances.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Instances from the Relay Interface (in the form of parameters)
#              and filters the instances that don't have a valid `lifetime` or `termination_date`
#              tag. It then sets the output variable `instanceIDs` to the list of instances to
#              terminate. 
# Inputs:
#   - terminationDateTag - user configurable tag indicating when instance should be terminated
#   - lifetimeTag - user configurable tag indicating how long instance should live
#   - instances - list of instances to filter
# Outputs:
#   - instanceIDs - list of instances to be terminated in the subsequent step

import datetime
import re

from relay_sdk import Interface, Dynamic as D


relay = Interface()

# The `MINUTES_TO_WAIT` global variable is the number of minutes to wait for
# a termination_date tag to appear for the EC2 instance. Please note that the
# AWS Lambdas are limited to a 5 minute maximum for their total run time.
MINUTES_TO_WAIT = 4

# The Indefinite lifetime constant
INDEFINITE = 'indefinite'

# Tag names (user-configurable)
TERMINATION_DATE_TAG = relay.get(D.terminationDateTag)
LIFETIME_TAG = relay.get(D.lifetimeTag)


def get_tag(ec2_instance, tag_name):
    """
    :param ec2_instance: a boto3 resource representing an Amazon EC2 Instance.
    :param tag_name: A string of the key name you are searching for.

    This method returns None if the ec2 instance currently has no tags
    or if the tag is not found. If the tag is found, it returns the tag
    value.
    """
    if ec2_instance['Tags'] is None:
        return None
    for tag in ec2_instance['Tags']:
        if tag['Key'] == tag_name:
            return tag['Value']
    return None


def timenow_with_utc():
    """
    Return a datetime object that includes the tzinfo for utc time.
    """
    time = datetime.datetime.utcnow()
    time = time.replace(tzinfo=datetime.timezone.utc)
    return time


def validate_lifetime_value(lifetime_value):
    """
    :param lifetime_value: A string from your ec2 instance.

    Return a match object if a match is found; otherwise, return the None from
    the search method.
    """
    search_result = re.search(r'^([0-9]+)(w|d|h|m)$', lifetime_value)
    if search_result is None:
        return None
    toople = search_result.groups()
    unit = toople[1]
    length = int(toople[0])
    return (length, unit)


def calculate_lifetime_delta(lifetime_tuple):
    """
    :param lifetime_match: Resulting regex match object from validate_lifetime_value.
    Check the value of the lifetime. If not indefinite convert the regex match from
    `validate_lifetime_value` into a datetime.timedelta.
    """
    length = lifetime_tuple[0]
    unit = lifetime_tuple[1]
    if unit == 'w':
        return datetime.timedelta(weeks=length)
    elif unit == 'h':
        return datetime.timedelta(hours=length)
    elif unit == 'd':
        return datetime.timedelta(days=length)
    elif unit == 'm':
        return datetime.timedelta(minutes=length)
    else:
        raise ValueError("Unable to parse the unit '{0}'".format(unit))


def get_iso_date(data):
    try:
        return datetime.datetime.strptime(data, r'%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        return datetime.datetime.strptime(data, r'%Y-%m-%dT%H:%M:%S%z')


def get_termination_date(ec2_instance, wait_time=MINUTES_TO_WAIT):
    """
    :param ec2_instance: a boto3 resource representing an Amazon EC2 Instance
    :param wait_time: The number of minutes to wait for the 'termination_date'

    This method returns when a 'termination_date' is found and raises an
    exception and terminates the instance when the wait_time has passed. The
    method looks for the 'lifetime' key, parses it, and sets the
    'termination_date' on the instance. The 'termination_date' can be set
    directly on the instance, bypassing the steps to parse the lifetime key and
    allowing this to return. This returns the termination_date value and reason
    if action should be taken at a given time; otherwise, it returns None (e.g.,
    for unlimited lifetimes or no tags available yet).
    """
    launch_date = get_iso_date(ec2_instance['LaunchTime'])

    termination_date = get_tag(ec2_instance, TERMINATION_DATE_TAG)
    if termination_date is None:
        lifetime = get_tag(ec2_instance, LIFETIME_TAG)
        if lifetime is None:
            if launch_date + datetime.timedelta(minutes=wait_time) > timenow_with_utc():
                # Timed out waiting for a tag, so go ahead and kill this instance.
                return (launch_date, 'Timed out waiting for tag')
            return (None, 'Waiting for tags to propagate')
        elif lifetime == INDEFINITE:
            return (None, 'Indefinite lifetime')
        else:
            lifetime_match = validate_lifetime_value(lifetime)
            if not lifetime_match:
                return (launch_date, 'Invalid lifetime tag value')

            try:
                lifetime_delta = calculate_lifetime_delta(lifetime_match)
                return (launch_date + lifetime_delta, 'Scheduled for termination')
            except ValueError as e:
                return (launch_date, 'Invalid lifetime tag value: {0}'.format(e))
    elif termination_date == INDEFINITE:
        return (None, 'Indefinite lifetime')
    else:
        return (get_iso_date(termination_date), 'Scheduled for termination')


if __name__ == '__main__':
    to_terminate = []
    
    raw_instances = None
    try:
        raw_instances = relay.get(D.instances)
    except:
        print('No instances found. Exiting.')
        exit(1)

    instances = filter(lambda i: i['State']['Name'] == 'running', raw_instances)
    for instance in instances:
        try:
            (termination_date, reason) = get_termination_date(instance)
            if termination_date is not None:
                if termination_date < timenow_with_utc():
                    to_terminate.append(instance['InstanceId'])
                    print('Terminating EC2 instance {0}: {1}'.format(instance['InstanceId'], reason))
                else:
                    print('EC2 instance {0} will be considered for termination at {1}'.format(instance['InstanceId'], termination_date))
            else:
                print('EC2 instance {0} not considered for termination: {1}'.format(instance['InstanceId'], reason))
        except Exception as e:
            print('EC2 instance {0} not considered for termination because of a processing error: {1}'.format(instance['InstanceId'], e))

    relay.outputs.set('instanceIDs', to_terminate)
