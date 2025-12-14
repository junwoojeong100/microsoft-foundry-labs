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
| **Chunking Strategy** | Manual implementation | Optimized defaults included |
| **Retrieval Optimization** | Manual tuning required | AI-powered automatic optimization |
| **Multi-source Integration** | Complex implementation | Seamless integration |
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
   
   ![Foundry IQ section](../../assets/04-01-foundry-iq-menu.png)
   
   - The message **Connect to an AI Search resource to get started** is displayed.
   
   ![Connect to AI Search resource message](../../assets/04-02-foundry-iq-connect.png)
   
   - Click the **Create new resource** button.

2. **Search Service Configuration**

   Navigate to Azure Portal's search service creation page:

   ```
   Resource group: foundry
   Service name: foundry<Your unique name>
   Location: Sweden Central
   Pricing tier: Basic
   ```
   
   ![Search Service creation settings](../../assets/04-04-ai-search-settings.png)

   **Pricing Tier Selection Guide**:
   - **Free**: Testing, 50MB, 3 indexes (1 per subscription)
   - **Basic**: Development/small-scale, 160GB, 15 indexes
   - **Standard**: Production, 512GB+, 50 indexes
   - **Storage Optimized**: Large-scale data, 2TB+
   
   ![Pricing tier selection screen](../../assets/04-05-ai-search-pricing-tiers.png)

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
   
   ![Managed Identity settings](../../assets/04-06-ai-search-identity.png)

2. **Enable System Assigned Identity**

   ```
   Status: On
   ```

   - Click the **Save** button.
   - Verify Object ID was created.

   ![Enable Managed Identity](../../assets/04-06-ai-search-identity-enable.png)

### Connect AI Search to Foundry

1. **Return to Foundry IQ**

   - Return to the **Foundry IQ** section in Foundry portal.

2. **Select Search Resource**

   - Click the **Select a resource** or **Connect** button.
   - Select the created Search Service from dropdown.

   ![Connect AI Search](../../assets/04-07-foundry-iq-connect.png)

3. **Complete Connection**

   - Click the **Connect** button.
   - Once connection is successful, Foundry IQ dashboard is enabled.
   
   ![AI Search connection complete](../../assets/04-07-foundry-iq-connected.png)

### ✅ Verification Checklist

- Verify AI Search resource is created and in "Running" state
- Confirm Managed Identity is enabled
- Check connection to Foundry IQ is complete

---

## Create Knowledge Base (AI Search Index)

Create a Knowledge Base using an existing AI Search Index.

### Create Storage Account and Container

1. **Create Storage Account**

   - Search for **Storage accounts** in Azure Portal.

   ![Storage Accounts](../../assets/04-08-storage-account.png)

   - Click the **+ Create** button.
   
   ![Storage Account creation button](../../assets/04-08-storage-create-button.png)

   ```
   Resource group: foundry
   Storage account name: foundry<Your unique name>
   Region: Sweden Central
   Preferred storage type: Azure Blob Storage
   Primary workload: Cloud native
   Performance: Standard
   Redundancy: Locally-redundant storage (LRS)
   ```
   ![Create Storage Account](../../assets/04-08-storage-create.png)

   - Click **Review + create** > **Create**.

2. **Create Container**

   - Open the created Storage Account.
   - Select **Containers** from the left menu.
   - Click the **+ Container** button.
   
   ![Container button](../../assets/04-09-container-button.png)

   - Click the **+Add container** button.

   ```
   Name: foundry
   Public access level: Private
   ```

   ![Add container button](../../assets/04-09-add-container-button.png)

   - Click **Create**.

   ![Create container](../../assets/04-09-container-create.png)

### Configure IAM Permissions

Configure permissions between Storage Account and AI Search.

