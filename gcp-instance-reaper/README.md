This workflow looks at all of the GCP instances in a given account and zone and
selects a subset of those to terminate. The termination criteria are:

* Not labelled with a termination date or lifetime after 4 minutes
* The `termination_date` or `lifetime` labels are present but cannot be parsed.
* The `termination_date` or `lifetime` labels indicate that the instance has
  expired.

An instance may be configured to never terminate if its `lifetime` label has
the special value `indefinite`. Other valid values for the `lifetime` label are
of the form `<number><unit>` where `<number>` is any integer and `<unit>` is a
time unit of `w` (weeks), `h` (hours), `d` (days) or `m` (months). So, as an
example, if the `lifetime` label for an instance has a value of `43w` then it
should be terminated after it's 43 weeks old.

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
   - **VALUE**: The GCP zone to run in.  
   - **KEY**: `terminationDateLabel`  
   - **VALUE**: The label to use for determining the termination date.  
   - **KEY**: `lifetimeLabel`  
   - **VALUE**: The label to use for determining the lifetime.  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, instances not in compliance with this workflow policy will
   immediately be terminated.  

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
#       terminationDateLabel: termination_date
#       lifetimeLabel: lifetime
#       dryRun: true
```

-  Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
-  Configure the following parameter bindings:  
   - Specify the `zone` to run in. 
   - Specify the `terminationLabel` to use.   
   - Specify the `lifetimeLabel` to use.    
   - Specify whether `dryRun` should be set to `true` or `false`.  
-  Click **Save changes**
