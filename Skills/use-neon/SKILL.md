---
name: use-neon
description: |
  Expert guidance on Neon, a serverless Postgres platform designed for developers seeking scalable, flexible, and cloud-native database solutions. Use this skill when users ask about Neon’s Postgres-compatible serverless infrastructure, branching workflows, logical replication, Neon CLI, API references, data import and migration tools, developer experience, or production readiness best practices. This skill helps with Neon’s core features such as multi-branch development workflows, Neon data API, connection management, and integrations with frameworks, ORMs, and AI tools.

---

# Instructions for Claude

This skill helps provide expert assistance using the comprehensive Neon documentation. All supporting content is located in the `resources/` subdirectory.

1. **Search for Relevant Information:**
   - When responding to a user query, first identify key terms like "Neon branching", "Neon CLI", "Neon API", "serverless Postgres", "logical replication", "data migration", or "Neon integrations".
   - Search through the markdown files in `resources/` using those terms to find the most relevant documents.

2. **Use the Most Authoritative Files:**
   - For API-related questions, prioritize `resources/docs-reference-api-reference.md` and `resources/docs-reference-neon-cli.md`.
   - For getting started and workflow queries, consult `resources/docs-get-started-connect-neon.md` and `resources/docs-get-started-workflow-primer.md`.
   - For branching and replication, see `resources/docs-guides-branching-intro.md` and `resources/docs-guides-logical-replication-neon-to-neon.md`.
   - For migration and import help, use `resources/docs-import-migrate-intro.md` and related migration files.

3. **Table of Contents:**
   - For any resource file over 100 lines, note that it includes a table of contents at the top to help navigate sections. Use this to quickly find the relevant subsection.

4. **Responding Best Practices:**
   - Provide clear, concise explanations focused on Neon’s features and workflows.
   - When multiple ways exist, recommend the default or most common approach unless the user specifies otherwise.
   - Avoid generic or vague answers; give concrete steps or references to Neon documentation sections.
   - Use consistent terminology: always use "Neon API endpoint", "Neon branching", "Neon CLI command", etc.
   - If the user asks about deprecated or old approaches, mention the "Old patterns" section if available.

5. **Avoid Time-Sensitive Details:**
   - Do not include specific dates or version numbers.
   - Use general terms like "current Neon best practices" or "latest Neon features".

6. **Examples of files to use:**
   - `resources/docs-get-started-connect-neon.md` for connection setup
   - `resources/docs-reference-api-reference.md` for API endpoint details
   - `resources/docs-guides-branching-intro.md` for branching workflows
   - `resources/docs-import-import-intro.md` for data import basics

By following these instructions, Claude will provide accurate and actionable help about Neon’s serverless Postgres platform using the detailed markdown resources.

---

# Examples

**Example 1:**
_User:_ "How do I create a development branch in Neon?"
_Claude:_ "Neon supports multi-branch workflows allowing you to create isolated development branches of your Postgres database. Refer to `resources/docs-guides-branching-intro.md`, which explains how to create and manage branches through the Neon dashboard or CLI. Typically, you create a branch from your main database to develop features without impacting production. You can then merge or delete branches as needed."

**Example 2:**
_User:_ "What API endpoints does Neon provide for data querying?"
_Claude:_ "Neon offers a Data API providing REST endpoints to query your Postgres data serverlessly. See `resources/docs-reference-api-reference.md` for detailed descriptions of the available endpoints, authentication methods, and usage examples. This API enables you to run SQL queries, manage connections, and handle results without maintaining persistent connections."

**Example 3:**
_User:_ "How can I migrate my existing Postgres database to Neon?"
_Claude:_ "Neon offers several migration paths detailed in `resources/docs-import-migrate-intro.md` and related migration guides like `docs-import-migrate-from-postgres.md`. You can migrate data using pg_dump/pg_restore, logical replication, or specialized tools like pgcopydb. The documentation explains prerequisites, step-by-step instructions, and best practices to ensure a smooth migration to Neon’s serverless Postgres environment."
