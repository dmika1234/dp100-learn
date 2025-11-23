# Azure Machine Learning Pipelines

In an enterprise data science process, you'll want to separate the overall process into individual tasks. You can group tasks together as pipelines. Pipelines are key to implementing an effective Machine Learning Operations (MLOps) solution in Azure.

Pipeline is built with components of individual tasks, making it easier to reuse and share code. You can then combine components into an Azure Machine Learning pipeline, which you'll run as a pipeline job.



## Create Components

A component consists of three parts:

- **Metadata**: Includes the component's name, version, etc.
- **Interface**: Includes the expected input parameters (like a dataset or hyperparameter) and expected output (like metrics and artifacts).
- **Command, code and environment**: Specifies how to run the code.

To create a component, you need two files:
- A script that contains the workflow you want to execute.
- A YAML file to define the metadata, interface, and command, code, and environment of the component.
You can create the YAML file, or use the command_component() function as a decorator to create the YAML file.

### Load a component

You can load a component from a YAML file:

```python
from azure.ai.ml import load_component
parent_dir = ""

prep_data_component = load_component(source=parent_dir + "./prep.yml")
```

You can load previously registered component by its name:
```python
prep_data_component = ml_client.components.get(name="prep_data", version="1")
```

### Register a component

To use components in a pipeline, you'll need the script and the YAML file. To make the components accessible to other users in the workspace, you can also register components to the Azure Machine Learning workspace.

You can register a component with the following code:

```python
prep = ml_client.components.create_or_update(prepare_data_component)
```


## Create a pipeline

In Azure Machine Learning, a pipeline is a workflow of machine learning tasks in which each task is defined as a component.

Components can be arranged sequentially or in parallel, enabling you to build sophisticated flow logic to orchestrate machine learning operations. Each component can be run on a specific compute target, making it possible to combine different types of processing as required to achieve an overall goal.

A pipeline can be executed as a process by running the pipeline as a pipeline job. Each component is executed as a child job as part of the overall pipeline job.

### Build a pipeline
An Azure Machine Learning pipeline is defined in a YAML file. The YAML file includes the pipeline job name, inputs, outputs, and settings.

You can create the YAML file, or use the @pipeline() function to create the YAML file.

For example, if you want to build a pipeline that first prepares the data, and then trains the model, you can use the following code:

```python
from azure.ai.ml.dsl import pipeline

@pipeline()
def pipeline_function_name(pipeline_job_input):
    prep_data = loaded_component_prep(input_data=pipeline_job_input)
    train_model = loaded_component_train(training_data=prep_data.outputs.output_data)

    return {
        "pipeline_job_transformed_data": prep_data.outputs.output_data,
        "pipeline_job_trained_model": train_model.outputs.model_output,
    }
```
To pass a registered data asset as the pipeline job input, you can call the function you created with the data asset as input:
```python
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes

pipeline_job = pipeline_function_name(
    Input(type=AssetTypes.URI_FILE, 
    path="azureml:data:1"
))
```

The result of running the `@pipeline()` function is a YAML file that you can review by printing the `pipeline_job` object you created when calling the function:
```python
print(pipeline_job)
```


## Run a pipeline Job
When you've built a component-based pipeline in Azure Machine Learning, you can run the workflow as a pipeline job.

### Configure a pipeline job

You can edit the pipeline configurations by specifying which parameters you want to change and the new value.

For example, you may want to change the output mode for the pipeline job outputs:

```python
# change the output mode
pipeline_job.outputs.pipeline_job_transformed_data.mode = "upload"
pipeline_job.outputs.pipeline_job_trained_model.mode = "upload"
```

Or, you may want to set the default pipeline compute. When a compute isn't specified for a component, it will use the default compute instead:

```python
# set pipeline level compute
pipeline_job.settings.default_compute = "aml-cluster"
```

You may also want to change the default datastore to where all outputs will be stored:

```python
# set pipeline level datastore
pipeline_job.settings.default_datastore = "workspaceblobstore"
```

To review your pipeline configuration, you can print the pipeline job object:

```python
print(pipeline_job)
```

### Run a pipeline job

When you've configured the pipeline, you're ready to run the workflow as a pipeline job.

To submit the pipeline job, run the following code:

```python
# submit job to workspace
pipeline_job = ml_client.jobs.create_or_update(
    pipeline_job, experiment_name="pipeline_job"
)
```

*   If there's an issue with the configuration of the pipeline itself, you'll find more information in the outputs and logs of the pipeline job.
*   If there's an issue with the configuration of a component, you'll find more information in the outputs and logs of the child job of the failed component.

### Schedule a pipeline job

A pipeline is ideal if you want to get your model ready for production. Pipelines are especially useful for automating the retraining of a machine learning model. To automate the retraining of a model, you can schedule a pipeline.

To schedule a pipeline job, you'll use the `JobSchedule` class to associate a schedule to a pipeline job.

There are various ways to create a schedule. A simple approach is to create a time-based schedule using the `RecurrenceTrigger` class with the following parameters:

*   `frequency`: Unit of time to describe how often the schedule fires. Value can be either `minute`, `hour`, `day`, `week`, or `month`.
*   `interval`: Number of frequency units to describe how often the schedule fires. Value needs to be an integer.

To create a schedule that fires every minute, run the following code:

```python
from azure.ai.ml.entities import RecurrenceTrigger
 
schedule_name = "run_every_minute"

recurrence_trigger = RecurrenceTrigger(
    frequency="minute",
    interval=1,
)
```

To schedule a pipeline, you'll need `pipeline_job` to represent the pipeline you've built:

```python
from azure.ai.ml.entities import JobSchedule

job_schedule = JobSchedule(
    name=schedule_name, trigger=recurrence_trigger, create_job=pipeline_job
)

job_schedule = ml_client.schedules.begin_create_or_update(
    schedule=job_schedule
).result()
```

The display names of the jobs triggered by the schedule will be prefixed with the name of your schedule. You can review the jobs in the Azure Machine Learning studio.
To delete a schedule, you first need to disable it.

```python
ml_client.schedules.begin_disable(name=schedule_name).result()
ml_client.schedules.begin_delete(name=schedule_name).result()
```




## Additional Materials

- [Pipelines and Components in Azure ML](./.././tutorials/Pipelines%20and%20Components%20in%20Azure%20ML.ipynb)
- [Microsoft Tutorial](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipeline-python?view=azureml-api-2)
- [Microsoft Lab](https://learn.microsoft.com/en-us/training/modules/run-pipelines-azure-machine-learning/)
- [Azure SD Examples - Job Schedule](https://github.com/Azure/azureml-examples/blob/main/sdk/python/schedules/job-schedule.ipynb)