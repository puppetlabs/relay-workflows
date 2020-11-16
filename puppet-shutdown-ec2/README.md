This workflow is an example of responding to changes in a Puppet run. In this example, when a sudoers file change is detected, the workflow will stop the EC2 instance that is running the Puppet agent. 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and stop EC2 instances (if not
  run in dry run mode).
- Puppetserver with the [Relay module](https://forge.puppet.com/puppetlabs/relay) installed. Check out the module for installation instructions.

## Configure the workflow

You may need to update some of the secrets or connection information
in this workflow to run in your environment. 
- Add your AWS credentials for `my-aws-account`
- Add your preferred region under `awsRegion` secret

## Set up the trigger

Follow the instructions in the [Relay module](https://forge.puppet.com/puppetlabs/relay) to set up the trigger. 