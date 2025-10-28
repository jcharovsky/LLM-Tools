---
name: use-replit
description: |
  Comprehensive expertise with Replit's cloud development platform and its documentation. Use this skill when users ask about Replit workspace features, coding environments, Replit AI capabilities, app deployment workflows, storage and database services, team collaboration, billing, and platform integrations. Trigger terms include Replit workspace, Replit AI agent, Replit apps, deployments, Replit database, SQL database, version control, Replit themes, Replit CLI, and cloud services on Replit.
---

# Instructions for Claude

This skill enables detailed and accurate assistance using the official Replit documentation located in the `resources/` folder.

## How to Use the Documentation

- When a user asks about any Replit feature, first identify the core topic (e.g., workspace, AI, deployments).
- Search inside the `resources/` directory for markdown files relevant to the topic. Filenames often include category names like `category-replit-ai.md`, `category-replit-workspace.md`, or specific feature guides.
- For broad topics, start with category files (e.g., `category-replit-ai.md` for AI features).
- For detailed questions about storage or databases, consult `category-storage-and-databases.md` and related files like `cloud-services-storage-and-databases-replit-database.md`.
- Use the `getting-started-quickstarts-*.md` files for user onboarding and basic workflows.
- For collaborative features and teams, see `category-teams.md` and `replit-app-collaborate.md`.
- Billing topics are covered in `category-billing.md`.
- For platform-specific details, consult `platforms-desktop-app.md` or `platforms-mobile-app.md`.

## Answering User Questions

- Provide clear, concise responses referencing specific Replit features or workflows.
- When multiple approaches exist, recommend the most common or official best practice as default.
- Avoid vague or generic answers; directly cite relevant documentation sections.
- If a document is long (over 100 lines), use its table of contents to navigate and extract relevant info.
- Use consistent terminology: always say "Replit workspace," "Replit AI agent," "Replit app deployment," "API endpoint," etc.
- Avoid time-sensitive or dated info; prefer evergreen best practices.
- If user questions involve deprecated methods, direct them to "Old patterns" sections if present.

## File Reference Guidelines

- All referenced markdown files are located directly in the `resources/` folder.
- Do not reference files from within other resource files; keep links one level deep.
- Examples of key resource files:
  - `resources/category-replit-ai.md`
  - `resources/category-replit-workspace.md`
  - `resources/category-storage-and-databases.md`
  - `resources/category-replit-apps.md`
  - `resources/replit-app-collaborate.md`
  - `resources/getting-started-quickstarts-from-scratch.md`

## Summary

This skill focuses solely on Replit platform features and documentation. Use it whenever users inquire about coding environments, AI tools, deployment, storage solutions, collaboration, billing, or workspace management within Replit.

# Examples

**User:** How do I deploy a web app on Replit?

**Claude:** To deploy a web app on Replit, you can use the deployment features described in `resources/category-replit-deployments.md`. Typically, you start by creating a Replit app, then configure the deployment settings via the Replit dashboard or CLI. The docs also cover continuous deployment options and environment variables.

---

**User:** What storage options are available on Replit?

**Claude:** Replit offers multiple storage solutions including the Replit Database and SQL databases. For details, see `resources/category-storage-and-databases.md` and `resources/cloud-services-storage-and-databases-replit-database.md`. The Replit Database is a simple key-value store ideal for small data, while SQL databases support more complex queries and relational data.

---

**User:** Can you explain how Replit AI agent works?

**Claude:** The Replit AI agent functionality is documented in `resources/category-replit-ai.md` and `resources/replitai-agent.md`. It provides AI-powered code completions, suggestions, and chatbot assistance integrated directly into the Replit workspace. You can enable and configure the AI agent through workspace settings and use it to accelerate coding tasks.
