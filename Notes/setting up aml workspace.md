## Create an Azure Machine Learning workspace

When you create a workspace, Azure usually provisions several supporting resources in the same resource group. Common components include:

- Azure Storage Account — stores files, notebooks and metadata for jobs and models.
- Azure Key Vault — securely stores secrets (keys, credentials) used by the workspace.
- Application Insights — monitoring and telemetry for deployed services.
- Azure Container Registry (ACR) — created as-needed to hold container images for environments.

### How to create a workspace

Options for creating a workspace:

- Azure Portal (UI)
- Azure Resource Manager (ARM) template — good for repeatable, infrastructure-as-code setups.
- Azure CLI with the Azure Machine Learning CLI extension (v2). See: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-workspace-template?view=azureml-api-2&tabs=azcli
- Azure Machine Learning Python SDK / MLClient