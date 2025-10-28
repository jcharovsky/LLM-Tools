# cloud-services-storage-and-databases-production-databases

**Source URL:** https://docs.replit.com/cloud-services/storage-and-databases/production-databases

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

Production Databases

Production databases are dedicated for your live data that powers your published Replit Apps. Unlike development databases where you experiment and build features, production databases keep your real-world data safe while you continue building, ensuring reliability, and performance. Understanding how to work with production databases is essential for building robust applications that can evolve and scale without disrupting your users.

![Production database management interface](https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/production-databases.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=0587b07401fa601fd2846d25b870ea55)

Production Database management features are currently in beta. While core database functionality is stable and ready for production use, advanced features like creating production databases for existing deployments and testing deployment previews are still in development.

## 

​

What are Production Databases?

Production databases are the live, operational databases that serve real users and their data. They differ significantly from development databases in several key ways:

### 

​

Production vs Development Databases

Aspect| Development Database| Production Database  
---|---|---  
**Purpose**|  Experimentation and feature development| Serving real users and storing business data  
**Data**|  Test data, dummy records, small datasets| Real user data, business-critical information  
**Performance**|  Optimized for development speed| Optimized for reliability and user experience  
**Changes**|  Frequent schema changes, rapid iteration| Careful, planned changes via data migrations and rollback strategies  
**Downtime**|  Acceptable during development| Must be minimized or eliminated  
**Backup**|  Optional for testing| Critical for business continuity  
  
  * Agent is not able to modify the production database, this restriction is in place so that your production database stays safe.
  * Agent can make edits to your development database. At the time of publishing, any changes you’ve made with the agent to the structure of your development database (i.e. adding and deleting columns / tables) will be - applied over to your production database.
  * You are manually able to edit your production data at anytime by going to database pane > production database > My data and toggling **Edit**



## 

​

Database Technology and Infrastructure

Production databases in Replit are built on the same robust foundation as our standard [SQL Database](/cloud-services/storage-and-databases/sql-database) offering. They use PostgreSQL 16 hosted on [Neon](https://neon.tech), providing enterprise-grade reliability and performance.

### 

​

Relationship to Replit SQL Database

Production databases share the same core technology stack as Replit’s SQL Database:

  * **PostgreSQL 16** : Industry-standard relational database with advanced features
  * **Neon Infrastructure** : Serverless database platform that provides automatic scaling and cost optimization
  * **Built-in Tools** : Access to SQL runner, Drizzle Studio, and visual data management tools
  * **Environment Variables** : Secure connection management through automatically generated credentials



For detailed information about database features, connection setup, and technical specifications, see the [SQL Database](/cloud-services/storage-and-databases/sql-database) documentation.

## 

​

Understanding Database Changes and Deployments

When you publish updates to your Replit App that include database changes, you may encounter scenarios where careful planning is essential to avoid downtime or data loss.

### 

​

Non-Backward Compatible Changes

Some database changes can break compatibility with your existing application code. These changes require special handling to ensure smooth deployments.

#### 

​

You may notice a temporary downtime of your published app during publishing. What’s happening?

**Database changes sometimes require stopping your app temporarily to avoid conflicts during the update process** **This prevents data loss or corruption that could happen if users were still using the app during the change**

### 

​

Common Non-Backward Compatible Changes

The following types of changes typically require careful publishing strategies:

  * **Removing database columns** that your application code still references
  * **Changing column data types** in ways that existing code cannot handle
  * **Adding required fields** without default values to existing tables
  * **Renaming tables or columns** that break existing queries
  * **Modifying constraints** that could reject existing application logic



## 

​

Deployment Previews and Testing

Before publishing database changes to production, Replit provides tools to test your changes safely in a preview environment.

### 

​

What is a Deployment Preview? (Coming Soon)

A deployment preview is a temporary, isolated copy of your production environment where you can test database changes and application updates before they affect real users. This preview environment mirrors your production setup but operates independently.

Deployment previews help you catch potential issues early and ensure your changes work correctly before going live.

### 

​

How to Test Your Deployment Preview (Coming Soon)

Testing your deployment is crucial for identifying issues before they impact your users. Follow these steps to ensure your database changes work correctly:

#### 

​

Testing Process

**1\. Functional Testing**

  * Verify that your app still works properly with the database changes applied
  * Test all major user flows to ensure functionality remains intact
  * Check that data displays correctly after the schema modifications

**2\. Data Integrity Verification**

  * Confirm that existing data has been properly migrated or transformed
  * Verify that new fields contain expected values or appropriate defaults
  * Test edge cases where data might not conform to new constraints

**3\. Performance Validation**

  * Monitor query response times in the preview environment
  * Check that new indexes are being used effectively
  * Verify that the changes don’t introduce performance regressions



## 

​

Best Practices for Production Database Management

Follow these proven strategies to maintain reliable, performant production databases:

### 

​

1\. Plan Changes Carefully

**Incremental Updates** : Make small, incremental changes rather than large, complex modifications that increase risk. **Timing Considerations** : Schedule significant changes during low-traffic periods when possible to minimize user impact. **Change Documentation** : Document all changes, their purpose, and expected impact for future reference and team communication.

### 

​

2\. Use Safe Migration Patterns

**Additive Changes First** : When modifying database structure, add new elements before removing old ones to maintain compatibility. **Gradual Transitions** : For major changes, implement them in phases to allow for testing and validation at each step. **Backward Compatibility** : Ensure changes don’t break existing application functionality during the transition period.

### 

​

3\. Security Best Practices

**Access Controls** : Limit database access to only necessary personnel and applications. **Connection Security** : Use encrypted connections and secure authentication methods. **Audit Logging** : Track database access and changes for security and compliance purposes.

## 

​

Troubleshooting Common Issues

### 

​

Publishing Failures

If your publishing fails due to database issues:

  1. **Check the publishing logs** for specific error messages about database connectivity or schema conflicts
  2. **Verify your database connection credentials** are correct and accessible from the published app environment
  3. **Review recent schema changes** for potential conflicts with existing application code
  4. **Test your changes in a preview environment** before attempting to republish



## 

​

Next Steps

To learn more about database management on Replit:

  * [SQL Database](/cloud-services/storage-and-databases/sql-database): Learn about Replit’s managed PostgreSQL database service
  * [Key-Value Store](/cloud-services/storage-and-databases/replit-database): Explore Replit’s simple key-value database option
  * [Deployments](/cloud-services/deployments/about-deployments): Understand how deployments work with database changes
  * [Object Storage](/cloud-services/storage-and-databases/object-storage): Learn about storing files and assets in the cloud



Was this page helpful?

YesNo

[Previous](/cloud-services/storage-and-databases/sql-database)[OverviewApp Storage is Replit's built-in file storage that lets your app easily host and save uploads like images, videos, and documents.Next](/cloud-services/storage-and-databases/object-storage)

⌘I

On this page

  * What are Production Databases?
  * Production vs Development Databases
  * Database Technology and Infrastructure
  * Relationship to Replit SQL Database
  * Understanding Database Changes and Deployments
  * Non-Backward Compatible Changes
  * You may notice a temporary downtime of your published app during publishing. What’s happening?
  * Common Non-Backward Compatible Changes
  * Deployment Previews and Testing
  * What is a Deployment Preview? (Coming Soon)
  * How to Test Your Deployment Preview (Coming Soon)
  * Testing Process
  * Best Practices for Production Database Management
  * 1\. Plan Changes Carefully
  * 2\. Use Safe Migration Patterns
  * 3\. Security Best Practices
  * Troubleshooting Common Issues
  * Publishing Failures
  * Next Steps