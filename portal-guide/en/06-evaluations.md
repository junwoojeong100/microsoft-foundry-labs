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

Before deploying AI agents to production, verification is essential across multiple dimensions:

```
Accuracy → Relevance → Consistency → Fluency → Safety
```

Deploying without proper evaluation can result in:
- ❌ Degraded user trust due to inaccurate responses
- ❌ Poor user experience from irrelevant answers
- ❌ Brand reputation damage from inconsistent quality
- ❌ Legal and compliance risks from inappropriate content generation

### Evaluation Types

| Evaluation Type | Description | When to Use |
|----------------|-------------|-------------|
| **Offline Evaluation** | Evaluate with test data before deployment | Development phase |
| **A/B Testing** | Compare two versions | Production deployment |
| **Online Monitoring** | Real-time performance monitoring | During operation |
| **Human Evaluation** | Direct human evaluation | Quality verification |

### Microsoft Foundry's Evaluation Features

Foundry automates:
- ✅ Test data generation (Synthetic generation)
- ✅ Apply various evaluation metrics
- ✅ Large-scale evaluation execution
- ✅ Result visualization and analysis

---

## Create Evaluation

Let's evaluate the previously created `ModelRouterAgent`.

### Step-by-Step Guide

1. **Navigate to Evaluations Section**

   - Select **Build** from the top right menu in the Foundry portal.
   - Click the **Evaluations** menu.
   
   ![Build > Evaluations menu](../../assets/06-01-evaluations-menu.png)

2. **Evaluation Catalog**

   ![Evaluations Catalog](../../assets/06-01-evaluations-catalog.png)

3. **Create New Evaluation**

   - Click the **+ Create new evaluation** or **New evaluation** button.
   
   ![Create new evaluation button](../../assets/06-02-create-evaluation.png)

4. **Select Target**

   Select the evaluation target:
   
   ![Select Target (Agent)](../../assets/06-03-evaluation-target.png)

   ```
   Target type: Agent
   Agent: ModelRouterAgent
   Version: Latest (or specific version)
   ```

   **Other Target Options**:
   - **Agent**: Evaluate single agent
   - **Workflow**: Evaluate workflow
   - **Model**: Evaluate model directly
   - **Endpoint**: Evaluate external API endpoint

5. **Configure Data**

   Select test data:
   
   ![Data configuration (Synthetic generation)](../../assets/06-04-evaluation-data1.png)

   ![Data configuration (Synthetic generation)](../../assets/06-04-evaluation-data2.png)

   ![Data configuration (Synthetic generation)](../../assets/06-04-evaluation-data3.png)

   ```
   Data source: Synthetic generation
   
   Topic: General conversation and information provision
   
   Number of samples: 50
   (More samples are more reliable but take longer)
   
   Languages: Korean, English
   ```

   **What is Synthetic Generation?**
   - AI automatically generates various test questions
   - Simulates actual usage patterns
   - No need to manually write test cases

   **Other Data Options**:
   - **Upload dataset**: Upload CSV/JSON file
   - **Use existing dataset**: Use previously saved dataset

6. **Select Criteria**

   Select evaluation criteria:

   ```
   ☑ Groundedness (Whether answer is fact-based)
   ☑ Relevance (Relevance between question and answer)
   ☑ Coherence (Answer consistency)
   ☑ Fluency (Answer naturalness)
   ```

   ![Select Metrics (Groundedness, Relevance, etc.)](../../assets/06-05-evaluation-metrics.png)

   See the section below for detailed explanation of each criterion.

7. **Review**

   Review settings:
   
   ![Review and create](../../assets/06-06-evaluation-review.png)

   ```
   Target: ModelRouterAgent (Latest)
   Data: Synthetic (50 samples, Korean/English)
   Criteria: Groundedness, Relevance, Coherence, Fluency
   Estimated time: ~10-15 minutes
   Estimated cost: $2-5 (varies by sample count)
   ```

8. **Submit**

   - After verifying all settings, click the **Submit** button.
   - Evaluation runs in the background.
   - Progress can be checked on the Evaluations page.

   ![Evaluation Run](../../assets/06-06-evaluation-run.png)

9. **Evaluation Result**

   ![Evaluation Result](../../assets/06-06-evaluation-result.png)

   ![Evaluation Result](../../assets/06-06-evaluation-result2.png)

   ![Evaluation Result](../../assets/06-06-evaluation-result3.png)

   ![Evaluation Result](../../assets/06-06-evaluation-result4.png)

   ![Evaluation Result](../../assets/06-06-evaluation-result5.png)

   ![Evaluation Result](../../assets/06-06-evaluation-result6.png)

