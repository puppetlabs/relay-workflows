#!/usr/bin/env python

# File: filter-volumes.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Volumes from the Relay Interface (in the form of parameters)
#              and filters the volumes that are unattached. It then sets the output
#              variable `volumeIDs` to the list of EBS volumes that are unattached. 
# Inputs:
#   - volumes - list of EBS volumes 
# Outputs:
#   - volumeids - list of EBS volume ids to be terminated in the subsequent step

from relay_sdk import Interface, Dynamic as D

relay = Interface()

to_terminate = []

# Filtering volumes with no attachments
volumes = filter(lambda i: len(i['Attachments']) == 0, relay.get(D.volumes))
for volume in volumes: 
    try:
        to_terminate.append(volume['VolumeId'])
        print('Terminating EBS volume {0} with no attachments'.format(volume['VolumeId']))
    except Exception as e:
        print('EBS volume {0} not considered for termination because of a processing error: {1}'.format(volume['VolumeId'], e))

if len(to_terminate) == 0:
    print('No volumes to terminate! Exiting.')
    exit()
else:    
    relay.outputs.set('volumeIDs', to_terminate)
    print('Setting output `volumeIDs` to {0}'.format(to_terminate))

