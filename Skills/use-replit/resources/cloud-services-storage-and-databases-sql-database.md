# cloud-services-storage-and-databases-sql-database

**Source URL:** https://docs.replit.com/cloud-services/storage-and-databases/sql-database

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

Database

Replit Database uses a fully-managed SQL database that lets you add persistent data storage to your Replit App from the Workspace.

The fastest way to get started is to ask **Agent** to add a database to your app. Agent will set up the integration, create the database schema, and update your app to store and retrieve data.

![screenshot of the database editor](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/database-editor.jpg?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=16fcd4d9230fbf84d6721fa467423d29)

## 

​

Features

The Replit Database tool provides the following features:

  * **Instant setup** : Add a production-ready SQL database with a single click
  * **Database tools** : Run queries, manage database schema, and visualize data with the built-in SQL tools
  * **Point-in-time restore** : Restore your database to a specific point in time within your specified retention period
  * **Usage-based billing** : Pay only for the storage and data transfer you use
  * **Environment variables** : Use environment variables in your Replit App to securely access the database



## 

​

Usage

You can access the Replit Database tool directly in your Replit App Workspace. The following sections guide you through setting up and managing your Database.

How to access the Replit Database tool

From the left **Tool dock** :

  1. Select ![All tools icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5b2c72713cc17ac272098bcbfd624d84) **All tools** to see a list of workspace tools.
  2. Select ![PostgresSQL database icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769) **Database**.

From the **Search bar** :

  1. Select the ![magnifying glass icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30) magnifying glass at the top to open the search tool
  2. Type “Replit Database” to locate the tool and select it from the results.



### 

​

Add a database

Use one of the following methods to add a Replit Database integration to your Replit App:

  * Ask **Agent** to add a PostgreSQL database to your Replit App, including details on what data your Replit App should store. Agent sets up the integration, creates the database schema, and updates the app to communicate with the database.
  * From the **Replit Database** tool, select **Create a database**. When using this method, you must create the tables and update your app to connect to the database.

![screenshot of the create database screen](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/create-database.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=76fef31b36b385f858210ccd82365c83)




### 

​

Run database commands

The SQL runner is a Workspace tool that lets you run SQL commands on your database and view the results.

How to access SQL runner

From the **Replit Database** tool:

  1. Select the **My Data** tab
  2. Select ![SQL runner icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-runner-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4f2e172b249503888506d56a5f7ba6b8) **SQL runner**



To run a query, enter the SQL statement in the text area and select the adjacent ![sql run icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/sql-play.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=09a71d59110569ebe7d0d4def83e24ac) run button as shown below:

![screenshot of the SQL runner and run button](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/sql-runner-run.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2008c7ed50b153c09f9e5694d1f533d2)

### 

​

Browse and modify data visually

