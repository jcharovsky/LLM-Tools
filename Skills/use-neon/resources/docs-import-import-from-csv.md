# import-import-from-csv

**Source URL:** https://neon.com/docs/import/import-from-csv

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/CSV

# Import data from CSV

This topic shows how to import data into a Neon database table from a CSV file using a simple example.

The instructions require a working installation of [psql](https://www.postgresql.org/download/). The `psql` client is the native command-line client for Postgres. It provides an interactive session for sending commands to Postgres. For installation instructions, see [How to install psql](/docs/connect/query-with-psql-editor#how-to-install-psql).

The following example uses the ready-to-use `neondb` database that is created with your Neon project, a table named `customer`, and a data file named `customer.csv`. Data is loaded from the `customer.csv` file into the `customer` table.

  1. ## Connect to your database

Connect to the `neondb` database using `psql`. For example:
         
         psql "<your_neon_database_connection_string>"

You can find your connection string on your Neon Project Dashboard. Click on the **Connect** button. Use the drop-down menu to copy a full `psql` connection command.

#### note

For more information about connecting to Neon with `psql`, see [Connect with psql](/docs/connect/query-with-psql-editor).

  2. ## Create the target table

Create the `customer` table — table you are importing to must exist in your database and the columns must match your CSV file.
         
         CREATE TABLE customer (
            id SERIAL,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(255),
            PRIMARY KEY (id)
         )

#### tip

You can also create tables using the **SQL Editor** in the Neon Console. See [Query with Neon's SQL Editor](/docs/get-started/query-with-neon-sql-editor).

  3. ## Prepare the CSV file

Prepare a `customer.csv` file with the following data — note that the columns in the CSV file match the columns in the table you created in the previous step.
         
         First Name,Last Name,Email
         1,Casey,Smith,casey.smith@example.com
         2,Sally,Jones,sally.jones@example.com

  4. ## Load the data

From your `psql` prompt, load the data from the `customer.csv` file using the `\copy` option.
         
         \copy customer FROM '/path/to/customer.csv' DELIMITER ',' CSV HEADER

If the command runs successfully, it returns the number of records copied to the database:
         
         COPY 2

For more information about the `\copy` option, refer to the [psql reference](https://www.postgresql.org/docs/current/app-psql.html), in the _PostgreSQL Documentation_.




## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[PreviousAWS DMS](/docs/import/migrate-aws-dms)[NextSample data](/docs/import/import-sample-data)

Last updated on August 2, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * 1Connect to your database
  * 2Create the target table
  * 3Prepare the CSV file
  * 4Load the data
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/import/import-from-csv.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/import/import-from-csv.md)

Neon Docs