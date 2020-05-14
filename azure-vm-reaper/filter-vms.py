#!/usr/bin/env python

# File: filter-vms.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Azure Virtual Machines from the Relay Interface (in the form of parameters)
#              and filters the VMs that have no tags. It then sets the output variable `resourceIDs` 
#              to the list of Azure Virtual Machines resource IDs that are untagged. 
# Inputs:
#   - virtualMachines - list of Azure Virtual Machines
# Outputs:
#   - resourceIDs - list of Azure Virtual Machine resource IDs to be terminated in the subsequent step

import re

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

if __name__ == '__main__':
    to_terminate = []
    to_keep = []

    # Filtering Azure virtual machines with no tags
    print('Looking for all Virtual Machines with no tags')
    vms = relay.get(D.virtualMachines) # Queries for `virtual_machines` parameter from Relay
    for vm in vms:
        if 'tags' in vm.keys():
            to_keep.append(vm['id'])
            continue
        else:
            try:
                to_terminate.append(vm['id'])
            except Exception as e:
                print('\nAzure Virtual Machine {0} not considered for termination because of a processing error: {1}'.format(vm['name'], e))
    
    print('\nFound {} Virtual machines (with tags) not considered for termination:'.format(len(to_keep)))
    print(*[vm_id for vm_id in to_keep], sep = "\n") 

    if len(to_terminate) == 0:    
        print('\nNo Virtual Machines to terminate! Exiting.')
        exit()
    else:    
        print('\nAdding {} Virtual machines (without tags) to terminate:'.format(len(to_terminate)))
        print(*[vm_id for vm_id in to_terminate], sep = "\n") 
        print('\nSetting output `resourceIDs` to list of {0} virtual machine resource ids to terminate:'.format(len(to_terminate)))
        relay.outputs.set('resourceIDs', to_terminate)
        print(*[vm_id for vm_id in to_terminate], sep = "\n")
