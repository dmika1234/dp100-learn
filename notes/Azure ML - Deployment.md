# Model Deployment in Azure Machine Learning

After training a model, you typically deploy it so applications can perform inference on new, unseen data. Azure Machine Learning supports two main deployment patterns:

* **Online Endpoints** — real-time, low-latency predictions for single or small batches of data.
* **Batch Endpoints** — large-scale, asynchronous batch scoring jobs.

---

## Online Endpoints

An online endpoint is an HTTPS endpoint that accepts input data and returns scored predictions almost instantly. The service hosts your scoring script, loads the model, performs inferencing, and returns the prediction.

### Endpoint Types

Azure Machine Learning supports two types of online endpoints:

* **Managed online endpoints** — Azure ML manages all underlying infrastructure; you only configure VM type and scaling.
* **Kubernetes online endpoints** — you manage your own Kubernetes cluster for full control and advanced configurations.

---

### Deploy your model

To deploy to a managed online endpoint you must provide:

* **Model assets** — model file(s) or a registered model.
* **Scoring script** — how to load the model and run inference.
* **Environment** — dependencies required on the endpoint’s compute.
* **Compute configuration** — VM size, instance count, and scaling rules.

#### Blue/green deployment

Managed endpoints support multiple deployments under a single endpoint. You route traffic (e.g., 90/10 split) between deployments to safely test and roll out new model versions with zero downtime.

---

### Create an endpoint

Create an endpoint using `ManagedOnlineEndpoint`:

```python
from azure.ai.ml.entities import ManagedOnlineEndpoint

endpoint = ManagedOnlineEndpoint(
    name="endpoint-example",
    description="Online endpoint",
    auth_mode="key",
)

ml_client.begin_create_or_update(endpoint).result()
```

---

### Deploy an MLflow model (recommended)

MLflow models are the simplest to deploy because Azure ML automatically handles scoring scripts and environments.

Required compute configuration:

* `instance_type` — supported VM SKU.
* `instance_count` — number of replicas.

```python
from azure.ai.ml.entities import Model, ManagedOnlineDeployment
from azure.ai.ml.constants import AssetTypes

model = Model(
    path="./model",
    type=AssetTypes.MLFLOW_MODEL,
    description="my sample mlflow model",
)

blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name="endpoint-example",
    model=model,
    instance_type="Standard_F4s_v2",
    instance_count=1,
)

ml_client.online_deployments.begin_create_or_update(blue_deployment).result()
```

Route 100% traffic to this deployment:

```python
endpoint.traffic = {"blue": 100}
ml_client.begin_create_or_update(endpoint).result()
```

Delete the endpoint and all deployments:

```python
ml_client.online_endpoints.begin_delete(name="endpoint-example")
```

---

### Deploy a custom model to a managed online endpoint

For custom models you provide the model files, scoring script, and environment.

#### Create a scoring script

```python
import json
import joblib
import numpy as np
import os

def init():
    global model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    data = np.array(json.loads(raw_data)["data"])
    predictions = model.predict(data)
    return predictions.tolist()
```

#### Create the deployment

```python
from azure.ai.ml.entities import ManagedOnlineDeployment, CodeConfiguration

blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name="endpoint-example",
    model=model,
    environment="deployment-environment",
    code_configuration=CodeConfiguration(
        code="./src",
        scoring_script="score.py",
    ),
    instance_type="Standard_DS2_v2",
    instance_count=1,
)

ml_client.online_deployments.begin_create_or_update(blue_deployment).result()
```

---

### Test managed online endpoints

You can test directly in Azure ML Studio or invoke via the Python SDK.
Requests must follow this format:

```json
{
  "data": [
    [0.1, 2.3, 4.1, 2.0],
    [0.2, 1.8, 3.9, 2.1]
  ]
}
```

Invoke:

```python
response = ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="blue",
    request_file="sample-data.json",
)

print(response)
```

---
## Batch endpoints

A batch endpoint is an HTTPS endpoint that you can call to trigger a batch scoring job. The advantage of such an endpoint is that you can trigger the batch scoring job from another service, such as Azure Synapse Analytics or Azure Databricks. A batch endpoint allows you to integrate the batch scoring with an existing data ingestion and transformation pipeline.

Whenever the endpoint is invoked, a batch scoring job is submitted to the Azure Machine Learning workspace. The job typically uses a compute cluster to score multiple inputs. The results can be stored in a datastore, connected to the Azure Machine Learning workspace.

### Create a batch endpoint
To deploy a model to a batch endpoint, you'll first have to create the batch endpoint.

To create a batch endpoint, you'll use the `BatchEndpoint` class. Batch endpoint names need to be unique within an Azure region.

To create an endpoint, use the following command:

```Python
# create a batch endpoint
endpoint = BatchEndpoint(
    name="endpoint-example",
    description="A batch endpoint",
)

ml_client.batch_endpoints.begin_create_or_update(endpoint)
```

You can deploy multiple models to a batch endpoint. Whenever you call the batch endpoint, which triggers a batch scoring job, the default deployment will be used unless specified otherwise. 

The ideal compute to use for batch deployments is the Azure Machine Learning compute cluster. If you want the batch scoring job to process the new data in parallel batches, you need to provision a compute cluster with more than one maximum instances.

### Deplying MLflow model

