This workflow looks at all of the GCP disks in a given account and zone and
selects a subset of those to terminate that don't have any users (i.e. unattached).

## Prerequisites

Before you run this workflow, you will need the following:
- A GCP account.  
- An GCP service account with permissions to list and terminate GCP disks (if not
  run in dry run mode).  
- One or more running GCP disks that are not attached to any instances.  

## Run the workflow

Follow these steps to run the workflow:  
1. Add your GCP service account credentials as a Connection:  
2. Click **Run workflow** and wait for the workflow run page to appear.  
3. Supply following parameters to the modal:  
   - **KEY**: `zone`  
   - **VALUE**: The GCP zone to run in.  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you dont want to actually delete the resources. Use this to test the workflow and ensure it is behaving as expected.  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, unattached disks will immediately be terminated.  

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
#       zone: us-central1-a
#       dryRun: true
```

-  Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
-  Configure the following parameter bindings:  
   - Specify the `zone` to run in. 
   - Specify whether `dryRun` should be set to `true` or `false`.  
-  Click **Save changes**