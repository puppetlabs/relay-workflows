Ok, so picture this. Your team is deploying an application change. It's been reviewed and tested and now rolling out. Everything looks good! However, unexpectedly you get alert from Datadog that the  deployment is causing other Kubernetes applications to misbehave. What are you going to do? Well, one option is to rollback the deployment and update the incident. 

This workflow rolls back a Kubernetes deployment to the previous version. Next, it updates a Datadog Incident Management incident upon completion. 

# Prerequisites

Before you run this workflow, you will need the following:
- Account on [Datadog](https://datadoghq.com)
- [Datadog incident](https://docs.datadoghq.com/monitors/incident_management/) 
- Kubernetes cluster with a deployment

# Configure the workflow  

Follow these steps to configure the workflow. Doing this will enable Relay to connect to your Datadog account and your Kubernetes cluster. 

You may see a warning that you are missing a required connection. This means you will need to add your Datadog and Kuberentes credentials as Connections. 

## Configuring your Datadog Connection
- Click **Fill in missing connections** or click **Settings** in the side nav.

![Fill in missing connections](/images/missing-connection.png)

![Click settings from side nav](/images/settings-sidenav.png)

- Find the Connection named `my-datadog-keys` and click the plus sign **(+)**. 

- In Datadog, create your keys:
    - Go to **Integrations** - **APIs** and create an **API key** 

    ![Create Datadog API key](/images/datadog-api-key.png)

    - Go to **Team** -> **Application Keys** and click **+ New Key**

    ![Create Application key](/images/datadog-application-key.png)

- Go back to Relay and fill out the form.

    - **Name** - You can’t change this with the form. The name is supplied by the YAML. If you wanted to change it you would need to do so in the Code tab.
    - **API key** - Copy the API key value from Datadog. 
    - **Application key** - Copy the application key value (not the id) from Datadog.
- Click **Save**

## Configuring your Kubernetes Connection
- Find the Connection named `my-kubernetes-cluster` and click the plus sign **(+)**. 
- Fill out the form
    - **Cluster server** - URL to your Kubernetes master 
    > How do you get this? Run this from your terminal:
    > `$ kubectl cluster-info`
    - **Certificate authority** - PEM-encoded CA certificate for your cluster.
    > How do you get this? Run this from your terminal:
    > `$ kubectl config view --raw --flatten -o json | jq -r '.clusters[] | select(.name == "'$(kubectl config current-context)'") | .cluster."certificate-authority-data"' | base64 --decode`
    - **Token** - Access token. 
    > How do you get this? Run this from your terminal:    
    > `kubectl config view --raw --minify --flatten -o jsonpath='{.users[].user.auth-provider.config.access-token}'`
- Click **Save**

# Run the workflow manually

Follow these steps to run this workflow. 

- Click **Run workflow** and wait for the workflow run page to appear. 

    ![Run workflow](/images/run-workflow-action.png)

- Supply values for the parameters fields when the modal appears:  

    ![Supply modal values](/images/datadog-k8s-rollback-modal.png)

    - **deployment** - Name of the kubernetes deployment to roll back
    - **namespace** - Name of the kubernetes namespace where deployment is located
    - **public_id** - Numeric part of the "friendly" id of the Datadog Incident to update; for IR-3 use "3"

- Click **Run Workflow**

