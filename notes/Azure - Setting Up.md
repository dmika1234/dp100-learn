# 🧰 Preparing Your Environment for DP-100
[🏠 Return Home](./../README.md)

The **DP-100: Designing and Implementing a Data Science Solution on Azure** exam focuses heavily on practical, hands-on experience with Azure services — especially **Azure Machine Learning**.
Before diving into the exercises and labs, you need to set up your development environment and tools.

---

## 1. Get an Azure Subscription

To complete the labs and practice scenarios, you’ll need access to an **Azure subscription** — ideally with **Owner** or **Contributor** permissions so you can create and manage resources.

### 🆓 Options for Free Access

* **[Free Azure Account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)** — includes **$200 credit for 30 days** and limited free-tier services for 12 months.
* **[Azure for Students](https://azure.microsoft.com/en-us/free/students/)** — provides **$100 credit** and free access to core services for 12 months, with **no credit card required**.

> 💡 Tip: Use a separate “sandbox” subscription for experiments to avoid affecting production resources.

---

## 2. Ways to Interact with Azure

Azure provides multiple ways to manage and interact with your cloud resources. For DP-100 preparation, it’s best to be comfortable with several of them.

| Interface                                                                                                         | Description                                                                                                                    | Best For                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| **[Azure Portal](https://portal.azure.com/)**                                                                     | Web-based graphical interface for managing all Azure services.                                                                 | Beginners, exploration, and quick management.      |
| **[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)**              | Command-line tool for managing Azure resources using text commands.                                                            | Automation, scripting, and reproducible setups.    |
| **[Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/new-azureps-module-az?view=azps-12.1.0)** | PowerShell-based automation for Windows and cross-platform environments.                                                       | Users familiar with PowerShell scripting.          |
| **[Azure SDKs](https://learn.microsoft.com/en-us/azure/developer/)**                                              | Software libraries for programming languages (Python, Java, etc.) that let you interact with Azure resources programmatically. | Building machine learning pipelines and apps.      |
| **[Azure Machine Learning Studio](https://ml.azure.com/)**                                                        | Browser-based interface for managing datasets, compute, jobs, and models.                                                      | Training, monitoring, and managing ML experiments. |
| **[Azure AI Foundry Studio](https://ai.azure.com/)**                                                              | Interface for building, testing, and deploying AI solutions.                                                                   | Generative AI workflows and model management.      |

---

## 3. Setting Up Your Development Environment

You can use Azure tools either **locally** or in a **cloud-based environment**.

### ☁️ Cloud-based Options (No Installation Needed)

* **[Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview)**
  Browser-based terminal with Azure CLI and Python pre-installed. Ideal for quick commands.
* **[Azure Machine Learning Notebooks](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2)**
  Cloud-hosted Jupyter environment integrated directly into Azure ML Studio.

### 💻 Local Development Setup

If you prefer to work locally (recommended for flexibility):

#### 1. Install Python

Download and install Python from the [official website](https://www.python.org/downloads/).
Verify the installation:

```bash
python --version
```

#### 2. Install Azure CLI

Follow the [official installation guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).
Verify it’s working:

```bash
az --version
```

#### 3. Authenticate Azure CLI

Log in to your Azure account:

```bash
az login
```

A browser window will open where you can sign in.
(For automation or CI/CD, you can also use a **service principal** for authentication — see [CLI authentication options](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)).

#### 4. Install Azure Machine Learning SDK v2 for Python

Once Python is ready, install the SDK:

```bash
pip install azure-ai-ml
```

This SDK lets you manage and automate Azure Machine Learning operations programmatically.
You can find more examples and setup details in the [Azure Machine Learning SDK v2 documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-ml-readme?view=azure-python).

---

## 4. Recommended Tools for Working with Python SDK

| Tool                                                               | Description                                                          | Notes                                                                          |
| ------------------------------------------------------------------ | -------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)** | Lightweight IDE that integrates with Azure and Jupyter Notebooks.    | Install the **Azure Tools** and **Python** extensions for the best experience. |
| **[Jupyter Notebooks](https://jupyter.org/)**                      | Interactive notebook environment for code, visualization, and notes. | Ideal for experimenting with ML SDK commands.                                  |
| **[Anaconda](https://www.anaconda.com/download)**                  | Python distribution with pre-installed data science libraries.       | Optional but simplifies environment management.                                |

> 💡 Tip: You can open VS Code inside an Azure ML Compute Instance directly from the Studio UI — this gives you a preconfigured cloud dev environment.

---

## 5. Summary

✅ Get an Azure subscription (free, student, or paid)

✅ Learn to use Azure Portal, CLI, and SDK v2

✅ Install and authenticate Azure CLI

✅ Set up Python and the Azure ML SDK v2

✅ Use VS Code or Jupyter for development

Once your environment is ready, you can start exploring:

* Creating workspaces and compute resources
* Registering and versioning datasets
* Submitting jobs using the Python SDK
* Managing and deploying models

[🏠 Return Home](./../README.md)