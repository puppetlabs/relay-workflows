This workflow looks at all of the unused EC2 key pairs in an account and sends a Slack notification about them.

## Prerequisites

Before you run this workflow, you will need the following:
- An AWS account.
- An AWS IAM user with permissions to list EC2 instances
- One or more running EC2 key pairs that are unused.
- A Slack API token with "bot user" permissions: `chat:write`, `chat:write.public`, `chat:write.customize`. The [Slack step README](https://github.com/relay-integrations/relay-slack/blob/master/steps/message-send/README.md) has instructions on how to create a token.

## Run the workflow

Follow these steps to run the workflow:
1. Add the workflow to your account from the [workflow's Library page](https://relay.sh/workflows/ec2-scan-unused-key-pairs/).

1. Add your AWS and Slack credentials as Connections. (If you already have usable Connections set up in Relay, adjust the workflow code to reference the existing names rather than add new ones.)
   - Navigate to the **Settings** tab of the workflow's page in your account
   - ✎ Edit the connection named `my-aws-account`, then click **Save**
      - **KEY**: `ACCESS KEY ID`
      - **VALUE**: Enter the AWS access key id associated with the account
      - **KEY**: `SECRET ACCESS KEY`
      - **VALUE**: Enter the AWS secret access key associated with the account
   - ✎ Edit the connection named `my-slack-token`, then click **Save**
      - **KEY**: `TOKEN`
      - **VALUE**: Paste the bot user token.

2. Click **Run workflow** and wait for the workflow run page to appear.

3. Supply following parameters, then click **Run**:
   - **KEY**: `region`
   - **VALUE**: The AWS region to run in
   - **KEY**: `slackChannel`
   - **VALUE**: The name of the channel to post to

## Run the workflow automatically

* **Schedule**: By default the workflow will run once a week, at 7:00PST on Mondays. To adjust this, edit the value of the `schedule` field in the `triggers` section. It uses standard cron syntax; for help building a custom schedule, check out https://crontab.guru/

* **Default Parameters**: You may want to adjust the default Slack channel and AWS region used by the workflow. Edit the workflow's `parameters` section to set appropriate values for these keys.