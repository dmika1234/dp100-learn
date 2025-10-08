# Azure ML Compute — DP-100 Notes

## Available Compute Types

- **Compute Instance** – Single-user VM for notebooks and experiments. Ideal for development and data exploration. Supports Spark for distributed data processing.  
- **Compute Cluster** – Scalable VM cluster that auto-scales based on workload. Best for training scripts, pipelines, or AutoML jobs. Enables parallel processing.  
- **Kubernetes Cluster (AKS)** – Container-based compute target offering full configuration control. Use Azure Kubernetes Service for cloud or Arc-enabled clusters for on-premises workloads.  
- **Attached Compute** – Attach existing compute (e.g., Azure VMs, Databricks) to your workspace.  
- **Serverless Compute** – Fully managed, on-demand compute for training and pipelines — no infrastructure management required.

---

## Choosing the Right Compute Type

### Experimentation
- **Compute Instance:** Managed Jupyter-like environment in the cloud for dev/testing.  
- **Spark Serverless Compute:** Run distributed Spark code in notebooks.

### Production
- **Compute Cluster:** Scales up during execution, scales down automatically afterward.  
- **Serverless Compute:** Alternative fully managed compute option for training/pipelines.

### Deployment
Depends on prediction type:

1. **Batch (on-demand) predictions**
   - Use **Compute Cluster** or **Serverless Compute** for scalable, on-demand processing (e.g., in pipeline jobs).
2. **Real-time predictions**
   - Deploy models to **containers** or **AKS (Kubernetes)** for live endpoints.

---

## Serverless Compute (When to Use)

Azure ML provides **serverless compute** for certain job types.  
If a job doesn’t specify a compute target, it may automatically run on serverless compute.

### Supported Job Types
- **Command jobs** (including interactive and distributed training)  
- **AutoML jobs**  
- **Sweep jobs**  
- **Parallel jobs**

### Benefits
- No need to manage clusters — Azure automatically handles VM size and scaling.  
- Avoids **cluster warm-up** and **idle costs** for short or bursty jobs.  
- Ideal for **on-demand** and **quick** workloads.  
- You must still specify a valid **environment** (Docker image or curated environment).  
- Be aware of **subscription quota limits**; check before using serverless heavily.

🔗 [Serverless compute docs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-serverless-compute?view=azureml-api-2&tabs=python)  
🔗 [Quota management](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2#view-your-usage-and-quotas-in-the-azure-portal)

---

## Creating a Compute Instance

- Each instance must have a **unique name per Azure region**.  
- Can be **created via script** for automation (package setup, repo cloning, etc.).  
- Assigned to a **single user**, not for parallel workloads.  
- Admins can pre-assign instances to users.  
- Configure **idle shutdown** or **start/stop schedules** to save costs.  
  🔗 [Docs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-compute-instance?view=azureml-api-2&tabs=python)

---

## Creating a Compute Cluster

Configure the following when creating a cluster:

- **`size`** – VM type for each node (CPU or GPU).  
- **`max_instances`** – Maximum number of nodes for scaling and parallel workloads.  
- **`tier`** – Choose **dedicated** (guaranteed availability) or **low-priority** (cheaper, but can be preempted).

**Use cases:**
- Running **pipelines** in the Designer.  
- Executing **AutoML** experiments.  
- Submitting **training scripts** as jobs.
