# Microsoft Foundry SDK

## Overview

- **Microsoft Foundry SDK**: Centralizes access to services and code libraries for building AI solutions on Azure.
- **Purpose**: Simplifies development by providing a unified programmatic interface for AI projects.

---

## What is the Microsoft Foundry SDK?

- **REST API**: Enables interaction with AI Foundry projects and their resources.
- **Language-Specific SDKs**: Available for Python, .NET, and JavaScript:
  - [Azure AI Projects for Python](https://pypi.org/project/azure-ai-projects)
  - [Azure AI Projects for Microsoft .NET](https://www.nuget.org/packages/Azure.AI.Projects)
  - [Azure AI Projects for JavaScript](https://www.npmjs.com/package/@azure/ai-projects)
- **Core Library**: `Azure AI Projects` – Connects to Foundry projects and accesses defined resources.
- **Note**: SDKs are maintained independently; features may differ between languages.

---

## Installation (Python Example)

```bash
pip install azure-ai-projects
```

- **Authentication**: Requires `azure-identity` package.
  ```bash
  pip install azure-identity
  ```

---

## Connecting to a Project

- **Each project has a unique endpoint** (found in the project’s Overview page in the Foundry portal).
- **Types of Endpoints**:
  - Project endpoint (for connections, agents, models)
  - Azure OpenAI Service APIs
  - Foundry Tools APIs (e.g., Azure Vision, Azure Language)
- **Python Example**:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://......"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)
```

- **Tip**: Run code in an authenticated Azure session (e.g., use `az login`).

- **Reference Image**:  
  ![Project Overview](https://learn.microsoft.com/en-us/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-overview.png#lightbox)

---

## Working with Project Connections

- **Connected Resources**: Defined at both the hub and project level; represent connections to external services (Azure Storage, AI Search, OpenAI, etc.).
- **Accessing Connections**:
  - `connections.list()`: Lists all connections (optionally filter by type, e.g., `ConnectionType.AZURE_OPEN_AI`)
  - `connections.get(connection_name, include_credentials)`: Gets a specific connection (returns credentials if `include_credentials=True`)

- **Python Example**:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://....."
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint,
)

connections = project_client.connections
print("List all connections:")
for connection in connections.list():
    print(f"{connection.name} ({connection.type})")
```

- **Reference Image**:  
  ![Project Connections](https://learn.microsoft.com/en-us/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-connections.png#lightbox)

---

## Creating a Chat Client

- **Scenario**: Connect to a generative AI model and interact via prompts.
- **Advantage**: Use the Foundry SDK to get an authenticated OpenAI chat client for any model deployed in the project (including non-OpenAI models like Microsoft Phi).
- **Python Example**:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI

project_endpoint = "https://......"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint,
)

chat_client = project_client.get_openai_client(api_version="2024-10-21")

user_prompt = input("Enter a question:")

response = chat_client.chat.completions.create(
    model=your_model_deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": user_prompt}
    ]
)
print(response.choices[0].message.content)
```

- **Note**: Requires `openai` package.
  ```bash
  pip install openai
  ```

---

## Summary Table

| Task                        | Key Library/Method                | Notes/References                                                                 |
|-----------------------------|-----------------------------------|----------------------------------------------------------------------------------|
| Install SDK (Python)        | `pip install azure-ai-projects`   | [PyPI](https://pypi.org/project/azure-ai-projects)                               |
| Authenticate                | `azure-identity`                  | `pip install azure-identity`                                                     |
| Connect to Project          | `AIProjectClient`                 | Use project endpoint from portal overview                                        |
| List Connections            | `connections.list()`              | Filter by type if needed                                                         |
| Get Specific Connection     | `connections.get()`               | Returns credentials if requested                                                 |
| Create Chat Client          | `get_openai_client()`             | Use for any deployed model, requires `openai` package                            |
| Reference Images            | Project Overview, Connections     | [Overview](https://learn.microsoft.com/en-us/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-overview.png#lightbox), [Connections](https://learn.microsoft.com/en-us/training/wwl-data-ai/ai-foundry-sdk/media/ai-project-connections.png#lightbox) |

---

**Keep these notes as a quick reference for the Microsoft Foundry SDK section of your DP-100 exam prep.**  
Let me know if you want to add more materials or need further breakdowns!
