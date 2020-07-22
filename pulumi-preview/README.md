
This workflow runs the `pulumi` command against a connected
GitHub repository via Relay. It's useful for implementing
CI/CD workflows which connect to services outside of GitHub.

In this example, the outcome of the Pulumi execution is passed
into Slack as a notification.

To use this workflow:
- add it to your relay account
- configure a Slack connection called 'my-workspace' 
  (or change this code to match your real connection's name)
- add workflow secrets for your pulumi and github accounts 
- copy the webhook url from the relay UI
- in your pulumi app repo on github, go to settings->webhooks
- paste the webhook url and set it to execute on PRs

