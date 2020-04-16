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

## Automatically running on a schedule

Policy-driven workflows are best run on a recurring schedule. To set up a
schedule trigger for this workflow:

1. Click **Edit** > **Triggers**.
2. Click **Define new trigger** and use the following values:
   - **Trigger type**: Schedule
   - **Trigger integration**: System
   - **Interval**: Intervals follow the [ISO 8601 repeating
     interval](https://en.wikipedia.org/wiki/ISO_8601#Repeating_intervals)
     format. To run this workflow every 5 minutes indefinitely from now on,
     enter: `R/2020-01-01T00:00:00Z/PT5M`. You can configure the interval at the
     end of this string to change the execution frequency.
3. Enter values for the parameter bindings that match your environment.
4. Click **Add trigger**.

Within the next 5 minutes, you should see the workflow run automatically for the
first time.
