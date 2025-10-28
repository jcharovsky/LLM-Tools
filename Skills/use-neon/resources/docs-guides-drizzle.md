# guides-drizzle

**Source URL:** https://neon.com/docs/guides/drizzle

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/[ORMs](/docs/get-started/orms)/Drizzle

# Connect from Drizzle to Neon

Learn how to connect to Neon from Drizzle

### What you will learn:

  * How to connect from Drizzle

  * How to use the Neon serverless driver with Drizzle




### Related resources

  * [Drizzle with Neon Postgres (Drizzle Docs)](https://orm.drizzle.team/docs/tutorials/drizzle-with-neon)
  * [Schema migration with Drizzle ORM](/docs/guides/drizzle-migrations)



### Source code

  * [Next.js Edge Functions with Drizzle](https://github.com/neondatabase/examples/tree/main/with-nextjs-drizzle-edge)



Drizzle is a modern ORM for TypeScript that provides a simple and type-safe way to interact with your database. This guide covers the following topics:

  * Connect to Neon from Drizzle
  * Use the Neon serverless driver with Drizzle



#### AI Rules available

Working with AI coding assistants? Check out our [AI rules for Drizzle ORM with Neon](/docs/ai/ai-rules-neon-drizzle) to help your AI assistant generate better code when using Drizzle with your Neon database.

## Connect to Neon from Drizzle

To establish a basic connection from Drizzle to Neon, perform the following steps:

  1. Find your database connection string by clicking the **Connect** button on your **Project Dashboard** to open the **Connect to your database** modal. Select a branch, a user, and the database you want to connect to. A connection string is constructed for you. ![Connection details modal](/_next/image?url=%2Fdocs%2Fconnect%2Fconnection_details.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V) The connection string includes the user name, password, hostname, and database name.

  2. Add a `DATABASE_URL` variable to your `.env` file and set it to the Neon connection string that you copied in the previous step. We also recommend adding `?sslmode=require&channel_binding=require` to the end of the connection string to ensure a [secure connection](/docs/connect/connect-securely).

Your setting will appear similar to the following:
         
         DATABASE_URL="postgresql://[user]:[password]@[neon_hostname]/[dbname]?sslmode=require&channel_binding=require"




## Use the Neon serverless driver with Drizzle

The Neon serverless driver is a low-latency Postgres driver for JavaScript (and TypeScript) that lets you query data from serverless and edge environments. For more information about the driver, see [Neon serverless driver](/docs/serverless/serverless-driver).

To set up Drizzle with the Neon serverless driver, use the Drizzle driver adapter. This adapter allows you to choose a different database driver than Drizzle's default driver for communicating with your database.

Install the Neon serverless driver and `ws` packages:
    
    
    npm install ws @neondatabase/serverless
    npm install -D @types/ws

Update your Drizzle instance:
    
    
    import 'dotenv/config';
    import { drizzle } from 'drizzle-orm/neon-http';
    import { neon } from '@neondatabase/serverless';
    
    import ws from 'ws';
    neonConfig.webSocketConstructor = ws;
    
    // To work in edge environments (Cloudflare Workers, Vercel Edge, etc.), enable querying over fetch
    // neonConfig.poolQueryViaFetch = true
    
    const sql = neon(process.env.DATABASE_URL);
    
    export const db = drizzle({ client: sql });

You can now use Drizzle instance as you normally would with full type-safety.

## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[PreviousDjango (Django ORM)](/docs/guides/django)[NextElixir Ecto](/docs/guides/elixir-ecto)

Last updated on October 10, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Connect to Neon from Drizzle
  * Use the Neon serverless driver with Drizzle
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/guides/drizzle.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/guides/drizzle.md)

Neon Docs