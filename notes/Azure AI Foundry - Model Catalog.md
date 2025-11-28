# 1. Overview: Foundation Models & Use Cases

- **Foundation models** (e.g., GPT family) are advanced language models for natural language understanding, generation, and interaction.
- **Common use cases:**
  - Speech-to-text & text-to-speech (e.g., video subtitles)
  - Machine translation (e.g., English ↔ Japanese)
  - Text classification (e.g., spam detection)
  - Entity extraction (e.g., keyword/name extraction)
  - Text summarization (e.g., summarizing documents)
  - Question answering (e.g., "What is the capital of France?")
  - Reasoning (e.g., solving math problems)
- Focus: Using foundation models for question answering and chat applications.

---

# 2. Exploring the Model Catalog

- **Microsoft Foundry Model Catalog**: Central repository to browse and deploy language models for generative AI use cases.
- **Other catalogs:**
  - [Hugging Face](https://huggingface.co/models): Open-source models across domains.
  - [GitHub Marketplace](https://github.com/marketplace/models-github): Models via GitHub Copilot and Marketplace.
  - [Microsoft Foundry](https://ai.azure.com/explore/models): Comprehensive, easy deployment.

## Key Questions When Choosing a Model

1. **Can AI solve my use case?**
   - Explore, filter, and deploy models from catalogs.
2. **How do I select the best model?**
   - Use criteria like task type, precision, openness, and deployment.
3. **Can I scale for real-world workloads?**
   - Consider deployment, monitoring, prompt management, and lifecycle (GenAIOps).

---

# 3. Model Selection Considerations

## Large vs. Small Language Models

- **LLMs** (e.g., GPT-4, Mistral Large, Llama3 70B): High performance, deep reasoning, complex tasks.
- **SLMs** (e.g., Phi3, Mistral OSS, Llama3 8B): Efficient, cost-effective, suitable for edge devices.

## Modality, Task, or Tool

- **Chat completion models**: Text-based responses (e.g., GPT-4, Mistral Large).
- **Reasoning models**: Advanced tasks (e.g., DeepSeek-R1, o1).
- **Multi-modal models**: Handle text + images/audio (e.g., GPT-4o, Phi3-vision).
- **Image generation**: DALL·E 3, Stability AI.
- **Embedding models**: Ada, Cohere (for search, RAG scenarios).
- **Function calling/JSON support**: For structured data/API automation.

## Regional & Domain-Specific Models

- **Core42 JAIS**: Arabic LLM.
- **Mistral Large**: Focus on European languages.
- **Nixtla TimeGEN-1**: Time-series forecasting.

## Open vs. Proprietary Models

- **Proprietary**: Best for enterprise, security, and support (e.g., OpenAI GPT-4, Mistral Large).
- **Open-source**: Flexible, cost-efficient, customizable (e.g., models from Hugging Face, Meta, Databricks, Nvidia).

**Enterprise requirements met by Microsoft Foundry:**
- Data privacy, security/compliance, responsible AI/content safety.

---

# 4. Filtering and Evaluating Models

## Criteria for Filtering

- **Task type**: Text, audio, video, multi-modal?
- **Precision**: Base vs. fine-tuned model?
- **Openness**: Need for fine-tuning?
- **Deployment**: Local, serverless, managed?

## Precision

- **Precision**: Accuracy of model outputs (true positives/total outputs).
- **Base model**: General, may lack domain precision.
- **Fine-tuned model**: Trained on specific data for higher precision.

## Performance

- **Benchmarks in Foundry catalog:**
  - Accuracy: Exact match with correct answer.
  - Coherence: Natural, human-like output.
  - Fluency: Grammatical, correct language.
  - Groundedness: Alignment with input data.
  - GPT Similarity: Semantic similarity to ground truth.
  - Quality index: Aggregate score (0–1).
  - Cost: Price per token.

- **Evaluation methods:**
  - Manual: Human rating of responses.
  - Automated: Metrics like precision, recall, F1 score.

---

# 5. Scaling for Real-World Workloads

- **Model deployment**: Choose best balance of performance/cost.
- **Monitoring & optimization**: Ongoing evaluation and improvement.
- **Prompt management**: Orchestrate/optimize prompts for accuracy.
- **Model lifecycle (GenAIOps)**: Manage updates to model, data, code.

---

# 6. Deploying a Model to an Endpoint

## Why Deploy?

- To make the model accessible via an **endpoint** (URL) for client apps or agents.
- Typical flow:
  1. User sends API request to endpoint.
  2. Model processes request.
  3. API response returns result to app.

## Deployment Options in Microsoft Foundry

- **Standard deployment**: Hosted in Foundry project resource (recommended).
- **Serverless compute**: Microsoft-managed endpoints, pay-as-you-go.
- **Managed compute**: Managed VMs, supports open/custom models.

| Option               | Supported Models                        | Hosting Service                | Billing Basis         |
|----------------------|-----------------------------------------|-------------------------------|----------------------|
| Standard deployment  | Foundry models, Azure OpenAI, MaaS      | Foundry resource              | Token-based          |
| Serverless compute   | Foundry models (pay-as-you-go)          | AI Project resource in a hub  | Token-based          |
| Managed compute      | Open and custom models                  | AI Project resource in a hub  | Compute-based        |

---

# 7. Optimizing Model Performance

## Prompt Engineering

- **Prompt**: The question/instruction sent to the model.
- **Prompt engineering**: Designing prompts for better, more accurate responses.

### Prompt Patterns (from [White et al., 2023](https://arxiv.org/abs/2302.11382))

- **Persona**: Instruct model to act as a specific role.
- **Question suggestions**: Ask model to suggest clarifying questions.
- **Format specification**: Provide templates for structured output.
- **Reasoning explanation**: Ask model to explain its reasoning (chain-of-thought).
- **Context addition**: Provide relevant context or data sources.

**System prompt**: Sets model behavior, not visible to end user.

## Model Optimization Strategies

- **Retrieval Augmented Generation (RAG)**: Use external data sources to ground responses.
- **Fine-tuning**: Train model further on specific data for consistency and style.

**Strategy selection:**
- Optimize for context (RAG) when accuracy is key.
- Optimize the model (fine-tuning) for consistent style/behavior.
- Combine strategies as needed (prompt engineering, RAG, fine-tuning).

---

# References

- [Hugging Face Model Catalog](https://huggingface.co/models)
- [GitHub Marketplace Models](https://github.com/marketplace/models-github)
- [Microsoft Foundry Model Catalog](https://ai.azure.com/explore/models)
- [Prompt Pattern Catalog (White et al., 2023)](https://arxiv.org/abs/2302.11382)

---

Let me know if you want these notes in a different format or need further breakdowns for specific exam objectives!