1. **Storage Blob Data Contributor - User Account**

   - Navigate to the created Storage Account.

   ![Storage Account](../../assets/04-10-storage-account.png)

   - Click **Access Control (IAM)** > **+ Add** > **Add role assignment**.

   ![Storage Account IAM menu Add role assignment](../../assets/04-11-storage-iam-add-role-assignment.png)

   ```
   Role: Storage Blob Data Contributor
   Assign access to: User, group, or service principal
   Members: [Select your Entra ID account]
   ```

   - Search for and select **Storage Blob Data Contributor**, then click the "Next" button.

   ![Storage Account IAM menu Role selection](../../assets/04-11-storage-iam-role-select.png)

   - Click **+Select members**, search for and select your Entra ID account, then click the "Select" button.

   ![Storage Account IAM menu Members selection](../../assets/04-11-storage-iam-member-select.png)

   - Click **Review + assign**.
   
   ![Storage Blob Data Contributor role assignment (User)](../../assets/04-12-storage-role-user.png)

2. **Storage Blob Data Contributor - Search Service**

   - Click **Add role assignment** again in the same way.

   ```
   Role: Storage Blob Data Contributor
   Assign access to: Managed identity
   Members:
     - Subscription: [Your subscription]
     - Managed identity: Search service
     - Select: foundry<Your unique name>
   ```

   - Search for and select **Storage Blob Data Contributor**, then click the "Next" button.
   - Select Managed identity in **Assign access to**.
   - Click **+Select members**, select your subscription, Search service, and Search service name, then click the "Select" button.

   ![Storage Blob Data Contributor role assignment (Search Service) - Managed Identity](../../assets/04-13-storage-role-search-managed-identity.png)

   - Click **Review + assign**.
   
   ![Storage Blob Data Contributor role assignment (Search Service)](../../assets/04-13-storage-role-search.png)

   ![Storage Blob Data Contributor role assignment (Search Service)](../../assets/04-13-storage-role-search-2.png)

Configure permissions between Microsoft Foundry and AI Search.

1. **Azure AI Project Manager Role Assignment**

   - Navigate to **Microsoft Foundry**.

   ![Foundry](../../assets/04-14-foundry.png)

   - Navigate to **Microsoft Foundry** resource.

   ![Foundry resource](../../assets/04-14-foundry-resource.png)

   - Click the created **Foundry resource** and click **Access Control (IAM)**.

   ![Click Foundry resource](../../assets/04-14-foundry-resource-click.png)

   - **Access Control (IAM)** > **+ Add** > **Add role assignment**

   - Search for and select **Azure AI Project Manager**, then click the "Next" button.

   ![Foundry resource IAM](../../assets/04-14-foundry-iam.png)

   - Select Managed identity in **Assign access to**.
   - Click **+Select members**, select your subscription, Search service, and Search service name, then click the "Select" button.

   ```
   Role: Azure AI Project Manager
   Assign access to: Managed identity
   Members:
     - Subscription: [Your subscription]
     - Managed identity: Search service
     - Select: foundry<Your unique name>
   ```

   ![Foundry resource IAM](../../assets/04-14-foundry-iam-2.png)

   - Click **Review + assign**.
   
   ![Azure AI Project Manager role assignment](../../assets/04-15-foundry-role-search.png)

   ![Azure AI Project Manager role assignment](../../assets/04-15-foundry-role-search-2.png)

### Upload Sample Data

   Download sample data provided by Microsoft:

   [Sample Data Link](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan)

   Download the following PDF files from the link above and upload them to the Container:
   - `Benefit_Options.pdf`
   - `employee_handbook.pdf`
   - `Northwind_Health_Plus_Benefits_Details.pdf`
   - `Northwind_Standard_Benefits_Details.pdf`
   - `PerksPlus.pdf`
   - `role_library.pdf`
   
   ![Upload sample data](../../assets/04-10-container-upload.png)

   ![Upload sample data](../../assets/04-10-container-upload-2.png)

### Run Import Data Wizard

