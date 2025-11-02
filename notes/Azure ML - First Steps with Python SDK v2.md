# First Steps with Python SDK v2
[🏠 Return Home](./../README.md)

For data scientists, the most convenient way to interact with Azure Machine Learning is through the **Azure ML Python SDK v2**.  
This SDK allows you to programmatically manage Azure ML resources, submit experiments, and deploy models directly from your local or cloud-based development environment.  
It can also manage other Azure resources (like storage accounts), but this guide focuses on Azure Machine Learning–specific workflows.

Before diving into specific tasks, it’s essential to correctly **set up your Python SDK v2 environment**.

---

## Development Environment Options

You can use Jupyter Notebooks in most IDEs (e.g., Visual Studio Code) for local development.  
If you prefer a managed environment, try [Azure Machine Learning Notebooks](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2), which run directly in the cloud and already include the SDK setup.

---

## Azure ML Workspace

If you’re developing **outside** of Azure ML (e.g., on your local machine or VM), you can use the SDK to create a workspace programmatically — see the [quickstart guide](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-azure-ml-in-a-day?view=azureml-api-2).  
However, for simplicity, we recommend creating it directly in the **Azure Portal**:

1. Search for “Azure Machine Learning” in the Portal.  
2. Follow the resource creation wizard.  
3. Note your **Subscription ID**, **Resource Group**, **Workspace Name**, and **Region** — you’ll need them later.

More details are available [here](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2).

---

## Setting the Azure Environment

If you’re using Azure Machine Learning Notebooks, much of the setup is already done.  
Still, it’s good practice to explicitly define key environment parameters.

You can store them in a `.env` file (recommended):

```env
SUBSCRIPTION_ID="your-subscription-id"
RESOURCE_GROUP="your-resource-group"
WORKSPACE_NAME="your-workspace-name"
PREFERRED_RESOURCE_LOCATION="your-preferred-region"
MAIN_STORAGE_ACCOUNT="your-storage-account-name"
MAIN_STORAGE_ACCOUNT_ACCESS_KEY="your-storage-account-access-key"
````

You can find these values under your Azure ML workspace **Overview** in the Azure Portal.
Storage account keys are available under **Security + Networking → Access keys**.

---

## Installing Python Packages

We strongly recommend using a **conda** or **virtual environment** to isolate dependencies.
Dependency conflicts are common, so start with a clean environment.

> 💡 Tip: Use the same Python version as Azure ML compute instances (as of writing, **Python 3.10.11**).

Install the required packages in the following order:

```bash
pip install azure-ai-ml
pip install mltable
pip install fsspec
pip install azureml-fsspec
pip install "mlflow<3.0.0"
pip install azureml-mlflow
```

If installation issues occur, recreate the environment and use our prepared [requirements file](../environment/local-development-environment/pip-requirements-2.txt).

---

## Authentication

Authentication depends on your execution environment — **Azure Compute Instance** or **Local Machine**.

### On Azure ML Compute Instance

When you create a Compute Instance in Azure ML, the configuration file is automatically generated.
It includes credentials needed to access your workspace.

Use the following code to connect:

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient

try:
    credential = DefaultAzureCredential()
    credential.get_token("https://management.azure.com/.default")
except Exception:
    credential = InteractiveBrowserCredential()

ml_client = MLClient.from_config(credential=credential)
```

---

### On a Local Machine

Before authenticating, make sure you’re signed in with the Azure CLI:

```bash
az login
```

Then, load environment variables and connect manually:

```python
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

# Load .env file
load_dotenv("<path-to-your-env-file>")

subscription_id = os.environ["SUBSCRIPTION_ID"]
resource_group = os.environ["RESOURCE_GROUP"]
workspace_name = os.environ["WORKSPACE_NAME"]

# Authenticate and initialize client
credentials = DefaultAzureCredential()
ml_client = MLClient(
    credential=credentials,
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name
)
```

---

## Verifying the Connection

You can confirm that the connection works with a simple check:

```python
try:
    ml_client.workspaces.get(ml_client.workspace_name)
    print("✅ Connection verified successfully.")
except Exception as e:
    print("❌ Failed to verify connection.")
    print(e)
```

---

## Summary

Your **Python SDK v2 environment** is now set up and authenticated.
You can start using `MLClient` to manage datasets, jobs, compute resources, and deployments directly from code.
You can try to run some of the examples from this note in this [notebook](../tutorials/First%20Azure%20ML%20Notebook.ipynb).

[🏠 Return Home](./../README.md)