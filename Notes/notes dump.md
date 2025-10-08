# Auto ML
Azure Automated Machine Learning allows you to try multiple preprocessing transformations and algorithms with your data to find the best machine learning model instead of manually having to test and evaluate various configurations to train a machine learning model.




## How does AutoML work?

During training, Azure Machine Learning creates many pipelines in parallel that try different algorithms and parameters for you. The service iterates through ML algorithms paired with feature selections, where each iteration produces a model with a training score. The better the score for the metric you want to optimize for, the better the model is considered to "fit" your data. It stops once it hits the exit criteria defined in the experiment.



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




[Docs](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml?view=azureml-api-2)
