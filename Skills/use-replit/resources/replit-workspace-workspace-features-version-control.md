# replit-workspace-workspace-features-version-control

**Source URL:** https://docs.replit.com/replit-workspace/workspace-features/version-control

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

    * [Overview](/category/workspace-features)
    * [Console](/replit-workspace/workspace-features/console)
    * [Dependency Management](/replit-workspace/dependency-management)
    * [File History](/replit-workspace/workspace-features/file-history)
    * [Keyboard Shortcuts](/replit-workspace/keyboard-shortcuts)
    * [Multiplayer](/replit-workspace/workspace-features/multiplayer)
    * [Ports](/replit-workspace/ports)
    * [User Settings](/replit-workspace/workspace-features/user-settings)
    * [Preview](/replit-workspace/workspace-features/preview)
    * [Authentication](/replit-workspace/replit-auth)
    * [Secrets](/replit-workspace/workspace-features/secrets)
    * [Security Scanner](/replit-workspace/workspace-features/security-scanner)
    * [Shell](/replit-workspace/workspace-features/shell)
    * [SSH](/replit-workspace/ssh)
    * Version Control

      * [Overview](/replit-workspace/workspace-features/version-control)
      * [Using the Git pane](/replit-workspace/workspace-features/git-interface)
    * [Workflows](/replit-workspace/workflows)
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

Version Control

Version control

Version control on Replit enables you to track, manage, and collaborate on your codebase with confidence. With built-in Git integration and GitHub connectivity, you can:

  * Track code changes and maintain a history of your development work
  * Collaborate with team members without code conflicts or lost work
  * Import, modify, and push code between Replit and GitHub
  * Work with branches to experiment with new features safely



## 

​

What is version control?

Version control is a system that records changes to files over time, allowing you to recall specific versions later. On Replit, version control is powered by Git—the industry-standard tool for tracking code changes—with a user-friendly visual interface that eliminates the need for command-line knowledge.

![Agent checkpoints in the Git pane](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/checkpoints-vc.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d83568932b7da97cb0eb4e072bafdb12)

### 

​

How version control works on Replit

All four version control options interact with the same underlying Git repository:

  1. **Agent Checkpoints** create commits automatically at important milestones when building with [Replit Agent](/replitai/agent). [Learn more about checkpoints and rollbacks](/replitai/checkpoints-and-rollbacks).
  2. **Git Pane** provides visual access to the complete Git repository
  3. **Git CLI** offers command-line access to all Git functionality
  4. **File History** tracks granular changes within individual files

Choose the interface that best matches your needs, with the confidence that everything is backed by Git’s robust version control system. Feature| Agent Checkpoints| Git Commits| File History  
---|---|---|---  
**Creation**|  Automatic at logical points| Manual or scheduled| Automatic for user edits  
**Granularity**|  Feature-level changes| Any change size| Character-level changes  
**Description**|  AI-generated summaries| User-written messages| Automatic timestamps  
**Rollback**|  One-click restore| Requires Git knowledge| One-click restore  
**Git capabilities**|  Full Git capabilities| Full Git capabilities| No Git capabilities  
**GitHub sync**|  Full GitHub sync capabilities| Full GitHub sync capabilities| No GitHub sync  
  
## 

​

Getting started

Access version control in your Replit App by adding the Git tool to your workspace:

  1. Navigate to the Tools section in your Replit App
  2. Select the **+** sign to add new tools
  3. Select **Git** from the list of available tools

To import existing projects from GitHub, see [Import from GitHub](/getting-started/quickstarts/import-from-github).

## 

​

Version control options

Replit’s version control is powered by Git at its core. You have multiple ways to interact with and benefit from version control:

![Git pane showing the initialize repository button](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/git-pane.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=edfa4f3de48eaca1b3fc39b26ef42efe)

### 

​

Automatic version control

Agent Checkpoints

Automatic snapshots created during AI-assisted development with [Replit Agent](/replitai/agent).**Best for** : Development with Replit Agent**Key capabilities** :

  * Automatic creation at logical milestones
  * One-click rollback
  * Feature-level snapshots
  * Progress tracking
  * No setup required
  * Visual timeline of development progress

Agent checkpoints are stored in Git and can be accessed through the Git Pane or Git CLI. You can also visualize all your checkpoints using the History feature, which provides:

  * Chronological checkpoint visualization
  * Detailed checkpoint descriptions
  * Direct access to checkpoint states
  * One-click rollback to any checkpoint



File History

Per-file version tracking with automatic saving for user edits.**Best for** : Quick recovery of recent file changes**Key capabilities** :

  * Single file focus
  * Character-level changes
  * Visual comparison
  * 30-day history
  * Playback feature

