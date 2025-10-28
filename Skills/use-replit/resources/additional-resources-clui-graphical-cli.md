# additional-resources-clui-graphical-cli

**Source URL:** https://docs.replit.com/additional-resources/clui-graphical-cli

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

Additional Resources

The Graphical Command Line Interface

CLUI (Command Line User Interface) is Replit’s interactive command bar that lets you perform various actions quickly without navigating through menus. It combines the efficiency of a command line with a graphical interface.

## 

​

Features

CLUI provides powerful command-driven interactions across three different contexts in Replit:

  * **Account management** : Manage your account settings, view warnings, and restore deleted Replit Apps
  * **Quick navigation** : Move between your Replit Apps and access common features via shortcuts
  * **Workspace operations** : Find files, search code, and access tools within your development environment



## 

​

Usage

### 

​

Account CLUI

The Account CLUI helps you manage your account, teams, and deleted Replit Apps.

![Account CLUI](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=3181c380c560e9400da3efe0ed05cc8f)

**How to access** : Navigate to the [CLUI page](https://replit.com/~/cli), type in the input box to search for a command, and press Enter to execute it.

Account commands

Type `account` to manage your account settings:

  * **view-warns** : View warnings you have been issued
  * **change-username** : Change your username (can only be done once)



Trash commands

Type `trash` to manage deleted Replit Apps:

  * **restore <title>**: Restore a deleted Replit App by its title (restores the most recently deleted if multiple exist with the same name)
  * **view** : View your most recently deleted Replit Apps



Team commands

Type `team` to manage your teams:

  * **view** : View the members of a team you’re in by its username
  * **fork-repl-to-project** : Fork an existing Replit App to create a Team Project



Clear command

Type `clear` to clear the screen of all past commands you’ve executed

### 

​

Shortcuts CLUI

The Shortcuts CLUI provides quick access to common Replit features from any page.

![Shortcuts CLUI](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=99740913ac05919aa87656d986943a33)

**How to access** : Press **CMD/CTRL + K** or click on the search icon in the top navigation bar on most Replit pages.

Available commands

  * **Search** : Search Replit for Replit Apps, Templates, Code, People, and more
  * **New** : Create a new Replit App
  * **My Replit Apps** : Browse and navigate to your Replit Apps
  * **My Code** : Search through the code in all of your Replit Apps



### 

​

Workspace CLUI

The Workspace CLUI helps you perform operations, access tools, find files, and search your code while working in a Replit App.

![Workspace CLUI](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=297576727cabb682ad242ef23c2d3e72)

**How to access** : Press **CMD/CTRL + K** or click the Search icon in the upper-left corner while in the Workspace.

Common operations

  * **Find files** : Quickly locate files in your project
  * **Search code** : Find specific code snippets across your files
  * **Access tools** : Open any tool or panel available in the Workspace
  * **Run commands** : Execute workspace-specific commands



Was this page helpful?

YesNo

[Previous](/extensions/faq)[Cheat SheetA handy cheat sheet summarizing the key features and functionalities of Replit.Next](/additional-resources/cheat-sheet)

⌘I

On this page

  * Features
  * Usage
  * Account CLUI
  * Shortcuts CLUI
  * Workspace CLUI