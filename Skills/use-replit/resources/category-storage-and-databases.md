# category-storage-and-databases

**Source URL:** https://docs.replit.com/category/storage-and-databases

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

Storage and Databases

Storage and Databases

Using Replit’s flexible storage solutions, you can quickly add the perfect data storage your app needs to run. You can use Replit’s database or object storage for apps with the following requirements, and Agent can automatically set up and integrate both solutions:

  * A game that needs to save player information such as progress or high scores
  * A content platform that manages media files



## 

​

What are Replit’s storage and database options

Replit offers the following data storage options:

  * **Database** : stores structured data such as user profiles, game scores, and product catalogs. You can store or retrieve data by attributes and relationships between data points.
  * **App Storage** : stores unstructured data such as images, videos, documents. You can store and retrieve large files and binary data.



### 

​

App Storage and database comparison

| Database| App Storage  
---|---|---  
**Ideal data format**|  Structured data with relationships| Large files (images, videos, documents)  
**Data model**|  Tables, rows, columns| Buckets, files  
**Query language**|  SQL| REST API  
**Clients**|  PostgresSQL-compatible clients and ORMs| Replit SDKs and GCS client libraries  
**Billing model**|  Pay for compute time and storage space| Pay for bandwidth and storage space  
  
### 

​

Workspace tools

Learn more about the following Replit tools to set up and manage your app’s data storage:

## [DatabaseIdeal for structured data and representing data relationships. Backed by Neon’s serverless PostgresSQL solution that scales with your app.](/cloud-services/storage-and-databases/sql-database)## [App StorageIdeal for unstructured data and large files, such as images, videos, and documents. Backed by Google Cloud Storage (GCS) for high availability and scalability. Agent can automatically set up App Storage with advanced authentication and access controls.](/cloud-services/storage-and-databases/object-storage)

## 

​

Getting started

The quickest way to get started with Replit’s storage solutions is to follow one of the tutorials below:

## [DatabaseConnect your app to a SQL database](/getting-started/quickstarts/database-connection)## [App Storage in PythonManage App Storage using the Replit Python SDK](/getting-started/quickstarts/object-storage-python)## [App Storage in JavaScriptManage App Storage using the Replit JavaScript SDK](/getting-started/quickstarts/object-storage-javascript)

## 

​

Use cases

The following examples show how the database and object storage tools can support your Replit Apps.

### 

​

E-commerce app

Store product information, customer profiles, and order history in the database. Use SQL queries to filter products by category, search for items, and manage customer orders.

![screenshot of an E-commerce app](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-ecommerce.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=ecabc5958aca20a29280aa274a8d9316)

### 

​

File sharing app

Share large files such as images, videos, and documents using App Storage. Use the Replit App Storage SDK to upload, download, and move files.

![screenshot of a file sharing app](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/use-case-fileshare.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2556548039bb1bdfec7ce3bb3df1c9d5)

## 

​

Next steps

  * [Database](/cloud-services/storage-and-databases/sql-database): Learn about the database workspace tool and how to connect your Replit App to a database
  * [App Storage](/cloud-services/storage-and-databases/object-storage): Learn how to use Replit’s App Storage solution



Was this page helpful?

YesNo

[Previous](/cloud-services/deployments/static-deployments-advanced)[DatabaseReplit Database is a SQL database built-in to your Replit App. It allows you to store and retrieve data for your app and users.Next](/cloud-services/storage-and-databases/sql-database)

⌘I

On this page

  * What are Replit’s storage and database options
  * App Storage and database comparison
  * Workspace tools
  * Getting started
  * Use cases
  * E-commerce app
  * File sharing app
  * Next steps