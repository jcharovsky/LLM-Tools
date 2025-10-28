# get-started-connect-neon

**Source URL:** https://neon.com/docs/get-started/connect-neon

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/2 - Connect

# Connecting Neon to your stack

Learn how to integrate Neon into your application

Using Neon as the serverless database in your tech stack means configuring connections. Whether it’s a direct connection string from your language or framework, setting environment variables for your deployment platform, connecting to ORMs like Prisma, or configuring deployment settings for CI/CD workflows, it starts with the connection.

## Connecting to your application

This section provides connection string samples for various frameworks and languages, helping you integrate Neon into your tech stack.

psql

.env

Next.js

Drizzle

Prisma

Python

.NET

Ruby

Rust

Go
    
    
    # psql example connection string
    psql postgresql://username:password@hostname:5432/database?sslmode=require&channel_binding=require

## Obtaining connection details

When connecting to Neon from an application or client, you connect to a database in your Neon project. In Neon, a database belongs to a branch, which may be the default branch of your project (`production`) or a child branch.

You can obtain the database connection details you require by clicking the **Connect** button on your **Project Dashboard** to open the **Connect to your database** modal. Select a branch, a compute, a database, and a role. A connection string is constructed for you.

![Connection details modal](/_next/image?url=%2Fdocs%2Fconnect%2Fconnection_details.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

Neon supports pooled and direct connections to the database. Use a pooled connection string if your application uses a high number of concurrent connections. For more information, see [Connection pooling](/docs/connect/connection-pooling#connection-pooling).

A Neon connection string includes the role, password, hostname, and database name.
    
    
    postgresql://alex:AbC123dEf@ep-cool-darkness-a1b2c3d4-pooler.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require
                 ^    ^         ^                         ^                              ^
           role -|    |         |- hostname               |- pooler option               |- database
                      |
                      |- password

#### note

The hostname includes the ID of the compute, which has an `ep-` prefix: `ep-cool-darkness-a1b2c3d4`. For more information about Neon connection strings, see [Connection string](/docs/reference/glossary#connection-string).

## Using connection details

You can use the details from the connection string or the connection string itself to configure a connection. For example, you might place the connection details in an `.env` file, assign the connection string to a variable, or pass the connection string on the command-line.

### `.env` file
    
    
    PGUSER=alex
    PGHOST=ep-cool-darkness-a1b2c3d4.us-east-2.aws.neon.tech
    PGDATABASE=dbname
    PGPASSWORD=AbC123dEf
    PGPORT=5432

### Variable
    
    
    DATABASE_URL="postgresql://alex:AbC123dEf@ep-cool-darkness-a1b2c3d4.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require"

### Command-line
    
    
    psql postgresql://alex:AbC123dEf@ep-cool-darkness-a1b2c3d4.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require

#### note

Neon requires that all connections use SSL/TLS encryption, but you can increase the level of protection by appending an `sslmode` parameter setting to your connection string. For instructions, see [Connect to Neon securely](/docs/connect/connect-securely).

## FAQs

### Where do I obtain a password?

It's included in your Neon connection string, which you can find by clicking the **Connect** button on your **Project Dashboard** to open the **Connect to your database** modal.

### What port does Neon use?

Neon uses the default Postgres port, `5432`.

## Network protocol support

Neon projects provisioned on AWS support both [IPv4](https://en.wikipedia.org/wiki/Internet_Protocol_version_4) and [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses. Neon projects provisioned on Azure currently only support IPv4.

Additionally, Neon provides a serverless driver that supports both WebSocket and HTTP connections. For further information, refer to our [Neon serverless driver](/docs/serverless/serverless-driver) documentation.

## Connection notes

  * Some older client libraries and drivers, including older `psql` executables, are built without [Server Name Indication (SNI)](/docs/reference/glossary#sni) support and require a workaround. For more information, see [Connection errors](/docs/connect/connection-errors).
  * Some Java-based tools that use the pgJDBC driver for connecting to Postgres, such as DBeaver, DataGrip, and CLion, do not support including a role name and password in a database connection string or URL field. When you find that a connection string is not accepted, try entering the database name, role, and password values in the appropriate fields in the tool's connection UI



## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[Previous1 - Basics](/docs/get-started/signing-up)[Next3 - Branching](/docs/get-started/workflow-primer)

Last updated on August 2, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Connecting to your application
  * Obtaining connection details
  * Using connection details
  * FAQs
  * Network protocol support
  * Connection notes
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/get-started/connect-neon.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/get-started/connect-neon.md)

Neon Docs