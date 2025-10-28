# replit-app-app-embed

**Source URL:** https://docs.replit.com/replit-app/app-embed

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

Replit Apps

Replit App Embed

### 

​

Running and deploying

To interact with the Replit App, such as running the code and seeing its output, users must fork it. Forking creates a personal copy of the Replit App in their workspace, where they can run and edit the code. For a more integrated experience, you can deploy your Replit App and use an iframe to embed the deployed application from `replit.app` directly into your site.

### 

​

How to embed a Replit App

To embed a public Replit App, append the `?embed=true` query parameter to the Replit App’s URL. This modification converts the URL into an embeddable link. Below is an example demonstrating how to embed a Replit App using an iframe in HTML:

Copy

Ask AI
    
    
    <iframe src="YOUR Replit App LINK?embed=true" width="600" height="400"></iframe>
    

Replace `YOUR Replit App LINK` with the actual link to your Replit App, for example, `https://replit.com/@user/repl-name.`

Here’s an example of an embedded Replit App:

### 

​

Customizing the theme

You can customize the appearance of the embedded Replit App by setting the theme. Add theme=light or theme=dark at the end of the URL to choose between a light or dark theme. For instance, to embed a Replit App with a light theme:

Copy

Ask AI
    
    
    <iframe src="YOUR Replit App LINK?embed=true&theme=light" width="600" height="400"></iframe>
    

Example with a light theme:

Was this page helpful?

YesNo

[Previous](/replit-app/configuration)[Developer FrameworksIf your Replit App can be used as a good starting point for other project, you might want to submit it as a developer framework! Let's learn what a Replit developer framework is and how to make a good one.Next](/replit-workspace/templates)

⌘I

On this page

  * Running and deploying
  * How to embed a Replit App
  * Customizing the theme