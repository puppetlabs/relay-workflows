## Prerequisites

Before you run this workflow, you will need the following:  
- An Azure Subscription  
- An Azure Service Principal with permissions to manage load balancers.  
- One or more Azure Load Balancers with zero back end configurations.  

## Configure the workflow  

![Setting up connections](/azure-delete-empty-loadbalancers/media/connections.gif)

Follow these steps to configure the workflow. Doing this will enable Relay to connect to your Azure account. 

- Add your Azure credentials as a Connection:  
   - Click **Settings** in the side nav to the left
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


## Run the workflow

![Run the workflow](/azure-delete-empty-loadbalancers/media/run-azure-lb.gif)

Follow these steps to run this workflow.

- Click **Run workflow** and wait for the workflow run page to appear.  
- Supply following parameters to the modal:  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations  

- **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, resources will be immediately terminated.  

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
#       dryRun: true
```

-  Configure the `schedule` trigger:  
   - Supply the run interval in [cron format](https://crontab.guru/).  
-  Configure the following parameter bindings:  
   - Specify whether `dryRun` should be set to `true` or `false`.  
-  Click **Save changes**
