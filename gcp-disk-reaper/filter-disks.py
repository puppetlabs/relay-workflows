#!/usr/bin/env python
from relay_sdk import Interface, Dynamic as D

relay = Interface()

if __name__ == '__main__':
    to_terminate = []
    print('Disk to be terminated')
    disks = relay.get(D.disks)
    for disk in disks:
        if "users" not in disk.keys():
            print(disk.get('name'))
            to_terminate.append(disk)

    print('Found {} disks that are unattached'.format(len(to_terminate)))
    print('Setting output `disks` to list of {} disks to terminate'.format(len(to_terminate)))

    relay.outputs.set('disks', to_terminate)