1. **Start Import Wizard in AI Search**

   - Open the created AI Search in Azure Portal.
   - Click the **Import data (new)** button.
   
   ![Import data (new) button](../../assets/04-16-import-data-button.png)

2. **Select Data Source**

   - **Data Source**: Azure Blob Storage
   
   ![Select Azure Blob Storage](../../assets/04-17-import-data-source.png)

   - **Scenario**: RAG (Retrieval Augmented Generation)

   ![Select Scenario](../../assets/04-17-import-data-source-2.png)

3. **Configure Azure Blob Storage**

   ```
   Subscription: [Your subscription]
   Storage account: foundry<Your unique name>
   Blob container: foundry
   ```

   - Click **Next**.
   
   ![Configure Blob Storage](../../assets/04-18-import-blob-config.png)

4. **Configure Text Vectorization**

   ```
   Kind: Microsoft Foundry
   Subscription: [Your subscription]
   Foundry project: proj-default
   Model deployment: text-embedding-3-large
   Authentication type: API key
   ```

   - Click the **Check** button to verify connection
   - Click **Next**.
   
   ![Configure text vectorization](../../assets/04-19-import-vectorize-text.png)

5. **Image Vectorization (Optional)**

   - Click **Next**.

   ![Image vectorization](../../assets/04-19-image-vectorize.png)

6. **Advanced Ranking Configuration**

   ```
   ☑ Enable semantic ranker
   Schedule: Once (initial indexing only)
   ```

   - Semantic Ranker improves search result relevance.
   
   ![Configure semantic ranker](../../assets/04-20-import-semantic-ranker.png)

7. **Review and Create**

   - Click **Create**.
   - Indexing takes approximately 5-10 minutes.
   
   ![Review and create](../../assets/04-21-import-review-create.png)

   ![Review and create](../../assets/04-21-import-review-create-2.png)
   
   ![Start Searching](../../assets/04-22-start-searching.png)

### Create Knowledge Base

1. **Return to Foundry IQ**

   - Navigate to the **Foundry IQ** section in Foundry portal.

   ![Foundry IQ](../../assets/04-23-foundry-iq.png)

2. **Create Knowledge Base**

   - Click the **Create a knowledge base** button.
   - Select **Azure AI Search Index** and click the **Connect** button.

   ![Create Knowledge Base](../../assets/04-25-knowledge-base-create.png)

   - Change the **Knowledge source name** suffix number to **100**.
   - Select **Azure AI Search Index**, then click the **Create** button.
   
   ![Create knowledge source](../../assets/04-23-knowledge-source-create.png)

   ```
   Knowledge base name: knowledgebase100
   Chat completions model: gpt-4.1
   Retrieval reasoning effort: minimal
   ```

   - Verify the created **Knowledge source** and click the **Save knowledge base** button.
   
   ![Knowledge Base settings](../../assets/04-24-knowledge-base-settings.png)

   ![Knowledge Base list](../../assets/04-24-knowledge-base-list.png)

---

## Create Knowledge Base (Blob Storage)

Create a Knowledge Base with automatic indexing by directly connecting Blob Storage.

### Step-by-Step Guide

1. **Create New Knowledge Base**

   - Click the **+ Create knowledge base** button in Foundry IQ.

2. **Select Data Source**

   - Select **Azure Blob Storage** and click the **Connect** button.

   ![Direct Blob Storage connection](../../assets/04-28-blob-knowledge-create.png)

3. **Configure Knowledge Source**

   ```
   Name: ks-azureblob-200
   Storage account: foundry<Your unique name>
   Use managed identity: Yes
   Container name: foundry
   Content extraction mode: minimal
   Embedding model: text-embedding-3-large
   Chat completions model: gpt-4.1
   ```
   
   ![Blob Storage Knowledge Source settings](../../assets/04-29-blob-knowledge-settings.png)

4. **Create Knowledge Source**

   - Click the **Create** button.
   - Foundry automatically monitors and indexes Blob Storage.

