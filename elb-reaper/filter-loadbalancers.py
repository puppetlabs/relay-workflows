#!/usr/bin/env python
import re

from nebula_sdk import Interface, Dynamic as D

ni = Interface()


if __name__ == '__main__':
    # For each load balancer => Get target groups => Get targets under target group 
    to_terminate = []

    elbs = ni.get(D.loadbalancers)
    target_groups = ni.get(D.targetgroups)
    target = ni.get(D.targets)

    if len(elbs) == 0:
        print('No ELBs found! Exiting ...')
        exit

    print('Evaluating the following Elastic Load Balancers: \n')
    # elb_arns = [i["LoadBalancerArn"] for i in elbs]
    # print(elb_arns)
    elb_names = [i["LoadBalancerName"] for i in elbs]
    print(elb_names)    

    for elb in elbs: 
        terminate = True
        elb_target_groups = target_groups[ elb['LoadBalancerName'] ]
        print('Evaluating the following Target Groups under {0}'.format(elb['LoadBalancerName']))
        print(elb_target_groups)
    #     target_group_arns = [i['TargetGroupArn'] for i in target_groups['TargetGroups']]
    #     print('For {1}, found the following target groups:\n {0}'.format(target_group_arns, arn))

    #     # Get targets within target group 
    #     for g in target_group_arns: 
    #         targets = elbv2.describe_target_health(TargetGroupArn=g)

    #         # If any targets found, don't terminate ELB 
    #         if len(targets['TargetHealthDescriptions'])>0:
    #             terminate = False
            
    #     if (terminate): 
    #         to_terminate.append(arn)

    # ni.outputs.set('elb_arns',to_terminate)