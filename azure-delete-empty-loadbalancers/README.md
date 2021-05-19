Removing unused resources in your Azure account (like load balancers) can help you avoid unnecessary charges on your monthly Azure bill. Whether it's just you picking up after yourself or the dozens of other teams in your company creating resources (and not deleting them *ah hem*) – this workflow can help to keep your Azure account clean. 

This workflow will first look for all Azure load balancers in a Subscription (or optionally, resource group). Then, it will filter that list for the load balancers that have zero back end configurations. Then, it waits for your approval. Finally, once approval has been granted, it will delete the empty load balancers. Problem solved! 

For more details, check out our blog post [Save time and money by automatically deleting Azure Load Balancers](https://relay.sh/blog/save-time-and-money-by-automatically-deleting-unused-azure-load-balancers/).

## Prerequisites

Before you run this workflow, you will need the following:  
- An Azure Subscription  
- An Azure Service Principal with permissions to manage load balancers.  
- One or more Azure Load Balancers with zero back end configurations.  

## Configure the workflow  

Follow these steps to configure the workflow. Doing this will enable Relay to connect to your Azure account. 

You may see a warning that you are missing a required connection. This means you will need to add your Azure credentials as a Connection.


1. Click **Fill in missing connections** or click **Settings** in the side nav.

![Fill in missing connections](/azure-delete-empty-loadbalancers/media/missing-connection.png)

![Click settings from side nav](/azure-delete-empty-loadbalancers/media/settings-sidenav.png)

2. Find the Connection named `my-azure-account` and click the plus sign **(+)**. Use the following values:  
      - **KEY**: `CLIENT ID`  
      - **VALUE**: Enter your Azure Client ID associated with the service principal  
      - **KEY**: `SECRET`  
      - **VALUE**: Enter your Azure Secret associated with the service principal  
      - **KEY**: `TENANT ID`  
      - **VALUE**: Enter your Azure Tenant ID associated with the service principal    
      - **KEY**: `SUBSCRIPTION ID`  
      - **VALUE**: Enter your Azure Subscription ID   
   - Click **Save** 

## Run the workflow manually

Follow these steps to run this workflow.

- Click **Run workflow** and wait for the workflow run page to appear.  
- Supply following parameters to the modal:  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations  

> **WARNING!** Be careful setting `dryRun` to `false`. Though the workflow comes with an approval step, once approved the resources will be terminated. Please use caution.

## Run the workflow on a schedule  

Follow these steps to run this workflow on a schedule:  
-  Un-comment out the Trigger block in the workflow file:  

> **TIP:** If you're using the Relay code editor, highlight the `triggers` section and type `⌘ + /` (Mac) or `Ctrl + /` (Windows) to uncomment.  

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
