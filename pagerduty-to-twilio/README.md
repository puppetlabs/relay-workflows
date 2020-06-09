This workflow responds to a PagerDuty incident by sending an SMS message to a
phone number you define.

## Prerequisites

Before you run this workflow, you will need the following:
- A [Twilio](https://twilio.com/) account with a phone number provisioned for
  sending an SMS.
- A [PagerDuty](https://www.pagerduty.com/) account.

## Configure the workflow

You will need to update some of the default parameters and secrets in this
workflow to run in your environment. 
- Set the `phoneNumber` parameter to the number that you want the message
  delivered to by default.
- Set the `twilioAccountSID` secret to the SID of your Twilio account.
- Set the `twilioAuthToken` secret to the auth token for your Twilio account.
- Set the `twilioPhoneNumber` secret to the phone number provisioned in Twilio
  for sending SMS messages.

## Test the workflow

You can test the workflow with dummy data by clicking the **Run** button. Ensure
the message you expect shows up in your Slack workspace. We recommend always 
testing workflows manually before configuring automated triggers.

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
