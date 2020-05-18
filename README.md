# Relay Workflows  
This repository contains workflows for [Relay](https://relay.sh). Feel free to use these workflows to get started.

| Workflow      | Integrations   | Description  |
| ------------- | ------------- | ------------ |
| [EC2 Reaper](./ec2-reaper) | aws-ec2 | Terminates EC2 instances not in compliance with a tagging policy. |
| [EBS Reaper](./ebs-reaper) | aws-ebs | Deletes EBS volumes that are unattached | 
| [Stop untagged EC2 instances](./ec2-stop-untagged-instances) | aws-ec2 | Stops untagged EC2 instances | 
| [Remediate publicly writeable S3 buckets](./s3-remediate-public-buckets) | aws-s3 | Finds all buckets with public write permissions and marks them `private` | 
| [Azure Disk Reaper](./azure-disk-reaper) | azure-disks | Deletes Azure Disks that are unattached |   
| [Azure VM Reaper](./azure-vm-reaper) | azure-virtual-machines | Deletes Azure Virtual Machines that don't have any tags |   