5. **Create Knowledge Base**

   ```
   Knowledge base name: knowledgebase200
   Description: Auto-indexed employee handbook
   Chat completions model: gpt-4.1
   Retrieval reasoning effort: minimal
   Knowledge sources: ks-azureblob-200
   ```

   - Click the **Save knowledge base** button.
   
   ![Create Blob Storage Knowledge Base](../../assets/04-30-blob-knowledge-create.png)

   ![Blob Storage Knowledge Base creation complete](../../assets/04-30-blob-knowledge-created.png)

   ![Knowledge Base list](../../assets/04-30-knowledge-base-list.png)

### Blob Storage Method Advantages

| Feature | AI Search Index | Blob Storage Direct |
|---------|-----------------|---------------------|
| **Setup Complexity** | High | Low |
| **Auto Updates** | Manual re-indexing required | Automatic detection and indexing |
| **Customization** | High (fields, schema, etc.) | Low (automatic configuration) |
| **Performance** | High (optimizable) | Medium |
| **Use Cases** | Complex search requirements | Simple document search |

---

## KnowledgeAgent Integration

Integrate the created Knowledge Base with agents to provide knowledge-based responses.

### KnowledgeAgent (AI Search Index Connection)

1. **Create New Agent**

   - Navigate to Build > Agents.
   - Click the **+ Create agent** button.

   ```
   Agent name: KnowledgeAgent
   Model: gpt-5.1
   ```
   
   ![Create KnowledgeAgent](../../assets/04-31-knowledge-agent-create.png)

2. **Configure Instructions**

   ```
   You are an agent that answers based on the connected knowledge base.
   
   Important rules:
   1. Always answer based on Knowledge Base information
   2. Provide accurate information and specify when uncertain
   3. Quote directly from documents to increase answer reliability
   4. Honestly state you don't know if information is not in the Knowledge Base
   ```
   
   ![KnowledgeAgent Instructions](../../assets/04-32-knowledge-agent-instructions.png)

3. **Connect Knowledge**

   - Click the **Add** button in the **Knowledge** section.
   - Select **Connect to Foundry IQ**.
   
   ![Connect Knowledge (Add button)](../../assets/04-33-knowledge-connect.png)

   ```
   Connection: foundry<Your unique name> (AI Search)
   Knowledge base: knowledgebase100
   ```

   - Click the **Connect** button.
   
   ![Select Knowledge base](../../assets/04-34-knowledge-select.png)

   - Click the **Save** button.

   ![Save Knowledge base](../../assets/04-34-knowledge-complete.png)

4. **Test Agent**

   Test the following questions in the Chat tab:

   ```
   User: Tell me about the items covered by PerkPlus
   ```
   Expected answer: Description of Health & Wellness, Professional Development, Work-Life Balance, Financial Benefits

   ```
   User: Tell me about items not covered
   ```
   Expected answer: Description of Non-Covered Items such as personal travel expenses, personal meal costs

   ```
   User: Tell me about roles requiring CPA certification
   ```
   Expected answer: Description of Financial Analyst, Controller, Tax Specialist roles
   
   ![KnowledgeAgent test](../../assets/04-35-knowledge-agent-test.png)

### KnowledgeAgent2 (Blob Storage Connection)

Create an agent using Blob Storage-based Knowledge Base in the same way.

1. **Create New Agent**

   ```
   Agent name: KnowledgeAgent2
   Model: gpt-5.1
   ```

2. **Configure Instructions**

   (Use the same Instructions as KnowledgeAgent above)

3. **Connect Knowledge**

   ```
   Connection: foundry<Your unique name> (AI Search)
   Knowledge base: knowledgebase200
   ```

4. **Test Agent**

   Test with the same questions and compare responses between the two agents.

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

[← Previous: Agent Development](./03-agents.md) | [Home](./README.md) | [Next: Workflows →](./05-workflows.md)
