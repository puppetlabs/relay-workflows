#!/usr/bin/env python
import datetime
import re

from nebula_sdk import Interface, Dynamic as D


relay = Interface()


bucketACLs = relay.get(D.bucketACLs)
for bucketACL in bucketACLs:
    print ("The bucket acl is {}".format(bucketACL))

# for instance in instances:
#     try:
#         if instance['Tags'] is None: 
#             to_stop.append(instance['InstanceId'])
#         else:
#             to_keep.append(instance['InstanceId'])
#     except Exception as e:
#             print('\nEC2 instance {0} not considered for termination because of a processing error: {1}'.format(instance['InstanceId'], e))

# print('\nFound {} instances (with tags) to keep:'.format(len(to_keep)))
# print(*[instance_id for instance_id in to_keep], sep = "\n") 

# print('\nFound {} instances without tags to stop:'.format(len(to_stop)))
# print(*[instance_id for instance_id in to_stop], sep = "\n") 

# relay.outputs.set('instanceIDs', to_stop)