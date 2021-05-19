This workflow finds empty ELBv2 load balancers by locating all load balancers that have
empty target groups (i.e. no registered targets). 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and delete ELBv2 load balancers (if not
  run in dry run mode).
- One or more ELBv2 load balancers that are empty (no targets). 

## Run the workflow

Follow these steps to run the workflow:  
1. Add your AWS credentials as a Connection:  
   - Click **Setup**  
   - Find the Connection named `my-aws-account` and click Edit(✎). Use the following values:  
      - **KEY**: `ACCESS KEY ID`  
      - **VALUE**: Enter your AWS access key id associated with the account  
      - **KEY**: `SECRET ACCESS KEY`  
      - **VALUE**: Enter your AWS secret access key associated with the account  
   - Click **Save**  
      
2. Click **Run workflow** and wait for the workflow run page to appear.  
3. Supply following parameters to the modal:  
   - **KEY**: `region`  
   - **VALUE**: The AWS region to run in  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you dont want to actually delete the resources. Use this to test the workflow and ensure it is behaving as expected.  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, load balancers that are empty will immediately be deleted.

## Run the workflow on a schedule  

Follow these steps to run this workflow on a schedule:  
-  Un-comment out the Trigger block in the workflow file:  

> TIP: If you're using the Relay code editor, highlight the `triggers` section and type `⌘ + /` (Mac) or `Ctrl + /` (Windows) to uncomment.  

```yaml
# triggers:
# - name: schedule
#   source:
#     type: schedule
#     schedule: '0 * * * *'
#   binding:
#     parameters:
#       region: us-east-1
#       dryRun: true
```

-  Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
-  Configure the following parameter bindings:  
   - Specify the `region` to run in.  
   - Specify whether `dryRun` should be set to `true` or `false`.  
-  Click **Save changes**