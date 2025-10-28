# sql

**Source URL:** https://orm.drizzle.team/docs/sql

---

[Drizzle Studio Gateway is now FREE 👀](https://gateway.drizzle.team/)

[ ](/) [ Documentation ](/docs/overview)

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

sql“ template  sql<T> sql``.mapWith()  sql``.as<T>()  sql.raw()  sql.fromList()  sql.join()  sql.append()  sql.empty()  Convert sql to string and params  sql select  sql in where  sql in orderBy  sql in having and groupBy 

Performance

[ Queries ](/docs/perf-queries)[ Serverless ](/docs/perf-serverless)

Advanced

[ Set Operations ](/docs/set-operations)[ Generated Columns ](/docs/generated-columns)[ Transactions ](/docs/transactions)[ Batch ](/docs/batch-api)[ Cache ](/docs/cache)[ Dynamic query building ](/docs/dynamic-query-building)[ Read Replicas ](/docs/read-replicas)[ Custom types ](/docs/custom-types)[ Goodies ](/docs/goodies)

Extensions

[ Prisma ](/docs/prisma)[ ESLint Plugin ](/docs/eslint-plugin)[ drizzle-zod ](/docs/zod)[ drizzle-typebox ](/docs/typebox)[ drizzle-valibot ](/docs/valibot)[ drizzle-arktype ](/docs/arktype)[ drizzle-graphql ](/docs/graphql)

System Light Dark

[ Become a Sponsor ](https://driz.link/sponsor) [ Twitter ](https://mobile.twitter.com/DrizzleORM) [ Discord ](https://discord.gg/yfjTbVXMW4)

[ v1.0 75% ](/roadmap)

[ Benchmarks ](/benchmarks) [ Extension ](https://driz.link/extension) [ Studio ](/drizzle-studio/overview) [ Studio Package ](https://github.com/drizzle-team/drizzle-studio-npm) [ Gateway ](https://gateway.drizzle.team) [ Drizzle Run ](https://drizzle.run)

Our goodies!

[ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMTU0IiB2aWV3Qm94PSIwIDAgMjAwIDE1NCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICA8cGF0aCBkPSJNMCA2OC42QzAgOTAuNCAxNy44NDk5IDEwOCAzOS45NTk0IDEwOEM2MS44NjYxIDEwOCA3OS45MTg5IDkwLjQgNzkuOTE4OSA2OC42Qzc5LjkxODkgNDcgNjEuODY2MSAyOS4yIDM5Ljk1OTQgMjkuMkMxNy44NDk5IDI5LjIgMCA0NyAwIDY4LjZaTTE3MS4xOTcgMTRDMTcxLjE5NyA2LjYgMTc3LjQ4NSAwIDE4NS4zOTYgMEMxOTMuMzA2IDAgMjAwIDYuNiAyMDAgMTRWOTRDMjAwIDEwMS40IDE5My4zMDYgMTA4IDE4NS4zOTYgMTA4QzE3Ny40ODUgMTA4IDE3MS4xOTcgMTAxLjQgMTcxLjE5NyA5NFYxNFpNMTAuNTQ3NyAxMjcuNkMxMi4xNzA0IDE0MS40IDIzLjczMjMgMTU0IDM5Ljk1OTQgMTU0QzU1Ljk4MzggMTU0IDY3Ljk1MTMgMTQxLjQgNjkuNTc0IDEyNy42QzcxLjgwNTMgMTA3LjYgNTMuMzQ2OSAxMTQuMiAzOS45NTk0IDExNC4yQzI2LjU3MiAxMTQuMiA4LjMxNjQzIDEwNy42IDEwLjU0NzcgMTI3LjZaTTEzOS4zNTEgNzQuMkMxNDAuNzcxIDcxIDE0NC40MjIgNjkgMTUxLjUyMSA2OUMxNjIuNjc3IDY4LjggMTY3LjE0IDYxLjYgMTYxLjI1OCA1MC4yQzE1Ny4yMDEgNDIuNCAxNTAuOTEzIDM2LjQgMTQyLjM5NCAzMi42QzEyMi4zMTIgMjMuOCA5OC41ODAxIDMyLjggODkuNjU1MiA1Mi42QzgwLjczMDIgNzIuMiA4OS42NTUyIDk1LjYgMTA5LjkzOSAxMDQuNkMxMTguNDU4IDEwOC4yIDEyNi45NzggMTA4LjggMTM1LjcgMTA2LjZDMTQ4LjI3NiAxMDMuMiAxNTAuOTEzIDk1IDE0My40MDggODYuOEMxMzguNzQyIDgxLjQgMTM3LjcyOCA3Ny42IDEzOS4zNTEgNzQuMloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl81OV80NikiLz4KICAgICAgICAgIDxkZWZzPgogICAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzU5XzQ2IiB4MT0iMjUwLjI1NCIgeTE9IjAiIHgyPSIyNTAuMjU0IiB5Mj0iMTU0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CiAgICAgICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjRkZDODAwIi8+CiAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjQ4MDAiLz4KICAgICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICAgICAgICA8L2RlZnM+CiAgICAgICAgPC9zdmc+) ![Gel](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMTU0IiB2aWV3Qm94PSIwIDAgMjAwIDE1NCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICA8cGF0aCBkPSJNMCA2OC42QzAgOTAuNCAxNy44NDk5IDEwOCAzOS45NTk0IDEwOEM2MS44NjYxIDEwOCA3OS45MTg5IDkwLjQgNzkuOTE4OSA2OC42Qzc5LjkxODkgNDcgNjEuODY2MSAyOS4yIDM5Ljk1OTQgMjkuMkMxNy44NDk5IDI5LjIgMCA0NyAwIDY4LjZaTTE3MS4xOTcgMTRDMTcxLjE5NyA2LjYgMTc3LjQ4NSAwIDE4NS4zOTYgMEMxOTMuMzA2IDAgMjAwIDYuNiAyMDAgMTRWOTRDMjAwIDEwMS40IDE5My4zMDYgMTA4IDE4NS4zOTYgMTA4QzE3Ny40ODUgMTA4IDE3MS4xOTcgMTAxLjQgMTcxLjE5NyA5NFYxNFpNMTAuNTQ3NyAxMjcuNkMxMi4xNzA0IDE0MS40IDIzLjczMjMgMTU0IDM5Ljk1OTQgMTU0QzU1Ljk4MzggMTU0IDY3Ljk1MTMgMTQxLjQgNjkuNTc0IDEyNy42QzcxLjgwNTMgMTA3LjYgNTMuMzQ2OSAxMTQuMiAzOS45NTk0IDExNC4yQzI2LjU3MiAxMTQuMiA4LjMxNjQzIDEwNy42IDEwLjU0NzcgMTI3LjZaTTEzOS4zNTEgNzQuMkMxNDAuNzcxIDcxIDE0NC40MjIgNjkgMTUxLjUyMSA2OUMxNjIuNjc3IDY4LjggMTY3LjE0IDYxLjYgMTYxLjI1OCA1MC4yQzE1Ny4yMDEgNDIuNCAxNTAuOTEzIDM2LjQgMTQyLjM5NCAzMi42QzEyMi4zMTIgMjMuOCA5OC41ODAxIDMyLjggODkuNjU1MiA1Mi42QzgwLjczMDIgNzIuMiA4OS42NTUyIDk1LjYgMTA5LjkzOSAxMDQuNkMxMTguNDU4IDEwOC4yIDEyNi45NzggMTA4LjggMTM1LjcgMTA2LjZDMTQ4LjI3NiAxMDMuMiAxNTAuOTEzIDk1IDE0My40MDggODYuOEMxMzguNzQyIDgxLjQgMTM3LjcyOCA3Ny42IDEzOS4zNTEgNzQuMloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl81OV80NikiLz4KICAgICAgICAgIDxkZWZzPgogICAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzU5XzQ2IiB4MT0iMjUwLjI1NCIgeTE9IjAiIHgyPSIyNTAuMjU0IiB5Mj0iMTU0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CiAgICAgICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjRkZDODAwIi8+CiAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjQ4MDAiLz4KICAgICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICAgICAgICA8L2RlZnM+CiAgICAgICAgPC9zdmc+) ](https://driz.link/edgedb)

[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Turso](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) 🚀 Drizzle is giving you 10% off Turso Scaler and Pro for 1 Year 🚀 ](https://driz.link/turso)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Payload](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/payload)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMDU0LjM1IDM3OS4xNEMxMDU0LjI0IDQ2OS4xMzcgMTAxOC4zNSA1NTUuNDA4IDk1NC41NiA2MTguOTcxVjYxOC45NjRMNzI4LjI3MyA4NDQuNDVDNzIwLjQzMiA4NTIuMjcgNzA3LjY5MyA4NTIuMjkgNzAwLjM0NiA4NDQuMDFDNjQ1LjMzMSA3ODIuMDE4IDYxNC43NTggNzAxLjgzOCA2MTQuODU2IDYxOC41MzVDNjE0Ljk2MSA1MjguNTM4IDY1MC44NTYgNDQyLjI2OCA3MTQuNjQzIDM3OC43MDVMNzE0LjY1IDM3OC43MTFMOTIxLjM5IDE3Mi42OTdDOTQwLjAyIDE1NC4xMjggOTcwLjUxIDE1My45OTYgOTg2LjMxIDE3NS4wMjJDMTAzMC4zIDIzMy41NDcgMTA1NC40NCAzMDUuMTEgMTA1NC4zNSAzNzkuMTRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMjAyXzcxKSIvPjxwYXRoIGQ9Ik0yNDQuNzg2IDYyMC4zNDVDMTgwLjk5OSA1NTYuNzgyIDE0NS4xMDUgNDcwLjUxMiAxNDUgMzgwLjUxNUMxNDQuOTEzIDMwNi40ODUgMTY5LjA0OCAyMzQuOTIxIDIxMy4wMzUgMTc2LjM5NkMyMjguODM4IDE1NS4zNyAyNTkuMzI4IDE1NS41MDMgMjc3Ljk2MyAxNzQuMDcyTDQ4NC43MDMgMzgwLjA4OEw0ODQuNzEgMzgwLjA4MUM1NDguNDk3IDQ0My42NDUgNTg0LjM5MSA1MjkuOTE0IDU4NC40OTcgNjE5LjkxMkM1ODQuNTk0IDcwMy4yMTQgNTU0LjAyMiA3ODMuMzk1IDQ5OS4wMDcgODQ1LjM4QzQ5MS42NTkgODUzLjY2IDQ3OC45MiA4NTMuNjQgNDcxLjA4IDg0NS44M0wyNDQuNzkzIDYyMC4zMzlMMjQ0Ljc4NiA2MjAuMzQ1WiIgZmlsbD0idXJsKCNwYWludDFfbGluZWFyXzIwMl83MSkiLz48cGF0aCBkPSJNOTQ2LjA1IDEwMjMuODNDOTI5LjQyIDEwNDQuMjIgODk5LjAyIDEwNDQuMDQgODgwLjQyIDEwMjUuNDJMNzUyLjcyNyA4OTcuNThDNzQ0Ljg5MSA4ODkuNzMgNzQ0LjkwNiA4NzcuMDIgNzUyLjc2IDg2OS4xOUw5NjQuODUgNjU3Ljg0OEM5NzIuNjkgNjUwLjAzNSA5ODUuNDggNjQ5Ljk4OSA5OTIuMzkgNjU4LjYzMkMxMDI5LjIgNzA0LjYyOCAxMDQzLjY4IDc2OC4xOTggMTAzMi43NCA4MzguMThDMTAyMi43MiA5MDIuMjQgOTkyLjA4IDk2Ny4zNyA5NDYuMDUgMTAyMy44M1oiIGZpbGw9InVybCgjcGFpbnQyX2xpbmVhcl8yMDJfNzEpIi8+PHBhdGggZD0iTTMxOC45MzEgMTAyNi44QzMwMC4zMzcgMTA0NS40MSAyNjkuOTI5IDEwNDUuNTkgMjUzLjMwNSAxMDI1LjJDMjA3LjI2OSA5NjguNzQgMTc2LjYzMyA5MDMuNjIgMTY2LjYxNyA4MzkuNTZDMTU1LjY3NSA3NjkuNTcxIDE3MC4xNDkgNzA2LjAwMSAyMDYuOTU5IDY2MC4wMDVDMjEzLjg3NiA2NTEuMzYzIDIyNi42NjMgNjUxLjQwOCAyMzQuNTA0IDY1OS4yMjFMNDQ2LjU5NSA4NzAuNTdDNDU0LjQ0OSA4NzguMzkgNDU0LjQ2NCA4OTEuMTEgNDQ2LjYyOSA4OTguOTVMMzE4LjkzMSAxMDI2LjhaIiBmaWxsPSJ1cmwoI3BhaW50M19saW5lYXJfMjAyXzcxKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU4Ljk5OSIgeDI9IjU5OS42NzYiIHkyPSI4NTkuNCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiM5Rjg3RkYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM4NTY2RkYiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU5IiB4Mj0iNTk5LjY3NiIgeTI9Ijg1OS40IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzlGODdGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg1NjZGRiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzIwMl83MSIgeDE9IjU5OS42NzYiIHkxPSI2NDMuNzY2IiB4Mj0iNTk5LjY3NiIgeTI9IjEwMzkuOTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjREU5OUY2Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRDY2OUZDIi8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9InBhaW50M19saW5lYXJfMjAyXzcxIiB4MT0iNTk5LjY3NiIgeTE9IjY0My43NjYiIHgyPSI1OTkuNjc2IiB5Mj0iMTAzOS45MyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNERTk5RjYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNENjY5RkMiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=) ![Xata](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMDU0LjM1IDM3OS4xNEMxMDU0LjI0IDQ2OS4xMzcgMTAxOC4zNSA1NTUuNDA4IDk1NC41NiA2MTguOTcxVjYxOC45NjRMNzI4LjI3MyA4NDQuNDVDNzIwLjQzMiA4NTIuMjcgNzA3LjY5MyA4NTIuMjkgNzAwLjM0NiA4NDQuMDFDNjQ1LjMzMSA3ODIuMDE4IDYxNC43NTggNzAxLjgzOCA2MTQuODU2IDYxOC41MzVDNjE0Ljk2MSA1MjguNTM4IDY1MC44NTYgNDQyLjI2OCA3MTQuNjQzIDM3OC43MDVMNzE0LjY1IDM3OC43MTFMOTIxLjM5IDE3Mi42OTdDOTQwLjAyIDE1NC4xMjggOTcwLjUxIDE1My45OTYgOTg2LjMxIDE3NS4wMjJDMTAzMC4zIDIzMy41NDcgMTA1NC40NCAzMDUuMTEgMTA1NC4zNSAzNzkuMTRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMjAyXzcxKSIvPjxwYXRoIGQ9Ik0yNDQuNzg2IDYyMC4zNDVDMTgwLjk5OSA1NTYuNzgyIDE0NS4xMDUgNDcwLjUxMiAxNDUgMzgwLjUxNUMxNDQuOTEzIDMwNi40ODUgMTY5LjA0OCAyMzQuOTIxIDIxMy4wMzUgMTc2LjM5NkMyMjguODM4IDE1NS4zNyAyNTkuMzI4IDE1NS41MDMgMjc3Ljk2MyAxNzQuMDcyTDQ4NC43MDMgMzgwLjA4OEw0ODQuNzEgMzgwLjA4MUM1NDguNDk3IDQ0My42NDUgNTg0LjM5MSA1MjkuOTE0IDU4NC40OTcgNjE5LjkxMkM1ODQuNTk0IDcwMy4yMTQgNTU0LjAyMiA3ODMuMzk1IDQ5OS4wMDcgODQ1LjM4QzQ5MS42NTkgODUzLjY2IDQ3OC45MiA4NTMuNjQgNDcxLjA4IDg0NS44M0wyNDQuNzkzIDYyMC4zMzlMMjQ0Ljc4NiA2MjAuMzQ1WiIgZmlsbD0idXJsKCNwYWludDFfbGluZWFyXzIwMl83MSkiLz48cGF0aCBkPSJNOTQ2LjA1IDEwMjMuODNDOTI5LjQyIDEwNDQuMjIgODk5LjAyIDEwNDQuMDQgODgwLjQyIDEwMjUuNDJMNzUyLjcyNyA4OTcuNThDNzQ0Ljg5MSA4ODkuNzMgNzQ0LjkwNiA4NzcuMDIgNzUyLjc2IDg2OS4xOUw5NjQuODUgNjU3Ljg0OEM5NzIuNjkgNjUwLjAzNSA5ODUuNDggNjQ5Ljk4OSA5OTIuMzkgNjU4LjYzMkMxMDI5LjIgNzA0LjYyOCAxMDQzLjY4IDc2OC4xOTggMTAzMi43NCA4MzguMThDMTAyMi43MiA5MDIuMjQgOTkyLjA4IDk2Ny4zNyA5NDYuMDUgMTAyMy44M1oiIGZpbGw9InVybCgjcGFpbnQyX2xpbmVhcl8yMDJfNzEpIi8+PHBhdGggZD0iTTMxOC45MzEgMTAyNi44QzMwMC4zMzcgMTA0NS40MSAyNjkuOTI5IDEwNDUuNTkgMjUzLjMwNSAxMDI1LjJDMjA3LjI2OSA5NjguNzQgMTc2LjYzMyA5MDMuNjIgMTY2LjYxNyA4MzkuNTZDMTU1LjY3NSA3NjkuNTcxIDE3MC4xNDkgNzA2LjAwMSAyMDYuOTU5IDY2MC4wMDVDMjEzLjg3NiA2NTEuMzYzIDIyNi42NjMgNjUxLjQwOCAyMzQuNTA0IDY1OS4yMjFMNDQ2LjU5NSA4NzAuNTdDNDU0LjQ0OSA4NzguMzkgNDU0LjQ2NCA4OTEuMTEgNDQ2LjYyOSA4OTguOTVMMzE4LjkzMSAxMDI2LjhaIiBmaWxsPSJ1cmwoI3BhaW50M19saW5lYXJfMjAyXzcxKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU4Ljk5OSIgeDI9IjU5OS42NzYiIHkyPSI4NTkuNCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiM5Rjg3RkYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM4NTY2RkYiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU5IiB4Mj0iNTk5LjY3NiIgeTI9Ijg1OS40IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzlGODdGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg1NjZGRiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzIwMl83MSIgeDE9IjU5OS42NzYiIHkxPSI2NDMuNzY2IiB4Mj0iNTk5LjY3NiIgeTI9IjEwMzkuOTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjREU5OUY2Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRDY2OUZDIi8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9InBhaW50M19saW5lYXJfMjAyXzcxIiB4MT0iNTk5LjY3NiIgeTE9IjY0My43NjYiIHgyPSI1OTkuNjc2IiB5Mj0iMTAzOS45MyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNERTk5RjYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNENjY5RkMiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=) ](https://driz.link/xataio)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Neon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/neon)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Nuxt](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://hub.nuxt.com/?utm_source=drizzle-docs)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQiIGhlaWdodD0iNTQiIHZpZXdCb3g9IjAgMCA1NCA1NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQ4LjQ2MDggMjdDNDguNDYwOCAzOC44Nzc5IDM4Ljg0IDQ4LjUgMjYuOTgwNCA0OC41QzE1LjEyMDkgNDguNSA1LjUgMzguODc3OSA1LjUgMjdDNS41IDE1LjEyMjEgMTUuMTIwOSA1LjUgMjYuOTgwNCA1LjVDMzguODQgNS41IDQ4LjQ2MDggMTUuMTIyMSA0OC40NjA4IDI3WiIgZmlsbD0iI0NGRTJGOCIgc3Ryb2tlPSIjQ0ZFMkY4IiBzdHJva2Utd2lkdGg9IjExIj48L3BhdGg+CjxwYXRoIGQ9Ik0yNC42Nzk2IDEyLjQ3NzVDMjcuMTkxNiA4LjM0MDQ5IDMyLjU3OTEgNy4wMjQ1NSAzNi43MTI4IDkuNTM4MjFDNDAuODQ2NiAxMi4wNTE5IDQyLjE2MTIgMTcuNDQzMyAzOS42NDkyIDIxLjU4MDNMMzEuNjcyNCAzNC43MTY5QzI5LjE2MDMgMzguODUzOCAyMy43NzI4IDQwLjE2OTggMTkuNjM5MSAzNy42NTYxQzE1LjUwNTMgMzUuMTQyNSAxNC4xOTA3IDI5Ljc1MSAxNi43MDI3IDI1LjYxNDFMMjQuNjc5NiAxMi40Nzc1WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zMC4yODkyIDMzLjg3NThMMzguMjY2IDIwLjczOTJDNDAuMzEzOCAxNy4zNjY3IDM5LjI0MjEgMTIuOTcxNiAzNS44NzIzIDEwLjkyMjVDMzIuNTAyNSA4Ljg3MzM1IDI4LjExMDYgOS45NDYxMSAyNi4wNjI3IDEzLjMxODZMMTguMDg1OSAyNi40NTUyQzE2LjAzODEgMjkuODI3NiAxNy4xMDk4IDM0LjIyMjcgMjAuNDc5NiAzNi4yNzE4QzIzLjg0OTUgMzguMzIxIDI4LjI0MTQgMzcuMjQ4MiAzMC4yODkyIDMzLjg3NThaTTM2LjcxMjggOS41MzgyMUMzMi41NzkxIDcuMDI0NTUgMjcuMTkxNiA4LjM0MDQ5IDI0LjY3OTYgMTIuNDc3NUwxNi43MDI3IDI1LjYxNDFDMTQuMTkwNyAyOS43NTEgMTUuNTA1MyAzNS4xNDI1IDE5LjYzOTEgMzcuNjU2MUMyMy43NzI4IDQwLjE2OTggMjkuMTYwMyAzOC44NTM4IDMxLjY3MjQgMzQuNzE2OUwzOS42NDkyIDIxLjU4MDNDNDIuMTYxMiAxNy40NDMzIDQwLjg0NjYgMTIuMDUxOSAzNi43MTI4IDkuNTM4MjFaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMxLjQzODkgMTkuNjczN0MzMS44MTcgMTkuOTEyMiAzMS45MzA0IDIwLjQxMjIgMzEuNjkyMSAyMC43OTA3TDE2LjExOTIgNDUuNTIzMkMxNS44ODEgNDUuOTAxNyAxNS4zODEzIDQ2LjAxNTEgMTUuMDAzMSA0NS43NzY3QzE0LjYyNSA0NS41MzgzIDE0LjUxMTYgNDUuMDM4MiAxNC43NDk5IDQ0LjY1OThMMzAuMzIyOCAxOS45MjcyQzMwLjU2MSAxOS41NDg4IDMxLjA2MDcgMTkuNDM1MyAzMS40Mzg5IDE5LjY3MzdaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMzLjEwNTEgMzAuOTk0OUMzMy4xNzc1IDMxLjM2MDYgMzIuOTQgMzEuNzE1OCAzMi41NzQ2IDMxLjc4ODJDMjcuNzM0NyAzMi43NDc4IDI1LjMxMyAzMi4xMzk0IDI0LjI2ODcgMzEuNDA0NEMyMy45NjQxIDMxLjE5IDIzLjg5MDggMzAuNzY4OSAyNC4xMDUgMzAuNDY0QzI0LjMxOTMgMzAuMTU5IDI0Ljc0IDMwLjA4NTcgMjUuMDQ0NyAzMC4zMDAxQzI1LjYyNzEgMzAuNzEgMjcuNTgxMSAzMS40MDIxIDMyLjMxMjYgMzAuNDY0QzMyLjY3NzkgMzAuMzkxNSAzMy4wMzI4IDMwLjYyOTIgMzMuMTA1MSAzMC45OTQ5WiIgZmlsbD0iYmxhY2siPjwvcGF0aD4KPC9zdmc+) ![SQLite Cloud](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQiIGhlaWdodD0iNTQiIHZpZXdCb3g9IjAgMCA1NCA1NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQ4LjQ2MDggMjdDNDguNDYwOCAzOC44Nzc5IDM4Ljg0IDQ4LjUgMjYuOTgwNCA0OC41QzE1LjEyMDkgNDguNSA1LjUgMzguODc3OSA1LjUgMjdDNS41IDE1LjEyMjEgMTUuMTIwOSA1LjUgMjYuOTgwNCA1LjVDMzguODQgNS41IDQ4LjQ2MDggMTUuMTIyMSA0OC40NjA4IDI3WiIgZmlsbD0iI0NGRTJGOCIgc3Ryb2tlPSIjQ0ZFMkY4IiBzdHJva2Utd2lkdGg9IjExIj48L3BhdGg+CjxwYXRoIGQ9Ik0yNC42Nzk2IDEyLjQ3NzVDMjcuMTkxNiA4LjM0MDQ5IDMyLjU3OTEgNy4wMjQ1NSAzNi43MTI4IDkuNTM4MjFDNDAuODQ2NiAxMi4wNTE5IDQyLjE2MTIgMTcuNDQzMyAzOS42NDkyIDIxLjU4MDNMMzEuNjcyNCAzNC43MTY5QzI5LjE2MDMgMzguODUzOCAyMy43NzI4IDQwLjE2OTggMTkuNjM5MSAzNy42NTYxQzE1LjUwNTMgMzUuMTQyNSAxNC4xOTA3IDI5Ljc1MSAxNi43MDI3IDI1LjYxNDFMMjQuNjc5NiAxMi40Nzc1WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zMC4yODkyIDMzLjg3NThMMzguMjY2IDIwLjczOTJDNDAuMzEzOCAxNy4zNjY3IDM5LjI0MjEgMTIuOTcxNiAzNS44NzIzIDEwLjkyMjVDMzIuNTAyNSA4Ljg3MzM1IDI4LjExMDYgOS45NDYxMSAyNi4wNjI3IDEzLjMxODZMMTguMDg1OSAyNi40NTUyQzE2LjAzODEgMjkuODI3NiAxNy4xMDk4IDM0LjIyMjcgMjAuNDc5NiAzNi4yNzE4QzIzLjg0OTUgMzguMzIxIDI4LjI0MTQgMzcuMjQ4MiAzMC4yODkyIDMzLjg3NThaTTM2LjcxMjggOS41MzgyMUMzMi41NzkxIDcuMDI0NTUgMjcuMTkxNiA4LjM0MDQ5IDI0LjY3OTYgMTIuNDc3NUwxNi43MDI3IDI1LjYxNDFDMTQuMTkwNyAyOS43NTEgMTUuNTA1MyAzNS4xNDI1IDE5LjYzOTEgMzcuNjU2MUMyMy43NzI4IDQwLjE2OTggMjkuMTYwMyAzOC44NTM4IDMxLjY3MjQgMzQuNzE2OUwzOS42NDkyIDIxLjU4MDNDNDIuMTYxMiAxNy40NDMzIDQwLjg0NjYgMTIuMDUxOSAzNi43MTI4IDkuNTM4MjFaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMxLjQzODkgMTkuNjczN0MzMS44MTcgMTkuOTEyMiAzMS45MzA0IDIwLjQxMjIgMzEuNjkyMSAyMC43OTA3TDE2LjExOTIgNDUuNTIzMkMxNS44ODEgNDUuOTAxNyAxNS4zODEzIDQ2LjAxNTEgMTUuMDAzMSA0NS43NzY3QzE0LjYyNSA0NS41MzgzIDE0LjUxMTYgNDUuMDM4MiAxNC43NDk5IDQ0LjY1OThMMzAuMzIyOCAxOS45MjcyQzMwLjU2MSAxOS41NDg4IDMxLjA2MDcgMTkuNDM1MyAzMS40Mzg5IDE5LjY3MzdaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMzLjEwNTEgMzAuOTk0OUMzMy4xNzc1IDMxLjM2MDYgMzIuOTQgMzEuNzE1OCAzMi41NzQ2IDMxLjc4ODJDMjcuNzM0NyAzMi43NDc4IDI1LjMxMyAzMi4xMzk0IDI0LjI2ODcgMzEuNDA0NEMyMy45NjQxIDMxLjE5IDIzLjg5MDggMzAuNzY4OSAyNC4xMDUgMzAuNDY0QzI0LjMxOTMgMzAuMTU5IDI0Ljc0IDMwLjA4NTcgMjUuMDQ0NyAzMC4zMDAxQzI1LjYyNzEgMzAuNzEgMjcuNTgxMSAzMS40MDIxIDMyLjMxMjYgMzAuNDY0QzMyLjY3NzkgMzAuMzkxNSAzMy4wMzI4IDMwLjYyOTIgMzMuMTA1MSAzMC45OTQ5WiIgZmlsbD0iYmxhY2siPjwvcGF0aD4KPC9zdmc+) ](https://driz.link/sqlitecloud)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Upstash](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/upstash)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Lokalise](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/lokalise)[ ![](data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJBcnR3b3JrIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNzkzLjggODcxLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDc5My44IDg3MS41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0Y1NjQwQzt9Cjwvc3R5bGU+CjxnPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM5Ni45LDM1Ni4xSDIyNy4yYy0xNi42LDAtMzAtMTMuNC0zMC0zMHYtOTkuOGMwLTE2LjYsMTMuNC0zMCwzMC0zMGgxMzkuN2MxNi42LDAsMzAsMTMuNCwzMCwzMFYzNTYuMXoiLz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik01NjYuNiw1MTUuOEgzOTYuOVYzNTYuMWgxNjkuN2MxNi41LDAsMjkuOSwxMy40LDI5LjksMjkuOXY5OS44QzU5Ni41LDUwMi40LDU4My4xLDUxNS44LDU2Ni42LDUxNS44eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM2Ni45LDY3NS42SDIyNy4yYy0xNi41LDAtMjkuOS0xMy40LTI5LjktMjkuOXYtOTkuOGMwLTE2LjUsMTMuNC0yOS45LDI5LjktMjkuOWgxNjkuN3YxMjkuOAoJCUMzOTYuOSw2NjIuMSwzODMuNSw2NzUuNiwzNjYuOSw2NzUuNnoiLz4KPC9nPgo8L3N2Zz4=) ![Replit](data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJBcnR3b3JrIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNzkzLjggODcxLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDc5My44IDg3MS41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0Y1NjQwQzt9Cjwvc3R5bGU+CjxnPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM5Ni45LDM1Ni4xSDIyNy4yYy0xNi42LDAtMzAtMTMuNC0zMC0zMHYtOTkuOGMwLTE2LjYsMTMuNC0zMCwzMC0zMGgxMzkuN2MxNi42LDAsMzAsMTMuNCwzMCwzMFYzNTYuMXoiLz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik01NjYuNiw1MTUuOEgzOTYuOVYzNTYuMWgxNjkuN2MxNi41LDAsMjkuOSwxMy40LDI5LjksMjkuOXY5OS44QzU5Ni41LDUwMi40LDU4My4xLDUxNS44LDU2Ni42LDUxNS44eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM2Ni45LDY3NS42SDIyNy4yYy0xNi41LDAtMjkuOS0xMy40LTI5LjktMjkuOXYtOTkuOGMwLTE2LjUsMTMuNC0yOS45LDI5LjktMjkuOWgxNjkuN3YxMjkuOAoJCUMzOTYuOSw2NjIuMSwzODMuNSw2NzUuNiwzNjYuOSw2NzUuNnoiLz4KPC9nPgo8L3N2Zz4=) ](https://driz.link/replit)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Sentry](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/sentry)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQuNzIwNDcgMEMyLjExMzQ0IDAgMCAyLjExMzQ0IDAgNC43MjA0N1YxOS4yNzk1QzAgMjEuODg2NiAyLjExMzQ0IDI0IDQuNzIwNDcgMjRIMTkuMjc5NUMyMS44ODY2IDI0IDI0IDIxLjg4NjYgMjQgMTkuMjc5NVY0LjcyMDQ3QzI0IDIuMTEzNDQgMjEuODg2NiAwIDE5LjI3OTUgMEg0LjcyMDQ3Wk05LjMwMjA0IDUuMDE1NjNWNy44NDM2N0g2Ljc0OTk4VjEwLjMyNjhDNi43NDk5OCAxMC44NDg3IDYuOTQzNzMgMTEuMDEzNCA3LjA2OTUxIDExLjEyMDRDNy4xMDI4NSAxMS4xNDg3IDcuMTMxMzkgMTEuMTczIDcuMTUwMzEgMTEuMTk4OEw5LjI3NzAyIDEzLjM4MTRINi43NDk5OFYxNi4xNzk4SDkuMjc3MDJWMTkuMDA3OEgxNC43MDYzVjE2LjE3OThIOS4yNzcwMlYxMy4zODE0SDE0LjAzNUMxNC42OTM4IDEzLjM4MTQgMTQuNjkzOCAxNC4xNzk1IDE0LjY5MzggMTQuNTQ0MVYxNi4xNzk4SDE3LjI0NThWMTMuNjk2N0MxNy4yNDU4IDEzLjE3NDggMTcuMDUyMSAxMy4wMTAxIDE2LjkyNjMgMTIuOTAzMUMxNi44OTMgMTIuODc0NyAxNi44NjQ0IDEyLjg1MDUgMTYuODQ1NSAxMi44MjQ3TDE0LjY5MzggMTAuNjQyMUgxNy4yNUwxNy4yNDU4IDcuODQzNjdIMTQuNzA2M0wxNC42OTM4IDEwLjY0MjFIOS45NjA4OEM5LjMwMjA0IDEwLjY0MjEgOS4zMDIwNCA5Ljg0Mzk1IDkuMzAyMDQgOS40NzkzNVY3Ljg0MzY3SDE0LjcwNjNWNS4wMTU2M0g5LjMwMjA0WiIgZmlsbD0iI0Y5NzMxNiIvPjwvc3ZnPg==) ![Sevalla](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQuNzIwNDcgMEMyLjExMzQ0IDAgMCAyLjExMzQ0IDAgNC43MjA0N1YxOS4yNzk1QzAgMjEuODg2NiAyLjExMzQ0IDI0IDQuNzIwNDcgMjRIMTkuMjc5NUMyMS44ODY2IDI0IDI0IDIxLjg4NjYgMjQgMTkuMjc5NVY0LjcyMDQ3QzI0IDIuMTEzNDQgMjEuODg2NiAwIDE5LjI3OTUgMEg0LjcyMDQ3Wk05LjMwMjA0IDUuMDE1NjNWNy44NDM2N0g2Ljc0OTk4VjEwLjMyNjhDNi43NDk5OCAxMC44NDg3IDYuOTQzNzMgMTEuMDEzNCA3LjA2OTUxIDExLjEyMDRDNy4xMDI4NSAxMS4xNDg3IDcuMTMxMzkgMTEuMTczIDcuMTUwMzEgMTEuMTk4OEw5LjI3NzAyIDEzLjM4MTRINi43NDk5OFYxNi4xNzk4SDkuMjc3MDJWMTkuMDA3OEgxNC43MDYzVjE2LjE3OThIOS4yNzcwMlYxMy4zODE0SDE0LjAzNUMxNC42OTM4IDEzLjM4MTQgMTQuNjkzOCAxNC4xNzk1IDE0LjY5MzggMTQuNTQ0MVYxNi4xNzk4SDE3LjI0NThWMTMuNjk2N0MxNy4yNDU4IDEzLjE3NDggMTcuMDUyMSAxMy4wMTAxIDE2LjkyNjMgMTIuOTAzMUMxNi44OTMgMTIuODc0NyAxNi44NjQ0IDEyLjg1MDUgMTYuODQ1NSAxMi44MjQ3TDE0LjY5MzggMTAuNjQyMUgxNy4yNUwxNy4yNDU4IDcuODQzNjdIMTQuNzA2M0wxNC42OTM4IDEwLjY0MjFIOS45NjA4OEM5LjMwMjA0IDEwLjY0MjEgOS4zMDIwNCA5Ljg0Mzk1IDkuMzAyMDQgOS40NzkzNVY3Ljg0MzY3SDE0LjcwNjNWNS4wMTU2M0g5LjMwMjA0WiIgZmlsbD0iI0Y5NzMxNiIvPjwvc3ZnPg==) ](https://driz.link/sevalla)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![GibsonAI](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/gibsonai)

Product by Drizzle Team 

[ One Dollar Stats $1 per mo web analytics christmas   
deal  ](https://driz.link/onedollarstats)

# Magical `sql` operator 🪄

When working with an ORM library, there may be cases where you find it challenging to write a specific query using the provided ORM syntax. In such situations, you can resort to using raw queries, which involve constructing a query as a raw string. However, raw queries often lack the benefits of type safety and query parameterization.

To address this, many libraries have introduced the concept of an `sql` template. This template allows you to write more type-safe and parameterized queries, enhancing the overall safety and flexibility of your code. Drizzle, being a powerful ORM library, also supports the sql template.

With Drizzle’s `sql` template, you can go even further in crafting queries. If you encounter difficulties in writing an entire query using the library’s query builder, you can selectively use the `sql` template within specific sections of the Drizzle query. This flexibility enables you to employ the sql template in partial SELECT statements, WHERE clauses, ORDER BY clauses, HAVING clauses, GROUP BY clauses, and even in relational query builders.

By leveraging the capabilities of the sql template in Drizzle, you can maintain the advantages of type safety and query parameterization while achieving the desired query structure and complexity. This empowers you to create more robust and maintainable code within your application.

## sql“ template

One of the most common usages you may encounter in other ORMs as well is the ability to use `sql` queries as-is for raw queries.
    
    
    import { sql } from 'drizzle-orm' 
    
    const id = 69;
    await db.execute(sql`select * from ${usersTable} where ${usersTable.id} = ${id}`)

It will generate the current query
    
    
    select * from "users" where "users"."id" = $1; --> [69]

Any tables and columns provided to the sql parameter are automatically mapped to their corresponding SQL syntax with escaped names for tables, and the escaped table names are appended to column names.

Additionally, any dynamic parameters such as `${id}` will be mapped to the $1 placeholder, and the corresponding values will be moved to an array of values that are passed separately to the database.

This approach effectively prevents any potential SQL Injection vulnerabilities.

## `sql<T>`

Please note that `sql<T>` does not perform any runtime mapping. The type you define using `sql<T>` is purely a helper for Drizzle. It is important to understand that there is no feasible way to determine the exact type dynamically, as SQL queries can be highly versatile and customizable.

You can define a custom type in Drizzle to be used in places where fields require a specific type other than `unknown`.

This feature is particularly useful in partial select queries, ensuring consistent typing for selected fields:
    
    
    // without sql<T> type defined
    const response: { lowerName: unknown }[] = await db.select({
        lowerName: sql`lower(${usersTable.id})`
    }).from(usersTable);
    
    // with sql<T> type defined
    const response: { lowerName: string }[] = await db.select({
        lowerName: sql<string>`lower(${usersTable.id})`
    }).from(usersTable);

## `sql``.mapWith()`

For the cases you need to make a runtime mapping for values passed from database driver to drizzle you can use `.mapWith()`

This function accepts different values, that will map response in runtime.

You can replicate a specific column mapping strategy as long as the interface inside mapWith is the same interface that is implemented by Column.
    
    
    const usersTable = pgTable('users', {
        id: serial('id').primaryKey(),
        name: text('name').notNull(),
    });
    
    //  at runtime this values will be mapped same as `text` column is mapped in drizzle
    sql`...`.mapWith(usersTable.name);

You can also pass your own implementation for the `DriverValueDecoder` interface:
    
    
    sql``.mapWith({
    	mapFromDriverValue: (value: any) => {
    		const mappedValue = value;
    		// mapping you want to apply
    		return mappedValue;
    	},
    });
        
    // or
    sql``.mapWith(Number);

## `sql``.as<T>()`

In different cases, it can sometimes be challenging to determine how to name a custom field that you want to use. You may encounter situations where you need to explicitly specify an alias for a field that will be selected. This can be particularly useful when dealing with complex queries.

To address these scenarios, we have introduced a helpful `.as('alias_name')` helper, which allows you to define an alias explicitly. By utilizing this feature, you can provide a clear and meaningful name for the field, making your queries more intuitive and readable.
    
    
    sql`lower(usersTable.name)`.as('lower_name')
    
    
    ... "usersTable"."name" as lower_name ...

## `sql.raw()`

There are cases where you may not need to create parameterized values from input or map tables/columns to escaped ones. Instead, you might simply want to generate queries as they are. For such situations, we provide the `sql.raw()` function.

The `sql.raw()` function allows you to include raw SQL statements within your queries without any additional processing or escaping. This can be useful when you have pre-constructed SQL statements or when you need to incorporate complex or dynamic SQL code directly into your queries.
    
    
    sql.raw(`select * from users where id = ${12}`);
    // vs
    sql`select * from users where id = ${12}`;
    
    
    select * from users where id = 12;
    --> vs
    select * from users where id = $1; --> [12]

You can also utilize `sql.raw()` within the sql function, enabling you to include any raw string without escaping it through the main `sql` template function.

By using `sql.raw()` inside the `sql` function, you can incorporate unescaped raw strings directly into your queries. This can be particularly useful when you have specific SQL code or expressions that should remain untouched by the template function’s automatic escaping or modification.
    
    
    sql`select * from ${usersTable} where id = ${12}`;
    // vs
    sql`select * from ${usersTable} where id = ${sql.raw(12)}`;
    
    
    select * from "users" where id = $1; --> [12]
    --> vs
    select * from "users" where id = 12;

## sql.fromList()

The `sql` template generates sql chunks, which are arrays of SQL parts that will be concatenated into the query and params after applying the SQL to the database or query in Drizzle.

In certain scenarios, you may need to aggregate these chunks into an array using custom business logic and then concatenate them into a single SQL statement that can be passed to the database or query. For such cases, the fromList function can be quite useful.

The fromList function allows you to combine multiple SQL chunks into a single SQL statement. You can use it to aggregate and concatenate the individual SQL parts according to your specific requirements and then obtain a unified SQL query that can be executed.
    
    
    const sqlChunks: SQL[] = [];
    
    sqlChunks.push(sql`select * from users`);
    
    // some logic
    
    sqlChunks.push(sql` where `);
    
    // some logic
    
    for (let i = 0; i < 5; i++) {
    	sqlChunks.push(sql`id = ${i}`);
    
    	if (i === 4) continue;
    	sqlChunks.push(sql` or `);
    }
    
    const finalSql: SQL = sql.fromList(sqlChunks)
    
    
    select * from users where id = $1 or id = $2 or id = $3 or id = $4 or id = $5; --> [0, 1, 2, 3, 4]

## sql.join()

Indeed, the `sql.join` function serves a similar purpose to the fromList helper. However, it provides additional flexibility when it comes to handling spaces between SQL chunks or specifying custom separators for concatenating the SQL chunks.

With `sql.join`, you can concatenate SQL chunks together using a specified separator. This separator can be any string or character that you want to insert between the chunks.

This is particularly useful when you have specific requirements for formatting or delimiting the SQL chunks. By specifying a custom separator, you can achieve the desired structure and formatting in the final SQL query.
    
    
    const sqlChunks: SQL[] = [];
    
    sqlChunks.push(sql`select * from users`);
    
    // some logic
    
    sqlChunks.push(sql`where`);
    
    // some logic
    
    for (let i = 0; i < 5; i++) {
    	sqlChunks.push(sql`id = ${i}`);
    
    if (i === 4) continue;
        sqlChunks.push(sql`or`);
    }
    
    const finalSql: SQL = sql.join(sqlChunks, sql.raw(' '));
    
    
    select * from users where id = $1 or id = $2 or id = $3 or id = $4 or id = $5; --> [0, 1, 2, 3, 4]

## sql.append()

If you have already generated SQL using the `sql` template, you can achieve the same behavior as `fromList` by using the append function to directly add a new chunk to the generated SQL.

By using the append function, you can dynamically add additional SQL chunks to the existing SQL string, effectively concatenating them together. This allows you to incorporate custom logic or business rules for aggregating the chunks into the final SQL query.
    
    
    const finalSql = sql`select * from users`;
    
    // some logic
    
    finalSql.append(sql` where `);
    
    // some logic
    
    for (let i = 0; i < 5; i++) {
    	finalSql.append(sql`id = ${i}`);
    
    	if (i === 4) continue;
    	finalSql.append(sql` or `);
    }
    
    
    select * from users where id = $1 or id = $2 or id = $3 or id = $4 or id = $5; --> [0, 1, 2, 3, 4]

## sql.empty()

By using sql.empty(), you can start with a blank SQL object and then dynamically append SQL chunks to it as needed. This allows you to construct the SQL query incrementally, applying custom logic or conditions to determine the contents of each chunk.

Once you have initialized the SQL object using sql.empty(), you can take advantage of the full range of sql template features such as parameterization, composition, and escaping. This empowers you to construct the SQL query in a flexible and controlled manner, adapting it to your specific requirements.
    
    
    const finalSql = sql.empty();
    
    // some logic
    
    finalSql.append(sql`select * from users`);
    
    // some logic
    
    finalSql.append(sql` where `);
    
    // some logic
    
    for (let i = 0; i < 5; i++) {
    	finalSql.append(sql`id = ${i}`);
    
    	if (i === 4) continue;
    	finalSql.append(sql` or `);
    }
    
    
    select * from users where id = $1 or id = $2 or id = $3 or id = $4 or id = $5; --> [0, 1, 2, 3, 4]

## Convert `sql` to string and params

In all the previous examples, you observed the usage of SQL template syntax in TypeScript along with the generated SQL output.

If you need to obtain the query string and corresponding parameters generated from the SQL template, you must specify the database dialect you intend to generate the query for. Different databases have varying syntax for parameterization and escaping, so selecting the appropriate dialect is crucial.

Once you have chosen the dialect, you can utilize the corresponding implementation’s functionality to convert the SQL template into the desired query string and parameter format. This ensures compatibility with the specific database system you are working with.

PostgreSQL

MySQL

SQLite
    
    
    import { PgDialect } from 'drizzle-orm/pg-core';
    
    const pgDialect = new PgDialect();
    pgDialect.sqlToQuery(sql`select * from ${usersTable} where ${usersTable.id} = ${12}`);
    
    
    select * from "users" where "users"."id" = $1; --> [ 12 ]
    
    
    import { MySqlDialect } from 'drizzle-orm/mysql-core';
    
    const mysqlDialect = new MySqlDialect();
    mysqlDialect.sqlToQuery(sql`select * from ${usersTable} where ${usersTable.id} = ${12}`);
    
    
    select * from `users` where `users`.`id` = ?; --> [ 12 ]
    
    
    import { SQLiteSyncDialect } from 'drizzle-orm/sqlite-core';
    
    const sqliteDialect = new SQLiteSyncDialect();
    sqliteDialect.sqlToQuery(sql`select * from ${usersTable} where ${usersTable.id} = ${12}`);
    
    
    select * from "users" where "users"."id" = ?; --> [ 12 ]

## `sql` select

You can use the sql functionality in partial select queries as well. Partial select queries allow you to retrieve specific fields or columns from a table rather than fetching the entire row.

For more detailed information about partial select queries, you can refer to the Core API documentation available at **[Core API docs](/docs/select#basic-and-partial-select)**.

**Select different custom fields from table**

Here you can see a usage for **[`sql<T>`](/docs/sql#sqlt)**, **[`sql``.mapWith()`](/docs/sql#sqlmapwith)** , **[`sql``.as<T>()`](/docs/sql#sqlast)**.
    
    
    import { sql } from 'drizzle-orm'
    import { usersTable } from 'schema'
    
    await db.select({
        id: usersTable.id,
        lowerName: sql<string>`lower(${usersTable.name})`,
        aliasedName: sql<string>`lower(${usersTable.name})`.as('aliased_column'),
        count: sql<number>`count(*)`.mapWith(Number) 
    }).from(usersTable)
    
    
    select `id`, lower(`name`), lower(`name`) as `aliased_column`, count(*) from `users`;

## `sql` in where

Indeed, Drizzle provides a set of available expressions that you can use within the sql template. However, it is true that databases often have a wider range of expressions available, including those provided through extensions or other means.

To ensure flexibility and enable you to utilize any expressions that are not natively supported by Drizzle, you have the freedom to write the SQL template directly using the sql function. This allows you to leverage the full power of SQL and incorporate any expressions or functionalities specific to your target database.

By using the sql template, you are not restricted to only the predefined expressions in Drizzle. Instead, you can express complex queries and incorporate any supported expressions that the underlying database system provides.

**Filtering by`id` but with sql**
    
    
    import { sql } from 'drizzle-orm'
    import { usersTable } from 'schema'
    
    const id = 77
    
    await db.select()
            .from(usersTable)
            .where(sql`${usersTable.id} = ${id}`)
    
    
    select * from "users" where "users"."id" = $1; --> [ 77 ]

**Advanced fulltext search where statement**
    
    
    import { sql } from 'drizzle-orm'
    import { usersTable } from 'schema'
    
    const searchParam = "Ale"
    
    await db.select()
            .from(usersTable)
            .where(sql`to_tsvector('simple', ${usersTable.name}) @@ to_tsquery('simple', ${searchParam})`)
    
    
    select * from "users" where to_tsvector('simple', "users"."name") @@ to_tsquery('simple', '$1'); --> [ "Ale" ]

## `sql` in orderBy

The `sql` template can indeed be used in the ORDER BY clause when you need specific functionality for ordering that is not available in Drizzle, but you prefer not to resort to raw SQL.
    
    
    import { sql } from 'drizzle-orm'
    import { usersTable } from 'schema'
    
    await db.select().from(usersTable).orderBy(sql`${usersTable.id} desc nulls first`)
    
    
    select * from "users" order by "users"."id" desc nulls first;

## `sql` in having and groupBy

The `sql` template can indeed be used in the HAVING and GROUP BY clauses when you need specific functionality for ordering that is not available in Drizzle, but you prefer not to resort to raw SQL.
    
    
    import { sql } from 'drizzle-orm'
    import { usersTable } from 'schema'
    
    await db.select({ 
        projectId: usersTable.projectId,
        count: sql<number>`count(${usersTable.id})`.mapWith(Number)
    }).from(usersTable)
        .groupBy(sql`${usersTable.projectId}`)
        .having(sql`count(${usersTable.id}) > 300`)
    
    
    select "project_id", count("users"."id") from users group by "users"."project_id" having count("users"."id") > 300;