This workflow demonstrates the use of the [AWS STS assume role step](https://github.com/relay-integrations/relay-aws-sts/tree/master/steps/aws-sts-step-assume-role). It
assumes an IAM role, then outputs the instances, images, key pairs, and volumes
in that account. 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to assume the privileged IAM role.
- An AWS IAM role with the user as a trusted entity and permissions to list EC2 instances.
- One or more running EC2 instances.

## Run the workflow

Follow these steps to run the workflow:  
1. Add your AWS IAM user credentials as a Connection:  
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
   - **KEY**: `roleARN`  
   - **VALUE**: The ARN of the IAM role to assume (e.g. arn:aws:iam::180094860577:role/EC2)

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
#       roleARN: ""
```

-  Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
-  Configure the following parameter bindings:  
   - Specify the `region` to run in.  
   - Specify the `roleARN` to assume 
-  Click **Save changes**