#!/usr/bin/env python
import datetime
import re

from nebula_sdk import Interface, Dynamic as D


ni = Interface()

# The `MINUTES_TO_WAIT` global variable is the number of minutes to wait for
# a termination_date label to appear for the GCP instance. Please note that the
# AWS Lambdas are limited to a 5 minute maximum for their total run time.
MINUTES_TO_WAIT = 4

# The Indefinite lifetime constant
INDEFINITE = 'indefinite'

# Tag names (user-configurable)
TERMINATION_DATE_LABEL = ni.get(D.terminationDateTag)
LIFETIME_LABEL = ni.get(D.lifetimeTag)


def get_label(gcp_instance, label_name):
    """
    :param gcp_instance: a description of a GCP instance.
    :param label_name: A string of the key name you are searching for.

    This method returns None if the GCP instance currently has no tags
    or if the label is not found. If the tag is found, it returns the label
    value.
    """
    if gcp_instance['labels'] is None:
        return None

    return gcp_instance['labels'][label_name] if label_name in gcp_instance['labels'] else None

def timenow_with_utc():
    """
    Return a datetime object that includes the tzinfo for utc time.
    """
    time = datetime.datetime.utcnow()
    time = time.replace(tzinfo=datetime.timezone.utc)
    return time


def validate_lifetime_value(lifetime_value):
    """
    :param lifetime_value: A string from your GCP instance.

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


def get_termination_date(gcp_instance, wait_time=MINUTES_TO_WAIT):
    """
    :param gcp_instance: a resource representing an GCP instance
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
    launch_date = get_iso_date(gcp_instance['creationTimestamp'])

    termination_date = get_label(gcp_instance, TERMINATION_DATE_LABEL)
    if termination_date is None:
        lifetime = get_label(gcp_instance, LIFETIME_LABEL)
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

    instances = filter(lambda i: i['status'] == 'RUNNING', ni.get(D.instances))
    for instance in instances:
        try:
            (termination_date, reason) = get_termination_date(instance)
            if termination_date is not None:
                if termination_date < timenow_with_utc():
                    to_terminate.append(instance)
                    print('Terminating GCP instance {0}: {1}'.format(instance['name'], reason))
                else:
                    print('GCP instance {0} will be considered for termination at {1}'.format(instance['name'], termination_date))
            else:
                print('GCP instance {0} not considered for termination: {1}'.format(instance['name'], reason))
        except Exception as e:
            print('GCP instance {0} not considered for termination because of a processing error: {1}'.format(instance['name'], e))

    ni.outputs.set('instances', to_terminate)
