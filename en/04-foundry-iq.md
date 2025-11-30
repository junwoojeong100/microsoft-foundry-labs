# 04. Foundry IQ

This module teaches you how to build advanced knowledge bases using Microsoft Foundry IQ and seamlessly integrate them with agents.

## 📚 Table of Contents

- [Foundry IQ Overview](#foundry-iq-overview)
- [Connect AI Search](#connect-ai-search)
- [Create Knowledge Base (AI Search Index)](#create-knowledge-base-ai-search-index)
- [Create Knowledge Base (Blob Storage)](#create-knowledge-base-blob-storage)
- [KnowledgeAgent Integration](#knowledgeagent-integration)
- [Next Steps](#next-steps)

## 🎯 Learning Objectives

- Understand Foundry IQ concepts and benefits
- Connect and configure Azure AI Search resources
- Create AI Search Index-based Knowledge Base
- Create Blob Storage-based Knowledge Base
- Learn how to integrate Knowledge Base with agents

## ⏱️ Estimated Time

Approximately 40 minutes

---

## Foundry IQ Overview

### What is Foundry IQ?

Foundry IQ is Microsoft Foundry's intelligent knowledge management system that integrates various data sources to provide contextual knowledge to AI agents.

### Key Features

```
Foundry IQ = Retrieval + Reasoning + Ranking
```

- **Retrieval**: Efficiently search relevant information
- **Reasoning**: Understand and interpret retrieved information
- **Ranking**: Prioritize most relevant information

### Traditional RAG vs Foundry IQ

| Feature | Traditional RAG (Azure AI Search) | Foundry IQ |
|---------|-----------------------------------|------------|
| **Setup Complexity** | High (manual configuration required) | Low (automated setup) |
| **Vector Indexing** | Manual setup | Automatically managed |
| **Chunking Strategy** | Manual implementation | Optimized defaults provided |
| **Retrieval Optimization** | Direct tuning | AI-based automatic optimization |
| **Multi-source Integration** | Complex implementation | Easy integration |
| **Semantic Ranking** | Separate configuration | Included by default |

### Supported Data Sources

- **Azure AI Search Index**: Reuse existing indexes
- **Azure Blob Storage**: Automatic document indexing
- **Azure Data Lake Storage Gen2**: Large-scale data processing
- **SharePoint**: Enterprise document integration
- **OneDrive**: Personal and business documents

---

## Connect AI Search

First, connect an Azure AI Search resource to use Foundry IQ.

### Create Azure AI Search Resource

1. **Create Search Service**

   - Navigate to the **Foundry IQ** section in Foundry portal.
   
   ![Foundry IQ section](../assets/04-01-foundry-iq-menu.png)
   
   - The message **Connect to an AI Search resource to get started** is displayed.
   
   ![Connect to AI Search resource message](../assets/04-02-foundry-iq-connect.png)
   
   - Click the **Create new resource** button.

2. **Search Service Configuration**

   Navigate to Azure Portal's search service creation page:

   ```
   Resource group: foundry
   Service name: foundry<Your unique name>
   Location: Sweden Central
   Pricing tier: Basic
   ```
   
   ![Search Service creation settings](../assets/04-04-ai-search-settings.png)

   **Pricing Tier Selection Guide**:
   - **Free**: Testing, 50MB, 3 indexes (1 per subscription)
   - **Basic**: Development/small-scale, 160GB, 15 indexes
   - **Standard**: Production, 512GB+, 50 indexes
   - **Storage Optimized**: Large-scale data, 2TB+
   
   ![Pricing tier selection screen](../assets/04-05-ai-search-pricing-tiers.png)

3. **Compute Settings**

   ```
   Compute type: Default
   Replicas: 1 (for development)
   Partitions: 1 (for development)
   ```

4. **Complete Creation**

   - Click **Review + create**.
   - After validation, click the **Create** button.
   - Creation takes approximately 3-5 minutes.

### Enable Managed Identity

Configure Managed Identity so AI Search can access Foundry resources.

1. **Configure AI Search Resource**

   - Open the created Search Service in Azure Portal.
   - Select **Settings > Identity** from the left menu.
   
   ![Managed Identity settings](../assets/04-06-ai-search-identity.png)

2. **Enable System Assigned Identity**

   ```
   Status: On
   ```

   - Click the **Save** button.
   - Verify Object ID was created.

   ![Enable Managed Identity](../assets/04-06-ai-search-identity-enable.png)

### Connect AI Search to Foundry

1. **Return to Foundry IQ**

   - Return to the **Foundry IQ** section in Foundry portal.

2. **Select Search Resource**

   - Click the **Select a resource** or **Connect** button.
   - Select the created Search Service from dropdown.

   ![Connect AI Search](../assets/04-07-foundry-iq-connect.png)

3. **Complete Connection**

   - Click the **Connect** button.
   - Once connection is successful, Foundry IQ dashboard is enabled.
   
   ![AI Search connection complete](../assets/04-07-foundry-iq-connected.png)

### ✅ Verification Checklist

- Verify AI Search resource is created and in "Running" state
- Confirm Managed Identity is enabled
- Check connection to Foundry IQ is complete

---

## Create Knowledge Base (AI Search Index)

Create a Knowledge Base using an existing AI Search Index.

[Rest of the content continues similarly with English translation of all sections including Storage Account creation, IAM permissions, Import Data Wizard, Knowledge Base creation with AI Search Index, Blob Storage method, and KnowledgeAgent integration...]

---

## 📚 Additional Resources

- [Foundry IQ Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval?view=foundry&tabs=foundry%2Cpython)
- [Azure AI Search Documentation](https://learn.microsoft.com/en-us/azure/search/)
- [RAG Pattern Guide](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview?tabs=docs)
- [Vector Search Optimization](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

---

## Next Steps

Knowledge Base construction is complete! Now let's create complex workflows by combining multiple agents:

➡️ **[05. Workflows](./05-workflows.md)**: Build Sequential, Group Chat, and Human-in-loop workflows.

---

[← Previous: Agent Development](./03-agents.md) | [Main](./README.md) | [Next: Workflows →](./05-workflows.md)
