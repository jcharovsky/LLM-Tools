# drizzle-studio-overview

**Source URL:** https://orm.drizzle.team/drizzle-studio/overview

---

[Drizzle Studio Gateway is now FREE 👀](https://gateway.drizzle.team/)

[ ](/)

[Get Started](/docs/get-started) [Documentation](/docs/overview) [Studio](/drizzle-studio/overview) [Benchmarks](/benchmarks)

[ 30k+ ](https://github.com/drizzle-team/drizzle-orm) [ ](/announcements)

Light 

Dark 

System 

meet drizzle

[ Get started ](/docs/get-started)[ Why Drizzle? ](/docs/overview)[ Guides ](/docs/guides)[ Tutorials ](/docs/tutorials)[ Latest releases ](/docs/latest-releases)[ Gotchas ](/docs/gotchas)

Fundamentals

[ Schema ](/docs/sql-schema-declaration)[ Database connection ](/docs/connect-overview)[ Query data ](/docs/data-querying)[ Migrations ](/docs/migrations)

Connect 

[ PostgreSQL ](/docs/get-started-postgresql)[ Gel ](/docs/get-started-gel)[ MySQL ](/docs/get-started-mysql)[ SQLite ](/docs/get-started-sqlite)[ SingleStore ](/docs/get-started-singlestore)

[ Neon ](/docs/connect-neon)[ Vercel Postgres ](/docs/connect-vercel-postgres)[ Prisma Postgres ](/docs/connect-prisma-postgres)[ Supabase ](/docs/connect-supabase)[ Xata ](/docs/connect-xata)[ PGLite ](/docs/connect-pglite)[ Nile ](/docs/connect-nile)[ Bun SQL ](/docs/connect-bun-sql)

[ PlanetScale ](/docs/connect-planetscale)[ TiDB ](/docs/connect-tidb)

[ Turso ](/docs/connect-turso)[ Cloudflare D1 ](/docs/connect-cloudflare-d1)[ Bun SQLite ](/docs/connect-bun-sqlite)[ Cloudflare Durable Objects ](/docs/connect-cloudflare-do)

[ Expo SQLite ](/docs/connect-expo-sqlite)[ OP SQLite ](/docs/connect-op-sqlite)[ React Native SQLite ](/docs/connect-react-native-sqlite)

[ AWS Data API Postgres ](/docs/connect-aws-data-api-pg)[ AWS Data API MySQL ](/docs/connect-aws-data-api-mysql)

[ Drizzle Proxy ](/docs/connect-drizzle-proxy)

Expand

Manage schema

Data types [ Indexes & Constraints ](/docs/indexes-constraints)[ Sequences ](/docs/sequences)[ Views ](/docs/views)[ Schemas ](/docs/schemas)[ Row-Level Security (RLS) ](/docs/rls) Extensions [ Relations ](/docs/relations)

Migrations

[ Overview ](/docs/kit-overview)[ `generate` ](/docs/drizzle-kit-generate)[ `migrate` ](/docs/drizzle-kit-migrate)[ `push` ](/docs/drizzle-kit-push)[ `pull` ](/docs/drizzle-kit-pull)[ `export` ](/docs/drizzle-kit-export)[ `check` ](/docs/drizzle-kit-check)[ `up` ](/docs/drizzle-kit-up)[ `studio` ](/docs/drizzle-kit-studio)[ Custom migrations ](/docs/kit-custom-migrations)[ Migrations for teams ](/docs/kit-migrations-for-teams)[ Web and mobile ](/docs/kit-web-mobile)[ drizzle.config.ts ](/docs/drizzle-config-file)

Seeding

[ Overview ](/docs/seed-overview)[ Generators ](/docs/seed-functions)[ Versioning ](/docs/seed-versioning)

Access your data

[ Query ](/docs/rqb)[ Select ](/docs/select)[ Insert ](/docs/insert)[ Update ](/docs/update)[ Delete ](/docs/delete)[ Filters ](/docs/operators)[ Utils ](/docs/query-utils)[ Joins ](/docs/joins)[ Magic sql`` operator ](/docs/sql)

Performance

[ Queries ](/docs/perf-queries)[ Serverless ](/docs/perf-serverless)

Advanced

[ Set Operations ](/docs/set-operations)[ Generated Columns ](/docs/generated-columns)[ Transactions ](/docs/transactions)[ Batch ](/docs/batch-api)[ Cache ](/docs/cache)[ Dynamic query building ](/docs/dynamic-query-building)[ Read Replicas ](/docs/read-replicas)[ Custom types ](/docs/custom-types)[ Goodies ](/docs/goodies)

Extensions

[ Prisma ](/docs/prisma)[ ESLint Plugin ](/docs/eslint-plugin)[ drizzle-zod ](/docs/zod)[ drizzle-typebox ](/docs/typebox)[ drizzle-valibot ](/docs/valibot)[ drizzle-arktype ](/docs/arktype)[ drizzle-graphql ](/docs/graphql)

System Light Dark

[ Become a Sponsor ](https://driz.link/sponsor) [ Twitter ](https://mobile.twitter.com/DrizzleORM) [ Discord ](https://discord.gg/yfjTbVXMW4)

# Meet Drizzle Studio

🖥 Drizzle Studio is a new way for you to explore SQL database on Drizzle projects.

![Drizzle Studio](/_astro/drizzle-studio.YeMH1cmC_15sm1a.webp)

Drizzle studio grabs your drizzle config file, connects to your database and lets you browse, add, delete and update everything based on your existing drizzle sql schema. It supports explicit `null` and `empty string` values, `booleans`, `numbers` and `big integers`, `json objects` and `json arrays`.

## Quick start

#### Install dependencies

Make sure to go through our [get started](/docs/get-started) guides first!

npm 

yarn 

pnpm 

bun 
    
    
    npm i drizzle-orm
    npm i -D drizzle-kit
    
    
    yarn add drizzle-orm
    yarn add -D drizzle-kit
    
    
    pnpm add drizzle-orm
    pnpm add -D drizzle-kit
    
    
    bun add drizzle-orm
    bun add -D drizzle-kit

#### Prepare your database schema

Check out extended schema declaration **[docs.](/docs/sql-schema-declaration)**

schema.ts
    
    
    import { pgTable, serial, text, varchar } from "drizzle-orm/pg-core";
    
    export const users = pgTable('users', {
      id: serial('id').primaryKey(),
      fullName: text('full_name'),
      phone: varchar('phone', { length: 256 }),
    });

#### Prepare config file

Check out extended config file **[docs.](/docs/drizzle-config-file)**

drizzle.config.ts
    
    
    import { defineConfig } from "drizzle-kit";
     
    export default defineConfig({
      schema: "./schema/*",
      out: "./drizzle",
      dialect: 'postgresql',
      dbCredentials: {
        url: process.env.DB_URL,
      }
    });

#### Launch Drizzle Studio

npm 

yarn 

pnpm 

bun 
    
    
    npx drizzle-kit studio
    
    
    yarn drizzle-kit studio
    
    
    pnpm drizzle-kit studio
    
    
    bunx drizzle-kit studio

You can launch studio with `port` cli flag to customize process port and `verbose` flag for extended SQL statements logging

npm 

yarn 

pnpm 

bun 
    
    
    npx drizzle-kit studio --port 3000 --verbose
    
    
    yarn drizzle-kit studio --port 3000 --verbose
    
    
    pnpm drizzle-kit studio --port 3000 --verbose
    
    
    bunx drizzle-kit studio --port 3000 --verbose

By default, Drizzle Studio will be launched on the `https://local.drizzle.studio` host, and studio server will be launched on 127.0.0.1 host but you can specify any host you want

npm 

yarn 

pnpm 

bun 
    
    
    npx drizzle-kit studio --host 0.0.0.0
    
    
    yarn drizzle-kit studio --host 0.0.0.0
    
    
    pnpm drizzle-kit studio --host 0.0.0.0
    
    
    bunx drizzle-kit studio --host 0.0.0.0

## What’s next?

We’re going to massively improve and extend Drizzle Studio in the upcoming months!  
Subscribe on [Twitter](https://twitter.com/DrizzleORM) and welcome to our [Discord](https://driz.link/discord)

[ ](/)

Headless TypeScript ORM with a head.

[ GitHub ](https://github.com/drizzle-team/drizzle-orm) [ Discord ](https://discord.gg/yfjTbVXMW4) [ ](https://twitter.com/DrizzleORM)

Documentation

[Get Started](/docs/overview) [Manage Schema](/docs/sql-schema-declaration) [Access Data](/docs/rqb) [Migrations](/docs/kit-overview)

Resources

[Drizzle Studio](/drizzle-studio/overview) [Drizzle Gateway](https://gateway.drizzle.team) [Benchmarks](/benchmarks)

Learn

[Guides](/docs/guides) [Tutorials](/docs/tutorials) [Latest Releases](/docs/latest-releases)