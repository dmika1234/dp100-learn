# Using MLflow in Azure Machine Learning


## What is MLflow?
MLflow is an open-source library for tracking and managing your machine learning experiments. In particular, MLflow Tracking is a component of MLflow that logs everything about the model you're training, such as parameters, metrics, and artifacts.

## Configure MLflow in notebooks

First you need to install necessary packages:
```
pip install mlflow
pip install azureml-mlflow
```

*NOTE*: To use MLflow on your local device you also need to set `mlflow.set_tracking_uri = "MLFLOW-TRACKING-URI"`. You can find the URL on the Azure ML resource page or extract it using this code `ml_client.workspaces.get("<your-workspace-name>").mlflow_tracking_uri`.


## Create an MLflow experiment
You can create a MLflow experiment, which allows you to group runs. If you don't create an experiment, MLflow will assume the default experiment with name Default.

To create an experiment, run the following command in a notebook:


```python
import mlflow

mlflow.set_experiment(experiment_name="heart-condition-classifier")
```

## Log results with MLflow
To start a run tracked by MLflow, you'll use `start_run()`. To track the model, you can:
- Enable **autologging**.
- Use **custom logging**.


### Enable autologging
MLflow supports automatic logging for popular machine learning libraries. If you're using a library that is supported by autolog, then MLflow tells the framework you're using to log all the metrics, parameters, artifacts, and models that the framework considers relevant.

You can turn on autologging by using the `autolog` method for the framework you're using. For example, to enable autologging for XGBoost models you can use `mlflow.xgboost.autolog()`.

The model is logged when the `.fit()` method is called. The framework you use to train your model is identified and included as the flavor of your model.

Optionally, you can specify which flavor you want your model to be identified as by using `mlflow.<flavor>.autolog()`. Some common flavors that you can use with autologging are:
- Keras: `mlflow.keras.autolog()`
- Scikit-learn: `mlflow.sklearn.autolog()`
- LightGBM: `mlflow.lightgbm.autolog()`
- XGBoost: `mlflow.xgboost.autolog()`
- TensorFlow: `mlflow.tensorflow.autolog()`
- PyTorch: `mlflow.pytorch.autolog()`
- ONNX: `mlflow.onnx.autolog()`


A notebook cell that trains and tracks a classification model using autologging may be similar to the following code example:
```python
from xgboost import XGBClassifier

with mlflow.start_run():
    mlflow.xgboost.autolog()

    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
```

### Use custom logging
Additionally, you can manually log your model with MLflow. Manually logging models is helpful when you want to log supplementary or custom information that isn't logged through autologging.
*NOTE*: You can choose to only use custom logging, or use custom logging in combination with autologging.


Common functions used with custom logging are:

- `mlflow.log_param()`: Logs a single key-value parameter. Use this function for an input parameter you want to log.
- `mlflow.log_metric`(): Logs a single key-value metric. Value must be a number. Use this function for any output you want to store with the run.
- `mlflow.log_artifact`(): Logs a file. Use this function for any plot you want to log, save as image file first.
- `mlflow.log_model`(): Logs a model. Use this function to create an MLflow model, which may include a custom signature, environment, and input examples.
To use custom logging in a notebook, start a run and log any metric you want:
```python
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

with mlflow.start_run():
    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
```
## Retrieve metrics with MLflow in a notebook

When you run a training script as a job in Azure Machine Learning, and track your model training with MLflow, you can query the runs in a notebook by using MLflow. Using MLflow in a notebook gives you more control over which runs you want to retrieve to compare.

When using MLflow to query your runs, you'll refer to experiments and runs.

### Search all the experiments

You can get all the active experiments in the workspace using MLFlow:
```python
experiments = mlflow.search_experiments(max_results=2)
for exp in experiments:
    print(exp.name)
```

If you want to retrieve archived experiments too, then include the option `ViewType.ALL`:
```python
from mlflow.entities import ViewType

experiments = mlflow.search_experiments(view_type=ViewType.ALL)
for exp in experiments:
    print(exp.name)
```
To retrieve a specific experiment, you can run:
```python
exp = mlflow.get_experiment_by_name(experiment_name)
print(exp)
```

### Retrieve runs

MLflow allows you to search for runs inside of any experiment. You need either the experiment ID or the experiment name.

For example, when you want to retrieve the metrics of a specific run:
```python
mlflow.search_runs(exp.experiment_id)
```

You can search runs across multiple experiments if necessary. Searching across experiments may be useful in case you want to compare runs of the same model when it's being logged in different experiments (by different people or different project iterations).

You can use `search_all_experiments=True` if you want to search across all the experiments in the workspace.

By default, experiments are ordered descending by `start_time`, which is the time the experiment was queued in Azure Machine Learning. However, you can change this default by using the parameter `order_by`.

