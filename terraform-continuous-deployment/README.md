This workflow runs a Terraform plan when a GitHub PR is merged into a configured
branch.

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS or GCP accout to store the Terraform state.
- A Git repository that has a Terraform plan in it.
- A Git repository on GitHub to configure the webhook trigger in.
  You can use the Terraform plan repo to have it run when you merge a PR into
  master for example.

## Run the workflow

1. Create a new workflow in Relay
2. Add the workflow and set the terraform vars secret if you need any:
   1. Click **Setup** 
   2. On the right sidebar, you will have a list of unconfigured secrets
   3. Click on the pencil next to **terraformVarsJSON**
   4. Add terraform vars as a JSON object. If you don't need any, just use an
      empty object instead: `{}`.
4. Under the same setup bar on the right side, copy the webhook URL for
   **github-pr-merge** under the **Webhook trigger** section.
5. To add it to your GitHub repository. Navigate to your repository on https://github.com.
   1. Navigate to the repository settings page by clicking **Settings** on the repository bar.
   2. Click **Webhooks**.
   3. Click **Add webhook**
   4. Paste the webhook URL in the **Payload URL** box
   5. Change **Content type** to `application/json`
   6. Click **Let me select individual events.**
   7. Check the **Pull requests** box
   8. Uncheck the **Pushes** box
   9. Click **Add webhook** at the bottom of the page

Relay will now receive webhook events for Pull Request merges and use them to
run your workflow.

Note: The default state storage provider is AWS S3. If you would rather use a GCP
storage bucket, then change how the credentials spec in the workflow:

```
...
spec:
  credentials:
    credentials.json: !Connection { type: gcp, name: my-gcp-credentials }
...
```
