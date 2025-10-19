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

**Creating a Compute Instance with Python SDK v2 - Example**
```python
from azure.ai.ml.entities import ComputeInstance

ci_basic_name = "basic-ci-12345"
ci_basic = ComputeInstance(
    name=ci_basic_name, 
    size="STANDARD_DS3_v2"
)
ml_client.begin_create_or_update(ci_basic).result()
```
---

## Creating a Compute Cluster

Configure the following when creating a cluster:

- **`size`** – VM type for each node (CPU or GPU).  
- **`max_instances`** – Maximum number of nodes for scaling and parallel workloads.  
- **`tier`** – Choose **dedicated** (guaranteed availability) or **low-priority** (cheaper, but can be preempted).


**Creating a Compute Cluster with Python SDK v2 - Example**
```python
from azure.ai.ml.entities import AmlCompute

cluster_basic = AmlCompute(
    name="cpu-cluster",
    type="amlcompute",
    size="STANDARD_DS3_v2",
    location="westus",
    min_instances=0,
    max_instances=2,
    idle_time_before_scale_down=120,
    tier="low_priority",
)
ml_client.begin_create_or_update(cluster_basic).result()
```

**Use cases:**
- Running **pipelines** in the Designer.  
- Executing **AutoML** experiments.  
- Submitting **training scripts** as jobs.

**Using a compute cluster in a job - Example**
```python
from azure.ai.ml import command

# configure job
job = command(
    code="./src",
    command="python diabetes-training.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="cpu-cluster",
    display_name="train-with-cluster",
    experiment_name="diabetes-training"
    )

# submit job
returned_job = ml_client.create_or_update(job)
aml_url = returned_job.studio_url
print("Monitor your job at", aml_url)
```


## Environments
Azure Machine Learning builds environment definitions into Docker images and conda environments. When you use an environment, Azure Machine Learning builds the environment on the Azure Container registry associated with the workspace.


## Curated Environments
Curated environments are prebuilt environments for the most common machine learning workloads, available in your workspace by default.

Curated environments use the prefix AzureML- and are designed to provide for scripts that use popular machine learning frameworks and tooling.
## Custom Environments
When you need to create your own environment in Azure Machine Learning to list all necessary packages, libraries, and dependencies to run your scripts, you can create custom environments.

You can define an environment from a Docker image, a Docker build context, and a conda specification with Docker image.

```yml
name: basic-env-cpu
channels:
  - conda-forge
dependencies:
  - python=3.7
  - scikit-learn
  - pandas
  - numpy
  - matplotlib
```


How to create an environments
```python
from azure.ai.ml.entities import Environment

env_docker_conda = Environment(
    image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04", # Base Image
    conda_file="./conda-env.yml",
    name="docker-image-plus-conda-example",
    description="Environment created from a Docker image plus Conda environment.",
)
ml_client.environments.create_or_update(env_docker_conda)
```

## Use environments


Most commonly, you use environments when you want to run a script as a (command) job.

To specify which environment you want to use to run your script, you reference an environment using the <curated-environment-name>:<version> or <curated-environment-name>@latest syntax.


Sample code
```python
from azure.ai.ml import command

# configure job
job = command(
    code="./src",
    command="python train.py",
    environment="docker-image-plus-conda-example:1",
    compute="aml-cluster",
    display_name="train-custom-env",
    experiment_name="train-custom-env"
)

# submit job
returned_job = ml_client.create_or_update(job)
```