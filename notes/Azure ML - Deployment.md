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

## Deploy your model

To deploy to a managed online endpoint you must provide:

* **Model assets** — model file(s) or a registered model.
* **Scoring script** — how to load the model and run inference.
* **Environment** — dependencies required on the endpoint’s compute.
* **Compute configuration** — VM size, instance count, and scaling rules.

### Blue/green deployment

Managed endpoints support multiple deployments under a single endpoint. You route traffic (e.g., 90/10 split) between deployments to safely test and roll out new model versions with zero downtime.

---

## Create an endpoint

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

## Deploy an MLflow model (recommended)

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

## Deploy a custom model to a managed online endpoint

For custom models you provide the model files, scoring script, and environment.

### Create a scoring script

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

### Create the deployment

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

## Test managed online endpoints

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

## Additional Materials

* [Azure Labs: Deploy a model to a managed online endpoint](https://learn.microsoft.com/en-us/training/modules/manage-compare-models-azure-machine-learning/)
* [Notebook: Deploy to online endpoint](azure-labs/azure-ml-dev/Labs/10/Deploy%20to%20online%20endpoint.ipynb)
* [Azure Labs: Deploy a model to a batch endpoint](https://learn.microsoft.com/en-us/training/modules/deploy-model-batch-endpoint/)
* [Notebook: Deploy to batch endpoint](azure-labs/azure-ml-dev/Labs/10/Deploy%20to%20batch%20endpoint.ipynb)

---

If you want, I can produce a matching **Batch Endpoints** section (clean + compact, like above).
