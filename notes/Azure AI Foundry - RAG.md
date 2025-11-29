# RAG in Microsoft Foundry

## 1. Groundedness in Language Models

- **Groundedness**: Ensures responses from language models are based on factual, relevant data.
- **Ungrounded responses**: Generated solely from training data, may be uncontextualized or inaccurate.
- **Grounded responses**: Augmented with external, factual data sources for accuracy.

## 2. Retrieval Augmented Generation (RAG)

- **RAG**: Technique to ground language models by retrieving relevant information for the user’s prompt.
- **RAG Steps**:
  1. Retrieve grounding data based on the user prompt.
  2. Augment the prompt with this data.
  3. Use a language model to generate a grounded response.

- **Benefits**: Improves factual accuracy and domain relevance of generative AI applications.

## 3. Adding Grounding Data in Microsoft Foundry

- **Supported Data Sources**:
  - Azure Blob Storage
  - Azure Data Lake Storage Gen2
  - Microsoft OneLake
  - Direct file/folder uploads

## 4. Making Data Searchable with Azure AI Search

- **Azure AI Search**: Acts as a retriever to index and query your data for relevant context in chat flows.
- **Index Types**:
  - **Text-based index**: Efficient, but limited to keyword matches.
  - **Vector-based index**: Uses embeddings (vectors of floating-point numbers) to represent text tokens, enabling semantic search.

    - **Embeddings**: Numeric representations of text, allowing semantic similarity calculations (e.g., cosine similarity).
    - Learn more: [Embeddings in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings)

- **Creating a Search Index**:
  - Organizes content for efficient retrieval (like a library catalog).
  - Can be configured for keyword, semantic, or vector search.
  - Learn more: [Vector Search Overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

## 5. Search Techniques

- **Keyword Search**: Finds documents by exact terms.
- **Semantic Search**: Finds documents by meaning, not just keywords.
- **Vector Search**: Uses embeddings to find semantically similar content.
- **Hybrid Search**: Combines keyword, semantic, and vector search for best results.
  - Learn more: [Hybrid Search Overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview)

## 6. RAG-based Client Application Example

- **Python Example**: Shows how to use Azure OpenAI and Azure AI Search for RAG.
- **Keyword-based Search**: Matches user prompt text to indexed documents.
- **Vector-based Search**: Uses embeddings for semantic matching; requires specifying an embedding model.

```python
from openai import AzureOpenAI

chat_client = AzureOpenAI(
    api_version = "2024-12-01-preview",
    azure_endpoint = open_ai_endpoint,
    api_key = open_ai_key
)

prompt = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]
input_text = input("Enter a question: ")
prompt.append({"role": "user", "content": input_text})

rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": search_url,
                "index_name": "index_name",
                "authentication": {
                    "type": "api_key",
                    "key": search_key,
                }
            }
        }
    ],
}

response = chat_client.chat.completions.create(
    model="<model_deployment_name>",
    messages=prompt,
    extra_body=rag_params
)
completion = response.choices[0].message.content
print(completion)
```

- **For vector-based search**, add:
```python
"query_type": "vector",
"embedding_dependency": {
    "type": "deployment_name",
    "deployment_name": "<embedding_model_deployment_name>",
}
```

## 7. Implementing RAG in Prompt Flow

- **Prompt Flow**: Framework for orchestrating LLM interactions.
  - **Inputs**: User question, chat history.
  - **Tools**: Python code, index lookup, prompt variants, LLM submission.
  - **Outputs**: Generated LLM results.

- **RAG in Prompt Flow**:
  - Use the **Index Lookup tool** to retrieve data from your index.
  - Learn more: [Index Lookup Tool](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/tools-reference/index-lookup-tool)

### Sample Chat Flow Steps

1. **Modify query with history**: LLM node combines chat history and user question.
2. **Look up relevant information**: Index Lookup tool queries the search index.
3. **Generate prompt context**: Python node combines retrieved documents into a single string for the prompt.
4. **Define prompt variants**: Test different system messages for groundedness.
5. **Chat with context**: LLM node generates a response using the augmented prompt.

---

**Summary Table**

| Concept                | Description                                                                                 | Reference/Link                                                                                  |
|------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Groundedness           | Ensuring LLM responses are factual and contextually relevant                               | -                                                                                               |
| RAG                    | Retrieval Augmented Generation: retrieve, augment, generate                                | -                                                                                               |
| Embeddings             | Numeric vector representations of text for semantic search                                  | [Embeddings in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings) |
| Vector Search          | Uses embeddings for semantic similarity                                                     | [Vector Search Overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) |
| Hybrid Search          | Combines keyword, semantic, and vector search                                               | [Hybrid Search Overview](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) |
| Index Lookup Tool      | Retrieves data from an index in prompt flow                                                 | [Index Lookup Tool](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/tools-reference/index-lookup-tool) |
| Prompt Flow            | Framework for orchestrating LLM and data retrieval steps                                   | -                                                                                               |

---

**Tips:**
- Use vector or hybrid search for best results in generative AI applications.
- Always ground LLM responses with up-to-date, relevant data for accuracy.
- Experiment with prompt variants to optimize groundedness and response quality.

---

Let me know if you want to expand any section or need more details on a specific part!
