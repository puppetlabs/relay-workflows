#!/usr/bin/env python
import re

from nebula_sdk import Interface, Dynamic as D
import boto3

ni = Interface()

sess = boto3.Session(
  aws_access_key_id=ni.get(D.aws.accessKeyID),
  aws_secret_access_key=ni.get(D.aws.secretAccessKey),
  region_name=ni.get(D.aws.region),
)

elbv2 = sess.client('elbv2')

if __name__ == '__main__':
    # For each load balancer => Get target groups => Get targets under target group 
    to_terminate = []

    elb_arns = [i["LoadBalancerArn"] for i in ni.get(D.elbs)]

    if len(elb_arns) == 0:
        print('No ELBs found! Exiting ...')
        exit

    print('Found the following Elastic Load Balancers: \n')
    print(elb_arns)

    for arn in elb_arns: 
        terminate = True
        target_groups = elbv2.describe_target_groups(LoadBalancerArn=arn)
        target_group_arns = [i['TargetGroupArn'] for i in target_groups['TargetGroups']]
        print('For {1}, found the following target groups:\n {0}'.format(target_group_arns, arn))

        # Get targets within target group 
        for g in target_group_arns: 
            targets = elbv2.describe_target_health(TargetGroupArn=g)

            # If any targets found, don't terminate ELB 
            if len(targets['TargetHealthDescriptions'])>0:
                terminate = False
            
        if (terminate): 
            to_terminate.append(arn)

    ni.outputs.set('elb_arns',to_terminate)