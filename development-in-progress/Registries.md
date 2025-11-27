A registry, much like a Git repository, decouples machine learning assets from workspaces and hosts the assets in a central location, making them available to all workspaces in your organization. You can use registries to store and share assets such as models, environments, components, and datasets.

To promote models across development, test, and production environments, you can start by iteratively developing a model in the development environment. When you have a good candidate model, you can publish it to a registry. You can then deploy the model from the registry to endpoints in different workspaces.


If you already have models registered in a workspace, you can promote the models to a registry. You can also register a model directly in a registry from the output of a training job.