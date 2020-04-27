# Automatically delete Azure Disks without attachments 

This workflow looks at all of the Azure Disks in a given subscription and (optionally) resource group that are unattached and terminates them.

## Prerequisites

Before you run this workflow, you will need the following:
- An Azure Subscription
- An Azure Service Principal with permissions to manage compute resources
- One or more running Azure Disks that are unattached. 

## Run the workflow

Follow these steps to run the workflow:
1. Add your Azure credentials as secrets:
   1. Click **Edit** > **Secrets**.
   2. Click **Define new secret** and use the following values:
      - **KEY**: `azure.client_id`
      - **VALUE**: Enter your Azure Client ID associated with the service principal
      - **KEY**: `azure.secret`
      - **VALUE**: Enter your Azure Secret associated with the service principal
      - **KEY**: `azure.tenant_id`
      - **VALUE**: Enter your Azure Tenant ID associated with the service principal 
      - **KEY**: `azure.subscription_id`
      - **VALUE**: Enter your Azure Subscription ID  

2. Click **Run workflow** and wait for the workflow run page to appear.
3. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, volumes that are unattached will immediately be terminated.
