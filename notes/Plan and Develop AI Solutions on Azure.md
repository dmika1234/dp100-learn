# Plan and prepare to develop AI solutions on Azure


## What is AI?
Common AI capabilities that developers can integrate into a software application include:

Capability	Description
Diagram of speech bubbles.
Generative AI	The ability to generate original responses to natural language prompts. For example, software for a real estate business might be used to automatically generate property descriptions and advertising copy for a property listing.
Diagram of a human head with a cog for a brain.
Agents	Generative AI applications that can respond to user input or assess situations autonomously, and take appropriate actions. For example, an "executive assistant" agent could provide details about the location of a meeting on your calendar, or even attach a map or automate the booking of a taxi or rideshare service to help you get there.
Diagram of an eye being scanned.
Computer vision	The ability to accept, interpret, and process visual input from images, videos, and live camera streams. For example, an automated checkout in a grocery store might use computer vision to identify which products a customer has in their shopping basket, eliminating the need to scan a barcode or manually enter the product and quantity.
Diagram of a speech bubble and a sound wave.
Speech	The ability to recognize and synthesize speech. For example, a digital assistant might enable users to ask questions or provide audible instructions by speaking into a microphone, and generate spoken output to provide answers or confirmations.
Diagram of a text document.
Natural language processing	The ability to process natural language in written or spoken form, analyze it, identify key points, and generate summaries or categorizations. For example, a marketing application might analyze social media messages that mention a particular company, translate them to a specific language, and categorize them as positive or negative based on sentiment analysis.
Diagram of a form containing information.
Information extraction	The ability to use computer vision, speech, and natural language processing to extract key information from documents, forms, images, recordings, and other kinds of content. For example, an automated expense claims processing application might extract purchase dates, individual line item details, and total costs from a scanned receipt.
Diagram of a chart showing an upward trend.
Decision support	The ability to use historic data and learned correlations to make predictions that support business decision making. For example, analyzing demographic and economic factors in a city to predict real estate market trends that inform property pricing decisions.
Determining the specific AI capabilities you want to include in your application can help you identify the most appropriate AI services that you'll need to provision, configure, and use in your solution.

## A closer look at generative AI
Generative AI represents the latest advance in artificial intelligence, and deserves some extra attention. Generative AI uses language models to respond to natural language prompts, enabling you to build conversational apps and agents that support research, content creation, and task automation in ways that were previously unimaginable.

Diagram of a prompt, a language model, and a response.

The language models used in generative AI solutions can be large language models (LLMs) that have been trained on huge volumes of data and include many millions of parameters; or they can be small language models (SLMs) that are optimized for specific scenarios with lower overhead. Language models commonly respond to text-based prompts with natural language text; though increasingly new multi-modal models are able to handle image or speech prompts and respond by generating text, code, speech, or images.


## Plan and prepare to develop AI solutions on Azure - Foundry Tools
Microsoft Azure provides a wide range of cloud services that you can use to develop, deploy, and manage an AI solution. The most obvious starting point for considering AI development on Azure is Foundry Tools; a set of out-of-the-box prebuilt APIs and models that you can integrate into your applications. The following table lists some commonly used Foundry Tools (for a full list of all available Foundry Tools, see [Available Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services#available-azure-ai-services?azure-portal=true)).

Expand table

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

To use Foundry Tools, you create one or more Azure AI resources in an Azure subscription and implement code in client applications to consume them. In some cases, AI services include web-based visual interfaces that you can use to configure and test your resources - for example to train a custom image classification model using the **Custom Vision** service you can use the visual interface to upload training images, manage training jobs, and deploy the resulting model.

Note

You can provision Foundry Tools resources in the Azure portal (or by using BICEP or ARM templates or the Azure command-line interface) and build applications that use them directly through various service-specific APIs and SDKs. However, as we'll discuss later in this module, in most medium to large-scale development scenarios it's better to provision Foundry Tools resources as part of an _Microsoft Foundry_ project - enabling you to centralize access control and cost management, and making it easier to manage shared resources and build the next generation of generative AI apps and agents.

#### Single service or Foundry Tools resource?

Most Foundry Tools, such as **Azure Vision**, **Azure Language**, and so on, can be provisioned as standalone resources, enabling you to create only the Azure resources you specifically need. Additionally, standalone Foundry Tools often include a free-tier SKU with limited functionality, enabling you to evaluate and develop with the service at no cost. Each standalone Azure AI resource provides an endpoint and authorization keys that you can use to access it securely from a client application.

Alternatively, you can provision a Foundry Tools resource that encapsulates multiple AI services in a single Azure resource. Using a Foundry Tools resource can make it easier to manage applications that use multiple AI capabilities. There are two Foundry resource types you can use:

Expand table

| Resource | Description |
| --- | --- |
| ![Foundry tools icon.](./../assets/imgs/foundry_files/cognitive-services.png)  <br>**Foundry Tools** | The Foundry Tools resource type includes the following services, making them available from a single endpoint:<br><br>*   Azure Speech<br>*   Azure Language<br>*   Azure Translator<br>*   Azure Vision<br>*   Azure AI Face<br>*   Azure AI Custom Vision<br>*   Azure Document Intelligence |
| ![Microsoft Foundry icon.](./../assets/imgs/foundry_files/ai-services.png)  <br>**Microsoft Foundry** | The Microsoft Foundry resource type includes the following services, and supports working with them through a Microsoft Foundry project\*:<br><br>*   Azure OpenAI<br>*   Azure Speech<br>*   Azure Language<br>*   Microsoft Foundry Content Safety<br>*   Azure Translator<br>*   Azure Vision<br>*   Azure AI Face<br>*   Azure Document Intelligence<br>*   Azure Content Understanding |

\* Microsoft Foundry is discussed in the next unit.

#### Regional availability

Some services and models are available in only a subset of Azure regions. Consider service availability and any regional quota restrictions for your subscription when provisioning Foundry Tools. Use the [product availability table](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table) to check regional availability of Azure services. Use the [model availability table](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability?azure-portal=true) in the Azure OpenAI documentation to determine regional availability for Azure OpenAI models.

#### Cost

Foundry Tools are charged based on usage, with different pricing schemes available depending on the specific services being used. As you plan an AI solution on Azure, use the [Foundry Tools pricing](https://azure.microsoft.com/pricing/details/cognitive-services) documentation to understand pricing for the AI services you intend to incorporate into your application. You can use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator) to estimate the costs your expected usage will incur.


