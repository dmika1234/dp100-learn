# Make data available in Azure Machine Learning

## Understand URIs

You can store data on your local device, or somewhere in the cloud. Wherever you store your data, you want to access the data when training machine learning models. To find and access data in Azure Machine Learning, you can use Uniform Resource Identifiers (URIs).

A URI references the location of your data. For Azure Machine Learning to connect to your data, you need to prefix the URI with the appropriate protocol. There are three common protocols when working with data in the context of Azure Machine Learning:

- `http(s)`: Use for data stores publicly or privately in an Azure Blob Storage or publicly available http(s) location.
- `abfs(s)`: Use for data stores in an Azure Data Lake Storage Gen 2.
- `azureml`: Use for data stored in a datastore.

## Creating a Datastore

In Azure Machine Learning, datastores are abstractions for cloud data sources. They encapsulate the information needed to connect to data sources, and securely store this connection information so that you don’t have to code it in your scripts.

When you create a datastore with an existing storage account on Azure, you have the choice between two different authentication methods:

- Credential-based: Use a service principal, shared access signature (SAS) token or account key to authenticate access to your storage account.
- Identity-based: Use your Microsoft Entra identity or managed identity.

To create a datastore using a SAS token to authenticate:
```
blob_datastore = AzureBlobDatastore(
name="blob_sas_example",
description="Datastore pointing to a blob container",
account_name="mytestblobstore",
container_name="data-container",
credentials=SasTokenConfiguration(
sas_token="?xx=XXXX-XX-XX&xx=xxxx&xxx=xxx&xx=xxxxxxxxxxx&xx=XXXX-XX-XXXXX:XX:XXX&xx=XXXX-XX-XXXXX:XX:XXX&xxx=xxxxx&xxx=XXxXXXxxxxxXXXXXXXxXxxxXXXXXxxXXXXXxXXXXxXXXxXXxXX"
),
)
ml_client.create_or_update(blob_datastore)
```
More connection methods [here] (https://learn.microsoft.com/en-us/azure/machine-learning/how-to-datastore?view=azureml-api-2&tabs=sdk-identity-based-access%2Csdk-adls-identity-access%2Csdk-azfiles-accountkey%2Csdk-adlsgen1-identity-access%2Csdk-onelake-identity-access).


## Create a data asset


### Supported asset paths

The supported paths you can use when creating a URI file data asset are:
- Local: `./<path>`
- Azure Blob Storage: `wasbs://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>`
- Azure Data Lake Storage (Gen 2): `abfss://<file_system>@<account_name>.dfs.core.windows.net/<folder>/<file>`
- Datastore: `azureml://datastores/<datastore_name>/paths/<folder>/<file>`

### Create a MLTable data asset
- Represents tabular data with an associated schema definition for reading it.
- Once created, the schema is stored with the asset — you don’t need to redefine it in every script.
- Ideal when the data schema is complex or changes often — update it once in the asset instead of across multiple scripts.
- You can define the schema to include only a subset of the data.
- Required for some Azure ML features (e.g., AutoML) that need explicit schema info.
- Defined via an MLTable file stored with the data, specifying both data paths and read instructions.
[More about different MLTable schemas](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-mltable?view=azureml-api-2).