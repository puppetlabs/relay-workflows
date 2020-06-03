This workflow responds to a PagerDuty incident by creating an issue in Jira.

## Prerequisites

Before you run this workflow, you will need the following:
- A [PagerDuty](https://www.pagerduty.com/) account.
- An instance of [Jira](https://www.atlassian.com/software/jira) available to
  the internet. Jira Cloud instances are compatible with this workflow.

## Configure the workflow

- Update the default parameter for `jiraProjectKey` for the Jira project where you 
  want tickets to be created. 
    - Currently, tickets will be created in the 'OPS' project by default.

- Define the following secrets to connect to your Jira instance:
    - `jiraURL`: The URL to the root of your Jira instance. For Jira Cloud, this is 
      `https://your-domain.atlassian.net`.
    - `jiraUsername`: The username to use when authenticating to Jira.
    - `jiraToken`: The [API token](https://confluence.atlassian.com/x/Vo71Nw) (for 
      Jira Cloud) or password to use when authenticating to Jira.

## Test the workflow

You can test the workflow with dummy data by clicking the **Run** button. Ensure
an appropriate issue is created in your Jira instance and the message you expect
shows up in your Slack workspace. We recommend always testing workflows manually
before configuring automated triggers.

## Set up the trigger

When you create this workflow for the first time, we'll automatically provision
a webhook for you. You need to provide this webhook to PagerDuty to complete the
integration.

In the workflow overview page in Relay, find the webhook URL by navigating to
the **Setup** sidebar. Copy the URL to your clipboard.

In PagerDuty, determine which services you want to run the workflow when an
incident is triggered. For each of those services:  

1. Click on the **Integrations** tab.  
2. At the bottom of the page, click **Add or manage extensions**.  
3. Create a **New Extension**:  
   - Extension Type: `Generic V2 Webhook`  
   - Name: `Relay`  
   - URL: Paste the webhook URL from your clipboard.  
4. Click **Save**.  

Whenever an incident is triggered for the first time, this workflow will run.  
You can reuse the same webhook URL for many services.  

![Gif of setting up Pagerduty webhook to trigger Relay](../images/setup-pagerduty-webhook.gif)