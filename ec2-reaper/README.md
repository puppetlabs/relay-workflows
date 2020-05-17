This workflow looks at all of the EC2 instances in a given account and region and selects a subset of those to terminate. The termination criteria are:

* Not tagged with a termination date or lifetime after 4 minutes
* The `termination_date` or `lifetime` tags are present but cannot be parsed
* The `termination_date` or `lifetime` tags indicate that the instance has
  expired

An instance may be configured to never terminate if its `lifetime` tag has the
special value `indefinite`.

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and terminate EC2 instances (if not
  run in dry run mode).
- One or more running EC2 instances that are configured to use the
  `termination_date` or `lifetime` tags.

## Run the workflow

Follow these steps to run the workflow:
1. Add your AWS credentials as a Connection:  
   1. Click **Setup**  
   2. Find the Connection named `my-aws-account` and click Edit(✎). Use the following values:  
      - **KEY**: `ACCESS KEY ID`  
      - **VALUE**: Enter your AWS access key id associated with the account  
      - **KEY**: `SECRET ACCESS KEY`  
      - **VALUE**: Enter your AWS secret access key associated with the account  
   3. Click **Save**  
      
2. Click **Run workflow** and wait for the workflow run page to appear.  
3. Supply following parameters to the modal:  
   - **KEY**: `region`  
   - **VALUE**: The AWS region to run in  
   - **KEY**: `terminationDateTag`  
   - **VALUE**: The name of the tag to use for determining the termination date  
   - **KEY**: `lifetimeTag`  
   - **VALUE**: The name of the tag to use for determining the lifetime  
   - **KEY**: `dryRun`  
   - **VALUE**: True if this workflow should only print the resources it would delete  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, instances not in compliance with this workflow policy will
   immediately be terminated.
