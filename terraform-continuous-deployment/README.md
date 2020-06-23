This workflow runs a Terraform plan when a GitHub PR is merged into a configured
branch.  

## Prerequisites

Before you run this workflow, you will need the following:  
- An AWS or GCP account to store the Terraform state file.  
- A Git repository that has a Terraform plan in it.  
- SSH key for above Git repository  
- A Git repository on GitHub to configure the webhook trigger in.  
  You can use the Terraform plan repo to have it run when you merge a PR into
  master for example.  

## Run the workflow  

1. Add the workflow and set the terraform vars secret if you need any:  
   - Click **Setup**   
   - On the right sidebar, you will have a list of unconfigured secrets  
   - Click on the (✎) next to **terraformVarsJSON**  
   - Add terraform vars as a JSON object. If you don't need any, just use an
      empty object instead: `{}`.  
2. Under the same setup bar on the right side, copy the webhook URL for
   **github-pr-merge** under the **Webhook trigger** section.  
3. To add it to your GitHub repository. Navigate to your repository on https://github.com.  
   - Navigate to the repository settings page by clicking **Settings** on the repository bar.  
   - Click **Webhooks**.  
   - Click **Add webhook**  
   - Paste the webhook URL in the **Payload URL** box  
   - Change **Content type** to `application/json`  
   - Click **Let me select individual events.**  
   - Check the **Pull requests** box  
   - Uncheck the **Pushes** box  
   - Click **Add webhook** at the bottom of the page  

Relay will now receive webhook events for Pull Request merges and use them to
run your workflow.  

**Note:** The default state storage provider is AWS S3. If you would rather use a GCP
storage bucket, then change how the credentials spec in the workflow:  

```
...
spec:
  credentials:
    credentials.json: !Connection { type: gcp, name: my-gcp-credentials }
...
```
