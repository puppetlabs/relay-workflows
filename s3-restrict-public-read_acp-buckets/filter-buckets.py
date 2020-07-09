#!/usr/bin/env python
from relay_sdk import Interface, Dynamic as D


relay = Interface()

to_modify = []
to_do_nothing = []

bucketACLs = relay.get(D.bucketACLs)

for bucketName in bucketACLs.keys():
    public_bucket = False

    # If the URI of the grant is "http://acs/amazonaws.com/groups/global/AllUsers" and the permission contains "READ_ACP", adding to list to remediate.
    for grant in bucketACLs[bucketName]:
        if grant['Grantee']['Type'] == "Group" and grant['Grantee']['URI'] == "http://acs.amazonaws.com/groups/global/AllUsers" and "READ_ACP" in str(grant['Permission']):
            public_bucket = True
        else:
            continue
                
    if public_bucket:
        to_modify.append(bucketName)
    else:
        to_do_nothing.append(bucketName)

print("\nFound {} bucket(s) that DON'T have public READ_ACP permissions:".format(len(to_do_nothing)))
print(*[bucket for bucket in to_do_nothing], sep = "\n")

print("\nFound {} bucket(s) that have public READ_ACP permissions:".format(len(to_modify)))
print(*[bucket for bucket in to_modify], sep = "\n")

print('\nSetting output variable `buckets` with list of {} bucket(s) with public READ_ACP permissions.'.format(len(to_modify)))
relay.outputs.set('buckets', to_modify)
