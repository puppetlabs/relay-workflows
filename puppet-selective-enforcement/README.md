# Selectively enforce Puppet Runs 

This workflow listens for a noop Puppet run and selectively enforces runs when corrective changes are found. 

## Prerequisites
Before you run this workflow, you will need the following:
- Puppetserver with the [Relay module](https://forge.puppet.com/puppetlabs/relay) installed. Check out the module for installation instructions.

## Set up the trigger
Follow the instructions in the [Relay module](https://forge.puppet.com/puppetlabs/relay) to set up the trigger. 