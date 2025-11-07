from pathlib import Path
import sys
from utils.consts import DEV_ENVIRONMENT, AZUREML_SUBSCRIPTION_ID as subscription_id, AZUREML_RESOURCE_GROUP as resource_group, AZUREML_WORKSPACE_NAME as workspace_name
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient
from azure.core.exceptions import ResourceNotFoundError
import warnings

target = "dp100-learn"
p = Path(__file__).resolve()
while p.name != target and p.parent != p:
    p = p.parent
project_dir = p
if str(p) not in sys.path:
    sys.path.append(str(p))
print("Added to sys.path:", p)


def get_azureml_client():
    """
    Get an Azure ML Client based on the current environment.
    - If running on Azure ML compute, use workspace config.
    - If running locally, use explicit parameters.
    - If the workspace does not exist, warn and return an MLClient without a workspace.
    """

    # Try DefaultAzureCredential, fall back to InteractiveBrowserCredential if needed
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception:
        credential = InteractiveBrowserCredential()

    try:
        if 'compute' in DEV_ENVIRONMENT.lower():
            ml_client = MLClient.from_config(credential=credential)
        else:
            ml_client = MLClient(
                credential=credential,
                subscription_id=subscription_id,
                resource_group_name=resource_group,
                workspace_name=workspace_name
            )
        # Validate workspace existence by calling a simple method
        _ = ml_client.workspaces.get(workspace_name)
    except ResourceNotFoundError:
        warnings.warn(
            f"⚠️ Azure ML workspace '{workspace_name}' not found. "
            "Creating MLClient without a workspace context."
        )
        ml_client = MLClient(
            credential=credential,
            subscription_id=subscription_id,
            resource_group_name=resource_group
        )
    except Exception as e:
        warnings.warn(
            f"⚠️ Unable to connect to Azure ML workspace: {e}. "
            "Returning client without workspace context."
        )
        ml_client = MLClient(
            credential=credential,
            subscription_id=subscription_id,
            resource_group_name=resource_group
        )

    return ml_client
