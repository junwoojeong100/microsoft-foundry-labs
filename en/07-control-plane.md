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

Control Plane is Microsoft Foundry's central management center for integrated management and monitoring of all AI resources.

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

Ensures in production environment:
- 📊 **Visibility**: Understand status and performance of all resources
- 🛡️ **Security**: Early detection of vulnerabilities and threats
- 💰 **Cost Management**: Optimize resource usage and costs
- ⚖️ **Compliance**: Monitor compliance status
- 🚨 **Alerts**: Immediate response to issues

---

## Fleet Overview

Fleet Overview is a dashboard for viewing the status of all deployed AI resources at a glance.

[Content continues with detailed sections on Fleet Overview metrics, Register Agent functionality, Assets Management, Compliance and Security settings, Quota Management, Admin features...]

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

[← Previous: Evaluations](./06-evaluations.md) | [Main](./README.md)
