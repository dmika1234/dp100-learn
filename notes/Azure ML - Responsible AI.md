# Responsible AI in Azure Machine Learning

Responsible AI ensures models are built and deployed in a safe, transparent, and ethical way. Beyond performance metrics, review whether your models conform to Responsible AI (RAI) principles. Azure Machine Learning provides a built-in **Responsible AI dashboard** you can create and customize to explore data and model behavior.

---

## Understand Responsible AI

Models often inform decisions that affect people; therefore you must consider bias, transparency, safety, privacy, and accountability. Which principles you emphasise depends on the use case, but it’s best practice to review all of them.

Microsoft’s five Responsible AI principles:

* **Fairness and inclusiveness**: Models should treat similar groups similarly and avoid harmful bias.
* **Reliability and safety**: Models should operate as intended, be robust to unexpected inputs, and resist manipulation.
* **Privacy and security**: Be transparent about data use; protect and minimize personal data.
* **Transparency**: People should be able to understand model-driven decisions when stakes are high.
* **Accountability**: Maintain human oversight and take responsibility for model-influenced decisions.

---

## Create the Responsible AI dashboard

Azure ML exposes built-in components that compute RAI insights and stitch them together into an interactive dashboard and an optional shareable scorecard (PDF). Below is the typical flow and components.

### Pipeline structure — short introduction

A RAI dashboard is produced by a pipeline that initializes an insights container, runs one or more RAI tools to compute insights, and then gathers those insights into the dashboard.

Typical pipeline structure (use these exact component names):

* `RAI Insights dashboard constructor` — initializes the RAI insights context / dashboard.
* `Add Explanation to RAI Insights dashboard` — generate model explanations (feature importance).
* `Add Causal to RAI Insights dashboard` — compute causal effects using historical data.
* `Add Counterfactuals to RAI Insights dashboard` — run counterfactual (what-if) queries.
* `Add Error Analysis to RAI Insights dashboard` — discover cohorts/subgroups with high error rates.
* `Gather RAI Insights dashboard` — combines component outputs into the final dashboard.
* *(Optional)* `Gather RAI Insights score card` — produces a PDF scorecard for sharing.

### Retrieve built-in components

You first have to retrieve the components you want to use. To leverage Azure built-in components you need to use `MLClient` with the registry specified (example):

```python
# Get handle to azureml registry for the RAI built in components
registry_name = "azureml"
ml_client_registry = MLClient(
    credential=credential,
    subscription_id=ml_client.subscription_id,
    resource_group_name=ml_client.resource_group_name,
    registry_name=registry_name,
)
print(ml_client_registry)
```

Then load the exact components by name/label:

```python
rai_constructor_component = ml_client_registry.components.get(
    name="microsoft_azureml_rai_tabular_insight_constructor", label="latest"
)
rai_explanation_component = ml_client_registry.components.get(
    name="microsoft_azureml_rai_tabular_explanation", label="latest"
)
rai_gather_component = ml_client_registry.components.get(
    name="microsoft_azureml_rai_tabular_insight_gather", label="latest"
)
```

### Build and run the pipeline — short intro

After retrieving components, build a pipeline that wires the components together, then run it. The pipeline should reference your registered datasets and model assets.

```python
from azure.ai.ml import Input, dsl
from azure.ai.ml.constants import AssetTypes

@dsl.pipeline(
    compute="aml-cluster",
    experiment_name="Create RAI Dashboard",
)
def rai_decision_pipeline(target_column_name, train_data, test_data):

    create_rai_job = rai_constructor_component(
        title="RAI dashboard diabetes",
        task_type="classification",
        model_info=expected_model_id,
        model_input=Input(type=AssetTypes.MLFLOW_MODEL, path=azureml_model_id),
        train_dataset=train_data,
        test_dataset=test_data,
        target_column_name="Predictions",
    )
    create_rai_job.set_limits(timeout=30)

    explanation_job = rai_explanation_component(
        rai_insights_dashboard=create_rai_job.outputs.rai_insights_dashboard,
        comment="add explanation",
    )
    explanation_job.set_limits(timeout=10)

    rai_gather_job = rai_gather_component(
        constructor=create_rai_job.outputs.rai_insights_dashboard,
        insight=explanation_job.outputs.explanation,
    )
    rai_gather_job.set_limits(timeout=10)
    rai_gather_job.outputs.dashboard.mode = "upload"

    return {"dashboard": rai_gather_job.outputs.dashboard}
```

Run the pipeline; when it finishes you can open the Responsible AI dashboard from the pipeline run in Studio. AML will attach a compute instance for interactive exploration.

---

## Explore and evaluate the Responsible AI dashboard

The dashboard aggregates outputs from the components you included. Below are the insights you’ll typically inspect and a short explanation of what each lets you do.

* **Error analysis** — find subgroups (cohorts) where the model performs poorly. Use the Error tree map to explore hierarchical cohort splits and the Error heat map to view errors over one or two features. These visuals help prioritise remediation.
* **Explanations** — understand how features drive predictions. Explanations provide **aggregate feature importance** (global influence across the test set) and **individual feature importance** (contribution to a single prediction). A common technique is the *mimic* explainer (train an interpretable surrogate).
* **Counterfactuals** — answer “what must change to get a different prediction?” Select an instance, specify the desired outcome and inspect suggested minimal feature changes. Useful for recourse analysis and actionable debugging.
* **Causal analysis** — estimate effects of interventions on outcomes. The dashboard provides **aggregate causal effects**, **individual causal effects**, and a **treatment policy** view to see which subgroups benefit most from a treatment.

---

## Notes & best practices (short)

* Register training/test datasets as MLTable data assets and register your model before building the RAI pipeline.
* Use `MLClient` with `registry_name="azureml"` to access the built-in components (as shown above).
* Include only the components you need for the use case — adding unnecessary components increases compute and runtime.
* Export the scorecard for reviews or compliance audits.


## Additional Materials
* [Azure Labs: Create and explore the Responsible AI dashboard for a model in Azure Machine Learning](https://learn.microsoft.com/en-us/training/modules/manage-compare-models-azure-machine-learning/)
* [Notebook: Create Responsible AI dashboard](azure-labs/azure-ml-dev/Labs/10/Create%20Responsible%20AI%20dashboard.ipynb)