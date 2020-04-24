#!/usr/bin/env python

# File: filter-loadbalancers.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of Load Balancers from the Relay Interface (in the form of parameters)
#              and finds the ones that don't have any targets under any target groups. It then 
#              sets the output variable `elb_arns` to the list of ELB v2 load balancers ARNs  
#              to be terminated. 
# Inputs:
#   - loadbalancers - list of EBS volumes
#   - targetgroups - dictionary of target groups (values) by ELB name (key)
#   - targets - dictionary of targets (values) by target group (key)
# Outputs:
#   - elb_arns - list of ELB v2 load balancer ARNs to terminate

import re
import logging

from nebula_sdk import Interface, Dynamic as D

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logging.info('Running step filter-loadbalancers')

ni = Interface()

if __name__ == '__main__':
    to_terminate = []

    try:
        elbs = ni.get(D.loadbalancers)
    except: 
        logging.warning('No ELBs found. Exiting')
        exit()
        
    all_target_groups = ni.get(D.targetgroups)
    all_targets = ni.get(D.targets)

    elb_names = [i["LoadBalancerName"] for i in elbs]
    logging.info('Evaluating the following Elastic Load Balancers: {0}'.format(elb_names))

    # Determining whether each ELB has any targets under any target groups.
    for elb in elbs: 
        terminate = True
        target_groups = all_target_groups[ elb['LoadBalancerName'] ]
        logging.info('Evaluating the following Target Groups under {0}'.format(elb['LoadBalancerName']))
        for tg in target_groups: 
            logging.info(tg['TargetGroupName'])
            if len(all_targets[ tg['TargetGroupName'] ]) > 0:
                terminate = False

        # If no targets are found (in any state), adding ELB to the terminate list
        if (terminate):
            to_terminate.append(elb['LoadBalancerArn'])

    logging.info('Adding the following Elastic Load Balancers to terminate: {0}'.format(to_terminate))
    ni.outputs.set('elb_arns', to_terminate)