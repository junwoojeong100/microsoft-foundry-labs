# 05. Workflows

This module teaches you how to build sophisticated workflows that orchestrate multiple agents to perform complex tasks.

## 📋 Table of Contents

- [Workflow Overview](#workflow-overview)
- [Sequential Workflow](#sequential-workflow)
- [Group Chat Workflow](#group-chat-workflow)
- [Human-in-loop Workflow](#human-in-loop-workflow)
- [Next Steps](#next-steps)

## 🎯 Learning Objectives

- Understand core concepts of Microsoft Foundry workflows
- Build sequential task flows through Sequential Workflow
- Implement multi-agent collaboration through Group Chat Workflow
- Set up human intervention points through Human-in-loop pattern
- Deploy workflows and programmatic invocation

## ⏱️ Estimated Time

Approximately 20 minutes

---

## Workflow Overview

### What is a Workflow?

A workflow is an automated system that coordinates multiple AI agents to perform complex tasks step by step.

### Workflow Types

```
Single Agent → Sequential Workflow → Group Chat → Human-in-loop
(Simple)                                                    (Complex)
```

| Type | Description | Use Cases |
|------|-------------|-----------|
| **Sequential** | Sequential execution | Data pipelines, document processing |
| **Parallel** | Parallel execution | Simultaneous analysis, multi-search |
| **Group Chat** | Agent-to-agent dialogue | Collaborative problem-solving, decision-making |
| **Human-in-loop** | Human intervention | Approval processes, verification |
| **Conditional** | Conditional branching | Dynamic routing, error handling |

### Workflow Components

```python
Workflow {
    Agents: [Agent1, Agent2, Agent3]
    Flow: Sequential | Parallel | Conditional
    Inputs: User request, Context
    Outputs: Final result, Intermediate results
    Handoffs: Agent transitions
    Termination: Completion condition
}
```

---

## Sequential Workflow

Build an agent chain that executes sequentially. We'll use a travel planning workflow as an example.

[Content continues with all the workflow creation steps, including TravelPlannerAgent, LocalAgent, TravelSummaryAgent creation, testing, and deployment instructions...]

---

## Group Chat Workflow

A workflow where multiple agents collaborate through conversation to solve problems.

[Content continues with StudentAgent and TeacherAgent creation, configuration, and testing...]

---

## Human-in-loop Workflow

A pattern that pauses the workflow at points requiring human approval or input.

[Content continues with Human-in-loop workflow design, configuration, and testing scenarios...]

---

## 📚 Additional Resources

- [Microsoft Foundry Workflows Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/workflow?view=foundry)
- [Microsoft Agent Framework Workflows Orchestrations Patterns](https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview)

## Next Steps

You've built complex workflows! Now learn how to evaluate agent and workflow performance:

➡️ **[06. Evaluations](./06-evaluations.md)**: Systematically evaluate agent and workflow quality.

---

[← Previous: Foundry IQ](./04-foundry-iq.md) | [Main](./README.md) | [Next: Evaluations →](./06-evaluations.md)
