## Prerequisites

Before you run this workflow, you will need the following:
- An Azure Subscription
- An Azure Service Principal with permissions to manage compute resources
- One or more running Azure Disks that are unattached. 

## Run the workflow

Follow these steps to run the workflow:  
1. Add your Azure credentials as a Connection:  
   1. Click **Setup**   
   2. Find the Connection named `my-azure-account` and click Edit(✎). Use the following values:  
      - **KEY**: `CLIENT ID`  
      - **VALUE**: Enter your Azure Client ID associated with the service principal  
      - **KEY**: `SECRET`  
      - **VALUE**: Enter your Azure Secret associated with the service principal  
      - **KEY**: `TENANT ID`  
      - **VALUE**: Enter your Azure Tenant ID associated with the service principal   
      - **KEY**: `SUBSCRIPTION ID`  
      - **VALUE**: Enter your Azure Subscription ID   
   3. Click **Save**  

2. Click **Run workflow** and wait for the workflow run page to appear.  
3. Supply following parameters to the modal:  
   - **KEY**: `dryRun`  
   - **VALUE**: True if you don't want to perform actual WRITE operations  

4. **Warning:** If you run the workflow with the `dryRun` parameter set to
   `false`, volumes that are unattached will immediately be terminated.
