# 03. Agent Development

This module teaches you how to create and deploy AI agents with diverse capabilities and functionalities.

## 📋 Table of Contents

- [Agent Overview](#agent-overview)
- [Create ModelRouterAgent](#create-modelrouteragent)
- [Create FileSearchAgent](#create-filesearchagent)
- [Create WebSearchAgent](#create-websearchagent)
- [Deploy and Invoke Agents](#deploy-and-invoke-agents)
- [Next Steps](#next-steps)

## 🎯 Learning Objectives

- Understand core concepts of Microsoft Foundry agents
- Build Model Router-based agents
- Create document-based agents using File Search
- Create real-time information retrieval agents using Web Search
- Learn agent deployment and programmatic invocation methods

## ⏱️ Estimated Time

Approximately 30 minutes

---

## Agent Overview

### What is a Microsoft Foundry Agent?

A Microsoft Foundry Agent is an intelligent system that understands user requests and performs tasks using appropriate tools and knowledge.

### Key Components

```
Agent = Model + Instructions + Tools + Knowledge
```

- **Model**: Base language model (GPT-5.1, Claude, etc.)
- **Instructions**: Agent behavior guidelines and persona
- **Tools**: File Search, Web Search, Function Calling, etc.
- **Knowledge**: Connected knowledge base (Foundry IQ)

### Agent Types

| Type | Description | Use Cases |
|------|-------------|-----------|
| **Conversational** | Dialogue-oriented agent | Chatbots, customer support |
| **Task-oriented** | Task-focused agent | Data analysis, document generation |
| **Retrieval-augmented** | Search-based agent | Knowledge base QA |
| **Multi-agent** | Multi-agent collaboration | Complex workflows |

---

## Create ModelRouterAgent

Create an agent that intelligently selects models using Model Router.

### Step-by-Step Guide

1. **Navigate to Agents Section**
   - Select **Build** from the top right menu in the Foundry portal.
   - Click the **Agents** menu.
   
   ![Build > Agents menu](../assets/03-01-agents-menu.png)

2. **Create New Agent**
   - Click the **+ Create agent** or **New agent** button.
   
   ![Create agent button](../assets/03-02-create-agent.png)

3. **Agent Configuration**
   ```
   Agent name: ModelRouterAgent
   Model: model-router (previously deployed Model Router)
   ```

   **Instructions Configuration**:
   ```
   You are an agent that answers questions.
   Use the most appropriate model based on the complexity and requirements of the request.
   Always provide clear, accurate, and helpful responses.
   ```
   
   Click the **Save** button to save.

   ![Agent basic settings](../assets/03-03-agent-basic-settings.png)

4. **Test Agent**

   **Test with these questions in the Chat tab:**

   ```
   User: Hello
   ```
   → Routes to a lightweight model for simple greetings

   ```
   User: What data were you trained on?
   ```
   → Uses the base model to respond with model information

   ```
   User: Create a hands-on guide for microsoft foundry new portal. 
   I need a guide that covers foundry models, model-router, foundry agents, 
   foundry tools, foundry knowledge, foundry control plane all in the foundry portal
   ```
   → Routes to a high-performance model for complex document generation
   
   ![Test in Chat tab](../assets/03-05-agent-chat-test.png)

5. **Explore Additional Tabs**

   **YAML Tab**:
   - View agent configuration in YAML format
   - Manageable as Infrastructure as Code
   
   ![YAML tab screen](../assets/03-06-agent-yaml.png)
   
   **Code Tab**:
   - View samples for calling agent with code
   - Supports various languages: Python, JavaScript, C#, etc.
   
   ![Code tab screen](../assets/03-07-agent-code.png)

   **Traces Tab**:
   - Track agent execution process
   - Verify model selection decisions
   - Analyze performance and costs

   **Enable Tracing** requires **creating and connecting App Insights**.
   **Agent tracing** is only available in **Sweden Central** in Foundry (new).
   
   ![Traces tab screen - Connect](../assets/03-08-agent-traces-connect.png)

   ![Traces tab screen - Create](../assets/03-08-agent-traces-create.png)

   ![Traces tab screen - Traces](../assets/03-08-agent-traces.png)

   ![Traces tab screen - Traces - Details](../assets/03-08-agent-traces-details.png)

   **Monitor Tab**:
   - Real-time metrics monitoring
   - Check error rates, response times, etc.
   
   ![Monitor tab screen](../assets/03-09-agent-monitor.png)

6. **Save Agent**
   - Click the **Save** button to save the agent.

### ✅ Verification Checklist

- Verify ModelRouterAgent appears in Agents list
- Test responses to questions of varying complexity
- Check which model was selected in Traces

---

## Create FileSearchAgent

Create an agent that finds information from uploaded documents using file search functionality.

### Step-by-Step Guide

1. **Create New Agent**
   ```
   Agent name: FileSearchAgent
   Model: gpt-5.1
   ```

2. **Instructions Configuration**

   Enter the following in the **Instructions** section of Playground:
   ```
   You are an agent that responds based on File search registered in Tools.
   
   Important rules:
   1. Only answer based on uploaded file content
   2. If information is not in files, respond "I cannot find that information in the provided documents"
   3. Mention source file name in responses
   4. Use accurate citations
   ```
   
   Click the **Save** button to save.

   ![Create FileSearchAgent](../assets/03-10-filesearch-create.png)

3. **Add File Search Tool**

   - Click the **+ Add** button in the **Tools** section.
   
   - Select the **File Search** option.
   - Verify File Search is added to Tools list.
   
   ![Select File Search tool](../assets/03-13-filesearch-tool-selection.png)

4. **Upload Files**

   - Click the **Attach files** button in the **Tools > File Search** section.
   
   ![Attach files button](../assets/03-14-filesearch-attach-files.png)
   
   - Upload the `knowledge-base.json` file.
   - Verify file uploaded successfully.
   
   ![File upload complete](../assets/03-15-filesearch-file-uploaded.png)

5. **Save Agent**
   - Click the **Save** button.

6. **Test Agent**

   **Test with these questions in the Chat tab:**

   ```
   User: Recommend good places for surfing
   ```
   Expected response: Recommendations for Yangyang Surfy Beach and Jeju Jungmun Saekdal Beach

   ```
   User: Find beaches good for healing
   ```
   Expected response: Information about Gangneung Gyeongpo Beach and Taean Mallipo Beach

   ```
   User: Where can I surf year-round?
   ```
   Expected response: Jeju Jungmun Saekdal Beach
   
   ![Test FileSearchAgent](../assets/03-16-filesearch-chat-test.png)

7. **Check Traces**

   - Check how File Search worked in the **Traces** tab.
   - You can view searched document chunks and relevance scores.
   
   ![Check File Search Traces](../assets/03-17-filesearch-traces.png)

   ![Check File Search Traces](../assets/03-17-filesearch-traces-2.png)

### ✅ Verification Checklist

- Verify File Search tool is enabled
- Test accurate responses based on uploaded file content
- Confirm agent says it doesn't know for information not in files

---

## Create WebSearchAgent

Create an agent that provides up-to-date information by performing real-time web searches.

### Step-by-Step Guide

1. **Create New Agent**
   ```
   Agent name: WebSearchAgent
   Model: gpt-4.1
   ```
   
   **Instructions Configuration**

   ```
   You are an agent that responds based on Web search registered in Tools.
   
   Important rules:
   1. Always use web search for questions requiring current information
   2. Provide accurate, up-to-date information based on search results
   3. Include source URLs in responses
   4. Provide balanced answers by synthesizing information from multiple sources
   5. Perform additional searches if results are insufficient
   ```
   
   ![Create WebSearchAgent](../assets/03-18-websearch-create.png)

2. **Add Web Search Tool**

   - Click the **+ Add** button in the **Tools** section.
   - Select the **Web search** option.
   - Verify Web Search is enabled.
   
   ![Add Web search tool](../assets/03-20-websearch-add-tool.png)

3. **Save Agent**
   - Click the **Save** button.

4. **Test Agent**

   **Test current information questions in Chat tab:**

   ```
   User: Summarize key new features of Microsoft Foundry announced at Microsoft Ignite 2025
   ```
   → Search and summarize latest announcement content via web search

   ```
   User: Tell me more about Foundry IQ
   ```
   → Explain latest features and characteristics of Foundry IQ

   ```
   User: How is this better than using Azure AI Search as before?
   ```
   → Explain comparative analysis and advantages
   
   ![Test WebSearchAgent](../assets/03-21-websearch-chat-test.png)

5. **Analyze Traces**

   - Check web search process in **Traces** tab:
     - Search query
     - List of searched websites
     - Extracted information
     - Final response generation process
   
   ![Check Web Search Traces](../assets/03-22-websearch-traces.png)

   ![Check Web Search Traces](../assets/03-22-websearch-traces-2.png)

### 💡 Web Search Usage Tips

- **Specific questions**: Be specific for clear search results
- **Current information**: Useful for news, events, technical announcements
- **Comparative analysis**: Provide balanced answers by synthesizing information from multiple sources
- **Verify sources**: Check source URLs for response reliability

### ✅ Verification Checklist

- Verify Web Search tool is enabled
- Test accurate search and summarization of current information
- Confirm source URLs are included in responses

---

## Deploy and Invoke Agents

Learn how to deploy created agents and invoke them externally.

### Publish

1. **Preview Stage**

   - Click the **Preview** button in Playground.
   - You can check the following options:
     - **Preview agent**: Preview agent with web interface
     - **View sample app code**: Check sample application code
   
   ![Preview button](../assets/03-23-agent-preview-button.png)

   ![Preview](../assets/03-23-agent-preview.png)

2. **Execute Publish**

   - Click the **Publish agent** button.
   
   ![Click Publish agent button](../assets/03-24-agent-publish-agent.png)

   - Click the **Publish** button.
   
   ![Click Publish button](../assets/03-24-agent-publish.png)
   
   - Verify publish settings:
     ```
     Version: 1.0
     Status: Published
     Endpoint: [Auto-generated endpoint]
     ```
   
   ![Verify publish completion](../assets/03-25-agent-published.png)

### Invoking Agents

#### 1. Azure CLI Login

First log in to Azure:

```bash
az login 
```

If using multi-tenant, specify tenant ID:
```bash
az login --tenant <tenant-id>
```

#### 2. Invoke Using Python SDK

> 💡 **Practice Tip**: The code below is for reference. During practice, open the `invokeAgent.py` file in the root path of this repository, modify `FOUNDRY_ENDPOINT` and `AGENT_NAME` values for your environment, then execute.

Example `invokeAgent.py` file:

```python
# Microsoft Foundry Agent Invocation using Activity Protocol
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# TODO: Update these values with your actual Microsoft Foundry details
# Get these from: https://ai.azure.com → Your Project → Deployments
FOUNDRY_ENDPOINT = "https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>"
AGENT_NAME = "ModelRouterAgent"  # Name of agent to invoke
API_VERSION = "2025-11-15-preview"

# Create OpenAI client with Azure authentication
client = OpenAI(
    api_key=get_bearer_token_provider(
        DefaultAzureCredential(), 
        "https://ai.azure.com/.default"
    ),
    base_url=f"{FOUNDRY_ENDPOINT}/applications/{AGENT_NAME}/protocols/openai",
    default_query={"api-version": API_VERSION}
)

try:
    # Call the agent using responses API
    response = client.responses.create(
        input="Recommend a 2 night 3 day travel itinerary for Jeju Island"
    )
    
    print(f"Response: {response.output_text}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\n🔍 Troubleshooting:")
    print("1. Check your endpoint URL at https://ai.azure.com")
    print("2. Verify the project name and agent name exist")
    print("3. Ensure you're logged in: az login")
    print("4. Confirm the agent is deployed and running")
```

#### 3. Check Endpoint Information

How to check endpoint information in Foundry portal:

1. Select published agent in Build > Agents
2. Click **Publish** button, then click **View details**
3. Copy the following information:
   - Agent application
   - Activity Protocol endpoint
   - Response API endpoint

![Check Endpoint information](../assets/03-26-agent-endpoint.png)

#### 4. Execute

```bash
# Create virtual environment (optional)
python -m venv .venv
source .venv/bin/activate  # Windows: venv\Scripts\activate

# Install required packages (including pre-release version)
pip install openai azure-identity
pip install --pre azure-ai-projects

# Run script
python invokeAgent.py
```

### 🔐 Authentication Options

#### Option 1: DefaultAzureCredential (Recommended)
```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
```

#### Option 2: Managed Identity (When running on Azure resources)
```python
from azure.identity import ManagedIdentityCredential
credential = ManagedIdentityCredential()
```

#### Option 3: Service Principal
```python
from azure.identity import ClientSecretCredential
credential = ClientSecretCredential(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)
```

### ✅ Verification Checklist

- Verify agent published successfully
- Confirm Python script runs without errors
- Check response returns as expected

---

## 📚 Additional Resources

- [Microsoft Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry)
- [Agent SDK Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?view=foundry&pivots=programming-language-python)
- [File Search Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/file-search?view=foundry&pivots=python)
- [Web Search Integration](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/web-search?view=foundry&pivots=python)

---

## Next Steps

You've created various agents! Now let's build an advanced knowledge base using Foundry IQ:

➡️ **[04. Foundry IQ](./04-foundry-iq.md)**: Learn knowledge base construction using AI Search and Blob Storage.

---

[← Previous: Models and Deployment](./02-models.md) | [Home](./README.md) | [Next: Foundry IQ →](./04-foundry-iq.md)
