### Serverless compute (when to use)

Azure ML provides serverless compute for certain job types. If a job does not specify a compute target, it may run on serverless compute. Serverless is useful for short-lived or bursty jobs, since it avoids cluster warm-up and idle costs.

Supported job types for serverless compute:

- Command jobs (including interactive jobs and distributed training)
- AutoML jobs
- Sweep jobs
- Parallel jobs

Serverless benefits and caveats:

- Serverless may automatically select VM size and node count where applicable.
- You don't need to wait for clusters to scale up or down to run a job.
- You still must provide a valid environment (Docker image or curated environment) for the job to run in.
- You can encounter quota limits; validate your subscription quotas before relying on serverless.

Further reading:

- Serverless compute: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-serverless-compute?view=azureml-api-2&tabs=python
- Quota management: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2#view-your-usage-and-quotas-in-the-azure-portal
