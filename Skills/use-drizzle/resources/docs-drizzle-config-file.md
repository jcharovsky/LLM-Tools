# drizzle-config-file

**Source URL:** https://orm.drizzle.team/docs/drizzle-config-file

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

Multiple configuration files  Migrations folder 

dialect  schema  out  driver 

dbCredentials  migrations  introspect 

tablesFilter  schemaFilter  extensionsFilters 

entities 

strict  verbose  breakpoints 

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

[ v1.0 75% ](/roadmap)

[ Benchmarks ](/benchmarks) [ Extension ](https://driz.link/extension) [ Studio ](/drizzle-studio/overview) [ Studio Package ](https://github.com/drizzle-team/drizzle-studio-npm) [ Gateway ](https://gateway.drizzle.team) [ Drizzle Run ](https://drizzle.run)

Our goodies!

[ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMTU0IiB2aWV3Qm94PSIwIDAgMjAwIDE1NCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICA8cGF0aCBkPSJNMCA2OC42QzAgOTAuNCAxNy44NDk5IDEwOCAzOS45NTk0IDEwOEM2MS44NjYxIDEwOCA3OS45MTg5IDkwLjQgNzkuOTE4OSA2OC42Qzc5LjkxODkgNDcgNjEuODY2MSAyOS4yIDM5Ljk1OTQgMjkuMkMxNy44NDk5IDI5LjIgMCA0NyAwIDY4LjZaTTE3MS4xOTcgMTRDMTcxLjE5NyA2LjYgMTc3LjQ4NSAwIDE4NS4zOTYgMEMxOTMuMzA2IDAgMjAwIDYuNiAyMDAgMTRWOTRDMjAwIDEwMS40IDE5My4zMDYgMTA4IDE4NS4zOTYgMTA4QzE3Ny40ODUgMTA4IDE3MS4xOTcgMTAxLjQgMTcxLjE5NyA5NFYxNFpNMTAuNTQ3NyAxMjcuNkMxMi4xNzA0IDE0MS40IDIzLjczMjMgMTU0IDM5Ljk1OTQgMTU0QzU1Ljk4MzggMTU0IDY3Ljk1MTMgMTQxLjQgNjkuNTc0IDEyNy42QzcxLjgwNTMgMTA3LjYgNTMuMzQ2OSAxMTQuMiAzOS45NTk0IDExNC4yQzI2LjU3MiAxMTQuMiA4LjMxNjQzIDEwNy42IDEwLjU0NzcgMTI3LjZaTTEzOS4zNTEgNzQuMkMxNDAuNzcxIDcxIDE0NC40MjIgNjkgMTUxLjUyMSA2OUMxNjIuNjc3IDY4LjggMTY3LjE0IDYxLjYgMTYxLjI1OCA1MC4yQzE1Ny4yMDEgNDIuNCAxNTAuOTEzIDM2LjQgMTQyLjM5NCAzMi42QzEyMi4zMTIgMjMuOCA5OC41ODAxIDMyLjggODkuNjU1MiA1Mi42QzgwLjczMDIgNzIuMiA4OS42NTUyIDk1LjYgMTA5LjkzOSAxMDQuNkMxMTguNDU4IDEwOC4yIDEyNi45NzggMTA4LjggMTM1LjcgMTA2LjZDMTQ4LjI3NiAxMDMuMiAxNTAuOTEzIDk1IDE0My40MDggODYuOEMxMzguNzQyIDgxLjQgMTM3LjcyOCA3Ny42IDEzOS4zNTEgNzQuMloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl81OV80NikiLz4KICAgICAgICAgIDxkZWZzPgogICAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzU5XzQ2IiB4MT0iMjUwLjI1NCIgeTE9IjAiIHgyPSIyNTAuMjU0IiB5Mj0iMTU0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CiAgICAgICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjRkZDODAwIi8+CiAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjQ4MDAiLz4KICAgICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICAgICAgICA8L2RlZnM+CiAgICAgICAgPC9zdmc+) ![Gel](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMTU0IiB2aWV3Qm94PSIwIDAgMjAwIDE1NCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICA8cGF0aCBkPSJNMCA2OC42QzAgOTAuNCAxNy44NDk5IDEwOCAzOS45NTk0IDEwOEM2MS44NjYxIDEwOCA3OS45MTg5IDkwLjQgNzkuOTE4OSA2OC42Qzc5LjkxODkgNDcgNjEuODY2MSAyOS4yIDM5Ljk1OTQgMjkuMkMxNy44NDk5IDI5LjIgMCA0NyAwIDY4LjZaTTE3MS4xOTcgMTRDMTcxLjE5NyA2LjYgMTc3LjQ4NSAwIDE4NS4zOTYgMEMxOTMuMzA2IDAgMjAwIDYuNiAyMDAgMTRWOTRDMjAwIDEwMS40IDE5My4zMDYgMTA4IDE4NS4zOTYgMTA4QzE3Ny40ODUgMTA4IDE3MS4xOTcgMTAxLjQgMTcxLjE5NyA5NFYxNFpNMTAuNTQ3NyAxMjcuNkMxMi4xNzA0IDE0MS40IDIzLjczMjMgMTU0IDM5Ljk1OTQgMTU0QzU1Ljk4MzggMTU0IDY3Ljk1MTMgMTQxLjQgNjkuNTc0IDEyNy42QzcxLjgwNTMgMTA3LjYgNTMuMzQ2OSAxMTQuMiAzOS45NTk0IDExNC4yQzI2LjU3MiAxMTQuMiA4LjMxNjQzIDEwNy42IDEwLjU0NzcgMTI3LjZaTTEzOS4zNTEgNzQuMkMxNDAuNzcxIDcxIDE0NC40MjIgNjkgMTUxLjUyMSA2OUMxNjIuNjc3IDY4LjggMTY3LjE0IDYxLjYgMTYxLjI1OCA1MC4yQzE1Ny4yMDEgNDIuNCAxNTAuOTEzIDM2LjQgMTQyLjM5NCAzMi42QzEyMi4zMTIgMjMuOCA5OC41ODAxIDMyLjggODkuNjU1MiA1Mi42QzgwLjczMDIgNzIuMiA4OS42NTUyIDk1LjYgMTA5LjkzOSAxMDQuNkMxMTguNDU4IDEwOC4yIDEyNi45NzggMTA4LjggMTM1LjcgMTA2LjZDMTQ4LjI3NiAxMDMuMiAxNTAuOTEzIDk1IDE0My40MDggODYuOEMxMzguNzQyIDgxLjQgMTM3LjcyOCA3Ny42IDEzOS4zNTEgNzQuMloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl81OV80NikiLz4KICAgICAgICAgIDxkZWZzPgogICAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzU5XzQ2IiB4MT0iMjUwLjI1NCIgeTE9IjAiIHgyPSIyNTAuMjU0IiB5Mj0iMTU0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CiAgICAgICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjRkZDODAwIi8+CiAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjQ4MDAiLz4KICAgICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICAgICAgICA8L2RlZnM+CiAgICAgICAgPC9zdmc+) ](https://driz.link/edgedb)

[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Turso](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) 🚀 Drizzle is giving you 10% off Turso Scaler and Pro for 1 Year 🚀 ](https://driz.link/turso)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Payload](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/payload)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMDU0LjM1IDM3OS4xNEMxMDU0LjI0IDQ2OS4xMzcgMTAxOC4zNSA1NTUuNDA4IDk1NC41NiA2MTguOTcxVjYxOC45NjRMNzI4LjI3MyA4NDQuNDVDNzIwLjQzMiA4NTIuMjcgNzA3LjY5MyA4NTIuMjkgNzAwLjM0NiA4NDQuMDFDNjQ1LjMzMSA3ODIuMDE4IDYxNC43NTggNzAxLjgzOCA2MTQuODU2IDYxOC41MzVDNjE0Ljk2MSA1MjguNTM4IDY1MC44NTYgNDQyLjI2OCA3MTQuNjQzIDM3OC43MDVMNzE0LjY1IDM3OC43MTFMOTIxLjM5IDE3Mi42OTdDOTQwLjAyIDE1NC4xMjggOTcwLjUxIDE1My45OTYgOTg2LjMxIDE3NS4wMjJDMTAzMC4zIDIzMy41NDcgMTA1NC40NCAzMDUuMTEgMTA1NC4zNSAzNzkuMTRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMjAyXzcxKSIvPjxwYXRoIGQ9Ik0yNDQuNzg2IDYyMC4zNDVDMTgwLjk5OSA1NTYuNzgyIDE0NS4xMDUgNDcwLjUxMiAxNDUgMzgwLjUxNUMxNDQuOTEzIDMwNi40ODUgMTY5LjA0OCAyMzQuOTIxIDIxMy4wMzUgMTc2LjM5NkMyMjguODM4IDE1NS4zNyAyNTkuMzI4IDE1NS41MDMgMjc3Ljk2MyAxNzQuMDcyTDQ4NC43MDMgMzgwLjA4OEw0ODQuNzEgMzgwLjA4MUM1NDguNDk3IDQ0My42NDUgNTg0LjM5MSA1MjkuOTE0IDU4NC40OTcgNjE5LjkxMkM1ODQuNTk0IDcwMy4yMTQgNTU0LjAyMiA3ODMuMzk1IDQ5OS4wMDcgODQ1LjM4QzQ5MS42NTkgODUzLjY2IDQ3OC45MiA4NTMuNjQgNDcxLjA4IDg0NS44M0wyNDQuNzkzIDYyMC4zMzlMMjQ0Ljc4NiA2MjAuMzQ1WiIgZmlsbD0idXJsKCNwYWludDFfbGluZWFyXzIwMl83MSkiLz48cGF0aCBkPSJNOTQ2LjA1IDEwMjMuODNDOTI5LjQyIDEwNDQuMjIgODk5LjAyIDEwNDQuMDQgODgwLjQyIDEwMjUuNDJMNzUyLjcyNyA4OTcuNThDNzQ0Ljg5MSA4ODkuNzMgNzQ0LjkwNiA4NzcuMDIgNzUyLjc2IDg2OS4xOUw5NjQuODUgNjU3Ljg0OEM5NzIuNjkgNjUwLjAzNSA5ODUuNDggNjQ5Ljk4OSA5OTIuMzkgNjU4LjYzMkMxMDI5LjIgNzA0LjYyOCAxMDQzLjY4IDc2OC4xOTggMTAzMi43NCA4MzguMThDMTAyMi43MiA5MDIuMjQgOTkyLjA4IDk2Ny4zNyA5NDYuMDUgMTAyMy44M1oiIGZpbGw9InVybCgjcGFpbnQyX2xpbmVhcl8yMDJfNzEpIi8+PHBhdGggZD0iTTMxOC45MzEgMTAyNi44QzMwMC4zMzcgMTA0NS40MSAyNjkuOTI5IDEwNDUuNTkgMjUzLjMwNSAxMDI1LjJDMjA3LjI2OSA5NjguNzQgMTc2LjYzMyA5MDMuNjIgMTY2LjYxNyA4MzkuNTZDMTU1LjY3NSA3NjkuNTcxIDE3MC4xNDkgNzA2LjAwMSAyMDYuOTU5IDY2MC4wMDVDMjEzLjg3NiA2NTEuMzYzIDIyNi42NjMgNjUxLjQwOCAyMzQuNTA0IDY1OS4yMjFMNDQ2LjU5NSA4NzAuNTdDNDU0LjQ0OSA4NzguMzkgNDU0LjQ2NCA4OTEuMTEgNDQ2LjYyOSA4OTguOTVMMzE4LjkzMSAxMDI2LjhaIiBmaWxsPSJ1cmwoI3BhaW50M19saW5lYXJfMjAyXzcxKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU4Ljk5OSIgeDI9IjU5OS42NzYiIHkyPSI4NTkuNCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiM5Rjg3RkYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM4NTY2RkYiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU5IiB4Mj0iNTk5LjY3NiIgeTI9Ijg1OS40IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzlGODdGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg1NjZGRiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzIwMl83MSIgeDE9IjU5OS42NzYiIHkxPSI2NDMuNzY2IiB4Mj0iNTk5LjY3NiIgeTI9IjEwMzkuOTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjREU5OUY2Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRDY2OUZDIi8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9InBhaW50M19saW5lYXJfMjAyXzcxIiB4MT0iNTk5LjY3NiIgeTE9IjY0My43NjYiIHgyPSI1OTkuNjc2IiB5Mj0iMTAzOS45MyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNERTk5RjYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNENjY5RkMiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=) ![Xata](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMDU0LjM1IDM3OS4xNEMxMDU0LjI0IDQ2OS4xMzcgMTAxOC4zNSA1NTUuNDA4IDk1NC41NiA2MTguOTcxVjYxOC45NjRMNzI4LjI3MyA4NDQuNDVDNzIwLjQzMiA4NTIuMjcgNzA3LjY5MyA4NTIuMjkgNzAwLjM0NiA4NDQuMDFDNjQ1LjMzMSA3ODIuMDE4IDYxNC43NTggNzAxLjgzOCA2MTQuODU2IDYxOC41MzVDNjE0Ljk2MSA1MjguNTM4IDY1MC44NTYgNDQyLjI2OCA3MTQuNjQzIDM3OC43MDVMNzE0LjY1IDM3OC43MTFMOTIxLjM5IDE3Mi42OTdDOTQwLjAyIDE1NC4xMjggOTcwLjUxIDE1My45OTYgOTg2LjMxIDE3NS4wMjJDMTAzMC4zIDIzMy41NDcgMTA1NC40NCAzMDUuMTEgMTA1NC4zNSAzNzkuMTRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMjAyXzcxKSIvPjxwYXRoIGQ9Ik0yNDQuNzg2IDYyMC4zNDVDMTgwLjk5OSA1NTYuNzgyIDE0NS4xMDUgNDcwLjUxMiAxNDUgMzgwLjUxNUMxNDQuOTEzIDMwNi40ODUgMTY5LjA0OCAyMzQuOTIxIDIxMy4wMzUgMTc2LjM5NkMyMjguODM4IDE1NS4zNyAyNTkuMzI4IDE1NS41MDMgMjc3Ljk2MyAxNzQuMDcyTDQ4NC43MDMgMzgwLjA4OEw0ODQuNzEgMzgwLjA4MUM1NDguNDk3IDQ0My42NDUgNTg0LjM5MSA1MjkuOTE0IDU4NC40OTcgNjE5LjkxMkM1ODQuNTk0IDcwMy4yMTQgNTU0LjAyMiA3ODMuMzk1IDQ5OS4wMDcgODQ1LjM4QzQ5MS42NTkgODUzLjY2IDQ3OC45MiA4NTMuNjQgNDcxLjA4IDg0NS44M0wyNDQuNzkzIDYyMC4zMzlMMjQ0Ljc4NiA2MjAuMzQ1WiIgZmlsbD0idXJsKCNwYWludDFfbGluZWFyXzIwMl83MSkiLz48cGF0aCBkPSJNOTQ2LjA1IDEwMjMuODNDOTI5LjQyIDEwNDQuMjIgODk5LjAyIDEwNDQuMDQgODgwLjQyIDEwMjUuNDJMNzUyLjcyNyA4OTcuNThDNzQ0Ljg5MSA4ODkuNzMgNzQ0LjkwNiA4NzcuMDIgNzUyLjc2IDg2OS4xOUw5NjQuODUgNjU3Ljg0OEM5NzIuNjkgNjUwLjAzNSA5ODUuNDggNjQ5Ljk4OSA5OTIuMzkgNjU4LjYzMkMxMDI5LjIgNzA0LjYyOCAxMDQzLjY4IDc2OC4xOTggMTAzMi43NCA4MzguMThDMTAyMi43MiA5MDIuMjQgOTkyLjA4IDk2Ny4zNyA5NDYuMDUgMTAyMy44M1oiIGZpbGw9InVybCgjcGFpbnQyX2xpbmVhcl8yMDJfNzEpIi8+PHBhdGggZD0iTTMxOC45MzEgMTAyNi44QzMwMC4zMzcgMTA0NS40MSAyNjkuOTI5IDEwNDUuNTkgMjUzLjMwNSAxMDI1LjJDMjA3LjI2OSA5NjguNzQgMTc2LjYzMyA5MDMuNjIgMTY2LjYxNyA4MzkuNTZDMTU1LjY3NSA3NjkuNTcxIDE3MC4xNDkgNzA2LjAwMSAyMDYuOTU5IDY2MC4wMDVDMjEzLjg3NiA2NTEuMzYzIDIyNi42NjMgNjUxLjQwOCAyMzQuNTA0IDY1OS4yMjFMNDQ2LjU5NSA4NzAuNTdDNDU0LjQ0OSA4NzguMzkgNDU0LjQ2NCA4OTEuMTEgNDQ2LjYyOSA4OTguOTVMMzE4LjkzMSAxMDI2LjhaIiBmaWxsPSJ1cmwoI3BhaW50M19saW5lYXJfMjAyXzcxKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU4Ljk5OSIgeDI9IjU5OS42NzYiIHkyPSI4NTkuNCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiM5Rjg3RkYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM4NTY2RkYiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU5IiB4Mj0iNTk5LjY3NiIgeTI9Ijg1OS40IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzlGODdGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg1NjZGRiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzIwMl83MSIgeDE9IjU5OS42NzYiIHkxPSI2NDMuNzY2IiB4Mj0iNTk5LjY3NiIgeTI9IjEwMzkuOTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjREU5OUY2Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRDY2OUZDIi8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9InBhaW50M19saW5lYXJfMjAyXzcxIiB4MT0iNTk5LjY3NiIgeTE9IjY0My43NjYiIHgyPSI1OTkuNjc2IiB5Mj0iMTAzOS45MyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNERTk5RjYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNENjY5RkMiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=) ](https://driz.link/xataio)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Neon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/neon)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Nuxt](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://hub.nuxt.com/?utm_source=drizzle-docs)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQiIGhlaWdodD0iNTQiIHZpZXdCb3g9IjAgMCA1NCA1NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQ4LjQ2MDggMjdDNDguNDYwOCAzOC44Nzc5IDM4Ljg0IDQ4LjUgMjYuOTgwNCA0OC41QzE1LjEyMDkgNDguNSA1LjUgMzguODc3OSA1LjUgMjdDNS41IDE1LjEyMjEgMTUuMTIwOSA1LjUgMjYuOTgwNCA1LjVDMzguODQgNS41IDQ4LjQ2MDggMTUuMTIyMSA0OC40NjA4IDI3WiIgZmlsbD0iI0NGRTJGOCIgc3Ryb2tlPSIjQ0ZFMkY4IiBzdHJva2Utd2lkdGg9IjExIj48L3BhdGg+CjxwYXRoIGQ9Ik0yNC42Nzk2IDEyLjQ3NzVDMjcuMTkxNiA4LjM0MDQ5IDMyLjU3OTEgNy4wMjQ1NSAzNi43MTI4IDkuNTM4MjFDNDAuODQ2NiAxMi4wNTE5IDQyLjE2MTIgMTcuNDQzMyAzOS42NDkyIDIxLjU4MDNMMzEuNjcyNCAzNC43MTY5QzI5LjE2MDMgMzguODUzOCAyMy43NzI4IDQwLjE2OTggMTkuNjM5MSAzNy42NTYxQzE1LjUwNTMgMzUuMTQyNSAxNC4xOTA3IDI5Ljc1MSAxNi43MDI3IDI1LjYxNDFMMjQuNjc5NiAxMi40Nzc1WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zMC4yODkyIDMzLjg3NThMMzguMjY2IDIwLjczOTJDNDAuMzEzOCAxNy4zNjY3IDM5LjI0MjEgMTIuOTcxNiAzNS44NzIzIDEwLjkyMjVDMzIuNTAyNSA4Ljg3MzM1IDI4LjExMDYgOS45NDYxMSAyNi4wNjI3IDEzLjMxODZMMTguMDg1OSAyNi40NTUyQzE2LjAzODEgMjkuODI3NiAxNy4xMDk4IDM0LjIyMjcgMjAuNDc5NiAzNi4yNzE4QzIzLjg0OTUgMzguMzIxIDI4LjI0MTQgMzcuMjQ4MiAzMC4yODkyIDMzLjg3NThaTTM2LjcxMjggOS41MzgyMUMzMi41NzkxIDcuMDI0NTUgMjcuMTkxNiA4LjM0MDQ5IDI0LjY3OTYgMTIuNDc3NUwxNi43MDI3IDI1LjYxNDFDMTQuMTkwNyAyOS43NTEgMTUuNTA1MyAzNS4xNDI1IDE5LjYzOTEgMzcuNjU2MUMyMy43NzI4IDQwLjE2OTggMjkuMTYwMyAzOC44NTM4IDMxLjY3MjQgMzQuNzE2OUwzOS42NDkyIDIxLjU4MDNDNDIuMTYxMiAxNy40NDMzIDQwLjg0NjYgMTIuMDUxOSAzNi43MTI4IDkuNTM4MjFaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMxLjQzODkgMTkuNjczN0MzMS44MTcgMTkuOTEyMiAzMS45MzA0IDIwLjQxMjIgMzEuNjkyMSAyMC43OTA3TDE2LjExOTIgNDUuNTIzMkMxNS44ODEgNDUuOTAxNyAxNS4zODEzIDQ2LjAxNTEgMTUuMDAzMSA0NS43NzY3QzE0LjYyNSA0NS41MzgzIDE0LjUxMTYgNDUuMDM4MiAxNC43NDk5IDQ0LjY1OThMMzAuMzIyOCAxOS45MjcyQzMwLjU2MSAxOS41NDg4IDMxLjA2MDcgMTkuNDM1MyAzMS40Mzg5IDE5LjY3MzdaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMzLjEwNTEgMzAuOTk0OUMzMy4xNzc1IDMxLjM2MDYgMzIuOTQgMzEuNzE1OCAzMi41NzQ2IDMxLjc4ODJDMjcuNzM0NyAzMi43NDc4IDI1LjMxMyAzMi4xMzk0IDI0LjI2ODcgMzEuNDA0NEMyMy45NjQxIDMxLjE5IDIzLjg5MDggMzAuNzY4OSAyNC4xMDUgMzAuNDY0QzI0LjMxOTMgMzAuMTU5IDI0Ljc0IDMwLjA4NTcgMjUuMDQ0NyAzMC4zMDAxQzI1LjYyNzEgMzAuNzEgMjcuNTgxMSAzMS40MDIxIDMyLjMxMjYgMzAuNDY0QzMyLjY3NzkgMzAuMzkxNSAzMy4wMzI4IDMwLjYyOTIgMzMuMTA1MSAzMC45OTQ5WiIgZmlsbD0iYmxhY2siPjwvcGF0aD4KPC9zdmc+) ![SQLite Cloud](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQiIGhlaWdodD0iNTQiIHZpZXdCb3g9IjAgMCA1NCA1NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQ4LjQ2MDggMjdDNDguNDYwOCAzOC44Nzc5IDM4Ljg0IDQ4LjUgMjYuOTgwNCA0OC41QzE1LjEyMDkgNDguNSA1LjUgMzguODc3OSA1LjUgMjdDNS41IDE1LjEyMjEgMTUuMTIwOSA1LjUgMjYuOTgwNCA1LjVDMzguODQgNS41IDQ4LjQ2MDggMTUuMTIyMSA0OC40NjA4IDI3WiIgZmlsbD0iI0NGRTJGOCIgc3Ryb2tlPSIjQ0ZFMkY4IiBzdHJva2Utd2lkdGg9IjExIj48L3BhdGg+CjxwYXRoIGQ9Ik0yNC42Nzk2IDEyLjQ3NzVDMjcuMTkxNiA4LjM0MDQ5IDMyLjU3OTEgNy4wMjQ1NSAzNi43MTI4IDkuNTM4MjFDNDAuODQ2NiAxMi4wNTE5IDQyLjE2MTIgMTcuNDQzMyAzOS42NDkyIDIxLjU4MDNMMzEuNjcyNCAzNC43MTY5QzI5LjE2MDMgMzguODUzOCAyMy43NzI4IDQwLjE2OTggMTkuNjM5MSAzNy42NTYxQzE1LjUwNTMgMzUuMTQyNSAxNC4xOTA3IDI5Ljc1MSAxNi43MDI3IDI1LjYxNDFMMjQuNjc5NiAxMi40Nzc1WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zMC4yODkyIDMzLjg3NThMMzguMjY2IDIwLjczOTJDNDAuMzEzOCAxNy4zNjY3IDM5LjI0MjEgMTIuOTcxNiAzNS44NzIzIDEwLjkyMjVDMzIuNTAyNSA4Ljg3MzM1IDI4LjExMDYgOS45NDYxMSAyNi4wNjI3IDEzLjMxODZMMTguMDg1OSAyNi40NTUyQzE2LjAzODEgMjkuODI3NiAxNy4xMDk4IDM0LjIyMjcgMjAuNDc5NiAzNi4yNzE4QzIzLjg0OTUgMzguMzIxIDI4LjI0MTQgMzcuMjQ4MiAzMC4yODkyIDMzLjg3NThaTTM2LjcxMjggOS41MzgyMUMzMi41NzkxIDcuMDI0NTUgMjcuMTkxNiA4LjM0MDQ5IDI0LjY3OTYgMTIuNDc3NUwxNi43MDI3IDI1LjYxNDFDMTQuMTkwNyAyOS43NTEgMTUuNTA1MyAzNS4xNDI1IDE5LjYzOTEgMzcuNjU2MUMyMy43NzI4IDQwLjE2OTggMjkuMTYwMyAzOC44NTM4IDMxLjY3MjQgMzQuNzE2OUwzOS42NDkyIDIxLjU4MDNDNDIuMTYxMiAxNy40NDMzIDQwLjg0NjYgMTIuMDUxOSAzNi43MTI4IDkuNTM4MjFaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMxLjQzODkgMTkuNjczN0MzMS44MTcgMTkuOTEyMiAzMS45MzA0IDIwLjQxMjIgMzEuNjkyMSAyMC43OTA3TDE2LjExOTIgNDUuNTIzMkMxNS44ODEgNDUuOTAxNyAxNS4zODEzIDQ2LjAxNTEgMTUuMDAzMSA0NS43NzY3QzE0LjYyNSA0NS41MzgzIDE0LjUxMTYgNDUuMDM4MiAxNC43NDk5IDQ0LjY1OThMMzAuMzIyOCAxOS45MjcyQzMwLjU2MSAxOS41NDg4IDMxLjA2MDcgMTkuNDM1MyAzMS40Mzg5IDE5LjY3MzdaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMzLjEwNTEgMzAuOTk0OUMzMy4xNzc1IDMxLjM2MDYgMzIuOTQgMzEuNzE1OCAzMi41NzQ2IDMxLjc4ODJDMjcuNzM0NyAzMi43NDc4IDI1LjMxMyAzMi4xMzk0IDI0LjI2ODcgMzEuNDA0NEMyMy45NjQxIDMxLjE5IDIzLjg5MDggMzAuNzY4OSAyNC4xMDUgMzAuNDY0QzI0LjMxOTMgMzAuMTU5IDI0Ljc0IDMwLjA4NTcgMjUuMDQ0NyAzMC4zMDAxQzI1LjYyNzEgMzAuNzEgMjcuNTgxMSAzMS40MDIxIDMyLjMxMjYgMzAuNDY0QzMyLjY3NzkgMzAuMzkxNSAzMy4wMzI4IDMwLjYyOTIgMzMuMTA1MSAzMC45OTQ5WiIgZmlsbD0iYmxhY2siPjwvcGF0aD4KPC9zdmc+) ](https://driz.link/sqlitecloud)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Upstash](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/upstash)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Lokalise](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/lokalise)[ ![](data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJBcnR3b3JrIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNzkzLjggODcxLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDc5My44IDg3MS41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0Y1NjQwQzt9Cjwvc3R5bGU+CjxnPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM5Ni45LDM1Ni4xSDIyNy4yYy0xNi42LDAtMzAtMTMuNC0zMC0zMHYtOTkuOGMwLTE2LjYsMTMuNC0zMCwzMC0zMGgxMzkuN2MxNi42LDAsMzAsMTMuNCwzMCwzMFYzNTYuMXoiLz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik01NjYuNiw1MTUuOEgzOTYuOVYzNTYuMWgxNjkuN2MxNi41LDAsMjkuOSwxMy40LDI5LjksMjkuOXY5OS44QzU5Ni41LDUwMi40LDU4My4xLDUxNS44LDU2Ni42LDUxNS44eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM2Ni45LDY3NS42SDIyNy4yYy0xNi41LDAtMjkuOS0xMy40LTI5LjktMjkuOXYtOTkuOGMwLTE2LjUsMTMuNC0yOS45LDI5LjktMjkuOWgxNjkuN3YxMjkuOAoJCUMzOTYuOSw2NjIuMSwzODMuNSw2NzUuNiwzNjYuOSw2NzUuNnoiLz4KPC9nPgo8L3N2Zz4=) ![Replit](data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJBcnR3b3JrIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNzkzLjggODcxLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDc5My44IDg3MS41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0Y1NjQwQzt9Cjwvc3R5bGU+CjxnPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM5Ni45LDM1Ni4xSDIyNy4yYy0xNi42LDAtMzAtMTMuNC0zMC0zMHYtOTkuOGMwLTE2LjYsMTMuNC0zMCwzMC0zMGgxMzkuN2MxNi42LDAsMzAsMTMuNCwzMCwzMFYzNTYuMXoiLz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik01NjYuNiw1MTUuOEgzOTYuOVYzNTYuMWgxNjkuN2MxNi41LDAsMjkuOSwxMy40LDI5LjksMjkuOXY5OS44QzU5Ni41LDUwMi40LDU4My4xLDUxNS44LDU2Ni42LDUxNS44eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM2Ni45LDY3NS42SDIyNy4yYy0xNi41LDAtMjkuOS0xMy40LTI5LjktMjkuOXYtOTkuOGMwLTE2LjUsMTMuNC0yOS45LDI5LjktMjkuOWgxNjkuN3YxMjkuOAoJCUMzOTYuOSw2NjIuMSwzODMuNSw2NzUuNiwzNjYuOSw2NzUuNnoiLz4KPC9nPgo8L3N2Zz4=) ](https://driz.link/replit)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Sentry](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/sentry)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQuNzIwNDcgMEMyLjExMzQ0IDAgMCAyLjExMzQ0IDAgNC43MjA0N1YxOS4yNzk1QzAgMjEuODg2NiAyLjExMzQ0IDI0IDQuNzIwNDcgMjRIMTkuMjc5NUMyMS44ODY2IDI0IDI0IDIxLjg4NjYgMjQgMTkuMjc5NVY0LjcyMDQ3QzI0IDIuMTEzNDQgMjEuODg2NiAwIDE5LjI3OTUgMEg0LjcyMDQ3Wk05LjMwMjA0IDUuMDE1NjNWNy44NDM2N0g2Ljc0OTk4VjEwLjMyNjhDNi43NDk5OCAxMC44NDg3IDYuOTQzNzMgMTEuMDEzNCA3LjA2OTUxIDExLjEyMDRDNy4xMDI4NSAxMS4xNDg3IDcuMTMxMzkgMTEuMTczIDcuMTUwMzEgMTEuMTk4OEw5LjI3NzAyIDEzLjM4MTRINi43NDk5OFYxNi4xNzk4SDkuMjc3MDJWMTkuMDA3OEgxNC43MDYzVjE2LjE3OThIOS4yNzcwMlYxMy4zODE0SDE0LjAzNUMxNC42OTM4IDEzLjM4MTQgMTQuNjkzOCAxNC4xNzk1IDE0LjY5MzggMTQuNTQ0MVYxNi4xNzk4SDE3LjI0NThWMTMuNjk2N0MxNy4yNDU4IDEzLjE3NDggMTcuMDUyMSAxMy4wMTAxIDE2LjkyNjMgMTIuOTAzMUMxNi44OTMgMTIuODc0NyAxNi44NjQ0IDEyLjg1MDUgMTYuODQ1NSAxMi44MjQ3TDE0LjY5MzggMTAuNjQyMUgxNy4yNUwxNy4yNDU4IDcuODQzNjdIMTQuNzA2M0wxNC42OTM4IDEwLjY0MjFIOS45NjA4OEM5LjMwMjA0IDEwLjY0MjEgOS4zMDIwNCA5Ljg0Mzk1IDkuMzAyMDQgOS40NzkzNVY3Ljg0MzY3SDE0LjcwNjNWNS4wMTU2M0g5LjMwMjA0WiIgZmlsbD0iI0Y5NzMxNiIvPjwvc3ZnPg==) ![Sevalla](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQuNzIwNDcgMEMyLjExMzQ0IDAgMCAyLjExMzQ0IDAgNC43MjA0N1YxOS4yNzk1QzAgMjEuODg2NiAyLjExMzQ0IDI0IDQuNzIwNDcgMjRIMTkuMjc5NUMyMS44ODY2IDI0IDI0IDIxLjg4NjYgMjQgMTkuMjc5NVY0LjcyMDQ3QzI0IDIuMTEzNDQgMjEuODg2NiAwIDE5LjI3OTUgMEg0LjcyMDQ3Wk05LjMwMjA0IDUuMDE1NjNWNy44NDM2N0g2Ljc0OTk4VjEwLjMyNjhDNi43NDk5OCAxMC44NDg3IDYuOTQzNzMgMTEuMDEzNCA3LjA2OTUxIDExLjEyMDRDNy4xMDI4NSAxMS4xNDg3IDcuMTMxMzkgMTEuMTczIDcuMTUwMzEgMTEuMTk4OEw5LjI3NzAyIDEzLjM4MTRINi43NDk5OFYxNi4xNzk4SDkuMjc3MDJWMTkuMDA3OEgxNC43MDYzVjE2LjE3OThIOS4yNzcwMlYxMy4zODE0SDE0LjAzNUMxNC42OTM4IDEzLjM4MTQgMTQuNjkzOCAxNC4xNzk1IDE0LjY5MzggMTQuNTQ0MVYxNi4xNzk4SDE3LjI0NThWMTMuNjk2N0MxNy4yNDU4IDEzLjE3NDggMTcuMDUyMSAxMy4wMTAxIDE2LjkyNjMgMTIuOTAzMUMxNi44OTMgMTIuODc0NyAxNi44NjQ0IDEyLjg1MDUgMTYuODQ1NSAxMi44MjQ3TDE0LjY5MzggMTAuNjQyMUgxNy4yNUwxNy4yNDU4IDcuODQzNjdIMTQuNzA2M0wxNC42OTM4IDEwLjY0MjFIOS45NjA4OEM5LjMwMjA0IDEwLjY0MjEgOS4zMDIwNCA5Ljg0Mzk1IDkuMzAyMDQgOS40NzkzNVY3Ljg0MzY3SDE0LjcwNjNWNS4wMTU2M0g5LjMwMjA0WiIgZmlsbD0iI0Y5NzMxNiIvPjwvc3ZnPg==) ](https://driz.link/sevalla)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![GibsonAI](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/gibsonai)

Product by Drizzle Team 

[ One Dollar Stats $1 per mo web analytics christmas   
deal  ](https://driz.link/onedollarstats)

# Drizzle Kit configuration file

This guide assumes familiarity with: 

  * Get started with Drizzle and `drizzle-kit` \- [read here](/docs/get-started)
  * Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration)
  * Database connection basics - [read here](/docs/connect-overview)
  * Drizzle migrations fundamentals - [read here](/docs/migrations)
  * Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file)



