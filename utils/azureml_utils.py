import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if str(project_dir) not in sys.path:
    sys.path.insert(0, str(project_dir))
from utils.consts import DEV_ENVIRONMENT, AZUREML_SUBSCRIPTION_ID as subscription_id, AZUREML_RESOURCE_GROUP as resource_group, AZUREML_WORKSPACE_NAME as workspace_name
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient




def get_azureml_client():
    """
    Get Azure ML Client based on the development environment.
    If running in Azure ML Compute, use DefaultAzureCredential to get the workspace from config.
    If running locally, use DefaultAzureCredential with explicit subscription, resource group, and workspace name.
    """
    if 'compute' in DEV_ENVIRONMENT.lower():
        try:
            credential = DefaultAzureCredential()
            # Check if given credential can get token successfully.
            credential.get_token("https://management.azure.com/.default")
        except Exception as ex:
            # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
            credential = InteractiveBrowserCredential()
        # Get a handle to workspace
        default_azureml_client = MLClient.from_config(credential=credential)
    else:
        credentials = DefaultAzureCredential()
        default_azureml_client = MLClient(
            credential=credentials,
            subscription_id=subscription_id,
            resource_group_name=resource_group,
            workspace_name=workspace_name
        )
    return default_azureml_client