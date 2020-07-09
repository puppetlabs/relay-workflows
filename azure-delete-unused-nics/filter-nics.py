#!/usr/bin/env python

# File: filter-loadbalancers.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Azure Network Interfaces and filters the ones that are unused e.g.
#              no VM configuration. 
# Inputs:
#   - networkInterfaces - list of Azure NICs
# Outputs:
#   - resourceIDs - list of Azure Virtual Machine resource IDs to be terminated in the subsequent step

from relay_sdk import Interface, Dynamic as D

relay = Interface()

to_terminate = []
to_keep = []

nics = relay.get(D.networkInterfaces)
for nic in nics:
    if 'virtual_machine' in nic.keys():
        to_keep.append(nic['id'])
    else:
        to_terminate.append(nic['id'])
        continue

print('\nFound {} Network Interfaces that are used:'.format(len(to_keep)))
print(*[i for i in to_keep], sep = "\n") 

print('\nFound {} Network Interfaces that are NOT used:'.format(len(to_terminate)))
print(*[i for i in to_terminate], sep = "\n") 

    
print('\nSetting output `resourceIDs` to list of {0} network interface resource ids to terminate.'.format(len(to_terminate)))
relay.outputs.set('resourceIDs', to_terminate)
