This workflow uses Terraform to provision an EC2 instance, then it runs a Bolt
plan to configure it.

## Prerequisites

Before you run the workflow, make sure you have access to the following:
- An AWS account that has the privilege to create an EC2 instance and a security group and the ability to read and write to an S3 bucket
- An AWS VPC where u want to deploy your setup
- A SSH key to connect to the EC2 instance (create or upload it to AWS).
- A Repository with a Boltdir that you would like to run on the EC2 instance.

## Run the workflow

1. Add the workflow in Relay
2. Setup unconfigured connections:
    - Click **Setup**
    - On the right sidebar, you will have a list of unconfigured Connections
    - Get your AWS account credentials and configure the `terraform-provider`
      aws connection.
    - Configure the `bolt-ec2-private-key` ssh connection.
    - Configure the `bolt-repo-private-key` ssh connection.
3. Click **Run** and when prompted, fill in any relevant parameters.
