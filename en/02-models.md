# 02. Models and Deployment

This module teaches you how to explore and deploy various LLM models available through Microsoft Foundry.

## 📋 Table of Contents

- [Discover Models](#discover-models)
- [Compare and Deploy Models](#compare-and-deploy-models)
- [Deploy Embedding Model](#deploy-embedding-model)
- [Deploy Model Router](#deploy-model-router)
- [Configure Model Router](#configure-model-router)
- [Next Steps](#next-steps)

## 🎯 Learning Objectives

- Compare model performance using the model leaderboard
- Understand how to deploy various AI models
- Set up and configure Model Router
- Understand model routing strategies

## ⏱️ Estimated Time

Approximately 15 minutes

---

## Discover Models

You can explore various AI models in the Discover section of the Foundry portal.

### Step-by-Step Guide

1. **Navigate to Discover Section**
   - Click **Discover** in the left menu of the Foundry portal.

   ![Discover > Models menu](../assets/02-00-discover-overview.png)

   - Select the **Models** menu.
   
   ![Discover > Models menu](../assets/02-01-discover-models.png)

2. **Check Model Leaderboard**
   - Click the **View leaderboard** option.
   - You can review performance metrics for various models:
     - Quality scores
     - Latency
     - Cost
     - Context window
     - Modality support (text, vision, audio)
   
   ![Model Leaderboard screen](../assets/02-02-model-leaderboard.png)

3. **Understand Model Categories**
   - **Language Models**: GPT-5.1, GPT-5, Claude, etc.
   - **Embedding Models**: text-embedding-3-large, text-embedding-ada-002, etc.

### 💡 Tips

- The leaderboard is updated regularly, so check for the latest models
- Review capabilities and limitations on each model's detail page

---

## Compare and Deploy Models

### Deploy GPT-5.1 Model

1. **Use Model Comparison Feature**
   - Click the **Compare models** button on the Models page.
   - Select the models you want to compare (e.g., GPT-5.1, GPT-5, Claude 4.5 Sonnet).
   - Compare performance, cost, and features.
   
   ![Compare models feature](../assets/02-03-model-compare.png)

2. **Select and Deploy GPT-5.1**
   - Find **gpt-5.1** in the model list.
   - Click the model card to view detailed information.
   
   ![GPT-5.1 model card](../assets/02-04-gpt51-model-card.png)

3. **Deployment Configuration**
   - Click the **Deploy** button.
   
   ![Deploy button](../assets/02-05-gpt51-deploy-button.png)

4. **Complete Deployment**
   - Click **Default settings** to start deployment.
   - Deployment takes approximately 1-2 minutes to complete.

### ✅ Verification Checklist

- Verify deployed `gpt-5.1` model in Build > Models section
- Confirm deployment status is "Succeeded"
- Check that Endpoint URL was created

![Verify deployed gpt-5.1 in Build > Models](../assets/02-07-gpt51-deployed.png)

---

## Deploy Embedding Model

Embedding models convert text into vectors, enabling semantic search and similarity calculations.

### Step-by-Step Guide

1. **Search for Embedding Model**
   - Enter **"text-embedding"** in the search box on the Discover > Models page.
   - You can use filters to display only Embedding models.
   
   ![Search text-embedding](../assets/02-08-embedding-search.png)

2. **Select text-embedding-3-large**
   - Select the **text-embedding-3-large** model.
   - Review model details:
     - Dimensions: 3072
   
   ![text-embedding-3-large model card](../assets/02-09-embedding-model-card.png)

3. **Deployment Configuration**
   ```
   Deployment name: text-embedding-3-large
   Model version: [Latest version]
   Deployment type: Standard
   ```

4. **Execute Deployment**
   - Click the **Deploy** button to deploy.
   
   ![Verify deployment completion](../assets/02-10-embedding-deployed.png)

---

## Deploy Model Router

Model Router provides intelligent routing across multiple models to optimize cost, quality, and performance.

### Step-by-Step Guide

1. **Search for Model Router**
   - Search for **"model-router"** in Discover > Models.
   
   ![Search model-router](../assets/02-11-model-router-search.png)

2. **Review Model Router Information**
   - Key features of Model Router:
     - Automatic model selection
     - Load balancing
     - Cost optimization
     - Quality-based routing

3. **Deployment Configuration**
   ```
   Deployment name: model-router
   Routing strategy: Balanced (default)
   Included models: [Automatically detected available models]
   ```
   
   ![Model Router deployment settings](../assets/02-12-model-router-deploy.png)

4. **Complete Deployment**
   - Click the **Deploy** button.
   - Model Router automatically detects available deployed models.

### ✅ Verification Checklist

- Verify `model-router` deployment in Build > Models
- Check deployment status
- Verify list of models accessible to the Router

![Complete Build > Models deployment list](../assets/02-15-models-overview.png)

---

## Configure Model Router

Configure the Model Router's routing strategy to align with your application requirements and optimize performance.

### Step-by-Step Guide

1. **Navigate to Model Router Details Page**
   - Go to Build > Models section.
   - Click the deployed **model-router**.

2. **Enter Edit Mode**
   - Select the **Details** tab.
   - Click the **Edit** button.
   
   ![Model Router settings screen (Edit mode)](../assets/02-13-model-router-config.png)

3. **Model Router Configuration**
   
   #### Routing Mode Options:
   
   ![Routing Mode options](../assets/02-14-model-router-modes.png)
   
   **a) Balanced Mode**
   ```
   Description: Maintains balance between cost, quality, and performance
   Use case: General production workloads
   Behavior: Automatically selects appropriate model based on request
   ```

   **b) Quality Mode**
   ```
   Description: Prioritizes highest quality responses
   Use case: Applications where accuracy is critical
   Behavior: Prioritizes best performing models
   Cost: Relatively higher cost
   ```

   **c) Cost Mode**
   ```
   Description: Prioritizes cost optimization
   Use case: Processing large volumes of simple requests
   Behavior: Prioritizes cost-efficient models
   Quality: Maintains basic quality
   ```

4. **Select Routing Mode**
   - For the workshop, select **Balanced** mode.
   - You can change to other modes as needed.

5. **Save and Apply**
   - Click the **Save** button to save settings.
   - Changes are applied immediately.

### 📊 Model Router Operation Example

```
User request → Model Router → Decision:
  - Simple question → GPT-5-nano (low cost)
  - Complex analysis → GPT-5-mini (high quality)
  - Code generation → Codex family
  - High load → Load balancing
```

### 💡 Optimization Tips

- **Development environment**: Cost Mode for cost savings
- **Production**: Balanced Mode for stability
- **Customer-facing service**: Quality Mode for user experience
- **A/B Testing**: Compare performance across modes

---

## 📚 Additional Resources

- [Model Catalog Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?view=foundry&tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard&pivots=azure-openai)
- [Model Router Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-router?view=foundry)
- [Embedding Models Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/embeddings?view=foundry&tabs=python-new)

---

## Next Steps

Model deployment is complete! Now let's use these models to build agents:

➡️ **[03. Agent Development](./03-agents.md)**: Create AI agents with various capabilities.

---

[← Previous: Environment Setup](./01-setup.md) | [Main](./README.md) | [Next: Agent Development →](./03-agents.md)
