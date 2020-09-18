This workflow codifies an incident response process for PagerDuty incidents. The
process in this workflow is to create a jira ticket and assign to the current
on-call person and set up an incident response slack room with the jira ticket
as the room title, and invite the on-call person to the slack room to start
documenting the remediation steps taken.

## Prerequisites

Before you run this workflow, you will need the following connections configured in Relay:
- A [PagerDuty](https://www.pagerduty.com/) account.
- A [Jira](https://www.atlassian.com/software/jira) account.
- A [Slack](https://slack.com/) workspace bot with the following permissions:
    - `channels:manage` to create the channel and set the topic
    - `users:read` to list users
    - `users:read.email` to read users' email addresses
    - `chat:write` to send messages
    - `chat:write.public` to send messages to channels without joining
    - `chat:write.customize` to sennd messages as a customized username and avatar

## Configure the workflow

You may need to update some of the default parameters or connection information
in this workflow to run in your environment. The default configuration assumes:
- Your PagerDuty connection is called `my-pagerduty-account`
- Your Jira connection is called `my-jira-account`
- Your Slack connection is called `my-slack-account`
- Your Jira issue ticker is `RLY`
- Your incident slack room is called `#team-relay-production-incident-<incidentID>`

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
