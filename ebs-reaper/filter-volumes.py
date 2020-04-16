#!/usr/bin/env python
import re

from nebula_sdk import Interface, Dynamic as D


ni = Interface()


if __name__ == '__main__':
    to_terminate = []

    volumes = filter(lambda i: len(i['Attachments']) == 0, ni.get(D.volumes))
    for volume in volumes: 
        try:
            to_terminate.append(volume['VolumeId'])
            print('Terminating EBS volume {0}: {1}'.format(volume['VolumeId'], reason]))
        except Exception as e:
            print('EBS volume {0} not considered for termination because of a processing error: {1}'.format(volume['VolumeId'], e))

    ni.outputs.set('volumeIDs', to_terminate)
