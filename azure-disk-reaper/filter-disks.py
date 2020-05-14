#!/usr/bin/env python

# File: filter-disks.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Azure Disks from the Relay Interface (in the form of parameters)
#              and filters the Disks that are unattached. It then sets the output
#              variable `resource_ids` to the list of Azure Disks volumes that are unattached. 
# Inputs:
#   - disks - list of Azure Disks 
# Outputs:
#   - resourceIDs - list of Azure Disk resource IDs to be terminated in the subsequent step

import re
import logging

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

if __name__ == '__main__':
    to_terminate = []

    # Filtering volumes with no attachments
    disks = filter(lambda i: i['disk_state'] == 'Unattached', relay.get(D.disks))
    for disk in disks: 
        try:
            to_terminate.append(disk['id'])
            print('Adding Azure Disk {0} with no attachments to termination list'.format(disk['name']))
        except Exception as e:
            print('Azure Disk {0} not considered for termination because of a processing error: {1}'.format(disk['name'], e))

    # Adding list of Azure Disk resource ids to output `resource_ids`
    if len(to_terminate) == 0:
        print('No Disks to terminate! Exiting.')
        exit()
    else:
        print('Setting output `resourceIDs` to list of {0} disks'.format(len(to_terminate)))    
        relay.outputs.set('resourceIDs', to_terminate)
    
