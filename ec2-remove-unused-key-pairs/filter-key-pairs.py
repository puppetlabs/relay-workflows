#!/usr/bin/env python

# File: filter-key-pairs.py 
# Description: This is an example script that you can author or modify that retrieves 
#              a list of key pairs from the Relay Interface (in the form of parameters)
#              and filters the key pairs that are unused. It then sets the output
#              variable `keypairs` to the list of key pairs that are unused. 
# Inputs:
#   - keyPairs - List of keyPairs to evaluate 
#   - instances - List of instances to compare against
# Outputs:
#   - keyPairNames - list of key pair names

from relay_sdk import Interface, Dynamic as D

relay = Interface()

to_delete = []
to_keep = []

all_keyPairs = list(map(lambda i: i['KeyName'], relay.get(D.keyPairs)))
used_keyPairs = list(map(lambda i: i['KeyName'], relay.get(D.instances)))

for key in all_keyPairs:
    if key in used_keyPairs:
        to_keep.append(key)
    else:
        to_delete.append(key)

print('\nFound {} used key pairs:'.format(len(to_keep)))
print(*[key for key in to_keep], sep = "\n") 

print('\nFound {} unused key pairs:'.format(len(to_delete)))
print(*[key for key in to_delete], sep = "\n") 

print("Setting output `keyPairNames` with list of {} key pairs to delete".format(len(to_delete)))
relay.outputs.set('keyPairNames', to_delete)