Drizzle Kit lets you declare configuration options in `TypeScript` or `JavaScript` configuration files.
    
    
    📦 <project root>
     ├ ...
     ├ 📂 drizzle
     ├ 📂 src
     ├ 📜 drizzle.config.ts
     └ 📜 package.json

drizzle.config.ts

drizzle.config.js
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "postgresql",
      schema: "./src/schema.ts",
      out: "./drizzle",
    });
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "postgresql",
      schema: "./src/schema.ts",
      out: "./drizzle",
    });

Example of an extended config file
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      out: "./drizzle",
      dialect: "postgresql",
      schema: "./src/schema.ts",
    
      driver: "pglite",
      dbCredentials: {
        url: "./database/",
      },
    
      extensionsFilters: ["postgis"],
      schemaFilter: "public",
      tablesFilter: "*",
    
      introspect: {
        casing: "camel",
      },
    
      migrations: {
        prefix: "timestamp",
        table: "__drizzle_migrations__",
        schema: "public",
      },
    
      entities: {
        roles: {
          provider: '',
          exclude: [],
          include: []
        }
      },
    
      breakpoints: true,
      strict: true,
      verbose: true,
    });

Expand

### Multiple configuration files

You can have multiple config files in the project, it’s very useful when you have multiple database stages or multiple databases or different databases on the same project:

