This workflow runs a Terraform plan when a GitHub PR is merged into a configured
branch.

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS or GCP accout to store the Terraform state.
- A Git repository that has a Terraform plan in it.
- A Git repository on GitHub to configure the webhook trigger in.
  You can use the Terraform plan repo to have it run when you merge a PR into
  master or something.

## Run the workflow

1. Create a new workflow in Relay
2. Add the workflow and set the required secrets
3. Adjust your parameter defaults to match your usecase.
4. Copy the trigger webhook URL and add it to your GitHub repository. You can do
   this through the repository settings under the "webhooks" subsection in
   GitHub.
