# Make Data Available in Azure Machine Learning

## Understanding URIs
Data can be stored locally or in the cloud, and Azure Machine Learning (AML) uses **URIs** (Uniform Resource Identifiers) to locate and access it.  
Each URI must include a protocol that specifies the storage type:

- **`http(s)`** – Public/private data in Azure Blob Storage or public web data.  
- **`abfs(s)`** – Data in Azure Data Lake Storage Gen2.  
- **`azureml`** – Data stored in an AML datastore.

---

## Creating a Datastore
A **datastore** is an abstraction for a cloud data source. It securely stores connection info, so credentials aren’t hardcoded in scripts.

### Authentication Methods
- **Credential-based** – Use a service principal, SAS token, or account key.  
- **Identity-based** – Use Microsoft Entra ID or managed identity.

### Example (Account Key)
```python
blob_datastore = AzureBlobDatastore(
    			name = "blob_example",
    			description = "Datastore pointing to a blob container",
    			account_name = "mytestblobstore",
    			container_name = "data-container",
    			credentials = AccountKeyConfiguration(
        			account_key="XXXxxxXXXxXXXXxxXXX"
    			),
)
ml_client.create_or_update(blob_datastore)
```
More connection methods [here] (https://learn.microsoft.com/en-us/azure/machine-learning/how-to-datastore?view=azureml-api-2&tabs=sdk-identity-based-access%2Csdk-adls-identity-access%2Csdk-azfiles-accountkey%2Csdk-adlsgen1-identity-access%2Csdk-onelake-identity-access).


## Create a Data Asset

### Supported Asset Paths
When creating a URI-based file data asset, you can use the following path formats:
- **Local:** `./<path>`
- **Azure Blob Storage:** `wasbs://<account_name>.blob.core.windows.net/<container>/<file>`
- **Azure Data Lake Gen2:** `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/<file>`
- **Datastore:** `azureml://datastores/<datastore_name>/paths/<folder>/<file>`

---

### Example
```python
my_path = '<supported-path>'
my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FOLDER,
    description="<description>",
    name="<name>",
    version='<version>'
)

ml_client.data.create_or_update(my_data)
```


### MLTable Data Asset
- Represents **tabular data** with a stored **schema definition** for reading.  
- Once created, the schema is saved with the asset — no need to redefine it elsewhere.  
- Best for **complex** or **frequently changing** schemas — update once in the asset.  
- Can include only a **subset** of the data.  
- Required for **AutoML** and other features needing a defined schema.  
- Defined through an `MLTable` file that specifies **data paths** and **read instructions**.  
🔗 [More about MLTable schemas](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-mltable?view=azureml-api-2)

---

### Folder URI
You can register a data asset that points to a **nonexistent folder** in storage and **upload data later**.
