This workflow finds empty ELBv2 load balancers by locating all load balancers that have
empty target groups (i.e. no registered targets). 

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list and delete ELBv2 load balancers (if not
  run in dry run mode).
- One or more running ELBv2 load balancers that are empty (no targets). 

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
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, load balancers that are empty will immediately be deleted.