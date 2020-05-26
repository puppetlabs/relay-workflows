## Prerequisites  

Before you run this workflow, you will need the following:  
- An Azure Subscription  
- An Azure Service Principal with permissions to manage Network Interfaces.  
- One or more unused Azure Network Interfaces (NIC).   

## Run the workflow  

Follow these steps to run the workflow:  
1. Add your Azure credentials as a Connection:  
   - Click **Setup**  
   - Find the Connection named `my-azure-account` and click Edit(✎). Use the following values:  
      - **KEY**: `CLIENT ID`  
      - **VALUE**: Enter your Azure Client ID associated with the service principal  
      - **KEY**: `SECRET`  
      - **VALUE**: Enter your Azure Secret associated with the service principal  
      - **KEY**: `TENANT ID`  
      - **VALUE**: Enter your Azure Tenant ID associated with the service principal    
      - **KEY**: `SUBSCRIPTION ID`  
      - **VALUE**: Enter your Azure Subscription ID   
   - Click **Save**  

2. Click **Run workflow** and wait for the workflow run page to appear.  
3. Supply following parameters to the modal:  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations   

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, unused Network Interfaces will immediately be terminated.  

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
#       dryRun: true
```

2. Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
3. Configure the following parameter bindings:  
   - Specify whether `dryRun` should be set to `true` or `false`.  
4. Click "Save changes"