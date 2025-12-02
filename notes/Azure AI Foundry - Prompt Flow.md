# Microsoft Foundry Prompt Flow – Key Notes

## 1. What is Prompt Flow?

- **Prompt Flow**: A feature in Azure Machine Learning Studio and Microsoft Foundry for developing, testing, tuning, and deploying LLM (Large Language Model) applications.
- **Prompt**: The input (text or instructions) given to an LLM to generate a response.
- **Flow**: A sequence of actions (pipeline) that processes input through LLMs to produce desired output.

---

## 2. LLM Application Development Lifecycle

**Four Main Stages:**

1. **Initialization**
   - Define the use case and solution.
   - Steps:
     1. Define the **objective**.
     2. Collect a **sample dataset** (diverse, privacy-compliant).
     3. Build a **basic prompt**.
     4. Design the **flow**.

2. **Experimentation**
   - Develop and test the flow with a small dataset.
   - Iterative process:
     1. **Run** the flow.
     2. **Evaluate** performance.
     3. If satisfied, move on; if not, **modify** the flow.

3. **Evaluation and Refinement**
   - Test the flow with a larger dataset.
   - Identify bottlenecks and optimize.
   - Refine iteratively, starting with small datasets before scaling up.

4. **Production**
   - **Optimize** the flow for efficiency.
   - **Deploy** to an endpoint.
   - **Monitor** performance and collect feedback for continuous improvement.

---

## 3. Core Components of Prompt Flow

- **Inputs**: Data passed into the flow (string, int, bool, etc.).
- **Nodes**: Executable units (tools) that process data.
- **Outputs**: Data produced by the flow.

**Flow Structure:**
- Multiple nodes can be linked, using outputs from previous nodes as inputs for subsequent ones.

---

## 4. Tools in Prompt Flow

- **LLM Tool**: For custom prompt creation using LLMs.
- **Python Tool**: For running custom Python scripts.
- **Prompt Tool**: For preparing prompts as strings, useful for complex scenarios.

**Custom Tools**: If built-in tools are insufficient, you can [create your own custom tool](https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/create-and-use-tool-package.html).

---

## 5. Types of Flows

- **Standard Flow**: General LLM-based applications.
- **Chat Flow**: For conversational/chatbot applications.
- **Evaluation Flow**: For performance evaluation and feedback analysis.

---

## 6. Connections and Runtimes

### Connections

- **Purpose**: Securely link flows to external data sources, services, or APIs.
- **Security**: Credentials are stored in Azure Key Vault.
- **Examples**:
  - Azure OpenAI, OpenAI, Azure AI Search, Serp, Custom APIs.
- **Benefits**: Automates credential management and enables secure data transfer.

### Runtimes

- **Definition**: Combination of compute instance and environment (packages/libraries).
- **Default Environment**: Available for quick development.
- **Custom Environments**: [Create if additional packages are needed](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-customize-environment-runtime).

---

## 7. Variants, Deployment, and Monitoring

### Variants

- **Definition**: Different versions of a tool node (currently for LLM tool only).
- **Use Cases**: Test different prompts or settings for the same task.
- **Benefits**:
  - Enhance LLM output quality.
  - Save time in prompt tuning.
  - Boost productivity.
  - Enable easy, side-by-side comparison.

### Deployment

- **Deploy to Endpoint**: Make your flow accessible via an online endpoint (URL + key).
- **Integration**: Allows real-time API calls from other applications.

### Monitoring

- **Purpose**: Track performance and ensure quality.
- **Metrics**:
  - **Groundedness**: Output alignment with input/source.
  - **Relevance**: Pertinence to input.
  - **Coherence**: Logical flow/readability.
  - **Fluency**: Grammatical/language accuracy.
  - **Similarity**: Match with ground truth.

- **Continuous Improvement**: Use metrics and feedback to iteratively refine your flow.

---

## References

- [Create and use custom tool packages in prompt flow](https://microsoft.github.io/promptflow/how-to-guides/develop-a-tool/create-and-use-tool-package.html)
- [Customize environment runtime in prompt flow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-customize-environment-runtime)
