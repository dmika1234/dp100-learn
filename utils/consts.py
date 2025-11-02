import os
import sys
from dotenv import load_dotenv


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if str(project_dir) not in sys.path:
    sys.path.insert(0, str(project_dir))
load_dotenv(os.path.join(project_dir, ".env"))

AZUREML_SUBSCRIPTION_ID = os.getenv("AZUREML_SUBSCRIPTION_ID")
AZUREML_RESOURCE_GROUP = os.getenv("AZUREML_RESOURCE_GROUP")
AZUREML_RESOURCE_LOCATION = os.getenv("AZUREML_RESOURCE_LOCATION")
AZUREML_WORKSPACE_NAME = os.getenv("AZUREML_WORKSPACE_NAME")
AZUREML_STORAGE_ACCOUNT_NAME = os.getenv("AZUREML_STORAGE_ACCOUNT_NAME")
AZUREML_STORAGE_ACCOUNT_ACCESS_KEY = os.getenv("AZUREML_STORAGE_ACCOUNT_ACCESS_KEY")
DEV_ENVIRONMENT = os.getenv("DEV_ENVIRONMENT")

