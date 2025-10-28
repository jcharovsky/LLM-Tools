# import-migrate-from-heroku

**Source URL:** https://neon.com/docs/import/migrate-from-heroku

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/Migrate from/Heroku

# Migrate from Heroku to Neon Postgres

This guide describes how to import your data from Heroku Postgres to Neon.

#### New feature

If you are looking to migrate your database to Neon, you may want to try our new **Migration Assistant** , which can help. Read the [guide](/docs/import/migration-assistant) to learn more.

The instructions assume that you have installed the Heroku CLI, which is used to transfer data from Heroku. For installation instructions, see [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

  1. ## Create a Neon project and copy the connection string

     1. Navigate to the [Projects](https://console.neon.tech/app/projects) page in the Neon Console.

     2. Click **New Project**.

     3. Specify your project settings and click **Create Project**.

     4. After creating a project, you are directed to the Neon **Dashboard** , where you can click **Connect** to find your database connection details. Copy the connection string. It is required to import your data from Heroku.

The example connection string used the instructions that follow is:
            
            postgresql://alex:AbC123dEf@ep-cool-darkness-123456.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require

  2. ## Retrieve your Heroku app name and database name

     1. Log in to [Heroku](https://dashboard.heroku.com/) and select the project you want to import data from.
     2. Select **Overview** and copy the name of the Heroku Postgres database, which appears under **Installed add-ons**.
     3. Click **Settings** and copy your Heroku **App Name**.

#### note

You can also retrieve the Heroku Postgres database name using the following Heroku CLI command:
    
    heroku pg:links --app <app>

where `<app>` is the Heroku App Name.

For example:
    
    $ heroku pg:links --app thawing-wave-57227
    === postgresql-trapezoidal-48645

  3. ## Import your data

From your terminal, run the following Heroku CLI command:
         
         heroku pg:pull --app [app] [heroku-pg-database] [neon-connection-string]

where:

     * `[app]` is the name of the Heroku app
     * `[heroku-pg-database]` is the name of the Heroku PostgreSQL database
     * `[neon-connection-string]` is the Neon connection string

For example:
    
    $ heroku pg:pull --app thawing-wave-57227 postgresql-trapezoidal-48645 postgresql://alex:AbC123dEf@ep-cool-darkness-123456.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require
    
    heroku-cli: Pulling postgresql-trapezoidal-48645 ---> postgresql://alex:AbC123dEf@ep-cool-darkness-123456.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require
    
    pg_dump: last built-in OID is 16383
    pg_dump: reading extensions
    pg_dump: identifying extension members
    pg_dump: reading schemas
    pg_dump: reading user-defined tables
    pg_dump: reading user-defined functions
    pg_dump: reading user-defined types
    pg_dump: reading procedural languages
    pg_dump: reading user-defined aggregate functions
    pg_dump: reading user-defined operators
    pg_dump: reading user-defined access methods
    pg_dump: reading user-defined operator classes
    pg_dump: reading user-defined operator families
    pg_dump: reading user-defined text search parsers
    pg_dump: reading user-defined text search templates
    pg_dump: reading user-defined text search dictionaries
    pg_dump: reading user-defined text search configurations
    pg_dump: reading user-defined foreign-data wrappers
    pg_dump: reading user-defined foreign servers
    pg_dump: reading default privileges
    pg_dump: reading user-defined collations
    pg_dump: reading user-defined conversions
    pg_dump: reading type casts
    pg_dump: reading transforms
    pg_dump: reading table inheritance information
    pg_dump: reading event triggers
    pg_dump: finding extension tables
    pg_dump: finding inheritance relationships
    pg_dump: reading column info for interesting tables
    pg_dump: finding the columns and types of table "public.customer"
    pg_dump: finding the columns and types of table "public.order"
    pg_dump: flagging inherited columns in subtables
    pg_dump: reading indexes
    pg_dump: reading indexes for table "public.customer"
    pg_dump: reading indexes for table "public.order"
    pg_dump: flagging indexes in partitioned tables
    pg_dump: reading extended statistics
    pg_dump: reading constraints
    pg_dump: reading foreign key constraints for table "public.customer"
    pg_dump: reading foreign key constraints for table "public.order"
    pg_dump: reading triggers
    pg_dump: reading triggers for table "public.customer"
    pg_dump: reading triggers for table "public.order"
    pg_dump: reading rewrite rules
    pg_dump: reading policies
    pg_dump: reading row-level security policies
    pg_dump: reading publications
    pg_dump: reading publication membership
    pg_dump: reading subscriptions
    pg_dump: reading large objects
    pg_dump: reading dependency data
    pg_dump: saving encoding = UTF8
    pg_dump: saving standard_conforming_strings = on
    pg_dump: saving search_path =
    pg_dump: saving database definition
    pg_dump: dumping contents of table "public.customer"
    pg_restore: connecting to database for restore
    pg_dump: dumping contents of table "public.order"
    pg_restore: creating SCHEMA "heroku_ext"
    pg_restore: creating TABLE "public.customer"
    pg_restore: creating TABLE "public.order"
    pg_restore: processing data for table "public.customer"
    pg_restore: processing data for table "public.order"
    pg_restore: creating CONSTRAINT "public.customer customer_pkey"
    pg_restore: creating CONSTRAINT "public.order order_pkey"
    pg_restore: creating FK CONSTRAINT "public.order order_customer_id_fkey"
    heroku-cli: Pulling complete.

  4. ## Verify that your data was imported

     1. Log in to the [Neon Console](https://console.neon.tech/app/projects).
     2. Select the Neon project that you transferred data to.
     3. Select the **Tables** tab.
     4. In the sidebar, verify that your database tables appear under the **Tables** heading.




[PreviousFirebase](/docs/import/migrate-from-firebase)[NextMSSQL](/docs/import/migrate-mssql)

Last updated on July 3, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * 1Create a Neon project and copy the connection string
  * 2Retrieve your Heroku app name and database name
  * 3Import your data
  * 4Verify that your data was imported



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/import/migrate-from-heroku.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/import/migrate-from-heroku.md)

Neon Docs