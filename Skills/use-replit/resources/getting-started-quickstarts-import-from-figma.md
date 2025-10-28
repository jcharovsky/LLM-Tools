# getting-started-quickstarts-import-from-figma

**Source URL:** https://docs.replit.com/getting-started/quickstarts/import-from-figma

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

Import from Figma

## 

​

Import your Figma design

⏰ _Estimated time: three minutes_ You can import your Figma designs and turn them into functional React apps on Replit.

This quickstart covers how to convert your designs into working applications using AI-powered code generation. For comprehensive import options including other platforms like GitHub, Bolt, and Lovable, see the [Import feature documentation](/replit-app/import-to-replit).

![Preview of Figma design import in Replit](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=38babb9582d24c957cf796a2835998ff)

## 

​

Import your design

  1. Navigate to [<https://replit.com/import>](https://replit.com/import).



![Replit import interface showing available sources](https://mintcdn.com/replit/Uf4zlH5lH2O96Q1m/images/workspace/import/importer.png?fit=max&auto=format&n=Uf4zlH5lH2O96Q1m&q=85&s=8876c5571e7129426779f3e154bdc702)

  2. Select **Figma** from the available import sources.
  3. **Connect your Figma account** to authorize access to your designs.



![Figma authentication process in Replit](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=b26e735e1ebc34e302383526641df7b4)

  4. **In Figma, select the frame** you want to build in Replit.



![Selecting a frame in Figma for import](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=1c46a57f9ac479f4e0dec81a1d6d27d7)

  5. **Copy the frame URL** from Figma and paste it into the Replit import interface.
  6. Select **Import** to start the conversion process.



![Figma import progress in Replit](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d27e3e9f76e7381f431826ee8d90bdb4)

## 

​

What gets imported

During the import process, Replit converts your Figma design into a functional React application:

  * **Theme & components**: Design system elements, colors, typography, and reusable components
  * **Assets & icons**: Images, icons, and other visual assets from your design
  * **App scaffolding** : Basic application structure and layout framework



## 

​

Figma design guidelines

To copy the Figma Design frame URL:

  1. Right-click the frame
  2. Select **Copy/Paste as**
  3. Select **Copy link to selection**

For optimal conversion results, ensure your Figma design is well-structured with clear component hierarchies complete with auto layout constraints. Follow [these guidelines](https://support.animaapp.com/en/articles/6431384-create-responsive-designs-in-figma) for responsive designs in Figma. You can also ask Agent to help you make your design responsive.

### 

​

Tips

  * Use auto layout constraints to ensure your design is responsive.
  * Name your layers something short and meaningful.
  * Convert any groups to frames
  * Mark image assets for export



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

Interact in Agent chat (beta)

After importing, you can paste Figma links into Agent chat to explore layers, extract tokens, and request code changes. These Agent chat features require a Figma **Dev** or **Full** seat; the initial import does not. See the guide: [Figma MCP Integration](/replitai/mcp/figma).

## 

​

Continue your journey

Now that you’ve imported your  , learn more about what you can do with your Replit App:

  * [Replit Agent](/replitai/agent): Get AI assistance with code review, testing, and feature implementation
  * [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public): Share your app as a Template for others to remix
  * [Replit Deployments](/category/replit-deployments): Publish your app to the cloud with a few clicks
  * [Collaborate](/replit-app/collaborate): Work with others on your imported projects



Was this page helpful?

YesNo

[Previous](/getting-started/quickstarts/import-from-github)[Import from BoltLearn how to import Bolt projects into Replit by exporting to GitHub first, then importing with Agent assistance.Next](/getting-started/quickstarts/import-from-bolt)

⌘I

On this page

  * Import your Figma design
  * Import your design
  * What gets imported
  * Figma design guidelines
  * Tips
  * Configure and run your app
  * Interact in Agent chat (beta)
  * Continue your journey