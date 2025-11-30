# Microsoft Foundry Hands-on Workshop

A hands-on workshop to learn Microsoft Foundry's core features through practical exercises. This workshop provides step-by-step experience with key Foundry functionalities, including model deployment, agent creation, knowledge base construction, and workflow design.

> 🌏 **Language / 언어**: [한국어 가이드](../README.md) | [English Guide](./README.md)

## 📚 Workshop Overview

This workshop covers the following topics using Microsoft Foundry's new portal:

- **Model Management**: Deploy various AI models and configure Model Router
- **Agent Development**: Build File Search, Web Search, and Knowledge-based agents
- **Foundry IQ**: Construct knowledge base using AI Search and Blob Storage
- **Workflows**: Design Sequential, Group Chat, and Human-in-loop workflows
- **Evaluations**: Evaluate and analyze agent performance
- **Management**: Operational monitoring through Control Plane

## 🎯 Prerequisites

### Required

- **Microsoft Entra ID account** (formerly Azure Active Directory)
- **Azure subscription** (activated account)
  - **Owner role** required for subscription
  - Permissions to create resources and assign roles needed
- **GitHub account**
- Azure Portal access
- Text editor or IDE (VS Code recommended)
- Python 3.8 or higher (for code execution practice)

### Recommended

- **GitHub Codespaces recommended** (enables browser-based practice)
  - No separate development environment setup required
  - Python, Azure CLI, and other tools pre-installed
  - Free usage hours included (120 core hours per month)
- Azure CLI installation (for local environment)
- Git installation (for local environment)
- Basic Python programming knowledge
- Basic REST API and JSON understanding

## 📖 Workshop Structure

Each module is structured for independent practice:

### [01. Environment Setup](./01-setup.md)
- Create Resource Group
- Create Foundry resource
- Enable New Foundry portal

### [02. Models and Deployment](./02-models.md)
- Explore model leaderboard
- Compare and deploy models
- Configure Model Router

### [03. Agent Development](./03-agents.md)
- Create ModelRouterAgent
- Build FileSearchAgent
- Build WebSearchAgent
- Build KnowledgeAgent
- Deploy and invoke agents

### [04. Foundry IQ](./04-foundry-iq.md)
- Foundry IQ overview
- Connect AI Search
- Create Knowledge Base (AI Search Index)
- Create Knowledge Base (Blob Storage)
- Integrate KnowledgeAgent

### [05. Workflows](./05-workflows.md)
- Build Sequential Workflow
- Build Group Chat Workflow
- Build Human-in-loop Workflow

### [06. Evaluations](./06-evaluations.md)
- Set up agent evaluation
- Define evaluation criteria
- Analyze evaluation results

### [07. Control Plane](./07-control-plane.md)
- Fleet Overview monitoring
- Assets management
- Compliance and security
- Quota management
- Admin features

## 🚀 Getting Started

1. **Start with Environment Setup**: Create necessary Azure resources by following [01-setup.md](./01-setup.md).

2. **Sequential learning recommended**: Since each module utilizes resources from previous modules, we recommend progressing in order.

3. **Select only needed parts**: If you're interested in specific features, you can select and practice only those sections.

## 📚 Reference Documentation

- [Microsoft Foundry Documentation](https://ai.azure.com/docs)
- [What is Microsoft Foundry](https://ai.azure.com/docs/what-is-azure-ai-foundry)
- [Get Started with Code](https://ai.azure.com/docs/quickstarts/get-started-code)
- [Foundry Agent Service at Ignite 2025](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-agent-service-at-ignite-2025-simple-to-build-powerful-to-deploy-trusted-/4469788)
- [Agents Overview](https://ai.azure.com/docs/agents/overview)

## 💡 Tips

- Clean up resources after each practice to reduce costs
- Check Azure Portal's Activity Log when errors occur
- Save code created during practice for reuse
- Periodically check resource usage in Control Plane

## 🤝 Contributing

If you have feedback or improvements for this workshop, please create an Issue.

## 📝 License

These workshop materials are provided for educational purposes.

---

**Next Steps**: [Set up Environment](./01-setup.md)
