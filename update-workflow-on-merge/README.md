This is a meta-workflow that can be run to update the current
version of a workflow stored in Relay from a GitHub repo. It's 
meant to be run automatically via GitHub webhook upon commit,
so that merging a workflow PR to the `main` branch of a git repo 
will sync it to Relay.

## Prerequisites

Before you run this workflow, you will need a public Github repository
where you intend to store the canonical version of your workflows.

Add this workflow to your Relay account, either from the workflow repository
(double-meta!) or directly. It will prompt you to add login credentials as
secrets; these can either be for your main account or a secondary account
that has Administrator access to your workflows.

## Set up the trigger

When you create this workflow for the first time, we'll automatically provision
a webhook for you. You need to provide this webhook to GitHub to complete the
integration.

In the workflow overview page in Relay, find the webhook URL by navigating to
the **Setup** sidebar. Copy the URL to your clipboard.

In the GitHub repo, go to **Setup**, then **Webhooks**. Paste the webhook
URL, leave the **Secret** field blank. Choose **Let me select individual events**
and select only "Pull Requests".

## Use the workflow

Now, whenever there's a PR event in your workflow repository, GitHub will
call the webhook with details of the PR. The workflow extracts information
about the PR from the webhook payload, clones the repository to find the
changed workflow file and updates the version which is stored on Relay.

It makes some assumptions in the name of brevity, specifically:
- the commit contains no more than one yaml file,
  which is the workflow to be updated
- the workflow name on the service matches the filename,
  minus the .yaml extension
- you've set up secrets with your login creds to relay itself.
