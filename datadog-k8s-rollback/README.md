This workflow rolls back a kubernetes deployment to the previous
version and updates a Datadog Incident Management incident upon completion.

## Prerequisites

Before you run this workflow, you will need the following:
- An account on [Datadog](https://datadoghq.com)
- An operating Kubernetes cluster with a deployment

## Run the workflow

1. Add the workflow in Relay
2. Set up your Datadog connection
    - In the Relay page for the new workflow, Click **Setup**
    - On the right sidebar, click the plus "+" under Connections for the Datadog connection and give it a name
    - In Datadog, go to **Integrations** - **APIs** and create both an API key and Application key
    - Copy these keys to the respective values in your Relay connection
    - Save the Connection
3. Setup your Kubernetes connection
    - In the Relay page for the workflow, expand the **Setup** sidebar
    - In the sidebar, click the plus "+" under Connections for the Kubernetes connection and give it a name
    - Fill in the **Cluster server** field with the URL to your Kubernetes master (`kubectl cluster-info` will show this)
    - Paste the PEM-encoded CA certificate for your cluster in the **Certificate authority** field. This command will display the CA cert: `kubectl config view --raw --flatten -o json | jq -r '.clusters[] | select(.name == "'$(kubectl config current-context)'") | .cluster."certificate-authority-data"' | base64 --decode`
    - Paste an access token into the **Token** field. This can be retrieved with the following command: `kubectl config view --raw --minify --flatten -o jsonpath='{.users[].user.auth-provider.config.access-token}'`