npm 

yarn 

pnpm 

bun 
    
    
    npx drizzle-kit generate --config=drizzle-dev.config.ts
    npx drizzle-kit generate --config=drizzle-prod.config.ts
    
    
    yarn drizzle-kit generate --config=drizzle-dev.config.ts
    yarn drizzle-kit generate --config=drizzle-prod.config.ts
    
    
    pnpm drizzle-kit generate --config=drizzle-dev.config.ts
    pnpm drizzle-kit generate --config=drizzle-prod.config.ts
    
    
    bunx drizzle-kit generate --config=drizzle-dev.config.ts
    bunx drizzle-kit generate --config=drizzle-prod.config.ts
    
    
    📦 <project root>
     ├ 📂 drizzle
     ├ 📂 src
     ├ 📜 .env
     ├ 📜 drizzle-dev.config.ts
     ├ 📜 drizzle-prod.config.ts
     ├ 📜 package.json
     └ 📜 tsconfig.json

### Migrations folder

`out` param lets you define folder for your migrations, it’s optional and `drizzle` by default.  
It’s very useful since you can have many separate schemas for different databases in the same project and have different migration folders for them.

Migration folder contains `.sql` migration files and `_meta` folder which is used by `drizzle-kit`
    
    
    📦 <project root>
     ├ ...
     ├ 📂 drizzle
     │ ├ 📂 _meta
     │ ├ 📜 user.ts 
     │ ├ 📜 post.ts 
     │ └ 📜 comment.ts 
     ├ 📂 src
     ├ 📜 drizzle.config.ts
     └ 📜 package.json
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "postgresql", // "mysql" | "sqlite" | "postgresql" | "turso" | "singlestore"
      schema: "./src/schema/*",
      out: "./drizzle",
    });