An easy way to deploy a model to a batch endpoint is to use an MLflow model. Azure Machine Learning will automatically generate the scoring script and environment for MLflow models.

To deploy an MLflow model to a batch endpoint, you'll use the `BatchDeployment` class.

When you deploy a model, you'll need to specify how you want the batch scoring job to behave. The advantage of using a compute cluster to run the scoring script (which is automatically generated by Azure Machine Learning), is that you can run the scoring script on separate instances in parallel.

When you configure the model deployment, you can specify:
- `instance_count`: Count of compute nodes to use for generating predictions.
- `max_concurrency_per_instance`: Maximum number of parallel scoring script runs per compute node.
- `mini_batch_size`: Number of files passed per scoring script run.
- `output_action`: What to do with the predictions: summary_only or append_row.
- `output_file_name`: File to which predictions will be appended, if you choose append_row for output_action.


```Python
from azure.ai.ml.entities import BatchDeployment, BatchRetrySettings
from azure.ai.ml.constants import BatchDeploymentOutputAction

deployment = BatchDeployment(
    name="forecast-mlflow",
    description="A sales forecaster",
    endpoint_name=endpoint.name,
    model=model,
    compute="aml-cluster",
    instance_count=2,
    max_concurrency_per_instance=2,
    mini_batch_size=2,
    output_action=BatchDeploymentOutputAction.APPEND_ROW,
    output_file_name="predictions.csv",
    retry_settings=BatchRetrySettings(max_retries=3, timeout=300),
    logging_level="info",
)
ml_client.batch_deployments.begin_create_or_update(deployment)
```

### Deploy custome model
If you want to deploy a model to a batch endpoint without using the MLflow model format, you need to create the scoring script and environment.

#### Create the scoring script
The scoring script is a file that reads the new data, loads the model, and performs the scoring.

The scoring script must include two functions:

- `init()`: Called once at the beginning of the process, so use for any costly or common preparation like loading the model.
- `run()`: Called for each mini batch to perform the scoring.
The `run()` method should return a pandas DataFrame or an array/list.

A scoring script may look as follows:

```Python
import os
import mlflow
import pandas as pd


def init():
    global model

    # get the path to the registered model file and load it
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")
    model = mlflow.pyfunc.load(model_path)


def run(mini_batch):
    print(f"run method start: {__file__}, run({len(mini_batch)} files)")
    resultList = []

    for file_path in mini_batch:
        data = pd.read_csv(file_path)
        pred = model.predict(data)

        df = pd.DataFrame(pred, columns=["predictions"])
        df["file"] = os.path.basename(file_path)
        resultList.extend(df.values)

    return resultList
```
There are some things to note from the example script:

- `AZUREML_MODEL_DIR` is an environment variable that you can use to locate the files associated with the model.
- Use `global` variable to make any assets available that are needed to score the new data, like the loaded model.
- The size of the `mini_batch` is defined in the deployment configuration. If the files in the mini batch are too large to be processed, you need to split the files into smaller files.
- By default, the predictions will be written to one single file.

### Configure and create the deployment
Your deployment requires an execution environment in which to run the scoring script. Any dependency your code requires should be included in the environment.


Finally, you can configure and create the deployment with the `BatchDeployment` class.

```Python
from azure.ai.ml.entities import BatchDeployment, BatchRetrySettings
from azure.ai.ml.constants import BatchDeploymentOutputAction

deployment = BatchDeployment(
    name="forecast-mlflow",
    description="A sales forecaster",
    endpoint_name=endpoint.name,
    model=model,
    compute="aml-cluster",
    code_path="./code",
    scoring_script="score.py",
    environment=env,
    instance_count=2,
    max_concurrency_per_instance=2,
    mini_batch_size=2,
    output_action=BatchDeploymentOutputAction.APPEND_ROW,
    output_file_name="predictions.csv",
    retry_settings=BatchRetrySettings(max_retries=3, timeout=300),
    logging_level="info",
)
ml_client.batch_deployments.begin_create_or_update(deployment)
```

### Invoke and troubleshoot batch endpoints
When you invoke a batch endpoint, you trigger an Azure Machine Learning pipeline job. The job will expect an input parameter pointing to the data set you want to score.


#### Trigger the batch scoring job
To prepare data for batch predictions, you can register a folder as a data asset in the Azure Machine Learning workspace.

You can then use the registered data asset as input when invoking the batch endpoint with the Python SDK:
```python
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes

input = Input(type=AssetTypes.URI_FOLDER, path="azureml:new-data:1")

job = ml_client.batch_endpoints.invoke(
    endpoint_name=endpoint.name, 
    input=input
)
```

## Additional Materials

* [Azure Labs: Deploy a model to a managed online endpoint](https://learn.microsoft.com/en-us/training/modules/manage-compare-models-azure-machine-learning/)
* [Notebook: Deploy to online endpoint](azure-labs/azure-ml-dev/Labs/10/Deploy%20to%20online%20endpoint.ipynb)
* [Azure Labs: Deploy a model to a batch endpoint](https://learn.microsoft.com/en-us/training/modules/deploy-model-batch-endpoint/)
* [Notebook: Deploy to batch endpoint](azure-labs/azure-ml-dev/Labs/10/Deploy%20to%20batch%20endpoint.ipynb)

---

If you want, I can produce a matching **Batch Endpoints** section (clean + compact, like above).
