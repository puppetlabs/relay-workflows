# Automatically delete EBS volumes without attachments 

This workflow looks at all of the EBS volumes in a given account and region that are unattached. The termination criteria are:

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and delete EBS volumes (if not
  run in dry run mode).
- One or more running EBS volumes that are unattached. 

## Run the workflow

Follow these steps to run the workflow:
1. Add your AWS credentials as secrets:
   1. Click **Edit** > **Secrets**.
   2. Click **Define new secret** and use the following values:
      - **KEY**: `aws.accessKeyID`
      - **VALUE**: Enter your AWS access key id associated with the account
      - **KEY**: `aws.secretAccessKey`
      - **VALUE**: Enter your AWS secret access key associated with the account
2. Click **Run workflow** and wait for the workflow run page to appear.
3. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, volumes that are unattached will immediately be terminated.