## \---

### `dialect`

Dialect of the database you’re using

|   
---|---  
type| `postgresql` `mysql` `sqlite` `turso` `singlestore`  
default| —  
commands| `generate` `migrate` `push` `pull` `check` `up`  
      
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "mysql", 
    });

### `schema`

[`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20'.js'&tests=/hello/world.js&tests=//%20This%20won't%20match!&tests=/test/some/globs) based path to drizzle schema file(s) or folder(s) contaning schema files.

|   
---|---  
type| `string` `string[]`  
default| —  
commands| `generate` `push`  
  
Example 1

Example 2

Example 3

Example 4
    
    
    📦 <project root>
     ├ ...
     ├ 📂 drizzle
     ├ 📂 src
     │ ├ ...
     │ ├ 📜 index.ts
     │ └ 📜 schema.ts 
     ├ 📜 drizzle.config.ts
     └ 📜 package.json
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      schema: "./src/schema.ts",
    });
    
    
    📦 <project root>
     ├ ...
     ├ 📂 drizzle
     ├ 📂 src
     │ ├ 📂 user
     │ │ ├ 📜 handler.ts 
     │ │ └ 📜 schema.ts 
     │ ├ 📂 posts
     │ │ ├ 📜 handler.ts 
     │ │ └ 📜 schema.ts 
     │ └ 📜 index.ts
     ├ 📜 drizzle.config.ts
     └ 📜 package.json
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      schema: "./src/**/schema.ts",
      //or
      schema: ["./src/user/schema.ts", "./src/posts/schema.ts"]
    });
    
    
    📦 <project root>
     ├ ...
     ├ 📂 drizzle
     ├ 📂 src
     │ ├ 📂 schema
     │ │ ├ 📜 user.ts 
     │ │ ├ 📜 post.ts 
     │ │ └ 📜 comment.ts 
     │ └ 📜 index.ts
     ├ 📜 drizzle.config.ts
     └ 📜 package.json
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      schema: "./src/schema/*",
    });
    
    
    📦 <project root>
     ├ ...
     ├ 📂 drizzle
     ├ 📂 src
     │ ├ 📜 userById.ts 
     │ ├ 📜 userByEmail.ts 
     │ ├ 📜 listUsers.ts 
     │ ├ 📜 user.sql.ts 
     │ ├ 📜 postById.ts 
     │ ├ 📜 listPosts.ts 
     │ └ 📜 post.sql.ts 
     │ 📜 index.ts
     ├ 📜 drizzle.config.ts
     └ 📜 package.json
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      schema: "./src/**/*.sql.ts", // Dax's favourite
    });

### `out`

Defines output folder of your SQL migration files, json snapshots of your schema and `schema.ts` from `drizzle-kit pull` command.

|   
---|---  
type| `string` `string[]`  
default| `drizzle`  
commands| `generate` `migrate` `push` `pull` `check` `up`  
      
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      out: "./drizzle", 
    });

### `driver`

Drizzle Kit automatically picks available database driver from your current project based on the provided `dialect`, yet some vendor specific databases require a different subset of connection params.

`driver` option let’s you explicitely pick those exceptions drivers.

|   
---|---  
type| `aws-data-api` `d1-http` `pglight`  
default| —  
commands| `migrate` `push` `pull`  
  
AWS Data API

PGLite

Cloudflare D1 HTTP
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "postgresql",
      schema: "./src/schema.ts",
      driver: "aws-data-api",
      dbCredentials: {
        database: "database",
        resourceArn: "resourceArn",
        secretArn: "secretArn",
      },
    });
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "postgresql",
      schema: "./src/schema.ts",
      driver: "pglite",
      dbCredentials: {
        // inmemory
        url: ":memory:"
        
        // or database folder
        url: "./database/"
      },
    });
    
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "sqlite",
      schema: "./src/schema.ts",
      driver: "d1-http",
      dbCredentials: {
        accountId: "accountId",
        databaseId: "databaseId",
        token: "token",
      },
    });

## \---

### `dbCredentials`

Database connection credentials in a form of `url`, `user:password@host:port/db` params or exceptions drivers(`aws-data-api` `d1-http` `pglight` ) specific connection options.

|   
---|---  
type| union of drivers connection options  
default| —  
commands| `migrate` `push` `pull`  
  
PostgreSQL

MySQL

SQLite

Turso

Cloudflare D1

AWS Data API

PGLite
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "postgresql",
      dbCredentials: {
        url: "postgres://user:password@host:port/db",
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    // via connection params
    export default defineConfig({
      dialect: "postgresql",
      dbCredentials: {
        host: "host",
        port: 5432,
        user: "user",
        password: "password",
        database: "dbname",
        ssl: true, // can be boolean | "require" | "allow" | "prefer" | "verify-full" | options from node:tls
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "mysql",
      dbCredentials: {
        url: "mysql://user:password@host:port/db",
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    // via connection params
    export default defineConfig({
      dialect: "mysql",
      dbCredentials: {
        host: "host",
        port: 5432,
        user: "user",
        password: "password",
        database: "dbname",
        ssl: "...", // can be: string | SslOptions (ssl options from mysql2 package)
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "sqlite",
      dbCredentials: {
        url: ":memory:", // inmemory database
        // or
        url: "sqlite.db", 
        // or
        url: "file:sqlite.db" // file: prefix is required by libsql
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "turso",
      dbCredentials: {
        url: "libsql://acme.turso.io" // remote Turso database url
        authToken: "...",
    
        // or if you need local db
    
        url: ":memory:", // inmemory database
        // or
        url: "file:sqlite.db", // file: prefix is required by libsql
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "sqlite",
      driver: "d1-http",
      dbCredentials: {
        accountId: "",
        databaseId: "",
        token: "",
      }
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "postgresql",
      driver: "aws-data-api",
      dbCredentials: {
        database: "database",
        resourceArn: "resourceArn",
        secretArn: "secretArn",
      },
    });
    
    
    import { defineConfig } from 'drizzle-kit'
    
    export default defineConfig({
      dialect: "postgresql",
      driver: "pglite",
      dbCredentials: {
        url: "./database/", // database folder path
      }
    });

### `migrations`

When running `drizzle-kit migrate` \- drizzle will records about successfully applied migrations in your database in log table named `__drizzle_migrations` in `public` schema(PostgreSQL only).

`migrations` config options lets you change both migrations log `table` name and `schema`.

|   
---|---  
type| `{ table: string, schema: string }`  
default| `{ table: "__drizzle_migrations", schema: "drizzle" }`  
commands| `migrate`  
      
    
    export default defineConfig({
      dialect: "postgresql",
      schema: "./src/schema.ts",
      migrations: {
        table: 'my-migrations-table', // `__drizzle_migrations` by default
        schema: 'public', // used in PostgreSQL only, `drizzle` by default
      },
    });

### `introspect`

Configuration for `drizzle-kit pull` command.

`casing` is responsible for in-code column keys casing

|   
---|---  
type| `{ casing: "preserve" | "camel" }`  
default| `{ casing: "camel" }`  
commands| `pull`  
  
camel

preserve
    
    
    import * as p from "drizzle-orm/pg-core"
    
    export const users = p.pgTable("users", {
      id: p.serial(),
      firstName: p.text("first-name"),
      lastName: p.text("LastName"),
      email: p.text(),
      phoneNumber: p.text("phone_number"),
    });
    
    
    SELECT a.attname AS column_name, format_type(a.atttypid, a.atttypmod) as data_type FROM pg_catalog.pg_attribute a;
    
    
     column_name   | data_type        
    ---------------+------------------------
     id            | serial
     first-name    | text
     LastName      | text
     email         | text
     phone_number  | text
    
    
    import * as p from "drizzle-orm/pg-core"
    
    export const users = p.pgTable("users", {
      id: p.serial(),
      "first-name": p.text("first-name"),
      LastName: p.text("LastName"),
      email: p.text(),
      phone_number: p.text("phone_number"),
    });
    
    
    SELECT a.attname AS column_name, format_type(a.atttypid, a.atttypmod) as data_type FROM pg_catalog.pg_attribute a;
    
    
     column_name   | data_type        
    ---------------+------------------------
     id            | serial
     first-name    | text
     LastName      | text
     email         | text
     phone_number  | text

## \---

### `tablesFilter`

If you want to run multiple projects with one database - check out [our guide](/docs/goodies#multi-project-schema).

`drizzle-kit push` and `drizzle-kit pull` will by default manage all tables in `public` schema. You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

`tablesFilter` option lets you specify [`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20'.js'&tests=/hello/world.js&tests=//%20This%20won't%20match!&tests=/test/some/globs) based table names filter, e.g. `["users", "user_info"]` or `"user*"`

|   
---|---  
type| `string` `string[]`  
default| —  
commands| `generate` `push` `pull`  
      
    
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      dialect: "postgresql",
      tablesFilter: ["users", "posts", "project1_*"],
    });

