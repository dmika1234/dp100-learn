# Azure ML Compute Targets — DP-100 Notes

## Available Compute Types

- **Compute Instance** – A single-user VM for running notebooks and experiments. Ideal for development and exploration. Supports Spark for distributed processing.
- **Compute Cluster** – A scalable cluster of VMs that automatically scales up or down based on workload. Suitable for running scripts, pipelines, or AutoML jobs. Supports parallel processing for faster execution.
- **Kubernetes Cluster** – A compute target based on Kubernetes technology, offering full control over configuration and management. You can attach your own Azure Kubernetes Service (AKS) cluster for cloud compute or an Arc-enabled cluster for on-premises workloads.
- **Attached Compute** – Lets you attach existing compute resources (e.g., Azure VMs, Databricks clusters) to your workspace.
- **Serverless Compute** – Fully managed, on-demand compute used for training or pipeline jobs without managing infrastructure.

---

## Choosing a Compute Type

- **Experimentation:**  
  Use a **compute instance** for running notebooks interactively (similar to local development). For distributed workloads, use **Spark serverless compute**.

- **Production:**  
  For automated or large-scale jobs, use a **compute cluster** or **serverless compute** — both are scalable and cost-efficient.

- **Deployment:**  
  - **Batch predictions:** Use **compute clusters** or **serverless compute** for running pipeline jobs on-demand.  
  - **Real-time predictions:** Use **lightweight containers** for continuous endpoints. Azure ML manages these automatically for managed online endpoints, or you can attach a **Kubernetes cluster** for custom real-time deployments.

---

## Creating a Compute Instance

- Each compute instance must have a **unique name within an Azure region**.  
- You can also **create compute instances via script** to automate package installation, repository cloning, and consistent setup for multiple users ([docs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-customize-compute-instance?view=azureml-api-2&azure-portal=true)).  
- A compute instance is **assigned to a single user** and cannot process parallel workloads. Admins can assign instances to users during creation.  
- To **save costs**, configure **idle shutdown** or **start/stop schedules** ([details](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-compute-instance?view=azureml-api-2&tabs=python)).

---

## Creating a Compute Cluster

When creating a cluster, configure:

- **`size`** – VM type for each node (CPU or GPU).  
- **`max_instances`** – Maximum number of nodes for scaling and parallel workloads.  
- **`tier`** – Choose between **dedicated** or **low-priority** VMs (lower cost but not guaranteed availability).

**Use cases:**
- Running **pipeline jobs** built in the Designer.  
- Running **Automated ML** experiments.  
- Running **scripts** as jobs.
