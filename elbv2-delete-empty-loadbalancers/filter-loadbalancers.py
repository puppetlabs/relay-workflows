#!/usr/bin/env python

# File: filter-loadbalancers.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Load Balancers and Target Groups from the Relay Interface (in 
#              the form of parameters) and filters the load balancers that are empty. 
# Inputs:
#   - loadbalancers - list of ELB v2 load balancers
#   - targetgroups - list of target groups 
# Outputs:
#   - loadbalancerARNs - list of empty ELBv2 load balancer ARNs to be deleted

from nebula_sdk import Interface, Dynamic as D

relay = Interface()

loadbalancer_arns = list(map(lambda i: i['LoadBalancerArn'], relay.get(D.loadbalancers)))
targets = relay.get(D.targets)

to_terminate = []
to_keep = []

# Only 1 Load Balancer can be associated per Target Group - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html
for arn in loadbalancer_arns:
    terminate = True 
    for group in relay.get(D.targetgroups):
        if arn in group['LoadBalancerArns'] and len(targets[group['TargetGroupArn']]) != 0:
            terminate = False
            to_keep.append(arn)
    if terminate:
        to_terminate.append(arn)

print("\nLoad Balancers that are NOT empty:\n")
print(*[a for a in to_keep], sep="\n")

print("\nLoad Balancers that are empty:\n")
print(*[a for a in to_terminate], sep="\n")

if len(to_terminate) == 0:
    exit()
else:
    print('\nSetting output `loadbalancerARNs` to list of {} load balancers to terminate'.format(len(to_terminate)))
    relay.outputs.set('loadbalancerARNs', to_terminate)