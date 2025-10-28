# category-replit-deployments

**Source URL:** https://docs.replit.com/category/replit-deployments

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

Publishing your App

Overview

Publishing lets you share your Replit App with the world using a simplified process.

## 

​

What is Publishing?

Publishing is a feature that saves a **snapshot** of your Replit App to the cloud, where everyone can interact with it. A snapshot captures the current state of the files in your Replit App. When you publish your Replit App, you create a **published app**. A published app is a running instance of your app on Replit’s cloud infrastructure. This makes the app reliably available on the internet, separate from the version in your workspace.

Replit’s infrastructure is backed by Google Cloud Platform (GCP). All published apps are hosted in the United States.

Publishing includes tools to monitor your published app status and view web analytics. Replit offers the following deployment types:

## [Autoscale DeploymentAutomatically adjusts resources based on your app’s usage.](/cloud-services/deployments/autoscale-deployments)## [Static DeploymentProvides an affordable way to host websites that don’t change based on user input.](/cloud-services/deployments/static-deployments)## [Reserved VM DeploymentProvides a consistent amount of computing resources for your app to run continuously.](/cloud-services/deployments/reserved-vm-deployments)## [Scheduled DeploymentRuns your app at scheduled times that you choose.](/cloud-services/deployments/scheduled-deployments)

## 

​

Getting started

Follow the steps below to publish your Replit App:

  1. From your Replit App workspace, select ![Publish icon](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=df3fa2573b451c54591523c9d9111db1) **Publish** at the top.
  2. In the **Publishing** tab, select your publishing option.
  3. If **Add a payment method** appears, follow the prompts to add a payment method.

Replit automatically selects the best publishing option for your app based on the project type and your needs. However, to choose a different deployment type, consider the following information.

## 

​

Choosing the right publishing option

The following video explains how to choose the right publishing option for your app:

Use the following decision tree featured in the video to help you choose:

![](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/decision-tree.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=8129fe2205ca99224ea9a3707072bcf9)

## 

​

Key features

Publishing offers the following convenient features:

  * **Multiple publishing options** : Select or update a deployment type that meets your needs in a few clicks.
  * **Custom domains** : Serve your app from your web domain.
  * **Analytics** : Track visitor data and other metrics for your published app.
  * **Monitoring tools** : View your published app status and configuration.
  * **Access controls** : Control who can see your app with a single click. Available only for **Teams** members.



## 

​

How it works

When you publish your Replit App, Replit creates a snapshot of your app’s files and dependencies. This snapshot is then sent to Replit’s cloud infrastructure, where it runs as a separate instance of your app. To update your published app with the latest changes, publish again to create a fresh snapshot.

Avoid saving and relying on data written to a published app’s filesystem. To store data, use a storage or database option such as Replit’s [Storage and Database](/category/storage-and-databases) offerings.

## 

​

Use cases

The following examples show different types of published apps.

### 

​

Autoscale deployment: Typing speed assessment app

Let the cloud scale up resources when users take typing tests and reduce them when not in use.

### 

​

Static deployment: Solar system simulation

Learn about the planets in a solar system visualization app on the web. This visualization renders in the browser and doesn’t transfer any user input to a server.

### 

​

Reserved VM deployment: Discord bot

Run a Discord bot that helps you moderate and onboard members. It’s always online to chat with users and respond to commands with predictable pricing and performance.

### 

​

Scheduled deployment: Home automation triggers

Schedule API calls to start and stop your smart home devices at specific times and days.

## 

​

Next steps

To learn more about Replit Publishing, see the following resources:

  * [Autoscale Deployment](/cloud-services/deployments/autoscale-deployments): Learn how to set up applications that scale with traffic
  * [Static Deployment](/cloud-services/deployments/static-deployments): Discover how to publish static websites quickly and efficiently
  * [Reserved VM Deployment](/cloud-services/deployments/reserved-vm-deployments): Explore dedicated VM options for specialized use cases
  * [Scheduled Deployment](/cloud-services/deployments/scheduled-deployments): Set up recurring tasks with simple scheduling
  * [Custom Domains](/cloud-services/deployments/custom-domains): Connect your published app to a custom domain



Was this page helpful?

YesNo

[Previous](/replit-workspace/replit-themes)[Autoscale DeploymentsAutoscale Deployments publish your Replit App to cloud servers that adjust automatically to handle your app's traffic and workload.Next](/cloud-services/deployments/autoscale-deployments)

⌘I

On this page

  * What is Publishing?
  * Getting started
  * Choosing the right publishing option
  * Key features
  * How it works
  * Use cases
  * Autoscale deployment: Typing speed assessment app
  * Static deployment: Solar system simulation
  * Reserved VM deployment: Discord bot
  * Scheduled deployment: Home automation triggers
  * Next steps