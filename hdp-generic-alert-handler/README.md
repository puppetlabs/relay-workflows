This workflow is a handler for ANY HDP event. It only uses the data that is guaranteed to be present in every webhook. More specific handlers are possible, but this is a great tool to get started with HDP + Relay.  

If you have been brought here from the HDP UI, and aren't familiar with Relay, please read [this](https://relay.sh/docs/getting-started/) to understand Relay first.

## Prerequisites

Before you run this workflow, you will need the following:
- A working HDP installation.
- A [Slack](https://slack.com/) workspace and an appropriate channel to send notifications to.

# Configure the workflow

First, create a Slack connection in Relay. If you're running into issues, try creating it from the "Connections" bar on the left, instead of directly in a workflow, which sometimes gives UUID-related errors.
Second, clone this workflow into your own Relay account, using the "Try this workflow" button, while also replacing the slack-connection on line 26 with the name of your own slack connection. Also, make sure to set your bot's username, and the channel you would like the HDP to send messages to.

## Configure the HDP

After you have created this workflow in your Relay account, copy the URL for the webhook trigger. Then, visit the Webhook setup page in your HDP settings. You can issue a test webhook from this page, using the URL you copied here.  
If your test webhook arrives in your slack channel, you're done! You can now set up alerts in your HDP. If you'd like more information in your alerts, like about which attribute changed, or which nodes were affected, you can use Relay to extract more specific data.
