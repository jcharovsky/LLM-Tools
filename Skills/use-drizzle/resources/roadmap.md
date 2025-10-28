# roadmap

**Source URL:** https://orm.drizzle.team/roadmap

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

# v1 Roadmap

### Drizzle Kit V1

  * `generated` columns support [beta branch]
  * Brocli integration to Drizzle Kit
  * Generated SQL migration strict mode without `try catches` and `if not exists`
  * Drizzle Kit goes OSS steam 🎉
  * PostgreSQL enums alternations improvements
  * PostgreSQL RLS support
  * `check` constraint support in Drizzle Kit
  * Exposed API for programmatic access in Drizzle Kit
  * `materialized views` support in Drizzle Kit
  * Drizzle Kit support for consuming schemas and migrations from Prisma, TypeORM and Sequelise to enrich ->Drizzle migration process
  * Drizzle Studio `mkcert` fixes for dockerised environments



### Drizzle ORM V1

  * `generated` columns support [beta branch]
  * MySQL `.$returningIds()`
  * `NODE_ENV` support for embedded `.env` consumer
  * `mode: number` and `mode: bigint` support for PostgreSQL `decimals`
  * Table declarations with `(t) => ` callback to optionally omit column type imports
  * Down migrations, better rollbacks and improvements to `migrate` experience in Drizzle Kit
  * Optional database aliases for columns in table declarations -> `id: serial()`
  * PostgreSQL RLS support
  * Relational Queries V2 API
  * `drizzle('pg', ...)` driver instantiation to lower the entrance learning curve
  * CockroachDB support (supported with strict SQL migrations)
  * Native seeding
  * fixes: [#2575](https://github.com/drizzle-team/drizzle-orm/issues/2575), [#2572](https://github.com/drizzle-team/drizzle-orm/issues/2572), [#2571](https://github.com/drizzle-team/drizzle-orm/issues/2571), [#2568](https://github.com/drizzle-team/drizzle-orm/issues/2568), [#2559](https://github.com/drizzle-team/drizzle-orm/issues/2559), [#2555](https://github.com/drizzle-team/drizzle-orm/issues/2555), [#2530](https://github.com/drizzle-team/drizzle-orm/issues/2530), [#2514](https://github.com/drizzle-team/drizzle-orm/issues/2514), [#2510](https://github.com/drizzle-team/drizzle-orm/issues/2510), [#2506](https://github.com/drizzle-team/drizzle-orm/issues/2506), [#2496](https://github.com/drizzle-team/drizzle-orm/issues/2496), [#2486](https://github.com/drizzle-team/drizzle-orm/issues/2486), [#2484](https://github.com/drizzle-team/drizzle-orm/issues/2484), [#2474](https://github.com/drizzle-team/drizzle-orm/issues/2474), [#2472](https://github.com/drizzle-team/drizzle-orm/issues/2472), [#2458](https://github.com/drizzle-team/drizzle-orm/issues/2458), [#2455](https://github.com/drizzle-team/drizzle-orm/issues/2455), add `drizzle-kit migrate/push --inspect` [#2488](https://github.com/drizzle-team/drizzle-orm/issues/2448), [#2432](https://github.com/drizzle-team/drizzle-orm/issues/2432), [#2430](https://github.com/drizzle-team/drizzle-orm/issues/2430), [#2426](https://github.com/drizzle-team/drizzle-orm/issues/2426), [#2424](https://github.com/drizzle-team/drizzle-orm/issues/2424), [#2418](https://github.com/drizzle-team/drizzle-orm/issues/2418), [#2414](https://github.com/drizzle-team/drizzle-orm/issues/2414), [#2401](https://github.com/drizzle-team/drizzle-orm/issues/2401), [#2396](https://github.com/drizzle-team/drizzle-orm/issues/2396), [#2395](https://github.com/drizzle-team/drizzle-orm/issues/2395), [#2394](https://github.com/drizzle-team/drizzle-orm/issues/2394), [#2390](https://github.com/drizzle-team/drizzle-orm/issues/2390), [#2389](https://github.com/drizzle-team/drizzle-orm/issues/2389), [#2388](https://github.com/drizzle-team/drizzle-orm/issues/2388), [#2387](https://github.com/drizzle-team/drizzle-orm/issues/2387), [#2384](https://github.com/drizzle-team/drizzle-orm/issues/2384), [#1210](https://github.com/drizzle-team/drizzle-orm/issues/1210), [#1157](https://github.com/drizzle-team/drizzle-orm/issues/1157), [#1113](https://github.com/drizzle-team/drizzle-orm/issues/1113), [#1020](https://github.com/drizzle-team/drizzle-orm/issues/1020), [#1003](https://github.com/drizzle-team/drizzle-orm/issues/1003), [#998](https://github.com/drizzle-team/drizzle-orm/issues/998), [#830](https://github.com/drizzle-team/drizzle-orm/issues/830), [#724](https://github.com/drizzle-team/drizzle-orm/issues/724), [#2254](https://github.com/drizzle-team/drizzle-orm/issues/2254), [#2239](https://github.com/drizzle-team/drizzle-orm/issues/2239), [#2236](https://github.com/drizzle-team/drizzle-orm/issues/2236), [#2224](https://github.com/drizzle-team/drizzle-orm/issues/2224), [#2216](https://github.com/drizzle-team/drizzle-orm/issues/2216), [#2198](https://github.com/drizzle-team/drizzle-orm/issues/2198), [#2189](https://github.com/drizzle-team/drizzle-orm/issues/2189), [#2183](https://github.com/drizzle-team/drizzle-orm/issues/2183), [#2174](https://github.com/drizzle-team/drizzle-orm/issues/2174), [#2169](https://github.com/drizzle-team/drizzle-orm/issues/2169), [#2157](https://github.com/drizzle-team/drizzle-orm/issues/2157), [#2151](https://github.com/drizzle-team/drizzle-orm/issues/2151), [#2146](https://github.com/drizzle-team/drizzle-orm/issues/2146), [#2136](https://github.com/drizzle-team/drizzle-orm/issues/2136), [#2122](https://github.com/drizzle-team/drizzle-orm/issues/2122), [#2085](https://github.com/drizzle-team/drizzle-orm/issues/2085), [#2067](https://github.com/drizzle-team/drizzle-orm/issues/2067), [#2047](https://github.com/drizzle-team/drizzle-orm/issues/2047), [#2015](https://github.com/drizzle-team/drizzle-orm/issues/2015), [#1928](https://github.com/drizzle-team/drizzle-orm/issues/1928), [#1835](https://github.com/drizzle-team/drizzle-orm/issues/1835), [#1804](https://github.com/drizzle-team/drizzle-orm/issues/1804), [#1765](https://github.com/drizzle-team/drizzle-orm/issues/1765), [#1748](https://github.com/drizzle-team/drizzle-orm/issues/1748), [#1744](https://github.com/drizzle-team/drizzle-orm/issues/1744), [#1625](https://github.com/drizzle-team/drizzle-orm/issues/1625), [#1428](https://github.com/drizzle-team/drizzle-orm/issues/1428), [#1402](https://github.com/drizzle-team/drizzle-orm/issues/1402), [#1315](https://github.com/drizzle-team/drizzle-orm/issues/1315), [#1313](https://github.com/drizzle-team/drizzle-orm/issues/1313), [#1294](https://github.com/drizzle-team/drizzle-orm/issues/1294), [#1272](https://github.com/drizzle-team/drizzle-orm/issues/1272), [#1269](https://github.com/drizzle-team/drizzle-orm/issues/1269), [#1225](https://github.com/drizzle-team/drizzle-orm/issues/1225), [#2378](https://github.com/drizzle-team/drizzle-orm/issues/2378), [#2343](https://github.com/drizzle-team/drizzle-orm/issues/2343), [#2322](https://github.com/drizzle-team/drizzle-orm/issues/2322), [#2315](https://github.com/drizzle-team/drizzle-orm/issues/2315), [#2282](https://github.com/drizzle-team/drizzle-orm/issues/2282), [#2279](https://github.com/drizzle-team/drizzle-orm/issues/2279)
  * 🎉 V1 RELEASE STREAM 🎉
  * MariaDB support
  * MSSQL support



[ ](/)

Headless TypeScript ORM with a head.

[ GitHub ](https://github.com/drizzle-team/drizzle-orm) [ Discord ](https://discord.gg/yfjTbVXMW4) [ ](https://twitter.com/DrizzleORM)

Documentation

[Get Started](/docs/overview) [Manage Schema](/docs/sql-schema-declaration) [Access Data](/docs/rqb) [Migrations](/docs/kit-overview)

Resources

[Drizzle Studio](/drizzle-studio/overview) [Drizzle Gateway](https://gateway.drizzle.team) [Benchmarks](/benchmarks)

Learn

[Guides](/docs/guides) [Tutorials](/docs/tutorials) [Latest Releases](/docs/latest-releases)