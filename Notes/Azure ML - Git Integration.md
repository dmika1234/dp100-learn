# Integrate Git with Azure Machine Learning

Microsoft owns GitHub, which enables seamless integration between both platforms. This allows you to connect your Git repositories directly with Azure Machine Learning (Azure ML) for version control, experiment tracking, and automated MLOps workflows.

When you run jobs in Azure ML that come from a Git-tracked repository, the job automatically records metadata such as the **repository URL**, **branch name**, and **commit hash**. This makes your experiments fully reproducible and traceable. You can also automate training and deployment processes using **GitHub Actions**.

---

## Git integration for Azure Machine Learning

Azure ML supports direct Git integration, allowing you to clone, edit, and use repositories within your workspace or compute instances.

To set it up:
1. Generate an SSH key on your Azure ML compute instance:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

2. Add the **public key** to your Git service (for example, GitHub → Settings → SSH and GPG keys).
3. Clone your repository using the SSH URL:

   ```bash
   git clone git@github.com:username/repo.git
   ```

Once configured, you can pull, commit, and push changes directly from Azure ML, and every experiment run will include the Git details in its job properties.

🔗 [Full tutorial on Git integration for Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration?view=azureml-api-2&utm_source=chatgpt.com)

---

## Use GitHub Actions with Azure Machine Learning

GitHub Actions can be used to automate Azure ML workflows, such as training, registering, or deploying models whenever code changes are pushed to your repository. This enables true MLOps practices directly from GitHub.

The official tutorial explains how to connect GitHub Actions with Azure ML using **OpenID Connect (OIDC)** or a **service principal** for secure authentication.

> ⚠️ To configure this integration, you must have at least **Cloud Application Administrator** privileges in the **Microsoft Entra admin center** (formerly Azure Active Directory).

🔗 [Full tutorial on using GitHub Actions with Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-github-actions-machine-learning?view=azureml-api-2&utm_source=chatgpt.com&tabs=openid)
