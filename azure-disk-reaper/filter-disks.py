#!/usr/bin/env python

# File: filter-disks.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Azure Disks from the Relay Interface (in the form of parameters)
#              and filters the Disks that are unattached. It then sets the output
#              variable `disks` to the list of Azure Disks volumes that are unattached. 
# Inputs:
#   - disks - list of Azure Disks 
# Outputs:
#   - disks - list of Azure Disks to be terminated in the subsequent step

import re
import logging

from nebula_sdk import Interface, Dynamic as D

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logging.info('Running step filter-disks')

ni = Interface()

if __name__ == '__main__':
    to_terminate = []

    # Filtering volumes with no attachments
    disks = filter(lambda i: i['disk_state'] == 'Unattached', ni.get(D.disks))
    for disk in disks: 
        try:
            to_terminate.append(disk)
            logging.info('Terminating Azure Disk {0} with no attachments'.format(disk['name']))
        except Exception as e:
            logging.error('Azure Disk {0} not considered for termination because of a processing error: {1}'.format(disk['name'], e))

    if len(to_terminate) == 0:
        logging.warning('No volumes to terminate! Exiting.')
        exit()
    else:    
        ni.outputs.set('disks', to_terminate)
        logging.info('Setting output `disks` to {0}'.format(to_terminate))
    