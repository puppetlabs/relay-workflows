This workflow looks at all of the GCP instances in a given account and zone and
selects a subset of those to terminate. The termination criteria are:

* Not tagged with a termination date or lifetime after 4 minutes
* The `termination_date` or `lifetime` labels are present but cannot be parsed
* The `termination_date` or `lifetime` labels indicate that the instance has
  expired

An instance may be configured to never terminate if its `lifetime` tag has the
special value `indefinite`.

## Prerequisites

Before you run this workflow, you will need the following:
- A GCP account.
- An GCP service account with permissions to list and terminate GCP instances (if not
  run in dry run mode).
- One or more running GCP instances that are configured to use the
  `termination_date` or `lifetime` labels.

## Run the workflow

Follow these steps to run the workflow:
1. Add your GCP service account credentials as a Connection:  
2. Click **Run workflow** and wait for the workflow run page to appear.  
3. Supply following parameters to the modal:  
   - **KEY**: `zone`  
   - **VALUE**: The GCP zone to run in  
   - **KEY**: `terminationDateLabel`  
   - **VALUE**: The label to use for determining the termination date  
   - **KEY**: `lifetimeLabel`  
   - **VALUE**: The label to use for determining the lifetime  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, instances not in compliance with this workflow policy will
   immediately be terminated.
