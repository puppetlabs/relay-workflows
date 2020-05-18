# Relay Workflows  
This repository contains workflows for [Relay](https://relay.sh). Feel free to use these workflows to get started.

| Workflow      | Integrations   | Description  |
| ------------- | ------------- | ------------ |
| [EC2 Reaper](./ec2-reaper) | aws-ec2 | Terminates EC2 instances not in compliance with a tagging policy. |
| [EBS Reaper](./ebs-reaper) | aws-ebs | Deletes EBS volumes that are unattached | 
| [Stop untagged EC2 instances](./ec2-stop-untagged-instances) | aws-ec2 | Stops untagged EC2 instances | 
| [Restrict publicly WRITE S3 buckets](./s3-restrict-public-write-buckets) | aws-s3 | Finds all buckets with public 'WRITE' permissions and marks them `private` | 
| [Restrict publicly READ S3 buckets](./s3-restrict-public-read-buckets) | aws-s3 | Finds all buckets with public 'READ' permissions and marks them `private` | 
| [Restrict publicly WRITE_ACP S3 buckets](./s3-restrict-public-write_acp-buckets) | aws-s3 | Finds all buckets with public 'WRITE_ACP' permissions and marks them `private` | 
| [Restrict publicly READ_ACP S3 buckets](./s3-restrict-public-read_acp-buckets) | aws-s3 | Finds all buckets with public 'READ_ACP' permissions and marks them `private` | 
| [Restrict S3 buckets with READ access to all Authenticated Users](./s3-restrict-authenticated_user-read-buckets) | aws-s3 | Finds all buckets with 'READ' permissions to all Authenticated Users and marks them `private` | 
| [Restrict S3 buckets with WRITE access to all Authenticated Users](./s3-restrict-authenticated_user-write-buckets) | aws-s3 | Finds all buckets with 'WRITE' permissions to all Authenticated Users and marks them `private` | 
| [Restrict S3 buckets with READ_ACP access to all Authenticated Users](./s3-restrict-authenticated_user-read_acp-buckets) | aws-s3 | Finds all buckets with 'READ_ACP' permissions to all Authenticated Users and marks them `private` | 
| [Restrict S3 buckets with WRITE_ACP access to all Authenticated Users](./s3-restrict-authenticated_user-write_acp-buckets) | aws-s3 | Finds all buckets with 'WRITE_ACP' permissions to all Authenticated Users and marks them `private` | 
| [Azure Disk Reaper](./azure-disk-reaper) | azure-disks | Deletes Azure Disks that are unattached |   
| [Azure VM Reaper](./azure-vm-reaper) | azure-virtual-machines | Deletes Azure Virtual Machines that don't have any tags |   
