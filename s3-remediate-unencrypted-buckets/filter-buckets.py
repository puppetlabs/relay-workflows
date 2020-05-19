#!/usr/bin/env python
from nebula_sdk import Interface, Dynamic as D


relay = Interface()

to_modify = []
to_do_nothing = []

encryptionConfigurations = relay.get(D.encryptionConfigurations)

for bucket in encryptionConfigurations.keys():
    # If the encryption configuration of a bucket is none, bucket is unencrypted. Adding these to list of buckets to encrypt. 
    if encryptionConfigurations[bucket] == None:
        to_modify.append(bucket)
    else:
        to_do_nothing.append(bucket)

print("\nFound {} bucket(s) that are encrypted:".format(len(to_do_nothing)))
print(*[bucket for bucket in to_do_nothing], sep = "\n")

print("\nFound {} bucket(s) that are NOT encrypted:".format(len(to_modify)))
print(*[bucket for bucket in to_modify], sep = "\n")

print('\nSetting output variable `buckets` with list of {} bucket(s) that are NOT encrypted.'.format(len(to_modify)))
relay.outputs.set('buckets', to_modify)
