# Using MLflow in Azure Machine Learninr


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


## Additional Materials
- [MLflow Documentation](https://www.mlflow.org/docs/latest/ml/tracking/).