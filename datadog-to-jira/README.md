When a Datadog alert fires, you might be doing something more important. But, you don't want to forget about it. With this workflow, you can automatically create an issue in Jira issue when a Datadog event is received.

# Prerequisites

Before you run this workflow, you will need the following:
- A [Datadog](https://www.datadog.com/) account.
- An instance of [Jira](https://www.atlassian.com/software/jira) available to the internet. Jira Server and Jira Cloud are both supported.

# Configure the workflow

Follow these steps to configure the workflow. Doing this will enable Relay to listen for alerts from Datadog and create tickets in Jira. 
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
## Configure the Jira integration

- Click **Fill in missing connections** or click **Settings** in the side nav.

![Fill in missing connections](/images/missing-connection.png)

![Click settings from side nav](/images/settings-sidenav.png)

- Fill out the form to create a Connection to your Jira instance. 
    - **jiraURL** - The URL to the root of your Jira instance. For Jira Cloud, this is
      `https://your-domain.atlassian.net`.  
    - **jiraUsername** - The username to use when authenticating to Jira.  
    - **jiraToken** - The [API token](https://confluence.atlassian.com/x/Vo71Nw) (for Jira Cloud) or password to use when authenticating to Jira.  

- Click **Save**

## Set the default Jira project 

Configure the default Jira project where you will create the tickets.
- Navigate to the **Code** tab. 

![Code tab](/images/code-tab.png)

- Find the parameter for `jiraProjectKey` and specify the `default:` project (e.g. `OPS`) where tickets will be created. 

```yaml
  jiraProjectKey:
    description: the JIRA project key to use when creating tickets
    default: OPS
```
# Run the workflow manually from Datadog

To test the Datadog alert:   
- Navigate to the Monitor that you configured earlier. 
- Click **Settings(⚙)** -> **Edit**   
- Scroll to the bottom of the page and click **Test Notifications**    
- Select **Alert** (default)  
- Click **Run Test**   

![Test alert in Datadog](/images/datadog-test-alert.png)