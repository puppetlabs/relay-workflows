This workflow sends a notification to Slack when DynamoDB provisioned capacity exceeds defined limits.

## Prerequisites

Before you run this workflow, you will need the following:
- An [AWS](https://aws.amazon.com/) account and credentials with read access to DynamoDB.
- A [Slack](https://slack.com/) workspace and an appropriate channel to send notifications to.

## Configure the workflow

- Define the following parameters:
    - `slackChannel`: the slack channel to send notifications to.
- Setup unconfigured connections from the **Settings** sidebar:
    - Configure the Slack connection `slack-connection`.
    - Configure the AWS connection `aws-connection`.
- Update the `capacity` specification if desired:
    - multiple, independent capacity thresholds can be defined
    - `regions` can be updated to `include` or `exclude` any desired regions
    - `aggregate` limits represent a total of the defined regions
    - `regional` limits apply per region

## Specification examples

```yaml
  spec:
    aws: !Connection { type: aws, name: aws-connection }
    ignore:
    - us-gov-east-1
    - us-gov-west-1
    - us-iso-east-1
    - us-isob-east-1
    capacity:
    - regions:
        include:
        - us-east-1
        - us-east-2
      limits:
        aggregate:
          read: 500
          write: 500
        regional:
          read: 300
          write: 300
    - regions:
        include:
        - us-west-1
        - us-west-2
      limits:
        aggregate:
          read: 750
          write: 500
        regional:
          read: 500
          write: 300
    - regions:
        all: true
        exclude:
        - us-east-1
        - us-east-2
        - us-west-1
        - us-west-2
      limits:
        aggregate:
          read: 0
          write: 0
        regional:
          read: 0
          write: 0
```
