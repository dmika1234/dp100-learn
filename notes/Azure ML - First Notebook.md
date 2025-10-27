# Running Your First Azure Machine Learning Notebook
[🏠 Return Home](./../README.md)

For data scientists the most convenient way to interact with Azure Machine Learning is through the **Azure ML Python SDK v2**.  
This SDK allows you to programmatically manage Azure ML resources, submit experiments, and deploy models directly from your local machine or development environment.
Before you start diving into specific Azure Machine Learning tasks, it’s essential to learn how to setup your Python SDK v2 environment.
As you probably now Jupyter Notebooks are ideal for analyzing, experimenting with the data and creating machine learning models prototypes.
if you're interacting with Azure Machine Learning on your local machine you can use Jupyter Notebooks in most IDEs including Visual Studio Code.
If you prefer a cloud-based solution, you can use [Azure Machine Learning Notebooks](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2).

## Azure ML workspace
In this notebook we assume that 

## Setting Azure Environment
If you're using Azure Machine Learning Notebooks most of the setup is already done for you. But you can still follow the steps below to learn what parameters you can configure.
You need to save in a safe place information on you Azure subscription, resource group, workspace name and region where your workspace is deployed.
You can use `.env` file to store these values in key-value pairs, for example:
```env
SUBSCRIPTION_ID = "your-subscription-id"
PREFERED_RESOURCE_LOCATION = "your-preferred-resource-location"
DEFAULT_RESOURCE_LOCATION = "your-default-resource-location"
MAIN_STORAGE_ACCOUNT_ACCESS_KEY = "your-main-storage-account-access-key"
```
You can find all the information in the Azure Portal under your Azure Machine Learning workspace overview.
Additionally if you want to interact with you storage account also via SDK you can also set the storage account name and access key. The access key can be found in the storage account settings under "Security + Networking > Access keys".

## Setting Up Python Packages
To interact with Azure Machine Learning using Python SDK v2, you need to install the required packages.
We recommend using a virtual or conda environment to manage your dependencies.
We stumbled upon many issues with dependency conflicts when installing the packages.
We recommend recreating our environment for the best experience, however our environment might be outdated in the near future.


If you're working on your local machine you need to install python first. We recommend installing python version that is used in Azure compute instances in AzureML enviorment. In our case we used python 3.10.11.
Then no matter if you're installing locally or on a compute instance use pip to install the required packages in the specified order:
```
azure-ai-ml
mltable
fsspec
azureml-fsspec
"mlflow<3.0.0"
azureml-mlflow
```
If this won't you can try to install the packages in a fresh conda or virtual environment and try installing with our [requirements files](../environment/local-development-environment/pip-requirements-2.txt).

## Authenticating 

This step will depend if you're working on a compute instance in AzureML or on your local machine.

### Authentication on Compute Instance
On Azure ML Compute Instances, the config file should be automatically created for you when you create a new compute instance. This file contains the necessary authentication information to access Azure services.
You don't need to enter you workspace details anywhere.
You can load your workspace using the following code:
```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

try:
    credential = DefaultAzureCredential()
    # Check if given credential can get token successfully.
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:
    # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
    credential = InteractiveBrowserCredential()

from azure.ai.ml import MLClient
# Get a handle to workspace
ml_client = MLClient.from_config(credential=credential)
```

### Local Authentication
Here we assume that you're already authenticated in Azure on your device. For example using Azure CLI `az login`. If not please follow the instruction [here](./../notes/Azure%20-%20Setting%20Up.md).
To authenticate in your local environment use the following code you need to fill in your subscription id, resource group name and workspace name.
```python
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

# Load environment variables from .env file
load_dotenv("<path-to-your-env-file>")

subscription_id = os.environ["<your-subscription-id>"]
resource_group = os.environ["<your-resource-group-name>"]
resource_location = os.environ["<your-resource-location>"]
workspace_name = os.environ["<your-workspace-name>"]

# Authenticate using DefaultAzureCredential (requires subscription_id to be set)
credentials = DefaultAzureCredential()
# Get a handle to workspace
ml_client = MLClient(
    credential=credentials,
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name
)
```

### Verifying the connection
After authenticating you can verify the connection using the following sample code.
```python
try:
    ml_client.workspaces.get("<your-workspace-name>")
    print("Connection verified successfully.")
except Exception as e:
    print("Failed to verify connection.")
    print(e)
```


## Summary

Now you have your Python SDK v2 environment set up and authenticated.

You can start using the Azure ML SDK to interact with your Azure Machine Learning workspace.

[🏠 Return Home](./../README.md)