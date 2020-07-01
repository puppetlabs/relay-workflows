#!/usr/bin/env python

# File: get-http-status.py 
# Description: This example script makes a request to a URL and sets its status
#              a the output. The status can be used in subsequent steps to
#              perform different bits of logic in a workflow. 

from urllib.request import urlopen

from relay_sdk import Interface, Dynamic as D

relay = Interface()

def get_http_status(url):
    try:
      with urlopen(url) as response:
	      return str(response.status)
    except:
      # empty string indicates something bad happened.
      return ""

if __name__ == '__main__':
  url = None
  try:
    url = relay.get(D.url)
  except:
    print('No URL was configured. Exiting.')
    exit(1)

  relay.outputs.set('status', get_http_status(url))