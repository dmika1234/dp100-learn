import os
from azure.identity import DefaultAzureCredential


STUDENT_SUBSCRIPTION_ID = os.environ["STUDENT_SUBSCRIPTION_ID"]
azure_credential = DefaultAzureCredential()


DEFAULT_RESOURCE_LOCATION = "eastus"
PREFERED_RESOURCE_LOCATION = "polandcentral"



