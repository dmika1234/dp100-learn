



```
conda create -n dp100 python=3.10.11
```
conda activate dp100
conda install --file conda-requirements.txt


pip install -r pip-requirements.txt
pip uninstall azure-ai-ml
pip install azure-ai-ml
pip install mltable
pip install fsspec azureml-fsspec
pip install "mlflow<3.0.0"
pip install azureml-mlflow