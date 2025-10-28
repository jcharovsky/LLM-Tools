# replit-app-import-to-replit

**Source URL:** https://docs.replit.com/replit-app/import-to-replit

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

Import

Replit’s import feature allows you to transform existing projects and designs from external development and design tools into Replit Agent Apps. This reference covers supported platforms, technical specifications, limitations, and compatibility requirements.

![Preview of Figma design import in Replit](https://mintcdn.com/replit/Uf4zlH5lH2O96Q1m/images/workspace/import/importer.png?fit=max&auto=format&n=Uf4zlH5lH2O96Q1m&q=85&s=8876c5571e7129426779f3e154bdc702)

## 

​

Supported import sources

Replit’s import feature supports the following external platforms:

  * **Figma** : Convert design frames into React applications using AI-powered code generation
  * **Bolt** : Import existing Bolt projects and migrate them to Replit Agent Apps
  * **Lovable** : Transfer Lovable projects to Replit with Agent assistance
  * **Vercel** : Import Vercel projects by linking your GitHub repository with Agent assistance
  * **Replit Agent** : Import previously exported Agent Apps from GitHub repositories
  * **GitHub** : Import compatible repositories as Agent Apps



All imported projects are validated for Agent compatibility before conversion begins.

## 

​

Quickstart guides

For step-by-step instructions to import from each platform, see the quickstart guides:

## [Import from GitHub⏱️ _2 minutes_ Import an existing GitHub repository into Replit.](/getting-started/quickstarts/import-from-github)## [Import from Figma⏱️ _3 minutes_ Convert your Figma designs into functional React applications.](/getting-started/quickstarts/import-from-figma)## [Import from Vercel⏱️ _3 minutes_ Import your Vercel projects by linking your GitHub repository.](/getting-started/quickstarts/import-from-vercel)## [Import from Bolt⏱️ _4 minutes_ Migrate your Bolt projects to Replit with Agent assistance.](/getting-started/quickstarts/import-from-bolt)## [Import from Lovable⏱️ _4 minutes_ Transfer your Lovable projects to Replit and continue building.](/getting-started/quickstarts/import-from-lovable)

## 

​

Features

  * **Automatic compatibility validation** : Ensures imported projects work with Replit Agent
  * **AI-powered migration** : Agent assists with project setup and feature completion
  * **Design-to-code conversion** : Transform Figma designs into functional React applications
  * **Enterprise-ready templates** : Import customized Agent Apps with internal configurations
  * **Real-time progress tracking** : Monitor import status with detailed progress updates



## 

​

Usage

### 

​

Accessing the import feature

  1. Navigate to [replit.com/import](https://replit.com/import)
  2. Select your desired import source from the available options
  3. Follow the platform-specific import workflow



### 

​

Import workflow

The import process follows these general steps:

1\. Source selection and validation

Choose your import source and provide the necessary project information. The system validates compatibility with Agent before proceeding.If your project is incompatible, you’ll see an error message with suggestions for resolving compatibility issues.

2\. Import processing

During the import process, you’ll see an interstitial screen showing progress updates. Processing time varies based on project complexity and source platform.

![Import progress interstitial screen](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d27e3e9f76e7381f431826ee8d90bdb4)

3\. Agent integration

Once import completes, Agent engages to finalize the setup and ensure your project is ready for development. This is similar to the end state of Agent Rapid Build.

## 

​

Platform-specific workflows

Figma imports

Import your Figma designs directly into Replit Agent Apps and turn them into functional web applications.

### 

​

Getting started

  1. **Connect your Figma account** to authorize access to your designs
  2. **In Figma, select the frame** you want to build in Replit
  3. **Copy the frame URL and paste it** into the Replit import interface

For a full guide on how to import a Figma design, see our [quickstart guide](/getting-started/quickstarts/import-from-figma).

### 

​

What we’ll import

  * **Theme & components**: Design system elements, colors, typography, and reusable components
  * **Assets & icons**: Images, icons, and other visual assets from your design
  * **App scaffolding** : Basic application structure and layout framework



### 

​

Import process

  1. Provide your Figma frame URL or file details
  2. The system converts your design into React code
  3. Agent wires the generated code to a JavaScript stack
  4. Your design becomes a functional web application



Ensure your Figma designs are well-structured with clear component hierarchies complete with auto layout constraints for optimal conversion results.

Vercel imports

Import your Vercel projects by linking the GitHub repository that backs your Vercel project with Agent assistance.

### 

​

Getting started

  1. **Navigate to the import page** and select Vercel from available sources
  2. **Connect your GitHub account** to authorize access to your repositories
  3. **Select the repository** that backs your Vercel project from the available repositories

For a full guide on how to import a Vercel project, see our [quickstart guide](/getting-started/quickstarts/import-from-vercel).

### 

​

What we’ll import

  * **Project structure** : Complete codebase and file organization
  * **Dependencies** : Package.json and dependency management
  * **Build configuration** : Optimized for Replit’s environment
  * **Environment setup** : Runtime and framework configuration



### 

​

What’s not included

  * **Environment variables** : You’ll be prompted to provide these during import
  * **Custom domains** : Set up separately in Replit Deployments
  * **Vercel-specific configurations** : Edge functions and middleware may need adjustment
  * **Analytics and monitoring** : Use Replit’s built-in monitoring tools



### 

​

Import process

  1. Agent scans your code and asks for any required secrets/env vars
  2. You provide environment variables one by one—only what isn’t already standard
  3. Your app boots on Replit with a clean workflow, live preview, and logs
  4. No manual rewiring of build commands or port configuration needed



Bolt imports

Import your Bolt projects by exporting them to GitHub first, then importing into Replit Agent Apps.

### 

​

Getting started

  1. **Export your Bolt project to GitHub** from your Bolt workspace
  2. **Connect your GitHub account to Replit** to authorize repository access
  3. **Select your new Bolt project repo** for import from the available repositories

For a full guide on how to import a Bolt project, see our [quickstart guide](/getting-started/quickstarts/import-from-bolt).

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

### 

​

Import process

  1. The system validates project structure and dependencies
  2. Agent assists with migration and feature completion
  3. Your project is optimized for the Replit environment



Lovable imports

Import your Lovable projects by exporting them to GitHub first, then importing into Replit Agent Apps.

### 

​

Getting started

  1. **Export your Lovable project to GitHub** from your Lovable workspace
  2. **Connect your GitHub account to Replit** to authorize repository access
  3. **Select your new Lovable project repo** for import from the available repositories

For a full guide on how to import a Lovable project, see our [quickstart guide](/getting-started/quickstarts/import-from-lovable).

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

Agent App imports

Import previously exported Agent Apps from GitHub repositories with preserved configurations.

### 

​

Getting started

  1. **Provide the GitHub repository URL** containing your exported Agent App
  2. **Verify repository access** ensuring the repository is accessible to your account
  3. **Confirm Agent App structure** in the repository

For a full guide on how to import a GitHub repository, see our [quickstart guide](/getting-started/quickstarts/import-from-github).

### 

​

What we’ll import

  * **Complete codebase** : All application code, dependencies, and configurations
  * **Agent configurations** : Preserved Agent-specific settings and optimizations
  * **Enterprise customizations** : Internal hardening and custom configurations
  * **Project structure** : Full project hierarchy and organization



### 

​

Import process

  1. The system validates the repository contains Agent App configurations
  2. Internal customizations and enterprise hardening are preserved
  3. The imported app is ready for immediate use or further development



GitHub repository imports

Import compatible GitHub repositories and convert them into Replit Agent Apps.

### 

​

Getting started

  1. **Provide the repository URL** of the GitHub project you want to import
  2. **Ensure repository access** with proper permissions or public visibility
  3. **Verify compatibility** with supported frameworks and technologies

For a full guide on how to import a GitHub repository, see our [quickstart guide](/getting-started/quickstarts/import-from-github).

### 

​

What we’ll import

  * **Source code** : Complete repository codebase and file structure
  * **Dependencies** : Package configurations and dependency definitions
  * **Documentation** : README files, documentation, and project notes
  * **Configuration files** : Build configs, environment setups, and project settings



### 

​

Import process

  1. The system analyzes the codebase for Agent compatibility
  2. If compatible, the repository is converted to an Agent App
  3. Agent assists with any necessary setup or configuration
  4. Project is optimized for the Replit environment



## 

​

Limitations and considerations

### 

​

Current limitations

  * **Database data** : Database contents are not imported; the system includes only schemas and edge functions
  * **Complex dependencies** : Some complex or proprietary dependencies may require manual configuration
  * **Large projects** : Very large projects may take longer to process or require optimization



### 

​

Future enhancements

  * **Database content migration** : Full database content import capabilities
  * **Enhanced validation** : Improved compatibility checking for complex projects



## 

​

Error handling

If an import fails, you’ll receive specific error messages indicating the issue:

  * **Compatibility errors** : The project structure may have issues that need to be resolved
  * **Access errors** : Unable to access the source project or repository
  * **Processing errors** : Technical issues during conversion



If you encounter persistent import issues, check that your source project is publicly accessible or that you have proper permissions.

## 

​

Best practices

### 

​

Preparing for import

  * **Clean project structure** : Ensure your source project has a clear, organized structure
  * **Remove sensitive data** : Remove API keys, credentials, and sensitive information before import
  * **Document dependencies** : Include clear documentation of external dependencies
  * **Test functionality** : Verify your source project works correctly before importing



### 

​

After import

  * **Review generated code** : Check the imported code for accuracy and completeness
  * **Test functionality** : Thoroughly test all features in the Replit environment
  * **Check secrets** : Agent will help you add secrets, but be sure to double check them and add any missing ones using [Replit’s Secret](/replit-workspace/workspace-features/secrets) management.
  * **Recreate databases** : If your project uses databases, recreate them using the [Database tool](/cloud-services/storage-and-databases/sql-database) or by asking Agent to help you.



## 

​

Billing

Import processing may consume Agent credits depending on the complexity of the migration and Agent involvement.

Imports that require Agent assistance for migration or setup will consume credits based on the amount of processing required. Simple imports may complete without more charges beyond your standard Replit usage.

## 

​

Troubleshooting

### 

​

Common issues

**Import validation fails**

  * Verify your source project uses supported frameworks and technologies
  * Check that all required files are present and accessible
  * Ensure your project follows standard conventions for your platform

**Import takes too long**

  * Large or complex projects may require extended processing time
  * Monitor the progress screen for status updates
  * Contact support if processing exceeds expected time frames

**Generated code doesn’t work as expected**

  * Review the imported code for missing dependencies or configurations
  * Use Agent to help debug and resolve any issues
  * Check that all external services and APIs are properly configured

For more support, visit the [Replit Help Center](https://docs.replit.com) or contact the support team.

Was this page helpful?

YesNo

[Previous](/category/replit-apps)[CollaborationOne of the great parts about Replit is that _everything_ you make can be shared with the world. Since your code is hosted in the cloud, it's as simple as one click!Next](/replit-app/collaborate)

⌘I

On this page

  * Supported import sources
  * Quickstart guides
  * Features
  * Usage
  * Accessing the import feature
  * Import workflow
  * Platform-specific workflows
  * Limitations and considerations
  * Current limitations
  * Future enhancements
  * Error handling
  * Best practices
  * Preparing for import
  * After import
  * Billing
  * Troubleshooting
  * Common issues