### `schemaFilter`

If you want to run multiple projects with one database - check out [our guide](/docs/goodies#multi-project-schema).

`drizzle-kit push` and `drizzle-kit pull` will by default manage all tables in `public` schema. You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

`schemaFilter` option lets you specify list of schemas for Drizzle Kit to manage

|   
---|---  
type| `string[]`  
default| `["public"]`  
commands| `push` `pull`  
      
    
    export default defineConfig({
      dialect: "postgresql",
      schemaFilter: ["public", "schema1", "schema2"],
    });

### `extensionsFilters`

Some extensions like [`postgis`](https://postgis.net/), when installed on the database, create its own tables in public schema. Those tables have to be ignored by `drizzle-kit push` or `drizzle-kit pull`.

`extensionsFilters` option lets you declare list of installed extensions for drizzle kit to ignore their tables in the schema.

|   
---|---  
type| `["postgis"]`  
default| `[]`  
commands| `push` `pull`  
      
    
    export default defineConfig({
      dialect: "postgresql",
      extensionsFilters: ["postgis"],
    });

## \---

### `entities`

This configuration is created to set up management settings for specific `entities` in the database.

For now, it only includes `roles`, but eventually all database entities will migrate here, such as `tables`, `schemas`, `extensions`, `functions`, `triggers`, etc

#### `roles`

If you are using Drizzle Kit to manage your schema and especially the defined roles, there may be situations where you have some roles that are not defined in the Drizzle schema. In such cases, you may want Drizzle Kit to skip those `roles` without the need to write each role in your Drizzle schema and mark it with `.existing()`.

The `roles` option lets you:

  * Enable or disable role management with Drizzle Kit.
  * Exclude specific roles from management by Drizzle Kit.
  * Include specific roles for management by Drizzle Kit.
  * Enable modes for providers like `Neon` and `Supabase`, which do not manage their specific roles.
  * Combine all the options above

|   
---|---  
type| `boolean | { provider: "neon" | "supabase", include: string[], exclude: string[]}`  
default| `false`  
commands| `push` `pull` `generate`  
  
By default, `drizzle-kit` won’t manage roles for you, so you will need to enable that. in `drizzle.config.ts`
    
    
    export default defineConfig({
      dialect: "postgresql",
      entities: {
        roles: true
      }
    });

**You have a role`admin` and want to exclude it from the list of manageable roles**
    
    
    // drizzle.config.ts
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      ...
      entities: {
        roles: {
          exclude: ['admin']
        }
      }
    });