### ✅ Verification Checklist

- Verify evaluation is in "Running" state
- Check estimated completion time
- Create evaluations for other agents or workflows if needed

---

## Understanding Evaluation Criteria

### Complete List of Foundry Provided Evaluators

Foundry provides 32 evaluators across 6 categories.

#### 🎯 General Purpose

| Evaluator | Description |
|-----------|-------------|
| **CoherenceEvaluator** | Measures logical consistency and flow of responses |
| **FluencyEvaluator** | Measures natural language quality and readability |
| **QAEvaluator** | Comprehensive Q&A evaluation *(Composite: Groundedness, Relevance, Coherence, Fluency, Similarity, F1Score)* |

#### 📊 Textual Similarity

| Evaluator | Description |
|-----------|-------------|
| **SimilarityEvaluator** | Semantic similarity between response and correct answer |
| **F1ScoreEvaluator** | Harmonic mean of precision and recall |
| **BleuScoreEvaluator** | Machine translation quality (n-gram based) |
| **GleuScoreEvaluator** | Sentence-level BLEU variation |
| **RougeScoreEvaluator** | Summary quality (n-gram recall) |
| **MeteorScoreEvaluator** | Translation evaluation considering synonyms/stems |

#### 🔍 RAG (Retrieval-Augmented Generation)

| Evaluator | Description |
|-----------|-------------|
| **RetrievalEvaluator** | Information retrieval effectiveness |
| **DocumentRetrievalEvaluator** | Retrieval accuracy vs correct answer |
| **GroundednessEvaluator** | Whether response matches context (1-5 score) |
| **GroundednessProEvaluator** | Advanced grounding evaluation (Azure AI Content Safety based) |
| **RelevanceEvaluator** | Relevance between response and question (1-5 score) |
| **ResponseCompletenessEvaluator** | Response completeness vs correct answer |

#### 🤖 Agentic

| Evaluator | Description |
|-----------|-------------|
| **IntentResolutionEvaluator** | User intent understanding accuracy |
| **TaskAdherenceEvaluator** | Degree of identified task execution |
| **ToolCallAccuracyEvaluator** | Correct tool selection and invocation |

#### 🛡️ Risk and Safety

| Evaluator | Description |
|-----------|-------------|
| **ViolenceEvaluator** | Detects violent content |
| **SexualEvaluator** | Detects sexual content |
| **SelfHarmEvaluator** | Detects self-harm related content |
| **HateUnfairnessEvaluator** | Detects hate/discrimination content |
| **IndirectAttackEvaluator** | Detects indirect attacks (jailbreak attempts, etc.) |
| **ProtectedMaterialEvaluator** | Detects copyrighted protected material |
| **UngroundedAttributesEvaluator** | Detects unfounded claims |
| **CodeVulnerabilityEvaluator** | Detects code security vulnerabilities |
| **ContentSafetyEvaluator** | Comprehensive safety evaluation *(Composite: Violence, Sexual, SelfHarm, HateUnfairness)* |

#### 🔧 Azure OpenAI Graders

| Evaluator | Description |
|-----------|-------------|
| **AzureOpenAILabelGrader** | Label-based grading |
| **AzureOpenAIStringCheckGrader** | String validation grading |
| **AzureOpenAITextSimilarityGrader** | Text similarity grading |
| **AzureOpenAIGrader** | General-purpose Azure OpenAI grading |

---

### 4 Core Evaluation Criteria

This workshop uses the 4 most commonly used evaluation criteria.

| Criterion | Definition | Scoring Criteria |
|-----------|------------|------------------|
| **Groundedness** | Whether answer is fact/context-based | 1=hallucination, 5=fact-based |
| **Relevance** | Whether answer relates to question | 1=irrelevant, 5=perfect match |
| **Coherence** | Whether answer is logically structured | 1=confused, 5=perfect structure |
| **Fluency** | Whether answer is grammatically natural | 1=awkward, 5=perfectly natural |

**Why Each Criterion Matters**:

| Groundedness | Relevance | Coherence | Fluency |
|--------------|-----------|-----------|---------|
| Secure user trust | Improve user satisfaction | Easy-to-understand answers | Enhance user experience |
| Minimize legal liability | Efficient information delivery | Professional image | Maintain brand image |
| Prevent misinformation | Maintain conversation flow | Improve reliability | Increase understanding |

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

[← Previous: Workflows](./05-workflows.md) | [Home](./README.md) | [Next: Control Plane →](./07-control-plane.md)
