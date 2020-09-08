This workflow sets a new image tag for a kubernetes deployment when an image is
pushed to Docker Hub.

## Prerequisites

Before you run this workflow, you will need the following:
- An account on [Docker Hub](https://hub.docker.com/)
- An operating Kubernetes cluster with a deployment

## Run the workflow

1. Add the workflow in Relay
2. Setup the Docker Hub webhook:
    - Click **Setup**
    - On the right sidebar, copy the webhook for the dockerhub-image-pushed trigger
    - Navigate to your repository on Docker Hub
    - Click **Webhooks** at the top
    - Add a name for your webhook and paste the url in the box **Webhook URL**
    - Click **Create**
3. Setup your Kubernetes connection
    - In the Relay page for the workflow, expand the **Setup** sidebar
    - In the sidebar, click the plus "+" under Connections for the Kubernetes connection and give it a name
    - Fill in the **Cluster server** field with the URL to your Kubernetes master (`kubectl cluster-info` will show this)
    - Paste the PEM-encoded CA certificate for your cluster in the **Certificate authority** field. This command will display the CA cert: `kubectl config view --raw --flatten -o json | jq -r '.clusters[] | select(.name == "'$(kubectl config current-context)'") | .cluster."certificate-authority-data"' | base64 --decode`
    - Paste an access token into the **Token** field. This can be retrieved with the following command: `kubectl config view --raw --minify --flatten -o jsonpath='{.users[].user.auth-provider.config.access-token}'`
4. Creating a new tag for your docker image and pushing it to Docker Hub should
   result in an update to your deployment container. You can validate with:
   `kubectl -n <namespace> get deployments <deploymentName> -o=jsonpath='{.metadata.name}{": "}{range .spec.template.spec.containers[*]}{.image}{end}'`.
