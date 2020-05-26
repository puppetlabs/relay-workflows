This workflow looks at all of the EC2 instances in a given account and region and stops the ones that are untagged. 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and terminate EC2 instances (if not
  run in dry run mode).
- One or more running EC2 instances that are untagged.

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
   - **VALUE**: True if you don't want to perform actual WRITE operations  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, instances not in compliance with this workflow policy will
   immediately be stopped.  

## Run the workflow on a schedule  

Follow these steps to run this workflow on a schedule:  
1. Uncomment out the Trigger block in the workflow file:  

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

2. Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
3. Configure the following parameter bindings:  
   - Specify the `region` to run in.  
   - Specify whether `dryRun` should be set to `true` or `false`.  
4. Click "Save changes"