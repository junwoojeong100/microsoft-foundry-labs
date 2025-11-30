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

A workflow is an automated orchestration system that coordinates multiple AI agents to perform complex, multi-step tasks in a structured manner.

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

### Create Required Agents

First, create the agents to be used in the workflow.

#### 1. TravelPlannerAgent

```
Agent name: TravelPlannerAgent
Description: Agent that plans travel destinations and itineraries
Model: gpt-5.1

Instructions:
You are a travel planning expert.

Responsibilities:
1. Analyze user's travel requirements
2. Recommend key attractions, restaurants, and accommodations at the destination
3. Create detailed daily travel itineraries
4. Present estimated costs and necessary items

Output format:
- Destination overview
- Daily itinerary (morning/lunch/evening activities)
- Recommended accommodations
- Estimated costs
- Packing list

Information to pass to next agent: Complete travel plan
```

#### 2. LocalAgent

```
Agent name: LocalAgent
Description: Agent that adds local information
Model: gpt-5.1

Tools: Web search (enabled)

Instructions:
You are a local information expert.

Responsibilities:
1. Receive travel plan from previous agent
2. Use Web search to find latest local information
3. Add real-time information:
   - Current weather and climate
   - Local festivals and events
   - Transportation information (routes, fares, duration)
   - Business hours and reservation information
   - Local culture and precautions

Output format:
- Original itinerary + enhanced local information
- Detailed transportation information
- List of places requiring reservations
- Local tips

Information to pass to next agent: Travel plan with added local information
```

#### 3. TravelSummaryAgent

```
Agent name: TravelSummaryAgent
Description: Agent that summarizes travel plan and creates final checklist
Model: gpt-5.1

Instructions:
You are a travel plan organization expert.

Responsibilities:
1. Synthesize information from previous agents
2. Organize into actionable final plan
3. Generate checklists

Output format:
📋 Travel Summary
- Destination: 
- Duration:
- Budget:

📅 Itinerary Summary (at-a-glance schedule)

✅ Pre-departure Checklist
- [ ] Item1
- [ ] Item2

🎒 Packing Checklist

📞 Emergency contacts and useful information

Final output: Printable travel guide
```

### Create Sequential Workflow

1. **Navigate to Workflows Section**

   - Select **Build** from the top right menu in the Foundry portal.
   - Click the **Workflows** menu.
   
   ![Build > Workflows menu](../assets/05-01-workflows-menu.png)

2. **Create New Workflow**

   - Click the **+ Create workflow** or **New workflow** button.
   - Select **Sequential Workflow**.
   
   ![Create workflow button](../assets/05-02-create-workflow.png)

   ![Create workflow button2](../assets/05-02-create-workflow-2.png)

3. **Add Agents**

   Add agents in sequence:
   
   ![Select an agent to invoke button](../assets/05-04-workflow-add-agent.png)

   ```
   Step 1: TravelPlannerAgent
     ↓
   Step 2: LocalAgent
     ↓
   Step 3: TravelSummaryAgent
   ```

   - Click **Select an agent to invoke** button at each step to select an agent.

   ![Select an agent to invoke button1](../assets/05-04-workflow-add-agent1.png)
   
   ![Select an agent to invoke button2](../assets/05-04-workflow-add-agent2.png)

   ![Select an agent to invoke button3](../assets/05-04-workflow-add-agent3.png)

   ![Complete workflow](../assets/05-02-overall-workflow.png)

4. **Save Workflow**

   - Click the **Save** button.

   ![Register workflow name](../assets/05-02-workflow-save.png)

   ![Save workflow name](../assets/05-02-workflow-saved.png)

### Test Workflow

1. **Preview Mode**

   - Click the **Preview** button.

2. **Test Question**

   ```
   User: Help me plan a 2-night 3-day trip to Jeju Island.
   ```

3. **Observe Execution Process**

   Check the output at each step:

   - **Step 1 (TravelPlannerAgent)**: Generate basic travel itinerary
   - **Step 2 (LocalAgent)**: Add local information (weather, transportation, events)
   - **Step 3 (TravelSummaryAgent)**: Final summary and checklist

   ![Workflow Preview](../assets/05-05-workflow-preview.png)

4. **Check Traces**

   - Execution time of each agent
   - Data transfer between agents
   - Final output generation process

### Deploy and Invoke Workflow

1. **Publish**

   - Click the **Publish** button.

   ![Workflow Publish-1](../assets/05-05-workflow-publish1.png)

   - Verify the version and publish.

   ![Workflow Publish-2](../assets/05-05-workflow-publish2.png)

   ![Workflow Publish-3](../assets/05-05-workflow-publish3.png)

