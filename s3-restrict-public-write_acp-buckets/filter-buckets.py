#!/usr/bin/env python
import datetime
import re

from nebula_sdk import Interface, Dynamic as D


relay = Interface()

to_modify = []
to_do_nothing = []

bucketACLs = relay.get(D.bucketACLs)

for bucketName in bucketACLs.keys():
    public_bucket = False

    # If the URI of the grant is "http://acs/amazonaws.com/groups/global/AllUsers" and the permission contains "WRITE_ACP", adding to list to remediate.
    for grant in bucketACLs[bucketName]:
        if grant['Grantee']['Type'] == "Group" and grant['Grantee']['URI'] == "http://acs.amazonaws.com/groups/global/AllUsers" and "WRITE_ACP" in str(grant['Permission']):
            public_bucket = True
        else:
            continue
                
    if public_bucket:
        to_modify.append(bucketName)
    else:
        to_do_nothing.append(bucketName)

print("\nFound {} bucket(s) that DON'T have public WRITE_ACP permissions:".format(len(to_do_nothing)))
print(*[bucket for bucket in to_do_nothing], sep = "\n")

print("\nFound {} bucket(s) that have public WRITE_ACP permissions:".format(len(to_modify)))
print(*[bucket for bucket in to_modify], sep = "\n")

print('\nSetting output variable `buckets` with list of {} bucket(s) with public WRITE_ACP permissions.'.format(len(to_modify)))
relay.outputs.set('buckets', to_modify)
