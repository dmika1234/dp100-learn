# Auto ML
Azure Automated Machine Learning allows you to try multiple preprocessing transformations and algorithms with your data to find the best machine learning model instead of manually having to test and evaluate various configurations to train a machine learning model.




## How does AutoML work?

During training, Azure Machine Learning creates many pipelines in parallel that try different algorithms and parameters for you. The service iterates through ML algorithms paired with feature selections, where each iteration produces a model with a training score. The better the score for the metric you want to optimize for, the better the model is considered to "fit" your data. It stops once it hits the exit criteria defined in the experiment.


AutoML applies scaling and normalization to numeric data automatically, helping prevent any large-scale features from dominating training. During an AutoML experiment, multiple scaling or normalization techniques will be applied.


Using Azure Machine Learning, you can design and run your automated ML training experiments with these steps:

1.**Identify the ML problem to be solved**: classification, forecasting, regression, computer vision, or NLP.
2. **Choose the way to interact with Auto ML**: Python SDK v2, Azure Machine Learning CLI or Azure Web UI.
3. **Specify the source of the labeled training data.**
4. **Configure the automated machine learning parameters.**
5. **Submit the training job.**
6. **Review the results.**

## Configuration 
- You can configure featurization, see [Data Featurization](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-train?view=azureml-api-2&tabs=python#data-featurization)
- You can also specify algorithms you want to use or block. Find the list of algorithms supported by [AutoML at Supported algorithms](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-train?view=azureml-api-2&tabs=python#supported-algorithms).
-  You need to prepare your input as an MLTable data asset: `my_training_data_input = Input(type=AssetTypes.MLTABLE, path="azureml:input-data-automl:1")`.
-  


## Configure optional featurization
You can choose to have AutoML apply preprocessing transformations, such as:
- Missing value imputation to eliminate nulls in the training dataset.
- Categorical encoding to convert categorical features to numeric indicators.
- Dropping high-cardinality features, such as record IDs.
- Feature engineering (for example, deriving individual date parts from DateTime features)

By default, AutoML will perform featurization on your data. You can disable it if you don't want the data to be transformed.
If you do want to make use of the integrated featurization function, you can customize it. For example, you can specify which imputation method should be used for a specific feature.

## Configure an AutoML experiment

When you use the Python SDK (v2) to configure an AutoML experiment or job, you configure the experiment using the `automl` class. For classification, you'll use the` automl.classification` function as shown in the following example:
```python
from azure.ai.ml import automl

# configure the classification job
classification_job = automl.classification(
    compute="aml-cluster",
    experiment_name="auto-ml-class-dev",
    training_data=my_training_data_input,
    target_column_name="Diabetic",
    primary_metric="accuracy",
    n_cross_validations=5,
    enable_model_explainability=True
)
```


### Specify the primary metric
One of the most important settings you must specify is the primary_metric. The primary metric is the target performance metric for which the optimal model will be determined. Azure Machine Learning supports a set of named metrics for each type of task.

To retrieve the list of metrics available when you want to train a classification model, you can use the ClassificationPrimaryMetrics function as shown here:
```python
from azure.ai.ml.automl import ClassificationPrimaryMetrics
 
list(ClassificationPrimaryMetrics)
```

### Set the limits
Training machine learning models will cost compute. To minimize costs and time spent on training, you can set limits to an AutoML experiment or job by using `set_limits()`.
There are several options to set limits to an AutoML experiment:
- `timeout_minutes`: Number of minutes after which the complete AutoML experiment is terminated.
- `trial_timeout_minutes`: Maximum number of minutes one trial can take.
- `max_trials`: Maximum number of trials, or models that will be trained.
- `enable_early_termination`: Whether to end the experiment if the score isn't improving in the short term.
```python
classification_job.set_limits(
    timeout_minutes=60, 
    trial_timeout_minutes=20, 
    max_trials=5,
    enable_early_termination=True,
)
```



[Docs](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml?view=azureml-api-2)