2. **Invoke with Python SDK**

   > 💡 **Practice Tip**: The code below is for reference. For actual practice, open the `invokeWorkflow.py` file in the root path of this repository, update the `PROJECT_ENDPOINT` and `WORKFLOW_NAME` values for your environment, and then execute.

   Example `invokeWorkflow.py` file:

   ```python
   # Microsoft Foundry Workflow Invocation using Foundry SDK
   # Before running: pip install --pre azure-ai-projects>=2.0.0b1
   from azure.identity import DefaultAzureCredential
   from azure.ai.projects import AIProjectClient
   from azure.ai.projects.models import ResponseStreamEventType
   
   # Project configuration
   PROJECT_ENDPOINT = "https://<foundry-resource-name>.services.ai.azure.com/api/projects/proj-default"
   WORKFLOW_NAME = "Sequential-Workflow"
   WORKFLOW_VERSION = "1"  # Update to published version
   
   # Create AI Project client
   project_client = AIProjectClient(
       endpoint=PROJECT_ENDPOINT,
       credential=DefaultAzureCredential(),
   )
   
   with project_client:
       workflow = {
           "name": WORKFLOW_NAME,
           "version": WORKFLOW_VERSION,
       }
       
       # Get OpenAI client from project
       openai_client = project_client.get_openai_client()
   
       # Create a conversation
       conversation = openai_client.conversations.create()
       print(f"Created conversation (id: {conversation.id})")
   
       # Call the workflow with streaming
       print(f"\nCalling workflow: {WORKFLOW_NAME}...\n")
       stream = openai_client.responses.create(
           conversation=conversation.id,
           extra_body={"agent": {"name": workflow["name"], "type": "agent_reference"}},
           input="Plan a 2-night 3-day trip to Jeju Island",
           stream=True,
           metadata={"x-ms-debug-mode-enabled": "1"},
       )
   
       # Process streaming events
       for event in stream:
           if event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DONE:
               print("\t", event.text)
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_ADDED and event.item.type == "workflow_action":
               print(f"\n{'='*60}")
               print(f"Actor - '{event.item.action_id}':")
               print(f"{'='*60}")
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_DONE and event.item.type == "workflow_action":
               print(f"\n✓ Workflow Item '{event.item.action_id}' is '{event.item.status}'")
               print(f"  (previous item was: '{event.item.previous_action_id}')")
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DELTA:
               print(event.delta, end="", flush=True)
   
       # Clean up
       print("\n\n✅ Workflow completed!")
       openai_client.conversations.delete(conversation_id=conversation.id)
       print("Conversation deleted")
   ```

3. **Execute**

   ```bash
   pip install --pre azure-ai-projects>=2.0.0b1
   python invokeWorkflow.py
   ```

### ✅ Verification Checklist

- Verify all agents execute in order
- Confirm each agent's output is passed to the next agent
- Check final output is generated correctly

---

## Group Chat Workflow

A workflow where multiple agents collaborate through conversation to solve problems.

### Create Required Agents

#### 1. StudentAgent

```
Agent name: StudentAgent
Description: Student role that answers questions
Model: gpt-5.1

Instructions:
You are an agent that answers questions. When a question comes, always provide an answer.

Responsibilities:
1. Understand user's question and generate answer
2. Provide basic answer on first attempt
3. Receive feedback from TeacherAgent and improve answer
4. Revise answer until all requirements are met

Considerations when answering:
- Schedule (dates, times)
- Cost (budget, prices)
- Preferences (likes, style)
- Constraints (limitations, conditions)

If improvement is needed, reflect TeacherAgent's feedback to enhance answer.
```

#### 2. TeacherAgent

```
Agent name: TeacherAgent
Description: Teacher role that evaluates answers and requests improvements
Model: gpt-5.1

Instructions:
You are an agent that evaluates answers. If the answer considers various conditions such as schedule, cost, and preferences, respond with [COMPLETE]. If not, do not display COMPLETE and request revisions.

Evaluation criteria:
1. Schedule: Does it include specific dates, times, and duration?
2. Cost: Does it include budget, price, and cost information?
3. Preferences: Does it consider user's preferences or style?
4. Practicality: Is it an executable plan?
5. Completeness: Does it include all necessary information?

Response format:
When evaluation complete: "[COMPLETE] All conditions are met."
When improvement needed: "Please supplement the following: [specific feedback]"

Important: Use [COMPLETE] only when all criteria are satisfied.
```

### Create Group Chat Workflow

1. **Create New Workflow**

   - Click the **+ Create workflow** button in Workflows section.
   - Select **Group Chat Workflow**.
   
   ![Create Group Chat Workflow](../assets/05-09-group-chat-create.png)

2. **Add Agents**

   ```
   Participants:
   - StudentAgent
   - TeacherAgent
   
   Termination condition: When TeacherAgent responds with [COMPLETE]
   Max turns: 4 (prevent infinite loops)
   ```

   ![Add multiple agents](../assets/05-10-group-chat-agents.png)

3. **Configure Conversation Flow**

   ```
   User → StudentAgent → TeacherAgent → StudentAgent → ...
   ```

   - StudentAgent provides answer first
   - TeacherAgent evaluates and provides feedback
   - Repeat until [COMPLETE] is issued

5. **Save Workflow**

   - Click the **Save** button.
   
   ![Save Group Chat Workflow](../assets/05-09-group-chat-save.png)
      
   ![Group Chat Workflow saved](../assets/05-09-group-chat-saved.png)

