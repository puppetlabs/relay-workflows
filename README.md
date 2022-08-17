# Relay Workflows

| Category | Workflow      | Description  |
| ---------| --------------| ------------ |
| Cost Optimization | [Terminate EC2 instances without valid lifetime tag](./ec2-reaper) | Terminates EC2 instances not in compliance with a tagging policy: specifying a `lifetime` or `termination_date` tag. |
| Cost Optimization | [Delete unattached EBS volumes](./ebs-reaper) | Deletes EBS volumes that are unattached |
| Cost Optimization | [Delete empty ELBv2 load balancers](./elbv2-delete-empty-loadbalancers) | Deletes empty ELBv2 load balancers |
| Cost Optimization | [DynamoDB capacity monitor](./dynamodb-capacity-monitor) | Monitors DynamoDB provisioned capacity |
| Cost Optimization | [Delete unattached Azure Disks](./azure-disk-reaper) | Deletes Azure Disks that are unattached |
| Cost Optimization | [Delete untagged Azure Virtual Machines](./azure-vm-reaper) | Deletes Azure Virtual Machines that don't have any tags |
| Cost Optimization | [Delete empty Azure Load Balancers](./azure-delete-empty-loadbalancers) | Deletes empty Azure Load Balancers |
| Cost Optimization | [Delete unused Azure Network Interfaces](./azure-delete-unused-nics) | Deletes unused Azure Network Interfaces |
| Cost Optimization | [Delete GCP instances without valid lifetime tag](./gcp-instance-reaper) | Deletes GCP instances not in compliance with a tagging policy: specifying a `lifetime` or `termination_date` tag. |
| Cost Optimization | [Delete unattached GCP disks](./gcp-disk-reaper) | Deletes GCP disks that are unattached |
| Incident Response | [When a Datadog event is received, send a message to Slack](./datadog-to-slack) | Sends a message to Slack when a Datadog event is received|
| Incident Response | [When a Datadog event is received, create a Jira issue](./datadog-to-jira) | Creates a Jira Server issue when a Datadog event is received |
| Incident Response | [Roll back a bad Kubernetes deployment and update a Datadog Incident](./datadog-k8s-rollback) | Rolls back a specified Kubernetes deployment and updates a Datadog Incident Management timeline |
| Incident Response | [Roll back a bad Kubernetes deployment and update a FireHydrant Incident](./firehydrant-rollback) | Rolls back a specified Kubernetes deployment and updates a FireHydrant Incident Management timeline |
| Incident Response | [When a PagerDuty incident is triggered, send a message to Slack](./pagerduty-to-slack) | Sends a message to Slack when a PagerDuty incident is triggered based on incident severity|
| Incident Response | [When a PagerDuty incident is triggered, create a Jira ticket](./pagerduty-to-jira) | Creates a Jira Server issue when a PagerDuty incident is triggered |
| Incident Response | [When a PagerDuty incident is triggered, send an SMS via Twilio](./pagerduty-to-twilio) | Deliver a custom notification via SMS when a PagerDuty incident is triggered |
| Incident Response | [When a Splunk On-Call incident is created, coordinate tickets and Slack response](./splunkoncall-incident-response) | Create a Jira ticket, Slack room, and update Splunk On-Call incident timeline |
| Security | [Stop untagged EC2 instances](./ec2-stop-untagged-instances) | Stops untagged EC2 instances |
| Security | [Assume role and stop untagged EC2 instances](./sts-stop-untagged-instances) | Stops untagged EC2 instances by first assuming an IAM role with EC2 permissions |
| Security | [Restrict public WRITE S3 buckets](./s3-restrict-public-write-buckets) | Finds all buckets with public 'WRITE' permissions and marks them `private` |
| Security | [Restrict public READ S3 buckets](./s3-restrict-public-read-buckets) | Finds all buckets with public 'READ' permissions and marks them `private` |
| Security | [Restrict public WRITE_ACP S3 buckets](./s3-restrict-public-write_acp-buckets) | Finds all buckets with public 'WRITE_ACP' permissions and marks them `private` |
| Security | [Restrict public READ_ACP S3 buckets](./s3-restrict-public-read_acp-buckets) | Finds all buckets with public 'READ_ACP' permissions and marks them `private` |
| Security | [Restrict S3 buckets with READ access to all Authenticated Users](./s3-restrict-authenticated_user-read-buckets) | Finds all buckets with 'READ' permissions to all Authenticated Users and marks them `private` |
| Security | [Restrict S3 buckets with WRITE access to all Authenticated Users](./s3-restrict-authenticated_user-write-buckets) | Finds all buckets with 'WRITE' permissions to all Authenticated Users and marks them `private` |
| Security | [Restrict S3 buckets with READ_ACP access to all Authenticated Users](./s3-restrict-authenticated_user-read_acp-buckets) | Finds all buckets with 'READ_ACP' permissions to all Authenticated Users and marks them `private` |
| Security | [Restrict S3 buckets with WRITE_ACP access to all Authenticated Users](./s3-restrict-authenticated_user-write_acp-buckets) | Finds all buckets with 'WRITE_ACP' permissions to all Authenticated Users and marks them `private` |
| Security | [Remediate unencrypted S3 buckets](./s3-remediate-unencrypted-buckets) | Finds all unencrypted S3 buckets and encrypts them with default encryption |
| Security | [Remove unused EC2 key pairs](./ec2-remove-unused-key-pairs) | Finds all unused EC2 key pairs and deletes them |
| Operations | [Assume role and describe EC2 objects](./sts-describe-ec2-objects) | Assumes IAM role and describes the EC2 instances, images, key pairs, and volumes in the account |
| Operations | [Update other workflows on PR commit](./update-workflow-on-merge) | Enables GitOps for Relay by updating workflows stored on the service when a pull request gets merged |
| Continuous Delivery | [Run Terraform when Pull Request merged in GitHub](./terraform-continuous-deployment) | Apply a Terraform configuration when a Pull Request is merged to a repository in GitHub. |
| Continuous Delivery | [Update Kubernetes deployment image tag on Docker Hub push](./kubectl-apply-on-dockerhub-push) | Updates a deployment image using a Docker Hub webhook to inform relay when a new Docker image is available |
| Continuous Delivery | [Provision an EC2 instance and configure with a Bolt plan](./ec2-provision-and-configure-with-bolt) | Uses terraform to create and provision a new EC2 instance, then uses a remote Bolt plan to configure it |
| Operations | [Restart EC2 instance on http health check](./http-health-check) | Restarts an EC2 instance your choosing when a HTTP health check does not return 200 status |
| Configuration | [Stop EC2 instance when sudoers file is changed with Puppet](./puppet-shutdown-ec2) | Listens for a sudoers file change on a Puppet run and shuts down the EC2 instance in response |
| Configuration | [Emit Puppet run data](./puppet-run-emit-data) | Demonstrates data emitted by Puppet run |
| Configuration | [Selectively enforce Puppet run](./puppet-selective-enforcement) | Selectively enforce Puppet run when corrective changes happen |
