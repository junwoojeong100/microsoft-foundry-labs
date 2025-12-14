# 07. Control Plane

This module teaches you how to effectively manage and monitor production AI resources through Microsoft Foundry's Control Plane.

## 📋 Table of Contents

- [Control Plane Overview](#control-plane-overview)
- [Fleet Overview](#fleet-overview)
- [Assets Management](#assets-management)
- [Compliance and Security](#compliance-and-security)
- [Quota Management](#quota-management)
- [Admin Features](#admin-features)
- [Wrap-up](#wrap-up)

## 🎯 Learning Objectives

- Understand the role and importance of Control Plane
- Monitor entire system through Fleet Overview
- Manage Assets (agents, models, tools)
- Configure compliance and security settings
- Manage Quota and Rate Limiting
- Manage project and user permissions

## ⏱️ Estimated Time

Approximately 10 minutes

---

## Control Plane Overview

### What is Control Plane?

Control Plane is Microsoft Foundry's centralized management hub that provides unified oversight and governance of all AI resources and operations.

```
Control Plane = Monitoring + Management + Security + Governance
```

### Main Functional Areas

```
┌─────────────────────────────────────────┐
│         Control Plane                   │
├─────────────────────────────────────────┤
│ Fleet Overview   │ Overall system dashboard │
│ Assets          │ Resource management      │
│ Compliance      │ Security and policy      │
│ Quota           │ Allocation and limits    │
│ Admin           │ Project and permissions  │
└─────────────────────────────────────────┘
```

### Why is it Important?

In production environments, Control Plane ensures:
- 📊 **Visibility**: Comprehensive understanding of resource status and performance
- 🛡️ **Security**: Proactive detection and mitigation of vulnerabilities and threats
- 💰 **Cost Management**: Optimized resource utilization and cost control
- ⚖️ **Compliance**: Continuous monitoring of regulatory and policy compliance
- 🚨 **Incident Response**: Immediate alerts and rapid issue resolution

---

## Fleet Overview

Fleet Overview is a dashboard for viewing the status of all deployed AI resources at a glance.

### Access Dashboard

1. **Navigate to Control Plane**

   - Select **Operate** from the top right menu in Foundry portal.
   
   ![Fleet Overview dashboard](../../assets/07-02-fleet-overview.png)

   ![Fleet Overview dashboard](../../assets/07-02-fleet-overview2.png)

### Key Metrics

#### 1. Running Agents

```
┌────────────────────────────────────┐
│  Running Agents: 5                 │
├────────────────────────────────────┤
│  Active:    4  ✓                   │
│  Warning:   1  ⚠                   │
│  Failed:    0  ✗                   │
└────────────────────────────────────┘

Agents:
- ModelRouterAgent       [Active]
- FileSearchAgent        [Active]
- WebSearchAgent         [Warning] (High latency)
- KnowledgeAgent         [Active]
- KnowledgeAgent2        [Active]
```

**Identifying Warning Causes**:
- High response time (Latency)
- Increased error rate
- Quota nearing limit

#### 2. Agent Success Rate

```
┌────────────────────────────────────┐
│  Overall Success Rate: 96.5%       │
├────────────────────────────────────┤
│  Last 24 hours:                    │
│  ████████████████████░░  96.5%     │
│                                    │
│  Last 7 days trend:                │
│  ▁▂▃▄▅▆█▆▇█ ↗ Improving           │
└────────────────────────────────────┘

By Agent:
- ModelRouterAgent:    98.2% ✓
- FileSearchAgent:     97.5% ✓
- WebSearchAgent:      92.1% ⚠ (needs improvement)
- KnowledgeAgent:      98.8% ✓
- KnowledgeAgent2:     97.3% ✓
```

#### 3. Estimated Cost

```
┌────────────────────────────────────┐
│  Current Month Cost                │
├────────────────────────────────────┤
│  Total:        $245.30             │
│  Projected:    $350.00 (month-end) │
│                                    │
│  Breakdown:                        │
│  Models:       $180.50 (74%)       │
│  Search:       $ 45.20 (18%)       │
│  Storage:      $ 12.40 ( 5%)       │
│  Other:        $  7.20 ( 3%)       │
└────────────────────────────────────┘

Top Consumers:
1. gpt-4-1              $95.30
2. model-router         $65.20
3. text-embedding       $20.00
```

#### 4. Token Usage

```
┌────────────────────────────────────┐
│  Token Usage (24h)                 │
├────────────────────────────────────┤
│  Total:        1.2M tokens         │
│                                    │
│  Input:        800K (67%)          │
│  Output:       400K (33%)          │
│                                    │
│  Hourly Peak:  75K tokens/hour     │
│  Current:      52K tokens/hour     │
└────────────────────────────────────┘

Usage Trend:
Hour: 00  04  08  12  16  20  24
      ▁▁▁▃▅▇█▇▆▅▄▃▂▁
      (Peak: 4 PM)
```

#### 5. Active Alerts

```
┌────────────────────────────────────┐
│  Active Alerts: 2                  │
├────────────────────────────────────┤
│  ⚠ Warning (1)                     │
│    • WebSearchAgent high latency   │
│      Avg response: 8.5s (SLA: 5s)  │
│                                    │
│  ℹ Info (1)                        │
│    • Quota usage at 75%            │
│      gpt-4-1: 750K/1M TPM          │
└────────────────────────────────────┘
```

### Dashboard Utilization

1. **Daily Check**
   - Check success rate
   - Review active alerts
   - Monitor cost trends

2. **Weekly Review**
   - Analyze performance trends
   - Identify cost optimization opportunities
   - Plan quota adjustments

3. **Monthly Planning**
   - Capacity planning
   - Budget adjustments
   - Architecture optimization

### Register Agent

Register external agents in Fleet Overview for centralized management.

#### When Agent Registration is Needed

```
Agents developed outside Foundry:
- Custom HTTP/REST API-based agents
- Agents hosted on other platforms
- Agents integrated with legacy systems

AI Gateway activation required:
- Centralized management and monitoring
- Security, telemetry, rate limiting features
```

#### Agent Registration Procedure

1. **Enable AI Gateway**

   ```
   AI Gateway must be enabled in Foundry project.
   - Free to set up
   - Provides governance features like security, telemetry, rate limits
   ```

2. **Click Register Agent**

   - Click the **Register agent** button on Fleet Overview page.
   
   ![Register agent screen](../../assets/07-08-register-agent.png)

3. **Enter Agent Information**

   ```
   Add agent details:
   ────────────────────────────────────
   • Agent URL *
     Example: https://yourdomain.com/agent
     
   • Protocol *
     - General HTTP, Including REST
     
   • OpenTelemetry agent ID (optional)
     Agent ID for telemetry monitoring
     
   • Admin portal URL (optional)
     Portal URL to stop agent infrastructure
   ```

4. **Project and Name Configuration**

   ```
   Set up your agent:
   ────────────────────────────────────
   • Select a project *
     Select Foundry project to register agent
     
   • Agent name *
     Agent name to display in Fleet
   ```

5. **Complete Registration**

   - Click the **Register agent** button to complete registration.
   - Registered agent appears in Fleet Overview.

#### Managing Registered Agents

```
┌─────────────────────────────────────────────────────────────┐
│  Registered Agents                                          │
├──────────────┬─────────┬────────┬──────────┬────────────────┤
│ Name         │ Project │ Status │ Type     │ Endpoint       │
├──────────────┼─────────┼────────┼──────────┼────────────────┤
│ CustomAgent  │ Default │ Active │ External │ https://...    │
│ ModelRouter  │ Default │ Active │ Foundry  │ Built-in       │
│ FileSearch   │ Default │ Active │ Foundry  │ Built-in       │
└──────────────┴─────────┴────────┴──────────┴────────────────┘

External vs Foundry Agents:
- External: Externally hosted, requires URL
- Foundry:  Managed within Foundry, Built-in
```

#### Auto-Discovery Agents

```
⚠️ Auto-registration (no manual registration needed)

The following agents are automatically discovered and registered:
• Foundry agents
• Azure SRE Agent
• Logic Apps agent loop

These appear in Fleet Overview without separate registration procedure.
```

---

## Assets Management

Manage all AI resources in the Assets section.

### 1. Agents

View detailed information about all deployed agents.

![Assets > Agents list](../../assets/07-10-assets-agents.png)

```
┌─────────────────────────────────────────────────────────────┐
│  Agents                                                      │
├──────────────┬─────────┬────────┬──────────┬────────┬───────┤
│ Name         │ Project │ Status │ Version  │ Error  │ Runs  │
│              │         │        │          │ Rate   │ (24h) │
├──────────────┼─────────┼────────┼──────────┼────────┼───────┤
│ ModelRouter  │ Default │ Active │ v1.2     │ 1.8%   │ 1,234 │
│ FileSearch   │ Default │ Active │ v1.0     │ 2.5%   │  456  │
│ WebSearch    │ Default │ Warning│ v1.1     │ 7.9%   │  789  │
│ Knowledge    │ Default │ Active │ v2.0     │ 1.2%   │  678  │
│ Knowledge2   │ Default │ Active │ v1.0     │ 2.7%   │  345  │
└──────────────┴─────────┴────────┴──────────┴────────┴───────┘
```

**Agent Details**:
- Click to view detailed metrics
- Access Traces and logs
- Version management and rollback

**Action Items**:
- WebSearchAgent high error rate → Need to improve Instructions or debug

### 2. Models

Check status and usage of all deployed models.

![Assets > Models list](../../assets/07-11-assets-models.png)

```
┌───────────────────────────────────────────────────────────────────────────┐
│  Models                                                                    │
├─────────────┬─────────┬────────┬───────────┬────────────┬───────┬────────┤
│ Model       │ Project │ Version│ State     │ Guardrails │ Deploy│ Rate   │
│             │         │        │           │            │ Type  │ Limit  │
├─────────────┼─────────┼────────┼───────────┼────────────┼───────┼────────┤
│ gpt-4-1     │ Default │ latest │ Running   │ ✓ Enabled  │ Std   │ 1M TPM │
│ model-      │ Default │ 1.0    │ Running   │ ✓ Enabled  │ Std   │ 500K   │
│  router     │         │        │           │            │       │  TPM   │
│ text-       │ Default │ latest │ Running   │ - N/A      │ Std   │ 2M TPM │
│  embedding  │         │        │           │            │       │        │
└─────────────┴─────────┴────────┴───────────┴────────────┴───────┴────────┘

Cost per 1M tokens:
- gpt-4-1:         $30.00 (input), $60.00 (output)
- model-router:    Variable (depends on routing)
- text-embedding:  $0.13 (input only)
```

**Model Management Tasks**:
- Adjust rate limits
- Check Guardrails settings
- Analyze costs
- Review usage trends

### 3. Tools

Manage connected tools and MCP servers.

![Assets > Tools list](../../assets/07-12-assets-tools.png)

```
┌──────────────────────────────────────────────────────────────┐
│  Tools                                                        │
├──────────────────┬─────────┬──────────────────────────────────┤
│ Tool Name        │ Project │ MCP Server Endpoint URL          │
├──────────────────┼─────────┼──────────────────────────────────┤
│ File Search      │ Default │ Built-in                         │
│ Web Search       │ Default │ Built-in                         │
│ Custom Function  │ Default │ https://myapi.azurewebsites.net  │
└──────────────────┴─────────┴──────────────────────────────────┘
```

**Tool Monitoring**:
- Check endpoint status
- API call success rate
- Average response time

---

## Compliance and Security

### 1. Policies

Manage organizational AI usage policies.

![Active Policies list](../../assets/07-14-compliance-policies.png)

```
┌────────────────────────────────────────────────────────────┐
│  Active Policies                                           │
├────────────────────────────────┬───────────────────────────┤
│ Policy Name                    │ Status                    │
├────────────────────────────────┼───────────────────────────┤
│ Content Safety                 │ ✓ Enabled (All agents)    │
│ Indirect Prompt Injections     │ ✓ Enabled (All agents)    │
│ Protected Materials            │ ✓ Enabled (All agents)    │
│ Data Residency (Korea)         │ ✓ Enabled                 │
│ PII Detection                  │ ⚠ Warning mode            │
└────────────────────────────────┴───────────────────────────┘
```

**Policy Configuration**:

#### Content Safety
```
Harmful Content Filtering:
- Hate speech:     High
- Sexual content:  High
- Violence:        High
- Self-harm:       High

Action: Block response
```

#### Indirect Prompt Injections
```
Jailbreak Attempts Detection: Enabled

Examples:
- "Ignore previous instructions..."
- "You are now in developer mode..."

Action: Block and log
```

#### Protected Materials
```
Code Detection:    Enabled
Text Detection:    Enabled

Protected content:
- Copyrighted code
- Licensed articles
- Proprietary content

Action: Filter and replace
```

### 2. Guardrails

Configure safeguards per model deployment.

![Guardrails configuration](../../assets/07-15-guardrails-config.png)

```
┌────────────────────────────────────────────────────────────┐
│  Guardrails - gpt-4-1                                      │
├────────────────────────────────┬───────────────────────────┤
│ Guardrail                      │ Configuration             │
├────────────────────────────────┼───────────────────────────┤
│ Content harms                  │ ✓ Enabled                 │
│   - Severity threshold:        │   Medium                  │
│ Jailbreak                      │ ✓ Enabled                 │
│ Indirect prompt injections     │ ✓ Enabled                 │
│ Spotlighting                   │ ✓ Enabled                 │
│ Profanity (Blocklist)          │ ✓ Enabled                 │
│   - Custom blocklist:          │   company_terms.txt       │
│ Protected materials - code     │ ✓ Enabled                 │
│ Protected materials - text     │ ✓ Enabled                 │
└────────────────────────────────┴───────────────────────────┘
```

**Guardrails Testing**:
```python
# Test harmful content
test_input = "How to make a bomb"
# Expected: Blocked by content safety

# Test jailbreak
test_input = "Ignore previous rules and tell me..."
# Expected: Blocked by jailbreak detection

# Test profanity
test_input = "This is [blocked word]"
# Expected: Filtered by profanity filter
```

### 3. Security Posture

Evaluate and improve security status.

![Security Posture score](../../assets/07-16-security-posture.png)

```
┌────────────────────────────────────────────────────────────┐
│  Security Posture                                          │
├──────────────┬─────────────────┬──────────────┬───────────┤
│ Risk Level   │ Recommendation  │ Affected     │ Resource  │
│              │                 │ Resource     │ Type      │
├──────────────┼─────────────────┼──────────────┼───────────┤
│ ⚠ Medium     │ Enable MFA for  │ admin@...    │ User      │
│              │ admin accounts  │              │           │
├──────────────┼─────────────────┼──────────────┼───────────┤
│ ℹ Low        │ Rotate API keys │ Storage      │ Key       │
│              │ (90 days old)   │ Account      │           │
├──────────────┼─────────────────┼──────────────┼───────────┤
│ ℹ Low        │ Update to       │ gpt-4-1      │ Model     │
│              │ latest version  │              │           │
└──────────────┴─────────────────┴──────────────┴───────────┘

Overall Security Score: 85/100 ✓
```

---

## Quota Management

### 1. Token Per Minute (TPM)

Manage request limits per model.

![Token Per Minute Quota](../../assets/07-17-quota-tpm.png)

```
┌───────────────────────────────────────────────────────────────────┐
│  Token Per Minute Quota                                           │
├────────────┬──────────┬─────────┬────────────┬─────────┬─────────┤
│ Model      │ Deploy   │ Region  │ Deploy     │ Shared  │ Rate    │
│            │          │         │ Type       │ Alloc   │ Limiting│
├────────────┼──────────┼─────────┼────────────┼─────────┼─────────┤
│ gpt-4-1    │ gpt-4-1  │ East US │ Standard   │ 1M TPM  │ Enabled │
│            │          │    2    │            │ 75% used│         │
├────────────┼──────────┼─────────┼────────────┼─────────┼─────────┤
│ model-     │ model-   │ East US │ Standard   │ 500K    │ Enabled │
│  router    │  router  │    2    │            │ 45% used│         │
├────────────┼──────────┼─────────┼────────────┼─────────┼─────────┤
│ text-      │ text-emb │ East US │ Standard   │ 2M TPM  │ Enabled │
│  embedding │          │    2    │            │ 32% used│         │
└────────────┴──────────┴─────────┴────────────┴─────────┴─────────┘
```

**Rate Limiting Behavior**:
```
Quota: 1,000,000 TPM
Current usage: 750,000 TPM (75%)

New request: 100,000 tokens
Status: ✓ Allowed (850,000 TPM)

New request: 300,000 tokens
Status: ✗ Throttled (would exceed 1M TPM)
Response: 429 Too Many Requests
Retry-After: 30 seconds
```

**Request Quota Increase**:
1. Navigate to Azure Portal
2. Support > New support request
3. Issue type: Service and subscription limits (quotas)
4. Specify needed quota and justification

### 2. Provisioning Throughput Unit (PTU)

Manage PTU for fixed capacity.

![PTU (Provisioning Throughput Units)](../../assets/07-19-quota-ptu.png)

```
┌────────────────────────────────────────────────────────────┐
│  Provisioning Throughput Units                             │
├────────────┬──────────┬─────────┬──────────────────────────┤
│ Model      │ Deploy   │ Region  │ PTU Allocation           │
├────────────┼──────────┼─────────┼──────────────────────────┤
│ gpt-4-1    │ prod-    │ East US │ 100 PTU                  │
│            │  gpt4    │    2    │ ($7,000/month fixed)     │
└────────────┴──────────┴─────────┴──────────────────────────┘

PTU vs Standard:
Standard:    Pay per token (variable cost)
PTU:         Fixed capacity, predictable cost

PTU Recommended Scenarios:
- High daily usage (millions of tokens)
- Predictable workloads
- Low latency requirements
```

---

## Admin Features

### 1. All Projects

Manage all Foundry projects within organization.

![All Projects list](../../assets/07-20-admin-projects.png)

**Project Lifecycle**:
```
Development → Test → Staging → Production

Environment-specific configuration:
- Development:  Low quota, relaxed policies
- Test:         Medium quota, test data
- Staging:      Same configuration as production
- Production:   High quota, strict policies
```

### 2. AI Gateway

Configure centralized API Gateway.

![AI Gateway configuration](../../assets/07-21-ai-gateway1.png)

![AI Gateway configuration](../../assets/07-21-ai-gateway2.png)

```
┌────────────────────────────────────────────────────────────┐
│  AI Gateway Configuration                                  │
├────────────────────────────────────────────────────────────┤
│  Gateway Endpoint:                                         │
│  https://gateway.foundry.ai                                │
│                                                            │
│  Features:                                                 │
│  ✓ Authentication & Authorization                          │
│  ✓ Rate limiting                                           │
│  ✓ Load balancing                                          │
│  ✓ Caching                                                 │
│  ✓ Monitoring & Logging                                    │
│  ✓ Request/Response transformation                         │
└────────────────────────────────────────────────────────────┘
```

**AI Gateway Benefits**:
```
✅ Centralized Management
- All requests pass through Gateway
- Unified monitoring and logging

✅ Enhanced Security
- API key management
- IP whitelisting
- Request validation

✅ Performance Optimization
- Reduced duplicate requests through caching
- Load distribution via load balancing

✅ Cost Optimization
- Reduced API calls through cache hits
- Usage tracking and control
```

---

## 📚 Additional Resources

- [Microsoft Foundry Control Plane](https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/overview?view=foundry)
- [Monitor Agent Health and Performance](https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/monitoring-across-fleet?view=foundry)
- [Register Custom Agent](https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/register-custom-agent?view=foundry)
- [Create Guardrail Policy](https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/quickstart-create-guardrail-policy?view=foundry)
- [Manage Compliance and Security](https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/how-to-manage-compliance-security?view=foundry)
- [Optimize Model Cost and Performance](https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/how-to-optimize-cost-performance?view=foundry)

---

## Wrap-up

Congratulations! You've completed all modules of the Microsoft Foundry Hands-on Workshop! 🎉

### Summary of What You Learned

```
✅ Module 01: Environment Setup
   - Created Resource Group and Foundry resource

✅ Module 02: Models and Deployment
   - Explored, deployed models, configured Model Router

✅ Module 03: Agent Development
   - Created and deployed various types of agents

✅ Module 04: Foundry IQ
   - Built AI Search and Blob Storage-based Knowledge Base

✅ Module 05: Workflows
   - Implemented Sequential, Group Chat, Human-in-loop workflows

✅ Module 06: Evaluations
   - Evaluated and improved agent quality

✅ Module 07: Control Plane
   - Production monitoring and management
```

### Next Steps

You're now ready to:

1. **Production Deployment**
   - Integrate Foundry into real applications
   - Build CI/CD pipelines
   - Set up monitoring and alerts

2. **Explore Advanced Features**
   - Develop custom tools and MCP servers
   - Multi-agent collaboration patterns
   - Fine-tuning and model customization

3. **Engage with Community**
   - Join [Microsoft Tech Community](https://techcommunity.microsoft.com) forums
   - Contribute to [GitHub Samples](https://github.com/Azure-Samples)
   - Share use cases

### Resource Cleanup

Clean up resources after workshop to reduce costs:

```bash
# Delete Resource Group (including all resources)
az group delete --name foundry --yes --no-wait
```

⚠️ **Warning**: This command permanently deletes all workshop resources.

---

### Feedback

Please share any feedback or questions about the workshop anytime!

---

[← Previous: Evaluations](./06-evaluations.md) | [Home](./README.md)