While File History provides its own interface, the underlying changes are part of Git’s history. Learn more about [File History](/replit-workspace/workspace-features/file-history).

### 

​

Git-based interfaces

Git Pane

A visual interface for Git operations that makes version control accessible without command-line knowledge.**Best for** : Most projects requiring GitHub integration and visual workflow**Key capabilities** :

  * Repository-wide tracking
  * Branch management
  * Visual diff viewing
  * One-click GitHub sync
  * Team collaboration

For detailed instructions on using the Git pane, see [Using the Git pane](/replit-workspace/workspace-features/git-interface).

Git CLI

Full command-line access to Git through the [Shell](/replit-workspace/workspace-features/shell) for advanced operations.**Best for** : Power users who need complete Git functionality**Key capabilities** :

  * Full Git command set
  * Advanced branching strategies
  * Custom workflows
  * Script automation
  * Complete repository control

For common Git commands and usage, see [Using the Git pane](/replit-workspace/workspace-features/git-interface#using-git-commands-in-shell).

## 

​

Key features

  * **Visual Git interface** : Manage repositories, commits, and branches without typing Git commands
  * **GitHub integration** : Connect to GitHub repositories for backup and collaboration
  * **Import from GitHub** : Turn any [GitHub repository into a Replit App](/getting-started/quickstarts/import-from-github) with a few clicks
  * **Branch management** : Create, switch between, and merge branches directly in your workspace
  * **Conflict resolution** : Identify and resolve merge conflicts with visual assistance



## 

​

Use cases

**Tracking your personal projects** Track changes to your code as you develop, allowing you to revert to previous versions if needed. The [Git pane](/replit-workspace/workspace-features/git-interface) shows your changes visually, making it easy to commit meaningful updates. **Collaborating with a team** Work with multiple developers on the same codebase without overwriting each other’s changes. Create branches for new features, then merge them back when ready. Learn more about [collaboration tools](/replit-app/collaborate).

## 

​

Agent checkpoints

When building applications with [Replit Agent](/replitai/agent), you benefit from an additional layer of version control through checkpoints. Checkpoints automatically capture the comprehensive state of your project—including workspace contents, AI conversation context, and connected databases—at key moments during AI-assisted development.

![Agent checkpoints in the Git pane](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/checkpoints.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=4962536194cdfa5b0c08503ad0d9b3af)

### 

​

How checkpoints work

Agent checkpoints function as comprehensive snapshots of your entire Replit App state:

  * **Automatic creation** : Agent creates checkpoints at logical points during development
  * **Complete state capture** : Each checkpoint preserves workspace contents, AI memory, and database states
  * **Implementation plans** : Before making changes, Agent presents a plan for your review
  * **Complex task tracking** : Multiple checkpoints may be created for larger tasks



### 

​

Benefits for AI-assisted development

Agent checkpoints provide unique advantages when building with AI:

  * **Safety net** : Experiment confidently knowing you can easily restore previous states across your entire development environment
  * **Progress tracking** : See exactly how Agent built your application step by step
  * **Logical milestones** : Checkpoints represent complete features rather than arbitrary save points
  * **Instant rollback** : Return to any previous state with a single click, including database and AI context restoration



For detailed information about what checkpoints capture and comprehensive rollback capabilities, see [Checkpoints and Rollbacks](/replitai/checkpoints-and-rollbacks).

While Agent checkpoints are powerful for development with AI, consider using Git commits for long-term version tracking and collaboration, especially when working with external repositories.

## 

​

Next steps

To learn more about version control on Replit, see the following resources:

  * [Using the Git pane](/replit-workspace/workspace-features/git-interface): Master Replit’s visual Git interface
  * [Import from GitHub](/getting-started/quickstarts/import-from-github): Turn GitHub repositories into Replit Apps
  * [Collaboration tools](/replit-app/collaborate): Work with others on shared projects
  * [File History](/replit-workspace/workspace-features/file-history): Explore file-level version history
  * [Replit Agent](/replitai/agent): Learn more about AI-assisted development



Was this page helpful?

YesNo

[Previous](/replit-workspace/ssh)[Using the Git paneThe Git pane streamlines version control directly in your workspace, making code tracking, branch management, and collaboration seamless.Next](/replit-workspace/workspace-features/git-interface)

⌘I

On this page

  * What is version control?
  * How version control works on Replit
  * Getting started
  * Version control options
  * Automatic version control
  * Git-based interfaces
  * Key features
  * Use cases
  * Agent checkpoints
  * How checkpoints work
  * Benefits for AI-assisted development
  * Next steps