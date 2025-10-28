# import-migrate-intro

**Source URL:** https://neon.com/docs/import/migrate-intro

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/Overview

# Neon data migration guides

Learn how to migrate data to Neon Postgres from different database providers and sources

Find instructions for migrating data from Postgres, CSV, other Neon projects, and other database providers. For near-zero downtime data migrations from other Postgres providers, consider using logical replication. Additionally, if you're new to Neon and want to try it out, our sample data guide provides datasets for exploration and testing.

## Data migration guides

  * ### [Import Data AssistantMove your existing database to Neon using our guided migration tool](/docs/import/import-data-assistant)
  * ### [Migrate with pg_dump and pg_restoreMigrate data from another Postgres database using pg_dump and pg_restore](/docs/import/migrate-from-postgres)
  * ### [Migrate from another Neon projectMigrate data from another Neon project for Postgres version, region, or account migration](/docs/import/migrate-from-neon)
  * ### [Migrate schema onlyMigrate only the schema from a Postgres database with pg_dump and pg_restore](/docs/import/migrate-schema-only)
  * ### [Import data from CSVImport data from a CSV file using the psql command-line utility](/docs/import/import-from-csv)
  * ### [Migrate from Firebase FirestoreMigrate data from Firebase Firestore to Neon Postgres using a custom Python script](/docs/import/migrate-from-firebase)
  * ### [Migrate from HerokuMigrate data from a Heroku Postgres database to Neon Postgres using the Heroku CLI](/docs/import/migrate-from-heroku)
  * ### [Migrate with AWS DMSMigrate data from another database source to Neon using the AWS Data Migration Service](/docs/import/migrate-aws-dms)
  * ### [Migrate from AzureMigrate from an Azure Database for PostgreSQL to Neon Postgres](/docs/import/migrate-from-azure-postgres)
  * ### [Migrate from Digital OceanMigrate data from Digital Ocean Postgres to Neon Postgres with pg_dump and pg_restore](/docs/import/migrate-from-digital-ocean)
  * ### [Import sample dataImport one of several sample datasets for exploration and testing](/docs/import/import-sample-data)
  * ### [Migrate from MySQLMigrate your MySQL data to Neon Postgres using pgloader.](/docs/import/migrate-mysql)
  * ### [Migrate from RenderMigrate data from Render to Neon Postgres with pg_dump and pg_restore](/docs/import/migrate-from-render)
  * ### [Migrate from SupabaseMIgrate data from Supabase to Neon Postgres with pg_dump and pg_restore](/docs/import/migrate-from-supabase)
  * ### [Migrate with pgcopydbMigrate data from another Postgres database using pgcopydb for parallel processing](/docs/import/pgcopydb)



## Use logical replication for near-zero downtime data migrations

Postgres logical replication in Neon provides an efficient way to migrate data from other Postgres providers with minimal downtime. By replicating data in real-time, this method allows you to transition your applications to Neon without interrupting your services. Please refer to our logical replication guides for instructions.

  * [![alloydb logo](/images/technology-logos/alloydb.svg)AlloyDBReplicate data from AlloyDB to Neon](/docs/guides/logical-replication-alloydb)
  * [![google-cloud-sql logo](/images/technology-logos/google-cloud-sql.svg)Cloud SQLReplicate data from Cloud SQL to Neon](/docs/guides/logical-replication-cloud-sql)
  * [![postgresql logo](/images/technology-logos/postgresql.svg)![postgresql logo](/images/technology-logos/postgresql-dark.svg)PostgreSQL to NeonReplicate data from PostgreSQL to Neon](/docs/guides/logical-replication-postgres-to-neon)
  * [![aws-rds logo](/images/technology-logos/aws-rds.svg)![aws-rds logo](/images/technology-logos/aws-rds-dark.svg)AWS RDSReplicate data from AWS RDS PostgreSQL to Neon](/docs/guides/logical-replication-rds-to-neon)
  * [![supabase logo](/images/technology-logos/supabase.svg)SupabaseReplicate data from Supabase to Neon](/docs/guides/logical-replication-supabase-to-neon)
  * [![azure logo](/images/technology-logos/azure.svg)Azure PostgreSQLReplicate data from Azure PostgreSQL to Neon](/docs/import/migrate-from-azure-postgres)



[Previous4 - Ready for production](/docs/get-started/production-checklist)[NextImport Data Assistant](/docs/import/import-data-assistant)

Last updated on July 22, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Data migration guides
  * Use logical replication for near-zero downtime data migrations



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/import/migrate-intro.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/import/migrate-intro.md)

Neon Docs