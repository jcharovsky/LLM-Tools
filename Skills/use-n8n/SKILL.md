---
name: use-n8n
description: |
  Comprehensive automation and workflow orchestration documentation for n8n. Use when users ask about building, customizing, and managing n8n workflows, nodes, credentials, API references, hosting setups, security configurations, user management, integrations, data handling, and advanced AI workflow capabilities within the n8n ecosystem. Trigger terms include n8n workflows, nodes, credentials, API endpoints, hosting, security, user management, integrations, advanced AI, and workflow executions.
---

# Instructions for Using the n8n Documentation Skill

This skill enables Claude to assist users with detailed questions about using n8n, the open source workflow automation platform. To provide accurate and helpful answers, Claude should follow these guidelines:

1. **Search and Read from Resources/**
   - All supporting documentation is located in the `resources/` directory.
   - When a user asks a question, first identify relevant keywords such as "workflow", "node", "API", "credential", "hosting", "security", "user management", "integration", or "advanced AI".
   - Search for these keywords in filenames and content of markdown files within `resources/`.
   - Open and read the most relevant markdown files to extract precise information.

2. **Use Table of Contents for Large Files**
   - Some resource files exceed 100 lines.
   - These files include a table of contents at the top to help navigate sections.
   - Use the TOC to quickly locate the exact subsection relevant to the user's question.

3. **Answering Best Practices**
   - Provide clear, concise, and actionable answers referencing specific n8n features or concepts.
   - Use consistent terminology such as "workflow", "node", "API endpoint", "credential", "execution", and "integration".
   - Avoid generic or vague responses; prefer concrete examples or step-by-step instructions when possible.
   - If multiple approaches exist, recommend the default or most common best practice.
   - Do not include time-sensitive details like version numbers or dates; if needed, mention deprecated approaches under "Old patterns" sections.

4. **Scope and Focus**
   - Focus solely on n8n capabilities as documented.
   - Avoid referencing unrelated automation platforms or generic workflow concepts outside n8n context.
   - When advanced AI workflows or integrations are involved, consult the `advanced-ai-*.md` files.

5. **File Reference Guidelines**
   - Always refer to files directly under the `resources/` folder.
   - Do not chain references through other resource files.
   - Use forward slashes for paths, for example, `resources/api-api-reference.md`.

6. **Common Topics Covered**
   - Workflow creation and execution (`workflows-create.md`, `workflows-executions.md`)
   - Node types and usage (`integrations-builtin-node-types.md`, `workflows-components-nodes.md`)
   - Credential management (`credentials.md`)
   - API usage and authentication (`api-api-reference.md`, `api-authentication.md`)
   - Hosting, scaling, and security (`hosting.md`, `hosting-configuration-*.md`, `hosting-securing-*.md`)
   - User management and access control (`user-management.md`, `user-management-rbac.md`, `user-management-saml.md`)
   - Advanced AI workflows and evaluations (`advanced-ai.md`, `advanced-ai-examples-*.md`)
   - Data handling and transformations (`data-data-*.md`)
   - Community nodes and integrations (`integrations-community-nodes-*.md`)

By following these instructions, Claude can efficiently use the extensive n8n documentation to assist users with a wide range of automation, integration, and workflow questions.

# Examples

**Example 1:**
User: "How do I create a new workflow in n8n and add a trigger node?"
Claude: "To create a new workflow in n8n, refer to `resources/workflows-create.md` which explains the step-by-step process including adding nodes. For adding a trigger node, check the section on node types in `resources/integrations-builtin-node-types.md` to select the appropriate trigger, such as Webhook or Cron."

**Example 2:**
User: "Can you explain how to authenticate API requests to the n8n API?"
Claude: "Yes, the `resources/api-authentication.md` file covers authentication methods for the n8n API, including API key and OAuth setups. Also, `resources/api-api-reference.md` provides details on the available endpoints and how to structure your requests."

**Example 3:**
User: "What are best practices for securing an n8n self-hosted instance?"
Claude: "Refer to `resources/hosting-securing-overview.md` for an overview of security practices. Specific guides like `resources/hosting-securing-set-up-ssl.md` and `resources/hosting-securing-hardening-task-runners.md` provide detailed instructions on setting up SSL and hardening your environment to secure your self-hosted n8n instance."
