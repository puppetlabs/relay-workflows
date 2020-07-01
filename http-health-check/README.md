This workflow checks the status of an http endpoint. If the
endpoint does not return a 200, then it restarts an EC2 
instance. 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to restart EC2 instances (if not
  run in dry run mode).
- One or more running EC2 instances running a HTTP service.

## Run the workflow manually

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
   - **KEY**: `instanceID`  
   - **VALUE**: The EC2 instance to restart in response to health check  
   - **KEY**: `url`  
   - **VALUE**: The URL to make a health check against.  

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
#       instanceID: i-1498314
#       url: 'https://relay.sh'
```

-  Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
-  Configure the following parameter bindings:  
   - Specify the `instanceID` to restart.  
   - Specify the `url` of the http service to check.  
-  Click **Save changes**