The Replit Database tool includes [Drizzle Studio](https://orm.drizzle.team/drizzle-studio/overview), a tool that lets you browse and modify data visually. These visual tools help you avoid syntax errors and offer the following functionality:

  * Filter and sort data to focus on specific information
  * Export data to a file for external use
  * Insert or modify row data
  * Create and manage schema, tables, views, and enums

You can access these tools in the **My Data** tab in the **Replit Database** tool. The following image shows a view from the Drizzle Studio builder interface:

![image of the table structure editor](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/table-structure-editor.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b24eb9f5e046a060fcb21276737a8b33)

You can connect to your database using any PostgresSQL-compatible SQL client using the connection string found in your environment variables.

### 

​

View database connection credentials

When you add a database, the Replit Database tool automatically saves your connection credentials as environment variables in your Replit App. Your app uses the credentials to securely connect to the database and run commands.

How to access your database connection credentials

  1. Navigate to the ![PostgresSQL database icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769) **Replit Database** tool in your workspace
  2. Select the ![angled brackets icon](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=aa97c1d6b9eae7dfa4af01802636a8a5) **Commands** tab and scroll to the **Environment variables** section



The list includes the following environment variables, which you can reference from your Replit App’s code:

Do not share your `DATABASE_URL`. It contains your database credentials. Never paste it in public places or support tickets. When contacting support, provide your app URL or masked connection details instead.

  * `DATABASE_URL`: Database connection string which contains all details for a secure connection
  * `PGHOST`: database hostname
  * `PGUSER`: database username
  * `PGPASSWORD`: database password

To learn how to use these credentials in your code, see [Connect your app to a SQL database](/getting-started/quickstarts/database-connection).

### 

​

Restore tool

The Restore tool lets you revert your database to a specific point in time. To activate this tool, you must select a retention period in the **History Retention** option. You can then restore from any point within that period.

Point-in-time restore cannot be undone or rolled forward. After you restore to a chosen timestamp, you cannot return to a later point in time.If you need a later state, run another restore using a later timestamp within your retention window. To minimize data loss, choose the closest valid timestamp to your desired restore point.

![Database rollbacks interface showing rollback options](https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/replitai/database-rollbacks.png?fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=9d12344d4571455f7a65bca637bb02c1)

Common uses for the Restore tool include the following:

  * Recovering from accidental data deletion or corruption
  * Reverting to a previous state for testing or debugging
  * Reviewing historical data from a specific point in time



How to access the Restore tool and History Retention setting

  1. Navigate to the ![PostgresSQL database icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769) **Replit Database** tool in your workspace
  2. Select the ![gear icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608) **Settings** tab and scroll to the **Restore** and **History Retention** sections



To restore your database to a specific time, follow the steps below:

  1. Enter the target date and time in the **Timestamp** field
  2. Select **Restore**. Select **Continue** to proceed in the confirmation dialog.



### 

​

Remove tool

The remove action is irreversible. Make sure to back up any important data before proceeding.

If you no longer need a database for your Replit App, you can remove it and all its data.

How to remove a database

From the **Replit Database** tool:

  1. Select the ![gear icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608) **Settings** tab
  2. Select **Remove database** and confirm by selecting **Yes, Remove database**



### 

​

Billing and resource usage

Replit optimizes your cost savings for database usage by using Neon, a serverless database provider. Neon’s serverless capabilities include the following:

  * Zero infrastructure setup or maintenance
  * Automatic scaling to handle your usage needs
  * Compute time billing only when the database is active

The database enters an idle state after five minutes of inactivity, pausing compute time billing. It instantly reactivates when it receives a query.

To learn more about this serverless database technology, see the [Neon Compute lifecycle](https://neon.tech/docs/introduction/compute-lifecycle) documentation.

Replit provides real-time tracking of your database usage. You can view the breakdown of compute time and storage usage for the current Replit App or for each Replit App on your account.

How to access database usage

To view your database compute time and storage usage for the current billing period, follow the steps below:From the **Replit Database** tool:

  1. Navigate to the ![PostgresSQL database icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/postgres.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3cf383ef9ff4e8b5bad4792121dd6769) **Replit Database** tool in your workspace
  2. Select the ![gear icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/settings-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=39c5a0a4872b7416378ddad9f2bef608) **Settings** tab
  3. Scroll to the **Account resource usage** section to view a usage summary

To view for every Replit App on your account from the **Account resource usage** section, follow the steps below:

  1. Select **View account resource limits** to open the **Usage** page
  2. Scroll to **Resource usage** section
  3. Expand the **PostgresSQL Storage** and **PostgresSQL Compute** rows for details on each Replit App



To learn how Replit charges for database usage, see [Deployments and Database Billing](/billing/about-usage-based-billing#databases).

### 

​

Security features

When you add a database integration using **Agent** , it adds an Object-Relational Mapper (ORM) that handles all database communications with built-in security. This ORM layer, combined with Agent’s security best practice implementation, protects your app from exploits through the following features:

  * **Schema validation** : Verifies data conforms to expected formats
  * **Data sanitization** : Automatically cleans up builder input to prevent SQL injection attacks



## 

​

Next steps

To learn how to connect to a Replit SQL database from code, see [Connect your app to a SQL database](/getting-started/quickstarts/database-connection).

Was this page helpful?

YesNo

[Previous](/category/storage-and-databases)[Production DatabasesLearn how to safely manage and publish database changes in production environments.Next](/cloud-services/storage-and-databases/production-databases)

⌘I

On this page

  * Features
  * Usage
  * Add a database
  * Run database commands
  * Browse and modify data visually
  * View database connection credentials
  * Restore tool
  * Remove tool
  * Billing and resource usage
  * Security features
  * Next steps