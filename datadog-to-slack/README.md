When a Datadog alert fires, you might be doing something more important. But, you don't want to forget about it. With this workflow, you can automatically send a message to a Slack channel when a Datadog event is received.

# Prerequisites

Before you run this workflow, you will need the following:
- A [Datadog](https://www.datadog.com/) account.
- A [Slack](https://slack.com/) workspace and an appropriate channel to send notifications to.

# Configure the workflow

Follow these steps to configure the workflow. Doing this will enable Relay to listen for alerts from Datadog and create messages in Slack. 

## Set up the Datadog trigger  

Follow these instructions to set up your Datadog trigger. 

From the main workflow page, find the `datadog` trigger and click the **Copy webhook URL** button.

![Set up Datadog trigger](/images/datadog-trigger.png)

In Datadog, add a new webhook: 

  - Click on the **Integrations** menu option.  
  - Install or configure the **Webhooks Integration**.  
  - Under **Webhooks**, click **New +**.  
    - Provide a meaningful name (e.g. `relay-webhook`)
    - Paste the URL to the webhook URL found in Relay.  
    - Additional properties can be added to the payload for workflow customization.  

![Set up Datadog webhook](/images/datadog-webhook.png)

  - Click **Save**.  

Configure the Datadog monitor:  
- Within the Monitor, click **Settings(⚙)** -> **Edit**  
- Under **Say what's happening**, add the above webhook with `@webhook-{name of webhook}` (e.g. `@webhook-relay`)  

![Set up Datadog monitor](/images/datadog-monitor.png)




- Click **Save**  

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

Configure the Datadog monitor:  
1. Within the Monitor, click **Settings(⚙)** -> **Edit**  
2. Under **Say what's happening**, add the above webhook with `@webhook-{name of webhook}` (e.g. `@webhook-relay`)  
3. Click **Save**  

# Run the workflow manually from Datadog

To test the Datadog alert:   
- Navigate to the Monitor that you configured earlier. 
- Click **Settings(⚙)** -> **Edit**   
- Scroll to the bottom of the page and click **Test Notifications**    
- Select **Alert** (default)  
- Click **Run Test**   

![Test alert in Datadog](/images/datadog-test-alert.png)  
