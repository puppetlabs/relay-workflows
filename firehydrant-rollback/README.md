# Roll back a Kubernetes deployment from a FireHydrant incident runbook

This workflow connects Relay to [FireHydrant.io](https://firehydrant.io), a service for managing incidents that affect the availability of your service. It demonstrates rolling back a bad Kubernetes deployment as a remediation action to fix a degraded service.

This documentation is a shorter version of the [Deployment Rollbacks via FireHydrant Runbook](http://relay.sh/blog/firehydrant-rollback-runbook/) blog post; see that for detailed instructions.

# Connecting the Services

In FireHydrant, we'll crate a Runbook that will trigger the workflow by sending a webhook to Relay. Create a new Runbook and add a **Send a Webhook** step. For the **Endpoint URL**, paste the webhook address from the Relay's **Settings** sidebar. The **HMAC Secret** field is an arbitrary string (not currently used). For the **JSON Payload** field, paste the following template:

```json
{
  "incident_id": "{{ incident.id }}",
  "name": "{{ incident.name }}",
  "summary": "{{ incident.summary }}",
  "service": "{{ incident.services[0].name | downcase }}",
  "environment": "{{ incident.environments[0].name | downcase }}",
  "channel_id": "{{ incident.channel_id }}",
  "channel_name": "{{ incident.channel_name }}"
}
```

Next, create a FireHydrant API key for Relay to post information back into the incident timeline. Under **Integrations** - **Bot users** in FireHydrant, create a new **Bot user** with a memorable name and description. Save the resulting API token into a Relay secret on the Relay workflow's **Settings** sidebar named `apiKey` (case-sensitive).

## GCP Authentication Setup

This workflow uses a GCP Connection type on Relay's end, which requires a [service account](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens)
configured on your cluster. Follow the GCP guide to API Server Authentication's ["Service in other environments"](https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#service_in_other_environments) section to set one up. This workflow will require the service account have the role `roles/container.developer` attached to it; if you re-use the connection for other workflows it may require additional permissions. Once you've gotten the service account JSON file downloaded, add a GCP Connection in Relay, name it `relay-service-account` and paste the contents of the JSON file into the dialog. Under the hood, Relay stores this securely in our Vault service and makes the contents available to workflow containers through the [!Connection custom type](https://relay.sh/docs/using-workflows/managing-connections/) in the workflow. 

## Configuring Services and Environments

The Environments section lets you enumerate the instances of your service, to better characterize the impact of an incident, help assign owners for remediation actions, and message outage information to the appropriate audiences. Check out this FireHydrant [helpdesk article on inventory management](https://help.firehydrant.io/en/articles/4192249-inventory-management-functionalities-services-and-environments) for more details on infrastructure organization. For our purposes, the goal of defining environments is to map them onto Kubernetes namespaces where our application is running. (For production workloads, it's more likely that your environments map to distinct clusters; that's totally possible to handle in Relay but is beyond the scope of this introduction!) 