For example, if you want to sort by start time and only show the last two results:


```python
mlflow.search_runs(exp.experiment_id, order_by=["start_time DESC"], max_results=2)
```
You can also look for a run with a specific combination in the hyperparameters:


```python
mlflow.search_runs(
    exp.experiment_id, filter_string="params.num_boost_round='100'", max_results=2
)
```
You can use search runs or experiments (`mlflow.search_runs()` or `mlflow.search_experiments()`) with additional comparators for string or numeric attributes. Find out more in the [documentation](https://mlflow.org/docs/latest/ml/search/search-runs/)

*NOTE*: Some capabilites and logging artifacts for MLflow 3.+ are not supported by `azure-mlflow` . So we suggest to downgrade the `mlflow` package (<3.0.0).

## Hyperparameters tuning with MLflow

To help you choose the best performing model Azure Machine Learning together with MLflow brings a set of tools that will help you achieve that. There are four main steps that you should do:
- Define a hyperparameter search space.
- Configure hyperparameter sampling.
- Select an early-termination policy.
- Run a sweep job.


### Define a search space


The set of hyperparameter values tried during hyperparameter tuning is known as the **search space**. The definition of the range of possible values that can be chosen depends on the type of hyperparameter.

#### Discrete hyperparameters

Some hyperparameters require _discrete_ values - in other words, you must select the value from a particular _finite_ set of possibilities. You can define a search space for a discrete parameter using a **Choice** from a list of explicit values, which you can define as a Python **list** (`Choice(values=[10,20,30])`), a **range** (`Choice(values=range(1,10))`), or an arbitrary set of comma-separated values (`Choice(values=(30,50,100))`)

You can also select discrete values from any of the following discrete distributions:

*   `QUniform(min_value, max_value, q)`: Returns a value like round(Uniform(min\_value, max\_value) / q) \* q
*   `QLogUniform(min_value, max_value, q)`: Returns a value like round(exp(Uniform(min\_value, max\_value)) / q) \* q
*   `QNormal(mu, sigma, q)`: Returns a value like round(Normal(mu, sigma) / q) \* q
*   `QLogNormal(mu, sigma, q)`: Returns a value like round(exp(Normal(mu, sigma)) / q) \* q

#### Continuous hyperparameters

Some hyperparameters are _continuous_ - in other words you can use any value along a scale, resulting in an _infinite_ number of possibilities. To define a search space for these kinds of value, you can use any of the following distribution types:

*   `Uniform(min_value, max_value)`: Returns a value uniformly distributed between min\_value and max\_value
*   `LogUniform(min_value, max_value)`: Returns a value drawn according to exp(Uniform(min\_value, max\_value)) so that the logarithm of the return value is uniformly distributed
*   `Normal(mu, sigma)`: Returns a real value that's normally distributed with mean mu and standard deviation sigma
*   `LogNormal(mu, sigma)`: Returns a value drawn according to exp(Normal(mu, sigma)) so that the logarithm of the return value is normally distributed

#### Defining a search space

To define a search space for hyperparameter tuning, create a dictionary with the appropriate parameter expression for each named hyperparameter.

For example, the following search space indicates that the `batch_size` hyperparameter can have the value 16, 32, or 64, and the `learning_rate` hyperparameter can have any value from a normal distribution with a mean of 10 and a standard deviation of 3.

```python
from azure.ai.ml.sweep import Choice, Normal

command_job_for_sweep = job(
    batch_size=Choice(values=[16, 32, 64]),    
    learning_rate=Normal(mu=10, sigma=3),
)
```

- - -
### Configure a sampling method

There are three main sampling methods available in Azure Machine Learning:

*   **Grid sampling**: Tries every possible combination. Grid sampling can only be applied when all hyperparameters are discrete, and is used to try every possible combination of parameters in the search space.
*   **Random sampling**: Randomly chooses values from the search space.
    *   **Sobol**: Adds a seed to random sampling to make the results reproducible.
*   **Bayesian sampling**: Chooses new values based on previous results. You can only use Bayesian sampling with **choice**, **uniform**, and **quniform** parameter expressions.


To use for example grid sampling you need to run the following code

```python
sweep_job = command_job_for_sweep.sweep(
    sampling_algorithm = "grid",
    ...
)
```

Sobol sampling requires slightly different syntax presented below.
```python
from azure.ai.ml.sweep import RandomSamplingAlgorithm

sweep_job = command_job_for_sweep.sweep(
    sampling_algorithm = RandomSamplingAlgorithm(seed=123, rule="sobol"),
    ...
)
```

---

### Early Termination Policies
Early termination policies allow you to stop underperforming runs before they complete, which can save time and computational resources.

There are two main parameters when you choose to use an early termination policy:

- `evaluation_interval`: Specifies at which interval you want the policy to be evaluated. Every time the primary metric is logged for a trial counts as an interval.
- `delay_evaluation`: Specifies when to start evaluating the policy. This parameter allows for at least a minimum of trials to complete without an early termination policy affecting them.

Azure Machine Learning supports several early termination policies.

- **Bandit policy**: Uses a `slack_factor` (relative) or `slack_amount`(absolute). Any new model must perform within the slack range of the best performing model.
- **Median stopping policy**: Uses the median of the averages of the primary metric. Any new model must perform better than the median.
- **Truncation selection policy**: Uses a `truncation_percentage`, which is the percentage of lowest performing trials. Any new model must perform better than the lowest performing trials.


To configure a bandit early termination policy, you can use the following code:
```python
from azure.ai.ml.sweep import BanditPolicy

early_termination_policy = BanditPolicy(
    slack_factor=0.2
    evaluation_interval=1,
    delay_evaluation=5,
)
```

### Run a sweep job
To run a sweep job, you need to create a training script just the way you would do for any other training job, except that your script **must**:

- Include an argument for each hyperparameter you want to vary.
- Log the target performance metric with MLflow. A logged metric enables the sweep job to evaluate the performance of the trials it initiates, and identify the one that produces the best performing model.


#### Configure and run a sweep job
To prepare the sweep job, you must first create a base command job that specifies which script to run and defines the parameters used by the script:

```Python
from azure.ai.ml import command

# configure command job as base
job = command(
    code="./src",
    command="python train.py --regularization ${{inputs.reg_rate}}",
    inputs={
        "reg_rate": 0.01,
    },
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="aml-cluster",
    )
```
You can then override your input parameters with your search space:

```Python
from azure.ai.ml.sweep import Choice

command_job_for_sweep = job(
    reg_rate=Choice(values=[0.01, 0.1, 1]),
)
```
Finally, call `sweep()` on your command job to sweep over your search space:

```Python
from azure.ai.ml import MLClient

# apply the sweep parameter to obtain the sweep_job
sweep_job = command_job_for_sweep.sweep(
    compute="aml-cluster",
    sampling_algorithm="grid",
    primary_metric="Accuracy",
    goal="Maximize",
)

# set the name of the sweep job experiment
sweep_job.experiment_name="sweep-example"

# define the limits for this sweep
sweep_job.set_limits(max_total_trials=4, max_concurrent_trials=2, timeout=7200)

# submit the sweep
returned_sweep_job = ml_client.create_or_update(sweep_job)
```

### Monitor and review sweep jobs
You can monitor sweep jobs in Azure Machine Learning studio. The sweep job will initiate trials for each hyperparameter combination to be tried. For each trial, you can review all logged metrics.

Additionally, you can evaluate and compare models by visualizing the trials in the studio. You can adjust each chart to show and compare the hyperparameter values and metrics for each trial.



## Register an MLflow model in Azure Machine Learning
Azure Machine Learning allows you to easily deploy models that you train and track with Mlflow. For example, when you have an MLflow model, you can opt for the no-code deployment in Azure Machine Learning.


>*NOTE: Some types of models are currently not supported by Azure Machine Learning and MLflow. In that case, you can register a custom model. Learn more about how to work with [(custom) models in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-models?view=azureml-api-2&tabs=cli).*

### Use autologging to log a model
When you train a model, you can include `mlflow.autolog()` to enable autologging. MLflow's autologging automatically logs parameters, metrics, artifacts, and the model you train. When you use autologging, an output folder is created which includes all necessary model artifacts, including the `MLmodel` file that references these files and includes the model's metadata.

### Manually log a model
When you want to have more control over how the model is logged, you can use autolog (for your parameters, metrics, and other artifacts), and set `log_models=False`. When you set the `log_models` parameter to false, MLflow doesn't automatically log the model, and you can add it manually.

Logging the model allows you to easily deploy the model. To specify how the model should behave at inference time, you can customize the model's expected inputs and outputs. The schemas of the expected inputs and outputs are defined as the signature in the `MLmodel` file.

#### Customize the signature
The model signature defines the schema of the model's inputs and outputs. The signature is stored in JSON format in the `MLmodel` file, together with other metadata of the model.

The model signature can be inferred from datasets or created manually by hand.

To log a model with a signature that is inferred from your training dataset and model predictions, you can use `infer_signature()`. For example, the following example takes the training dataset to infer the schema of the inputs, and the model's predictions to infer the schema of the output:
```python
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

iris = datasets.load_iris()
iris_train = pd.DataFrame(iris.data, columns=iris.feature_names)
clf = RandomForestClassifier(max_depth=7, random_state=0)
clf.fit(iris_train, iris.target)

# Infer the signature from the training dataset and model's predictions
signature = infer_signature(iris_train, clf.predict(iris_train))

# Log the scikit-learn model with the custom signature
mlflow.sklearn.log_model(clf, "iris_rf", signature=signature)
```
Alternatively, you can create the signature manually:
```python
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec

# Define the schema for the input data
input_schema = Schema([
  ColSpec("double", "sepal length (cm)"),
  ColSpec("double", "sepal width (cm)"),
  ColSpec("double", "petal length (cm)"),
  ColSpec("double", "petal width (cm)"),
])

# Define the schema for the output data
output_schema = Schema([ColSpec("long")])

# Create the signature object
signature = ModelSignature(inputs=input_schema, outputs=output_schema)
```

### Understand the MLflow model format
MLflow uses the MLmodel format to store all relevant model assets in a folder or directory. One essential file in the directory is the `MLmodel` file. The `MLmodel` file is the single source of truth about how the model should be loaded and used.

Explore the `MLmodel` file format
The `MLmodel` file may include:
- `artifact_path`: During the training job, the model is logged to this path.
- `flavor`: The machine learning library with which the model was created.
- `model_uuid`: The unique identifier of the registered model.
- `run_id`: The unique identifier of job run during which the model was created.
- `signature`: Specifies the schema of the model's inputs and outputs:
- `inputs`: Valid input to the model. For example, a subset of the training dataset.
- `outputs`: Valid model output. For example, model predictions for the input dataset.

An example of a MLmodel file created for a computer vision model trained with fastai may look like:
```yml
artifact_path: classifier
flavors:
  fastai:
    data: model.fastai
    fastai_version: 2.4.1
  python_function:
    data: model.fastai
    env: conda.yaml
    loader_module: mlflow.fastai
    python_version: 3.8.12
model_uuid: e694c68eba484299976b06ab9058f636
run_id: e13da8ac-b1e6-45d4-a9b2-6a0a5cfac537
signature:
  inputs: '[{"type": "tensor",
             "tensor-spec": 
                 {"dtype": "uint8", "shape": [-1, 300, 300, 3]}
           }]'
  outputs: '[{"type": "tensor", 
              "tensor-spec": 
                 {"dtype": "float32", "shape": [-1,2]}
            }]'
```

#### Choose the flavor
A flavor is the machine learning library with which the model was created. Flavor in MLflow tells you how a model should be persisted and loaded. Because each model flavor indicates how they want to persist and load models, the MLModel format doesn't enforce a single serialization mechanism that all the models need to support.

**Python function** flavor is the default model interface for models created from an MLflow run. Any MLflow python model can be loaded as a `python_function` model, which allows for workflows like deployment to work with any python model regardless of which framework was used to produce the model. This interoperability is immensely powerful as it reduces the time to operationalize in multiple environments.

#### Configure the signature
Apart from flavors, the `MLmodel` file also contains signatures that serve as data contracts between the model and the server running your model.

There are two types of signatures:
- **Column-based**: used for tabular data with a `pandas.Dataframe` as inputs.
- **Tensor-based**: used for n-dimensional arrays or tensors (often used for unstructured data like text or images), with `numpy.ndarray` as inputs.

As the `MLmodel` file is created when you register the model, the signature also is created when you register the model. When you enable MLflow's autologging, the signature is inferred in the best effort way. If you want the signature to be different, you need to manually log the model.


### Register an MLflow model
In Azure Machine Learning, models are trained in jobs. When you want to find the model's artifacts, you can find it in the job's outputs. To more easily manage your models, you can also store a model in the Azure Machine Learning **model registry**.

>*NOTE: You can also register models trained outside Azure Machine Learning by providing the local path to the model's artifacts.*

There are three types of models you can register:
- **MLflow**: Model trained and tracked with MLflow. Recommended for standard use cases.
- **Custom**: Model type with a custom standard not currently supported by Azure Machine Learning.
- **Triton**: Model type for deep learning workloads. Commonly used for TensorFlow and PyTorch model deployments.


To register a model you can use the job name to find the job run and register the model from its outputs.
```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

job_name = returned_job.name

run_model = Model(
    path=f"azureml://jobs/{job_name}/outputs/artifacts/paths/model/",
    name="mlflow-diabetes",
    description="Model created from run.",
    type=AssetTypes.MLFLOW_MODEL,
)
# Uncomment after adding required details above
ml_client.models.create_or_update(run_model)
```

All registered models are listed in the Models page of the Azure Machine Learning studio. The registered model includes the model's output directory. When you log and register an MLflow model, you can find the `MLmodel` file in the artifacts of the registered model.

## Additional Materials
- [MLflow Documentation](https://www.mlflow.org/docs/latest/ml/tracking/).