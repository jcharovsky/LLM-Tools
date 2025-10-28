# guides-row-level-security

**Source URL:** https://neon.com/docs/guides/row-level-security

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/[Postgres RLS](/docs/guides/row-level-security)/RLS in Neon

# Row-Level Security with Neon

How Neon features use Postgres Row-Level Security

### What you will learn:

  * How the Data API uses Row-Level Security




### Related docs

  * [Data API](/docs/data-api/get-started)
  * [Simplify RLS with Drizzle](/docs/guides/rls-drizzle)
  * [Postgres RLS Tutorial](/postgresql/postgresql-administration/postgresql-row-level-security)



Row-Level Security (RLS) is a Postgres feature that controls access to individual rows in a table based on the current user. Here's a simple example that limits the `notes` a user can see by matching rows where their `user_id` matches the session's `auth.user_id()`:
    
    
    -- Enable RLS on a table
    ALTER TABLE notes ENABLE ROW LEVEL SECURITY;
    
    -- Create a policy that only allows users to access their own notes
    CREATE POLICY "users_can_only_access_own_notes" ON notes
      FOR ALL USING (auth.user_id() = user_id);

When using the Data API for client-side querying, RLS policies are required to secure your data.

## Data API with RLS

The **Data API** turns your database tables on a given branch into a REST API, and it requires RLS policies on all tables to ensure your data is secure.

### How it works

  * The Data API handles JWT validation and provides the `auth.user_id()` function.
  * Your RLS policies use `auth.user_id()` to control access.
  * All tables accessed via the Data API must have RLS enabled.


  * ### [Get startedLearn how to enable and use the Data API with RLS policies](/docs/data-api/get-started)
  * ### [Building a note-taking appSee a complete example of the Data API with RLS in action](/docs/data-api/demo)



## RLS with Drizzle ORM

Drizzle makes it simple to write RLS policies that work with the Data API. We highly recommend using its `crudPolicy` helper to simplify common RLS patterns.

  * ### [Simplify RLS with DrizzleLearn how to use Drizzle's crudPolicy function to simplify RLS policies](/docs/guides/rls-drizzle)



## Postgres RLS Tutorial

To learn the fundamentals of Row-Level Security in Postgres, including detailed concepts and examples, see the Postgres tutorial:

  * ### [Postgres RLS TutorialA complete guide to Postgres Row-Level Security concepts and implementation](/postgresql/postgresql-administration/postgresql-row-level-security)



[PreviousCustom Pages](/docs/neon-auth/customization/custom-pages)[NextSimplify RLS with Drizzle](/docs/guides/rls-drizzle)

Last updated on September 25, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Data API with RLS
  * RLS with Drizzle ORM
  * Postgres RLS Tutorial



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/guides/row-level-security.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/guides/row-level-security.md)

Neon Docs