# import-import-data-assistant

**Source URL:** https://neon.com/docs/import/import-data-assistant

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/Utilities/Import Data Assistant

# Import Data Assistant

beta

Move your database to Neon using our automated import tool

When you're ready to move your data to Neon, our Import Data Assistant can help you automatically copy your existing database to Neon. You only need to provide a connection string to get started.

#### Beta

**Import Data Assistant** is in beta and ready to use. We're actively improving it based on feedback from developers like you. Share your experience in our [Discord](https://discord.gg/92vNTzKDGp) or via the [Neon Console](https://console.neon.tech/app/projects?modal=feedback).

#### Migrate between Neon projects

You can also use the **Import Data Assistant** to migrate data between Neon projects. This is useful if you want to upgrade to a newer Postgres version (for example, from Postgres 16 to 17), or move your database to a different region. Just create a new project with the desired Postgres version or region, then use the database connection string from your existing Neon project to import the data into the new one.

## Ways to import

The Import Data Assistant always creates a **new branch** for your imported data. There are two ways to launch the import:

  1. **From the Projects page:**  
Start from the project list to create a new project and import your data into a new branch as part of the flow.

![Import Data Assistant from Projects page](/_next/image?url=%2Fdocs%2Fimport%2Fimport_data_assistant_project.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

  2. **From within a project:**  
Use the Getting Started widget on a project dashboard to import your data into a new branch of the existing project.

![Import Data Assistant from Quick Start widget](/_next/image?url=%2Fdocs%2Fimport%2Fimport_data_assistant_quickstart_widget.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)




Both options use the same automated import process — just provide your database connection string and we'll handle the rest.

## Before you start

You'll need:

  * A **Neon account**. Sign up at [Neon](https://neon.tech) if you don't have one.
  * A **connection string** to your current database in this format:
        
        postgresql://username:password@host:port/database?sslmode=require&channel_binding=require

  * **Admin privileges** on your source database. We recommend using a superuser or a user with the necessary `CREATE`, `SELECT`, `INSERT`, and `REPLICATION` privileges.
  * A database **smaller than 10 GB** in size for automated import
  * We recommend migrating to a Neon project created in the same region as your current database. This helps ensure a faster import. There is a 1-hour time limit on import operations.


  1. ## Check Compatibility

Enter your database connection string and we'll verify:

     * Database size is within the current 10 GB limit
     * Postgres version compatibility (Postgres 14 to 17)
     * Extension compatibility
     * Region availability

  2. ## Import Your Data

Once checks pass, we'll:

     * Create a new branch for your imported data.
     * Copy your data automatically using `pg_dump` and `pg_restore`.
     * Verify that the import completed successfully.

#### note

During import, your source database remains untouched — we only read from it to create a copy in Neon.

### Known Limitations

     * Currently limited to databases **smaller than 10GB**. We are actively working on supporting bigger workloads. In the meantime, contact support if you are looking to migrate bigger databases.
     * There is a 1-hour limit on import operations. For faster imports, we recommend importing to a Neon project created in the same region as your source database.
     * The feature is supported in **AWS regions** only.
     * Supabase and Heroku databases are not supported due to unsupported Postgres extensions.
     * Databases running on **IPv6 are not supported yet**.
     * AWS RDS is generally supported, though some incompatibilities may exist. Support for other providers may vary.

  3. ## Next Steps

After a successful import:

     1. Find your newly imported database branch on the **Branches** page of your project.

![Branches page showing imported branch](/_next/image?url=%2Fdocs%2Fimport%2Fimport_data_assistant_branch.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

_Imported branches are typically named with a timestamp, as shown here._

     2. Run some test queries to ensure everything imported correctly.

     3. Click on the three dots next to the branch name and select **Set as default** to make it your default branch.

     4. Optional cleanup:

        * Delete the old branches (`production` and `development`) if they are no longer needed.
        * Rename the new branch to `production` for clarity and consistency.
     5. Switch your connection string to point to your new Neon database.




## Need Help?

  * For **technical issues** : [Contact support](/docs/introduction/support)
  * For **provider-specific questions** : Let us know what database provider you're using when you contact us



If your database import failed for any reason, please [contact our support team](/docs/introduction/support). We're here to help you get up and running.

[PreviousOverview](/docs/import/migrate-intro)[Nextpg_dump / pg_restore](/docs/import/migrate-from-postgres)

Last updated on July 22, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Ways to import
  * Before you start
  * 1Check Compatibility
  * 2Import Your Data
  * 3Next Steps
  * Need Help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/import/import-data-assistant.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/import/import-data-assistant.md)

Neon Docs