### Test Workflow

1. **Preview Mode**

   - Click the **Preview** button.

   ![Group Chat Workflow Preview](../assets/05-09-group-chat-preview.png)

2. **Test Question**

   ```
   User: Plan a 2-night 3-day trip to Jeju Island.
   ```

3. **Observe Conversation Flow**

   ```
   Turn 1:
   StudentAgent: "Here's recommended Jeju itinerary. Day 1: Seongsan Sunrise Peak..."
   
   Turn 2:
   TeacherAgent: "Cost information is missing. Please include budget."
   
   Turn 3:
   StudentAgent: "Updated itinerary. Total budget 500,000 won... Day 1: Seongsan Sunrise Peak (admission 5,000 won)..."
   
   Turn 4:
   TeacherAgent: "Specific times are missing. Please add hourly schedule."
   
   Turn 5:
   StudentAgent: "Final itinerary. Day 1 9:00 AM: Seongsan Sunrise Peak..."
   
   Turn 6:
   TeacherAgent: "[COMPLETE] All conditions are met."
   ```

### 💡 Group Chat Tips

- **Role Assignment**: Give each agent a clear role
- **Termination Condition**: Set clear termination condition to prevent infinite loops
- **Max Turns**: Set maximum turn count as safety measure
- **Feedback Specificity**: More specific TeacherAgent feedback leads to better improvements

### ✅ Verification Checklist

- Verify conversation flows naturally between agents
- Verify TeacherAgent's evaluation criteria are appropriate
- Verify workflow terminates at [COMPLETE] condition

---

## Human-in-loop Workflow

A pattern that pauses the workflow at points requiring human approval or input.

### Concept

```
Agent 1 → [Human Approval] → Agent 2 → [Human Input] → Agent 3
```

Human-in-loop is useful in these situations:
- Approving important decisions
- Verifying sensitive information
- Budget approval
- Personal preference input

### Workflow Design

1. **Agent Configuration**

   Based on the previously created Sequential Workflow:

   ```
   TravelPlannerAgent → [User Approval] → LocalAgent → TravelSummaryAgent
   ```

2. **Add Human Approval Point**

   - Add **Human approval** step after TravelPlannerAgent.
   - User reviews draft travel plan and:
     - ✅ Approve → Proceed to LocalAgent
     - ❌ Reject → Return to TravelPlannerAgent for regeneration
     - 📝 Request modifications → Regenerate with feedback

3. **Workflow Configuration**

   ```
   Workflow name: Human-in-loop-Workflow
   Description: Travel planning workflow with user approval
   
   Steps:
   1. TravelPlannerAgent (generate draft)
   2. Human Approval (user review)
   3. LocalAgent (add local information when approved)
   4. TravelSummaryAgent (final summary)
   ```

4. **Approval Configuration**

   ```
   Approval message: "Please review the generated travel plan. Do you approve?"
   
   Options:
   - Approve: Proceed to next step
   - Reject: Return to TravelPlannerAgent
   - Modify: Accept modification request input
   
   Timeout: 24 hours (auto-reject if no response)
   ```

### Test Scenarios

1. **Approval Scenario**

   ```
   User: Hello
   TravelPlannerAgent: Generate draft travel itinerary
   [System]: Waiting for user approval...
   User: Approve
   LocalAgent: Add local information
   TravelSummaryAgent: Final summary
   ```

2. **Rejection and Regeneration Scenario**

   ```
   User: Plan a Jeju Island trip
   TravelPlannerAgent: Generate draft (hotel-focused)
   [System]: Waiting for user approval...
   User: Reject. Change to pension
   TravelPlannerAgent: Generate modified plan (pension-focused)
   [System]: Waiting for user approval...
   User: Approve
   LocalAgent: Add local information
   TravelSummaryAgent: Final summary
   ```

   ![Human-in-Loop Workflow Preview](../assets/05-10-human-in-loop-workflow-preview.png)

### 💡 Human-in-loop Best Practices

```
✅ Recommendations:
- Clearly mark approval points
- Prevent infinite waiting with timeout settings
- Provide context to users (previous conversation summary)
- Offer simple approval options (Yes/No/Modify)

❌ Things to Avoid:
- Too many approval points
- Unclear approval questions
- Long timeouts (degrades user experience)
- Non-reversible structure after approval
```

### ✅ Verification Checklist

- Verify workflow stops correctly at approval points
- Verify proper branching based on approval/rejection
- Verify timeout functions normally

---

## 📚 Additional Resources

- [Microsoft Foundry Workflows Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/workflow?view=foundry)
- [Microsoft Agent Framework Workflows Orchestrations Patterns](https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview)

## Next Steps

You've built complex workflows! Now let's learn how to evaluate agent and workflow performance:

➡️ **[06. Evaluations](./06-evaluations.md)**: Systematically evaluate the quality of agents and workflows.

---

[← Previous: Foundry IQ](./04-foundry-iq.md) | [Home](./README.md) | [Next: Evaluations →](./06-evaluations.md)
