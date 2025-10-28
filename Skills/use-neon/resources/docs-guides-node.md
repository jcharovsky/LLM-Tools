# guides-node

**Source URL:** https://neon.com/docs/guides/node

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/[Frameworks](/docs/get-started/frameworks)/Node.js

# Connect a Node.js application to Neon

Set up a Neon project in seconds and connect from a Node.js application

This guide describes how to create a Neon project and connect to it from a Node.js application. Examples are provided for using the [node-postgres](https://www.npmjs.com/package/pg) and [Postgres.js](https://www.npmjs.com/package/postgres) clients. Use the client you prefer.

#### note

The same configuration steps can be used for Express and Next.js applications.

To connect to Neon from a Node.js application:

  1. ## Create a Neon project

If you do not have one already, create a Neon project.

     1. Navigate to the [Projects](https://console.neon.tech/app/projects) page in the Neon Console.
     2. Click **New Project**.
     3. Specify your project settings and click **Create Project**.

  2. ## Create a NodeJS project and add dependencies

     1. Create a NodeJS project and change to the newly created directory.
            
            mkdir neon-nodejs-example
            cd neon-nodejs-example
            npm init -y

     2. Add project dependencies using one of the following commands:

Neon serverless driver

node-postgres

postgres.js
            
            npm install @neondatabase/serverless dotenv

  3. ## Store your Neon credentials

Add a `.env` file to your project directory and add your Neon connection details to it. You can find your Neon database connection details by clicking the **Connect** button on your **Project Dashboard** to open the **Connect to your database** modal. Please select Node.js from the **Connection string** dropdown. For more information, see [Connect from any application](/docs/connect/connect-from-any-app).
         
         PGHOST='[neon_hostname]'
         PGDATABASE='[dbname]'
         PGUSER='[user]'
         PGPASSWORD='[password]'
         ENDPOINT_ID='[endpoint_id]'

#### note

A special `ENDPOINT_ID` variable is included in the `.env` file above. This variable can be used with older Postgres clients that do not support Server Name Indication (SNI), which Neon relies on to route incoming connections. If you are using a newer [node-postgres](https://node-postgres.com/) or [postgres.js](https://github.com/porsager/postgres) client, you won't need it. For more information, see Endpoint ID variable.

#### important

To ensure the security of your data, never expose your Neon credentials to the browser.

  4. ## Configure the Postgres client

Add an `app.js` file to your project directory and add the following code snippet to connect to your Neon database:

Neon serverless driver

node-postgres

postgres.js
         
         require('dotenv').config();
         
         const { neon } = require('@neondatabase/serverless');
         
         const { PGHOST, PGDATABASE, PGUSER, PGPASSWORD } = process.env;
         
         const sql = neon(
           `postgresql://${PGUSER}:${PGPASSWORD}@${PGHOST}/${PGDATABASE}?sslmode=require&channel_binding=require`
         );
         
         async function getPgVersion() {
           const result = await sql`SELECT version()`;
           console.log(result[0]);
         }
         
         getPgVersion();

  5. ## Run app.js

Run `node app.js` to view the result.
         
         {
           version: 'PostgreSQL 16.0 on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit'
         }




## Endpoint ID variable

For older clients that do not support Server Name Indication (SNI), the `postgres.js` example below shows how to include the `ENDPOINT_ID` variable in your application's connection configuration. This is a workaround that is not required if you are using a newer [node-postgres](https://node-postgres.com/) or [postgres.js](https://github.com/porsager/postgres) client. For more information about this workaround and when it is required, see [The endpoint ID is not specified](/docs/connect/connection-errors#the-endpoint-id-is-not-specified) in our [connection errors](/docs/connect/connection-errors) documentation.
    
    
    // app.js
    
    require('dotenv').config();
    
    const postgres = require('postgres');
    
    const { PGHOST, PGDATABASE, PGUSER, PGPASSWORD, ENDPOINT_ID } = process.env;
    
    const sql = postgres({
      host: PGHOST,
      database: PGDATABASE,
      username: PGUSER,
      password: PGPASSWORD,
      port: 5432,
      ssl: 'require',
      connection: {
        options: `project=${ENDPOINT_ID}`,
      },
    });
    
    async function getPgVersion() {
      const result = await sql`select version()`;
      console.log(result);
    }
    
    getPgVersion();

## Source code

You can find the source code for the application described in this guide on GitHub.

  * ### [Get started with Node.js and NeonGet started with Node.js and Neon](https://github.com/neondatabase/examples/tree/main/with-nodejs)



## Community resources

  * [Serverless Node.js Tutorial – Neon Serverless Postgres, AWS Lambda, Next.js, Vercel](https://youtu.be/cxgAN7T3rq8)



## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[PreviousNext.js](/docs/guides/nextjs)[NextNuxt](/docs/guides/nuxt)

Last updated on June 30, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * 1Create a Neon project
  * 2Create a NodeJS project and add dependencies
  * 3Store your Neon credentials
  * 4Configure the Postgres client
  * 5Run app.js
  * Endpoint ID variable
  * Source code
  * Community resources
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/guides/node.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/guides/node.md)

Neon Docs