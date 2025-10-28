# getting-started-quickstarts-import-from-lovable

**Source URL:** https://docs.replit.com/getting-started/quickstarts/import-from-lovable

---

Skip to main content

[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

  * [Docs](/getting-started/intro-replit)
  * [Tutorials](/tutorials/vibe-coding-101)
  * [Trust & Billing](/category/billing)
  * [Teams and Enterprise](/category/teams)
  * [Changelog](/updates/2025/10/24/changelog)



##### Getting Started

  * [Introduction](/getting-started/intro-replit)
  * Quickstarts

    * [Remix](/getting-started/quickstarts/remix-an-app)
    * [Create with AI](/getting-started/quickstarts/ask-ai)
    * [Build from Scratch](/getting-started/quickstarts/from-scratch)
    * Import

      * [Import from GitHub](/getting-started/quickstarts/import-from-github)
      * [Import from Figma](/getting-started/quickstarts/import-from-figma)
      * [Import from Bolt](/getting-started/quickstarts/import-from-bolt)
      * [Import from Lovable](/getting-started/quickstarts/import-from-lovable)
      * [Import from Vercel](/getting-started/quickstarts/import-from-vercel)
  * [Replit Core](/replit-core/replit-core)



##### Replit Apps

  * [Overview](/category/replit-apps)
  * [Import](/replit-app/import-to-replit)
  * [Collaboration](/replit-app/collaborate)
  * [Visibility](/replit-app/visibility)
  * [Advanced Configuration](/replit-app/configuration)
  * [App Embed](/replit-app/app-embed)
  * [Developer Frameworks](/replit-workspace/templates)



##### Replit AI

  * [Overview](/category/replit-ai)
  * [Agent](/replitai/agent)
  * Autonomy & validation

  * Features

  * Integrations

  * Visual edits




##### Replit Workspace

  * [Overview](/category/replit-workspace)
  * Features

  * [Themes](/replit-workspace/replit-themes)



##### Publishing your App

  * [Overview](/category/replit-deployments)
  * Deployment Types

  * Advanced Configuration




##### Storage and Databases

  * [Overview](/category/storage-and-databases)
  * [Database](/cloud-services/storage-and-databases/sql-database)
  * [Production Databases](/cloud-services/storage-and-databases/production-databases)
  * App Storage

  * [Key-Value Store](/cloud-services/storage-and-databases/replit-database)



##### Platforms

  * [Mobile App](/platforms/mobile-app)
  * [Desktop App](/platforms/desktop-app)



##### Extensions

  * [Overview](/extensions/extensions)
  * Basics

  * Development

  * Examples

  * API Reference

  * [Overview](/extensions/publish)
  * [Overview](/extensions/faq)



##### Additional Resources

  * [CLUI](/additional-resources/clui-graphical-cli)
  * [Cheat Sheet](/additional-resources/cheat-sheet)
  * [FAQ](/faq)



  * [Start Building](https://replit.com/signup)
  * 


[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

Search...

Navigation

Import

Import from Lovable

## 

​

Import your Lovable project

⏰ _Estimated time: four minutes_ You can import your Lovable projects into Replit by exporting them to GitHub first, then importing them as Replit Agent Apps. This quickstart covers the step-by-step process to migrate your Lovable projects to Replit. For comprehensive import options including other platforms like GitHub, Figma, and Bolt, see the [Import feature documentation](/replit-app/import-to-replit).

![Preview of Lovable project import in Replit](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/lovable.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=259c9b27b6acf2b6dcf3f86c26ffebe6)

## 

​

Export and import process

  1. **Export your Lovable project to GitHub** from your Lovable workspace.
  2. Navigate to [<https://replit.com/import>](https://replit.com/import).
  3. Select **Lovable** from the available import sources.
  4. **Connect your GitHub account to Replit** to authorize repository access.
  5. **Select your new Lovable project repo** for import from the available repositories.
  6. Select **Import** to start the migration process.



## 

​

What gets imported

During the import process, Replit migrates your  project with Agent assistance:

  * **Code** : All application code and logic from your  project
  * **Design and styles** : UI components, styling, and visual design elements
  * **Assets** : Images, icons, and other static resources
  * **Backend functionality** : If your  project includes backend functionality, it is imported into the Replit environment.
  * **Database schema** : Database structure and table definitions are imported into a Neon Postgres database, which is integrated directly into the Replit environment.



### 

​

What’s not included

  * **Supabase database** : Database content and data are not migrated
  * **Secrets** : Environment variables and API keys must be added separately

You can ask Agent to help build out functionality, add secrets, and recreate databases in your new app.

## 

​

Configure and run your app

During the import process, . If your app doesn’t run as expected, Replit offers the following workspace tools to help you resolve the issues:

  * **[Agent](/replitai/agent)** : Use AI to add new features and refine your imported project
  * **[Assistant](/replitai/assistant)** : Get help with code questions and debugging
  * **[Secrets](/replit-workspace/workspace-features/secrets)** : Add your API keys and environment variables
  * **[Workflows](/replit-workspace/workflows)** : Configure the Run button to your preferred command



## 

​

Continue your journey

Now that you’ve imported your  , learn more about what you can do with your Replit App:

  * [Replit Agent](/replitai/agent): Get AI assistance with code review, testing, and feature implementation
  * [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public): Share your app as a Template for others to remix
  * [Replit Deployments](/category/replit-deployments): Publish your app to the cloud with a few clicks
  * [Database setup](/cloud-services/storage-and-databases/sql-database): Let Agent help you configure and optimize your database
  * [Collaborate](/replit-app/collaborate): Work with others on your imported projects



Was this page helpful?

YesNo

[Previous](/getting-started/quickstarts/import-from-bolt)[Import from VercelLearn how to import Vercel projects into Replit by linking your GitHub repository and letting Agent handle the setup.Next](/getting-started/quickstarts/import-from-vercel)

⌘I

On this page

  * Import your Lovable project
  * Export and import process
  * What gets imported
  * What’s not included
  * Configure and run your app
  * Continue your journey