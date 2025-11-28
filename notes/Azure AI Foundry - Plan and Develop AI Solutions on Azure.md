# Plan and prepare to develop AI solutions on Azure

## What is AI?

AI enables applications to perform tasks such as generating content, responding autonomously, interpreting images and speech, extracting information, and supporting decisions. Choosing the right capability helps determine which Azure AI services you need.

**Common capabilities include:**

* **Generative AI:** Produces text, code, or images from natural-language prompts.
* **Agents:** Autonomous systems that can act on user input and perform tasks.
* **Computer vision:** Interprets images and video (object detection, OCR, captions).
* **Speech:** Speech-to-text, text-to-speech, translation, and speaker recognition.
* **Natural language processing:** Summarization, classification, entity detection.
* **Information extraction:** Extracts structured fields from documents, images, or audio.
* **Decision support:** Predictive modeling based on historical data.

## A closer look at generative AI

Generative AI relies on LLMs or SLMs that can produce natural language text and multimodal outputs. Modern models accept text, image, or speech inputs and generate text, images, or code—forming the foundation of conversational applications and agents.

## Plan and prepare to develop AI solutions on Azure - Foundry Tools

Azure provides prebuilt **Foundry Tools**, each exposing ready-to-use APIs for vision, speech, language, translation, search, and generative AI. These services can be used directly or as part of a Microsoft Foundry project.

| Service | Description |
| --- | --- |
| ![Azure OpenAI service icon.](./../assets/imgs/foundry_files/open-ai.png)  <br>**Azure OpenAI** | Azure OpenAI in Foundry Models provides access to OpenAI generative AI models including the GPT family of large and small language models and DALL-E image-generation models within a scalable and securable cloud service on Azure. |
| ![Azure Vision service icon.](./../assets/imgs/foundry_files/vision.png)  <br>**Azure Vision** | The Azure Vision service provides a set of models and APIs that you can use to implement common computer vision functionality in an application. With the AI Vision service, you can detect common objects in images, generate captions, descriptions, and tags based on image contents, and read text in images. |
| ![Azure Speech service icon.](./../assets/imgs/foundry_files/speech-service.png)  <br>**Azure Speech** | The Azure Speech service provides APIs that you can use to implement _text to speech_ and _speech to text_ transformation, as well as specialized speech-based capabilities like speaker recognition and translation. |
| ![Azure Language service icon.](./../assets/imgs/foundry_files/language.png)  <br>**Azure Language** | The Azure Language service provides models and APIs that you can use to analyze natural language text and perform tasks such as entity extraction, sentiment analysis, and summarization. The AI Language service also provides functionality to help you build conversational language models and question answering solutions. |
| ![Microsoft Foundry Content Safety service icon.](./../assets/imgs/foundry_files/content-safety.png)  <br>**Microsoft Foundry Content Safety** | Microsoft Foundry Content Safety provides developers with access to advanced algorithms for processing images and text and flagging content that is potentially offensive, risky, or otherwise undesirable. |
| ![Azure Translator service icon.](./../assets/imgs/foundry_files/translator.png)  <br>**Azure Translator** | The Azure Translator service uses state-of-the-art language models to translate text between a large number of languages. |
| ![Azure AI Face service icon.](./../assets/imgs/foundry_files/face.png)  <br>**Azure AI Face** | The Azure AI Face service is a specialist computer vision implementation that can detect, analyze, and recognize human faces. Because of the potential risks associated with personal identification and misuse of this capability, access to some features of the AI Face service are restricted to approved customers. |
| ![Azure AI Custom Vision service icon.](./../assets/imgs/foundry_files/custom-vision.png)  <br>**Azure AI Custom Vision** | The Azure AI Custom Vision service enables you to train and use custom computer vision models for image classification and object detection. |
| ![Azure Document Intelligence service icon.](./../assets/imgs/foundry_files/document-intelligence.png)  <br>**Azure Document Intelligence** | With Azure Document Intelligence, you can use pre-built or custom models to extract fields from complex documents such as invoices, receipts, and forms. |
| ![Azure Content Understanding service icon.](./../assets/imgs/foundry_files/content-understanding.png)  <br>**Azure Content Understanding** | The Azure Content Understanding service provides multi-modal content analysis capabilities that enable you to build models to extract data from forms and documents, images, videos, and audio streams. |
| ![Azure AI Search service icon.](./../assets/imgs/foundry_files/search.png)  <br>**Azure AI Search** | The Azure AI Search service uses a pipeline of AI skills based on other Foundry Tools and custom code to extract information from content and create a searchable index. AI Search is commonly used to create vector indexes for data that can then be used to _ground_ prompts submitted to generative AI language models, such as those provided in Azure OpenAI. |

