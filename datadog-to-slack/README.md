This workflow sends a notification to Slack when a Datadog event is received.

## Prerequisites

Before you run this workflow, you will need the following:
- A [Datadog](https://www.datadog.com/) account.
- A [Slack](https://slack.com/) workspace and an appropriate channel to send notifications to.

## Configure the workflow

- Define the following parameters:
    - `slackChannel`: the slack channel to send notifications to.
- Configure a Slack connection in Relay.
    - The default name is `slack-connection`.

## Set up the trigger

In the workflow overview page in Relay, find the webhook URL by navigating to
the **Setup** sidebar.

In Datadog, add a new webhook:

1. Click on the **Integrations** menu option.
2. Install or configure the **Webhooks Integration**.
2. Under **Webhooks**, click **New +**.
   - Provide a meaningful name.
   - Update the URL to the webhook URL found in Relay.
   - Additional properties can be added to the payload for workflow customization.
4. Click **Save**.
