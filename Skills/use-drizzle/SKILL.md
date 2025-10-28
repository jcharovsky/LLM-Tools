---
name: use-drizzle
description: |
  Expert guidance on Drizzle ORM usage and its extensive documentation. Use this skill when users ask about Drizzle ORM features such as database connection setups (MySQL, PostgreSQL, SQLite, Cloudflare D1, and more), query building, migrations, caching, batch APIs, schema declaration, relations, transactions, seed functions, Drizzle Kit tools, and Drizzle Studio. Trigger terms include Drizzle ORM, Drizzle Kit, Drizzle Studio, database connectors, SQL schema, migrations, query utils, and ORM caching.
---

# Instructions for Using the Drizzle Skill

1. **Start with a clear understanding of the user question:** Identify if the user needs help with Drizzle ORM database connections, query building, migrations, schema design, or Drizzle Kit tools.

2. **Search the `resources/` directory:** All supporting documentation files are in the `resources/` folder. Look for filenames starting with `docs-` as they cover specific Drizzle ORM topics.

3. **Prioritize reading these key files for common requests:**
   - `resources/docs-overview.md` for general understanding
   - `resources/docs-get-started.md` and related `docs-get-started-*.md` files for connection setup
   - `resources/docs-drizzle-kit-overview.md` and `docs-drizzle-kit-*.md` for migration and tooling
   - `resources/docs-data-querying.md`, `docs-update.md`, `docs-insert.md`, `docs-delete.md` for query operations
   - `resources/docs-schemas.md` and `docs-sql-schema-declaration.md` for schema design
   - `resources/docs-cache.md` and `docs-batch-api.md` for advanced features
   - `resources/drizzle-studio-overview.md` for Drizzle Studio

4. **If the file is longer than 100 lines, first check the table of contents at its top** to navigate to relevant sections quickly.

5. **When multiple approaches exist in the docs, recommend the default or most common practice** rather than listing all alternatives.

6. **Use consistent terminology:** Always refer to "database connectors," "migrations," "query builders," and "ORM features" clearly to avoid confusion.

7. **Avoid including outdated or deprecated methods unless specifically asked; reference the "Old patterns" sections in the docs only if user requests**.

8. **When answering, quote or paraphrase relevant documentation sections for accuracy, and provide examples if available.**

9. **For specialized connectors (e.g., AWS Data API, Cloudflare D1, Bun SQL), refer to the corresponding `docs-connect-*` markdown files.**

10. **If user asks about Drizzle Studio or Drizzle Kit tooling, refer to `drizzle-studio-overview.md` and related `docs-drizzle-kit-*.md` files respectively.**

# Examples

**User:** "How do I set up a PostgreSQL connection using Drizzle ORM?"

**Claude:** "To set up a PostgreSQL connection with Drizzle ORM, you can follow the steps outlined in `resources/docs-get-started-postgresql.md` and `resources/docs-connect-vercel-postgres.md`. Typically, you install the necessary packages, configure your connection parameters in your Drizzle config file (`docs-drizzle-config-file.md`), and then initialize the client. Would you like a code example?"

---

**User:** "Can you explain how to handle migrations with Drizzle Kit?"

**Claude:** "Certainly! Drizzle Kit migrations are covered extensively in `resources/docs-drizzle-kit-overview.md` and `resources/docs-drizzle-kit-migrate.md`. The typical workflow involves generating migration files, applying them to your database using Drizzle Kit CLI commands like `migrate` and `push`. It's recommended to use the Drizzle Kit tooling to keep your schema and database in sync."

---

**User:** "What features does Drizzle Studio provide?"

**Claude:** "Drizzle Studio is an integrated development environment for working with Drizzle ORM. You can find an overview in `resources/drizzle-studio-overview.md`. It offers GUI tools for managing your database schema, running queries, and visualizing relations. It's designed to streamline your ORM development experience."
