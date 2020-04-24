#!/usr/bin/env python
import re

from nebula_sdk import Interface, Dynamic as D

ni = Interface()

if __name__ == '__main__':
    to_terminate = []

    try:
        elbs = ni.get(D.loadbalancers)
    except: 
        print('No ELBs found. Exiting')
        exit()
        
    all_target_groups = ni.get(D.targetgroups)
    all_targets = ni.get(D.targets)

    if len(elbs) == 0:
        print('No ELBs found! Exiting ...')
        exit

    print('Evaluating the following Elastic Load Balancers: \n')
    elb_names = [i["LoadBalancerName"] for i in elbs]
    print(elb_names)    

    # Determining whether each ELB has any targets under any target groups.
    for elb in elbs: 
        terminate = True
        target_groups = all_target_groups[ elb['LoadBalancerName'] ]
        print('Evaluating the following Target Groups under {0}'.format(elb['LoadBalancerName']))
        for tg in target_groups: 
            print(tg['TargetGroupName'])
            if len(all_targets[ tg['TargetGroupName'] ]) > 0:
                terminate = False

        # If no targets are found (in any state), adding ELB to the terminate list
        if (terminate):
            to_terminate.append(elb['LoadBalancerArn'])

    print('Adding the following Elastic Load Balancers to terminate: {0}'.format(to_terminate))
    ni.outputs.set('elb_arns', to_terminate)