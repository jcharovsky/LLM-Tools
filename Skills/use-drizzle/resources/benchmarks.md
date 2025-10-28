# benchmarks

**Source URL:** https://orm.drizzle.team/benchmarks

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

Biased benchmarks 

We ran perf tests, results are in the awesome dashboard below 

Take them with a grain of salt, ofc 

1x2x4x8x16x32x

Pause

0 VUs

01k

1k2k

2k3k

3k

Drizzle vs Prisma

  


Micro database size

E-commerce

PostgreSQL

  


Lenovo M720q

Linux 5.15.0-86-generic x86_64

Intel Core i3-9100T

RAM 32GB DDR4 2666MHz

Benchmark Config

Drizzle

v0.33.0

Bun v1.1.25

Bun Logo

Bun v1.1.25Node 22.6.0 (Current)Node v20.16.0 (LTS)Node v18.20.4 (LTS)

prisma

v5.18.0

Bun v1.1.25

Bun Logo

Bun v1.1.25Node 22.6.0 (Current)Node v20.16.0 (LTS)Node v18.20.4 (LTS)

QueriesJoins

avg latency: 0.0ms

avg latency: 0.0ms

avg: 0 req/sec

Failed requests

Drizzle handled xNaN more requests

0

avg: 0 req/sec

Failed requests

Drizzle handled xNaN more requests

0

avg CPU load: 0.0%

avg CPU load: 0.0%

ORMDatabase sizeProject typeDatabase

Drizzle vs Prisma

Drizzle vs TypeORM

coming soon

[Open on Github ↗︎](https://github.com/drizzle-team/drizzle-benchmarks)

## How it works

Drizzle has been originally designed to be a thin layer on top of SQL and introduce minimal runtime overhead and by introducing Prepared Statements and Relational Queries — we’ve [smashed it](https://medium.com/drizzle-stories/weve-built-typescript-orm-for-821-days-then-this-happened-71282a8b0206). It’s now both fast and has exceptional DX and no n+1 problem for relational queries.

But how fast is it? Is it Drizzle or is it SQL who’s fast? What to measure?

What is a meaningful benchmark? We’ve spent quite some time doing synthetic benchmarks with mitata, tested everything in one runtime and then in separate containerised so there’s no GC cross-influence, community made their own benchmarks and helped us allocate Relational Queries performance and row reads bottlenecks and make them really fast and efficient.

We’ve tested different SQL dialects across all the competitors, and while we were crazy fast, in some cases 100+ times faster than Prisma with SQLite, we only wanted to share benchmarks that were meaningful for businesses and developers.

From business perspective— request roundtrip is the most important metric when it comes down to the server-side performance. While you can influence network latency with services like Cloudflare Argo, on the server side it usually comes down to the database queries.

We’ve composed a test case with a ~370k records in a PostgreSQL database and generated production-like E-commerce traffic benchmarks on 1GB ethernet to eliminate any discrepancies. On Lenovo M720q Drizzle can handle 4.6k reqs/s while maintaining a ~100ms p95 latency.

![](/_astro/benchmark-result.ybx85SlV_Z1SJ5Ig.webp)

We ran our benchmarks on 2 separate machines, so that observer does not influence results. For database we’re using PostgreSQL instance with 42MB of E-commerce data(~370k records).  
K6 benchmarking instance lives on MacBook Air and makes [1M prepared requests](https://github.com/drizzle-team/drizzle-benchmarks/blob/main/data/requests.json) through 1GB ethernet to Lenovo M720q with Intel Core i3-9100T and 32GB of RAM.

![image](/_astro/how-it-works.BsFqMOfn_2iTNGW.webp)

To run your own tests - follow instructions below!

## Prepare test machine

  1. Spin up a docker container with PostgreSQL using `pnpm start:docker` command. You can configure a desired database port in `./src/docker.ts` file:


    
    
    ...
    }
    
    const desiredPostgresPort = 5432; // change here
    main();

  2. Update `DATABASE_URL` with allocated database port in .env file:


    
    
    DATABASE_URL="postgres://postgres:postgres@localhost:5432/postgres"

  3. Seed your database with test data using `pnpm start:seed` command, you can change the size of the database in `./src/seed.ts` file:


    
    
    ...
    }
    
    main("micro"); // nano | micro

  4. Make sure you have Node version 18 installed or above. You can use [`nvm use 18`](https://github.com/nvm-sh/nvm) command
  5. Start Drizzle/Prisma server:


    
    
    ## Drizzle
    pnpm start:drizzle
    
    ## Prisma
    pnpm prepare:prisma
    pnpm start:prisma

## Prepare testing machine

  1. Generate a list of http requests with `pnpm start:generate`. It will output a list of http requests to be run on the tested server | `./data/requests.json`
  2. Install [k6 load tester](https://k6.io/)
  3. Configure tested server url in `./k6.js` file


    
    
    // const host = `http://192.168.31.144:3000`; // drizzle
    const host = `http://192.168.31.144:3001`; // prisma

  4. Run tests with `k6 run bench.js` 🚀



[ ](/)

Headless TypeScript ORM with a head.

[ GitHub ](https://github.com/drizzle-team/drizzle-orm) [ Discord ](https://discord.gg/yfjTbVXMW4) [ ](https://twitter.com/DrizzleORM)

Documentation

[Get Started](/docs/overview) [Manage Schema](/docs/sql-schema-declaration) [Access Data](/docs/rqb) [Migrations](/docs/kit-overview)

Resources

[Drizzle Studio](/drizzle-studio/overview) [Drizzle Gateway](https://gateway.drizzle.team) [Benchmarks](/benchmarks)

Learn

[Guides](/docs/guides) [Tutorials](/docs/tutorials) [Latest Releases](/docs/latest-releases)