**You have a role`admin` and want to include to the list of manageable roles**
    
    
    // drizzle.config.ts
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      ...
      entities: {
        roles: {
          include: ['admin']
        }
      }
    });

**If you are using`Neon` and want to exclude roles defined by `Neon`, you can use the provider option**
    
    
    // drizzle.config.ts
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      ...
      entities: {
        roles: {
          provider: 'neon'
        }
      }
    });

**If you are using`Supabase` and want to exclude roles defined by `Supabase`, you can use the provider option**
    
    
    // drizzle.config.ts
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      ...
      entities: {
        roles: {
          provider: 'supabase'
        }
      }
    });

important

You may encounter situations where Drizzle is slightly outdated compared to new roles specified by database providers, so you may need to use both the `provider` option and `exclude` additional roles. You can easily do this with Drizzle:
    
    
    // drizzle.config.ts
    import { defineConfig } from "drizzle-kit";
    
    export default defineConfig({
      ...
      entities: {
        roles: {
          provider: 'supabase',
          exclude: ['new_supabase_role']
        }
      }
    });

## \---

### `strict`

Prompts confirmation to run printed SQL statements when running `drizzle-kit push` command.

|   
---|---  
type| `boolean`  
default| `false`  
commands| `push`  
      
    
    export default defineConfig({
      dialect: "postgresql",
      strict: false,
    });

### `verbose`

Print all SQL statements during `drizzle-kit push` command.

|   
---|---  
type| `boolean`  
default| `true`  
commands| `generate` `pull`  
      
    
    export default defineConfig({
      dialect: "postgresql",
      verbose: false,
    });

### `breakpoints`

Drizzle Kit will automatically embed `--> statement-breakpoint` into generated SQL migration files, that’s necessary for databases that do not support multiple DDL alternation statements in one transaction(MySQL and SQLite).

`breakpoints` option flag lets you switch it on and off

|   
---|---  
type| `boolean`  
default| `true`  
commands| `generate` `pull`  
      
    
    export default defineConfig({
      dialect: "postgresql",
      breakpoints: false,
    });