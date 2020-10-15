This workflow codifies an incident response process for VictorOps incidents. The process in this workflow is to create a JIRA ticket, set up an incident response slack room, and post the information about created tickets back into the incident timeline.

## Prerequisites

Before you run this workflow, you will need the following connections configured in Relay:
- A [Jira](https://www.atlassian.com/software/jira) account.
- A [Slack](https://slack.com/) workspace bot with the following permissions:
    - `channels:manage` to create the channel and set the topic
    - `users:read` to list users
    - `users:read.email` to read users' email addresses
    - `chat:write` to send messages
    - `chat:write.public` to send messages to channels without joining
    - `chat:write.customize` to sennd messages as a customized username and avatar

You'll also need to enable the REST integration point on VictorOps and add the generated endpoint URL as a workflow Secret named `endpointURL`. Note that the incoming webhook from VictorOps to Relay uses the [escalation webhook integration](https://help.victorops.com/knowledge-base/escalation-webhooks/), not the Enterprise-level [custom webhooks](https://help.victorops.com/knowledge-base/custom-outbound-webhooks).

## Configure the workflow

You may need to update some of the default parameters or connection information
in this workflow to run in your environment. The default configuration assumes:
- Your Jira connection is called `my-jira-account`
- Your Slack connection is called `my-slack-account`
- Your Jira project key is `RLY`
- Your incident slack channels will be named `#team-relay-production-incident-<incidentID>`

## Set up the trigger

When you create this workflow for the first time, we'll automatically provision
a webhook for you. You need to provide this webhook to PagerDuty to complete the
integration.

In the workflow overview page in Relay, find the webhook URL by navigating to
the **Setup** sidebar. Copy the URL to your clipboard.

In VictorOps, go to **Integrations** and enable the **Webhooks** integration. Add a new webhook, give it a memorable name and paste the Relay URL into the dialog box. 

You'll then need to associate the webhook name with one or more Escalation Policies, so the workflow will be triggered upon incident creation. Updates from Relay will be associated with the timeline of the VictorOps incident which triggered them.
