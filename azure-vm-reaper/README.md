[Tagging resources in Azure](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=/azure/azure-resource-manager/management/toc.json) can be super useful for billing, organizing resources by department, or really just remembering what that one VM called `super-important-2153` actually does. That's a great start. However, you know what's even better? Tag enforcement. With this workflow, you can save money on your monthly Azure bill and enforce your tagging policy by deleting untagged VMs. 

This workflow will first look for all Azure virtual machines in a Subscription (or optionally, resource group). Then, it will filter that list for the untagged virtual machines. Then, it waits for your approval. Finally, once approval has been granted, it will delete the untagged virtual machines. Nice!

# Prerequisites

Before you run this workflow, you will need the following:  
- An Azure Subscription  
- An Azure Service Principal with permissions to manage compute resources  
- One or more running Azure Virtual Machines with no tags.  

# Configure the workflow  

Follow these steps to configure the workflow. Doing this will enable Relay to connect to your Azure account. 

You may see a warning that you are missing a required connection. This means you will need to add your Azure credentials as a Connection.


- Click **Fill in missing connections** or click **Settings** in the side nav.

![Fill in missing connections](/media/missing-connection.png)

![Click settings from side nav](/media/settings-sidenav.png)

- Find the Connection named `my-azure-account` and click the plus sign **(+)**. 

![Guide connections](/media/guide-connections.png)

- Fill out the form:  

   - **Name** - You can’t change this with the form. The name is supplied by the YAML. If you wanted to change it you would need to do so in the Code tab.
   - **Subscription ID** - Enter your Azure Subscription ID
   - **Client ID** - Enter your Azure Client ID associated with the service principal  
   - **Tenant ID** - Enter your Azure Tenant ID associated with the service principal
   - **Secret** - Enter your Azure Secret associated with the service principal  

> **TIP** If you need help getting your Azure credentials, check out our [blog post](https://relay.sh/blog/save-time-and-money-by-automatically-deleting-unused-azure-load-balancers/).

-  Click **Save** 
# Run the workflow manually

Follow these steps to run this workflow.

- Click **Run workflow** and wait for the workflow run page to appear.  

    ![Run workflow](/media/run-workflow-action.png)

- Supply values for the parameters fields when the modal appears:  

    ![Supply modal values](/media/dry-run-modal.png)

    - **dryRun** - `true` or `false` 
       - `true` if you dont want to actually delete the resources. Use this to test the workflow and ensure it is behaving as expected.
       - `false` if you want the resources to be immediately deleted.  

> **WARNING!** Be careful setting `dryRun` to `false`. Though the workflow comes with an approval step, once approved the resources will be terminated. Please use caution.

# Run the workflow on a schedule  
Follow these steps to run this workflow on a schedule:  
- Un-comment out the included Trigger block in the workflow YAML. You can do this in the **Code** tab.

![Code tab](/media/code-tab.png)

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
   - Configure the following parameter bindings:  
      - Specify whether `dryRun` should be set to `true` or `false`.  
```yaml
  binding:
    parameters:
      dryRun: true
```

- Click **Save changes**