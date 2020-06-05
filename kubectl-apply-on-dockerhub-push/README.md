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
3. Setup cluster secrets:
    - Click **Setup**
    - On the right sidebar, fill in the secrets **cluster-master-url**,
      **cluster-cadata**, and **cluster-token** with your Kubernetes cluster
      credentials. You can find instructions for creating those by following
      this guide:
      https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
      or by following a guide provided by your Kubernetes cloud provider.
4. Creating a new tag for your docker image and pushing it to Docker Hub should
   result in an update to your deployment container. You can validate with:
   `kubectl -n <namespace> get deployments <deploymentName> -o=jsonpath='{.metadata.name}{": "}{range .spec.template.spec.containers[*]}{.image}{end}'`.
