#!/usr/bin/env python

# File: filter-key-pairs.py
# Description: This is an example script that you can author or modify that retrieves
#              a list of key pairs from the Relay Interface (in the form of parameters)
#              and filters the key pairs that are unused. It sets the output
#              variable `keypairs` to the list of key pairs that are unused,
#              and the output variable `formatted` to a human-readable representation.
# Inputs:
#   - keyPairs - List of keyPairs to evaluate
#   - instances - List of instances to compare against
# Outputs:
#   - keyPairNames - list of key pair names
#   - formatted - nicely formatted output for use in notifications or messages

from relay_sdk import Interface, Dynamic as D

relay = Interface()

to_delete = []
to_keep = []

keyPairs = relay.get(D.keyPairs)
instances = relay.get(D.instances)
formatted = "Results of keypair filter:\n"

err = 0

if not keyPairs:
    formatted += 'No keypairs found.\n'
    err = 1
if not instances:
    formatted += 'No instances found.\n'
    err = 1

if err == 0:
    all_keyPairs = list(map(lambda i: i['KeyName'], relay.get(D.keyPairs)))
    used_keyPairs = list(map(lambda i: i['KeyName'], relay.get(D.instances)))

    for key in all_keyPairs:
        if key in used_keyPairs:
            to_keep.append(key)
        else:
            to_delete.append(key)

    formatted += '\nFound {} used key pairs:'.format(len(to_keep))
    for key in to_keep:
        formatted += key + "\n"

    formatted += '\nFound {} unused key pairs:'.format(len(to_delete))
    for key in to_delete:
        formatted += key + "\n"

    print("Setting output `keyPairNames` with list of {} unused keypairs".format(len(to_delete)))
    relay.outputs.set('keyPairNames', to_delete)

print(formatted)
relay.outputs.set('formatted',formatted)