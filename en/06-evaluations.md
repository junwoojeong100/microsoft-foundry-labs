# 06. Evaluations

This module teaches you how to systematically evaluate and measure the performance of AI agents and workflows.

## 📋 Table of Contents

- [Evaluation Overview](#evaluation-overview)
- [Create Evaluation](#create-evaluation)
- [Understanding Evaluation Criteria](#understanding-evaluation-criteria)
- [Run Evaluation and Analyze Results](#run-evaluation-and-analyze-results)
- [Evaluation Best Practices](#evaluation-best-practices)
- [Next Steps](#next-steps)

## 🎯 Learning Objectives

- Understand importance of AI agent evaluation
- Utilize Foundry's automatic evaluation features
- Learn meaning and usage of various evaluation metrics
- Perform evaluation using synthetic data
- Interpret evaluation results and derive improvements

## ⏱️ Estimated Time

Approximately 10 minutes

---

## Evaluation Overview

### Why is Evaluation Important?

Before deploying AI agents to production, you need to verify:

```
Accuracy → Relevance → Consistency → Fluency → Safety
```

Deploying without evaluation leads to:
- ❌ User trust degradation from inaccurate responses
- ❌ Poor user experience from irrelevant responses
- ❌ Brand image damage from inconsistent quality
- ❌ Legal issues from inappropriate content generation

### Evaluation Types

| Evaluation Type | Description | When to Use |
|----------------|-------------|-------------|
| **Offline Evaluation** | Evaluate with test data before deployment | Development phase |
| **A/B Testing** | Compare two versions | Production deployment |
| **Online Monitoring** | Real-time performance monitoring | During operation |
| **Human Evaluation** | Direct human evaluation | Quality verification |

### Azure AI Foundry's Evaluation Features

Foundry automates:
- ✅ Test data generation (Synthetic generation)
- ✅ Apply various evaluation metrics
- ✅ Large-scale evaluation execution
- ✅ Result visualization and analysis

---

## Create Evaluation

Let's evaluate the previously created `ModelRouterAgent`.

[Content continues with step-by-step evaluation creation, metric selection, and result analysis...]

---

## Understanding Evaluation Criteria

### Complete List of Foundry Provided Evaluators

Foundry provides 32 evaluators across 6 categories.

[Content continues with detailed descriptions of all evaluator categories: General Purpose, Textual Similarity, RAG, Agentic, Risk and Safety, Azure OpenAI Graders...]

---

## Evaluation Best Practices

| Item | Recommendation |
|------|---------------|
| **Sample Count** | Development: 10-20 / Testing: 50-100 / Production: 200+ |
| **Test Scenarios** | General·Complex·Ambiguous·Multilingual questions + Edge cases |
| **Evaluation Frequency** | During development: Every update / Pre-deployment: Required / Post-deployment: Weekly/Monthly |
| **Baseline Scores** | Groundedness ≥4.0 / Others ≥3.5 / Pass rate ≥80% |
| **Human Evaluation** | Parallel with automatic evaluation to discover new problem patterns |

---

## 📚 Additional Resources

- [Azure AI Evaluation Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability?view=foundry#what-are-evaluators)
- [Run Evaluations in Foundry Portal](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluate-generative-ai-app?view=foundry)
- [Agent Evaluation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators?view=foundry)

---

## Next Steps

You've learned how to evaluate agent and workflow quality! Now learn how to manage and monitor resources in production:

➡️ **[07. Control Plane](./07-control-plane.md)**: Learn Fleet management, monitoring, compliance, etc.

---

[← Previous: Workflows](./05-workflows.md) | [Main](./README.md) | [Next: Control Plane →](./07-control-plane.md)
