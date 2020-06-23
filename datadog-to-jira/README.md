This workflow creates an issue in Jira issue when a Datadog event is received.

## Prerequisites

Before you run this workflow, you will need the following:
- A [Datadog](https://www.datadog.com/) account.
- An instance of [Jira](https://www.atlassian.com/software/jira) available to
  the internet. Jira Server and Jira Cloud are both supported.

## Configure the workflow

- Define the following parameters:  
    - `jiraProjectKey`: the Jira project where you want issues to be created.  
- Define the following secrets to connect to your Jira instance:  
    - `jiraURL`: The URL to the root of your Jira instance. For Jira Cloud, this is
      `https://your-domain.atlassian.net`.  
    - `jiraUsername`: The username to use when authenticating to Jira.  
    - `jiraToken`: The [API token](https://confluence.atlassian.com/x/Vo71Nw) (for
      Jira Cloud) or password to use when authenticating to Jira.  

## Set up the trigger  

In the workflow overview page in Relay, find the webhook URL by navigating to
the **Setup** sidebar.  

In Datadog, add a new webhook:  

1. Click on the **Integrations** menu option.  
2. Install or configure the **Webhooks Integration**.  
3. Under **Webhooks**, click **New +**.  
   - Provide a meaningful name (e.g. relay)
   - Update the URL to the webhook URL found in Relay.  
   - Additional properties can be added to the payload for workflow customization.  
4. Click **Save**.  

Configure the Datadog monitor:  
1. Within the Monitor, click **Settings(⚙)** -> **Edit**  
2. Under **Say what's happening**, add the above webhook with `@webhook-{name of webhook}` (e.g. `@webhook-relay`)  
3. Click **Save**  

## Testing Alerts  

To test the Datadog alert:   
1. Click **Settings(⚙)** -> **Edit**   
2. Scroll to the bottom of the page and click **Test Notifications**    
3. Select **Alert** (default)  
4. Click **Run Test**   
