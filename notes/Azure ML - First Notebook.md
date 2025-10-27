# Setting Up Python SDK v2 Environment for Azure Machine Learning
[🏠 Return Home](./../README.md)

For data scientists the most convenient way to interact with Azure Machine Learning is through the **Azure ML Python SDK v2**.  
This SDK allows you to programmatically manage Azure ML resources, submit experiments, and deploy models directly from your local machine or development environment.
Before you start diving into specific Azure Machine Learning tasks, it’s essential to learn how to setup your Python SDK v2 environment.
As you probably now Jupyter Notebooks are ideal for analyzing, experimenting with the data and creating machine learning models prototypes.
if you're interacting with Azure Machine Learning on your local machine you can use Jupyter Notebooks in most IDEs including Visual Studio Code.
If you prefer a cloud-based solution, you can use [Azure Machine Learning Notebooks](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2).

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
We recommend recreating our environment for the best experience, however our environment might be outdated in the 



[🏠 Return Home](./../README.md)