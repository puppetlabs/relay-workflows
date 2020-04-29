#!/usr/bin/env python

# File: filter-vms.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Azure Virtual Machines from the Relay Interface (in the form of parameters)
#              and filters the VMs that have no tags. It then sets the output
#              variable `vms` to the list of Azure Virtual Machines that are untagged. 
# Inputs:
#   - virtual_machines - list of Azure Virtual Machines
# Outputs:
#   - virtual_machines - list of Azure Virtual Machines to be terminated in the subsequent step

import re

from nebula_sdk import Interface, Dynamic as D

ni = Interface()

if __name__ == '__main__':
    to_terminate = []
    to_keep = []

    # Filtering Azure virtual machines with no tags
    print('Looking for all Virtual Machines with no tags')
    vms = ni.get(D.virtual_machines)
    for vm in vms:
        if 'tags' in vm.keys():
            to_keep.append(vm)
            continue
        else:
            try:
                to_terminate.append(vm)
            except Exception as e:
                print('\nAzure Virtual Machine {0} not considered for termination because of a processing error: {1}'.format(vm['name'], e))
    
    print ('\nFound {} Virtual machines (with tags) not considered for termination:'.format(len(to_keep)))
    print(*[vm['name'] for vm in to_keep], sep = "\n") 

    if len(to_terminate) == 0:    
        print('\nNo Virtual Machines to terminate! Exiting.')
        exit()
    else:    
        print('\nAdding {} Virtual machines (without tags) to terminate:'.format(len(to_terminate)))
        print(*[vm['name'] for vm in to_terminate], sep = "\n") 
        print('\nSetting output `virtual_machines` to list of {0} virtual machines'.format(len(to_terminate)))
        ni.outputs.set('virtual_machines', to_terminate)
    
