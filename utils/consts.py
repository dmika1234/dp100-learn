from pathlib import Path
import sys
from dotenv import load_dotenv
import os


target = "dp100-learn"
p = Path(__file__).resolve()
while p.name != target and p.parent != p:
    p = p.parent
project_dir = p
if str(p) not in sys.path:
    sys.path.append(str(p))
print("Added to sys.path:", p)

load_dotenv(os.path.join(project_dir, ".env"))

AZUREML_SUBSCRIPTION_ID = os.getenv("AZUREML_SUBSCRIPTION_ID")
AZUREML_RESOURCE_GROUP = os.getenv("AZUREML_RESOURCE_GROUP")
AZUREML_RESOURCE_LOCATION = os.getenv("AZUREML_RESOURCE_LOCATION")
AZUREML_WORKSPACE_NAME = os.getenv("AZUREML_WORKSPACE_NAME")
AZUREML_STORAGE_ACCOUNT_NAME = os.getenv("AZUREML_STORAGE_ACCOUNT_NAME")
AZUREML_STORAGE_ACCOUNT_ACCESS_KEY = os.getenv("AZUREML_STORAGE_ACCOUNT_ACCESS_KEY")
DEV_ENVIRONMENT = os.getenv("DEV_ENVIRONMENT")


FOUNDRY_PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
FOUNDRY_LABS_MODEL_DEPLOYMENT = os.getenv("FOUNDRY_LABS_MODEL_DEPLOYMENT")

FOUNDRY_OPEN_AI_ENDPOINT = os.getenv("FOUNDRY_OPEN_AI_ENDPOINT")
FOUNDRY_OPEN_AI_KEY = os.getenv("FOUNDRY_OPEN_AI_KEY")
FOUNDRY_CHAT_MODEL = os.getenv("FOUNDRY_CHAT_MODEL")
FOUNDRY_EMBEDDING_MODEL = os.getenv("FOUNDRY_EMBEDDING_MODEL")
FOUNDRY_SEARCH_URL = os.getenv("FOUNDRY_SEARCH_URL")
FOUNDRY_SEARCH_KEY = os.getenv("FOUNDRY_SEARCH_KEY")
FOUNDRY_INDEX_NAME = os.getenv("FOUNDRY_INDEX_NAME")