### Considerations for Foundry Tools resources

You provision AI services in Azure and call them via SDKs or REST. Many services provide simple visual interfaces for testing or training custom models. For medium/large projects, it’s usually better to organize resources inside a **Microsoft Foundry** project to unify identity, costs, and development workflow.

#### Single service or Foundry Tools resource?

You can deploy:

* **Individual services** (Vision, Language, Speech, etc.) — fine-grained and often include free tiers.
* **Foundry Tools** resources — single endpoint containing multiple AI services.
* **Microsoft Foundry** resources — include generative AI models and additional tools for agents, content safety, and evaluation.

#### Regional availability

Models and services differ by region. Check the [product availability](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) and [model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability?azure-portal=true).

#### Cost

Services are billed per usage. Use the [Foundry Tools pricing](https://azure.microsoft.com/pricing/details/cognitive-services) and the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator) to estimate costs.

---

## Microsoft Foundry

Microsoft Foundry provides a centralized platform for AI development, including a portal and SDK. It simplifies project organization, resource access, model deployment, evaluation, and responsible AI workflows.

### Microsoft Foundry projects


#### Foundry projects

Linked to a **Microsoft Foundry resource**. Provide access to OpenAI models, agent services, Foundry Tools, and evaluation tools. Ideal for most generative AI applications.

#### Hub-based projects

Linked to an **Azure AI hub** resource. Include compute, storage, Key Vault, Prompt Flow support, and integration with Azure ML. Best for advanced workflows like fine-tuning or collaborative ML development.

---

## Developer tools and SDKs

### Development tools and environments

#### The Microsoft Foundry for Visual Studio Code extension

Streamlines creating projects, deploying/testing models, and building agents directly inside VS Code.

#### GitHub and GitHub Copilot

Integrated into VS/VS Code for source control and AI-assisted coding.

### Programming languages, APIs, and SDKs
You can develop AI applications using many common programming languages and frameworks, including Microsoft C#, Python, Node, TypeScript, Java, and others. When building AI solutions on Azure, some common SDKs you should plan to install and use include:

- The **Microsoft Foundry SDK**, which enables you to write code to connect to Microsoft Foundry projects and access resource connections, which you can then work with using service-specific SDKs.
- The **Microsoft Foundry Models API**, which provides an interface for working with generative AI model endpoints hosted in Microsoft Foundry.
- The **Azure OpenAI in Microsoft Foundry Models API**, which enables you to build chat applications based on OpenAI models hosted in Microsoft Foundry.
- **Foundry Tools SDKs** - AI service-specific libraries for multiple programming languages and frameworks that enable you to consume Foundry Tools resources in your subscription. You can also use Foundry Tools through their REST APIs.
- The **Microsoft Foundry Agent Service**, which is accessed through the Microsoft Foundry SDK and can be integrated with frameworks like Semantic Kernel to build comprehensive AI agent solutions.

---

## Responsible AI

AI systems must be designed with societal impact, fairness, privacy, and safety in mind. Key principles:

### Fairness

Models should avoid disadvantaging groups. Ensure representative data and monitor performance across user subgroups.

### Reliability and safety

Systems must be robust and thoroughly tested, especially where mispredictions can cause harm.

### Privacy and security

Protect training and inference data, implement safeguards, and securely manage access.

### Inclusiveness

Design with diverse perspectives and ensure accessibility for all users.

### Transparency

Communicate model purpose, limitations, confidence scores, and data usage clearly.

### Accountability

Developers and organizations remain responsible for model behavior and should follow governance and compliance standards.
