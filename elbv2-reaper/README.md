# Automatically delete ELB v2 load balancers with no targets  

This workflow looks at all of the ELB v2 load balancers in an account and region that have no targets. 
If no targets are found, ELB v2 will be terminated based on a manual approval. 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and delete ELB v2 load balancers.
- One or more running ELB v2 load balancers that have no targets. 

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
   `false`, load balancers with no targets will immediately be terminated.