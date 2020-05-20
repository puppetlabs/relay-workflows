#!/usr/bin/env python

# File: filter-loadbalancers.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Azure Load Balancers and filters the ones that are empty e.g.
#              no backend configurations. 
# Inputs:
#   - loadBalancers - list of Azure Load Balancers
# Outputs:
#   - resourceIDs - list of Azure Virtual Machine resource IDs to be terminated in the subsequent step

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

to_terminate = []
to_keep = []

lbs = relay.get(D.loadBalancers) # Queries for `virtual_machines` parameter from Relay
for lb in lbs:
    if len(lb['backend_address_pools']) == 0:
        to_terminate.append(lb['id'])
    else:
        to_keep.append(lb['id'])
        continue

print('\nFound {} Load Balancers that are NOT empty:'.format(len(to_keep)))
print(*[i for i in to_keep], sep = "\n") 

print('\nFound {} Load Balancers that are empty:'.format(len(to_terminate)))
print(*[i for i in to_terminate], sep = "\n") 

    
print('\nSetting output `resourceIDs` to list of {0} load balancer resource ids to terminate.'.format(len(to_terminate)))
relay.outputs.set('resourceIDs', to_terminate)
