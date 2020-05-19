#!/usr/bin/env python

# File: filter-loadbalancers.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Load Balancers and Target Groups from the Relay Interface (in 
#              the form of parameters) and filters the volumes that are unattached. It 
#              then sets the output variable `loadbalancers` to the list of ELB v2 load 
#              balancers that are empty. 
# Inputs:
#   - loadbalancers - list of ELB v2 load balancers
#   - targetgroups - list of target groups 
# Outputs:
#   - loadbalancerARNs - list of empty ELBv2 load balancer ARNs to be deleted

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

loadbalancer_arns = list(map(lambda i: i['LoadBalancerArn'], relay.get(D.loadbalancers)))

for group in relay.get(D.targetgroups):
    for arn in group['LoadBalancerArns']:
        try:
            loadbalancer_arns.remove(arn)
        except:
            pass

if len(loadbalancer_arns) == 0:
    print('No empty load balancers! Exiting.')
    exit()
else:
    print('Setting output `loadbalancerARNs` to list of {} load balancers to terminate'.format(len(loadbalancer_arns)))
    relay.outputs.set('loadbalancerARNs', loadbalancer_arns)
    
