# seed-overview

**Source URL:** https://orm.drizzle.team/docs/seed-overview

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

[ Overview ](/docs/seed-overview)

Installation  Basic Usage  Options  Reset database  Refinements  Weighted Random  Complex example  Limitations 

[ Generators ](/docs/seed-functions)[ Versioning ](/docs/seed-versioning)

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

# Drizzle Seed

PostgreSQL

SQLite

MySQL

SingleStore

IMPORTANT

`drizzle-seed` can only be used with `[[email protected]](/cdn-cgi/l/email-protection)` or higher. Versions lower than this may work at runtime but could have type issues and identity column issues, as this patch was introduced in `[[email protected]](/cdn-cgi/l/email-protection)`

`drizzle-seed` is a TypeScript library that helps you generate deterministic, yet realistic, fake data to populate your database. By leveraging a seedable pseudorandom number generator (pRNG), it ensures that the data you generate is consistent and reproducible across different runs. This is especially useful for testing, development, and debugging purposes.

#### What is Deterministic Data Generation?

Deterministic data generation means that the same input will always produce the same output. In the context of `drizzle-seed`, when you initialize the library with the same seed number, it will generate the same sequence of fake data every time. This allows for predictable and repeatable data sets.

#### Pseudorandom Number Generator (pRNG)

A pseudorandom number generator is an algorithm that produces a sequence of numbers that approximates the properties of random numbers. However, because it’s based on an initial value called a seed, you can control its randomness. By using the same seed, the pRNG will produce the same sequence of numbers, making your data generation process reproducible.

#### Benefits of Using a pRNG:

  * Consistency: Ensures that your tests run on the same data every time.
  * Debugging: Makes it easier to reproduce and fix bugs by providing a consistent data set.
  * Collaboration: Team members can share seed numbers to work with the same data sets.



With drizzle-seed, you get the best of both worlds: the ability to generate realistic fake data and the control to reproduce it whenever needed.

## Installation

npm 

yarn 

pnpm 

bun 
    
    
    npm i drizzle-seed
    
    
    yarn add drizzle-seed
    
    
    pnpm add drizzle-seed
    
    
    bun add drizzle-seed

## Basic Usage

In this example we will create 10 users with random names and ids
    
    
    import { pgTable, integer, text } from "drizzle-orm/pg-core";
    import { drizzle } from "drizzle-orm/node-postgres";
    import { seed } from "drizzle-seed";
    
    const users = pgTable("users", {
      id: integer().primaryKey(),
      name: text().notNull(),
    });
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
      await seed(db, { users });
    }
    
    main();

## Options

**`count`**

By default, the `seed` function will create 10 entities. However, if you need more for your tests, you can specify this in the seed options object
    
    
    await seed(db, schema, { count: 1000 });

**`seed`**

If you need a seed to generate a different set of values for all subsequent runs, you can define a different number in the `seed` option. Any new number will generate a unique set of values
    
    
    await seed(db, schema, { seed: 12345 });

## Reset database

With `drizzle-seed`, you can easily reset your database and seed it with new values, for example, in your test suites
    
    
    // path to a file with schema you want to reset
    import * as schema from "./schema.ts";
    import { reset } from "drizzle-seed";
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
      await reset(db, schema);
    }
    
    main();

Different dialects will have different strategies for database resetting

PostgreSQL 

MySQL 

SQLite 

For PostgreSQL, the `drizzle-seed` package will generate `TRUNCATE` statements with the `CASCADE` option to ensure that all tables are empty after running the reset function
    
    
    TRUNCATE tableName1, tableName2, ... CASCADE;

For MySQL, the `drizzle-seed` package will first disable `FOREIGN_KEY_CHECKS` to ensure the next step won’t fail, and then generate `TRUNCATE` statements to empty the content of all tables
    
    
    SET FOREIGN_KEY_CHECKS = 0;
    TRUNCATE tableName1;
    TRUNCATE tableName2;
    ...
    SET FOREIGN_KEY_CHECKS = 1;

For SQLite, the `drizzle-seed` package will first disable the `foreign_keys` pragma to ensure the next step won’t fail, and then generate `DELETE FROM` statements to empty the content of all tables
    
    
    PRAGMA foreign_keys = OFF;
    DELETE FROM tableName1;
    DELETE FROM tableName2;
    ...
    PRAGMA foreign_keys = ON;

## Refinements

In case you need to change the behavior of the seed generator functions that `drizzle-seed` uses by default, you can specify your own implementation and even use your own list of values for the seeding process

`.refine` is a callback that receives a list of all available generator functions from `drizzle-seed`. It should return an object with keys representing the tables you want to refine, defining their behavior as needed. Each table can specify several properties to simplify seeding your database:

  * `columns`: Refine the default behavior of each column by specifying the required generator function.
  * `count`: Specify the number of rows to insert into the database. By default, it’s 10. If a global count is defined in the `seed()` options, the count defined here will override it for this specific table.
  * `with`: Define how many referenced entities to create for each parent table if you want to generate associated entities.



info

You can also specify a weighted random distribution for the number of referenced values you want to create. For details on this API, you can refer to Weighted Random docs docs section

**API**
    
    
    await seed(db, schema).refine((f) => ({
      users: {
        columns: {},
        count: 10,
        with: {
            posts: 10
        }
      },
    }));

Let’s check a few examples with an explanation of what will happen:

schema.ts
    
    
    import { pgTable, integer, text } from "drizzle-orm/pg-core";
    
    export const users = pgTable("users", {
      id: integer().primaryKey(),
      name: text().notNull(),
    });
    
    export const posts = pgTable("posts", {
      id: integer().primaryKey(),
      description: text(),
      userId: integer().references(() => users.id),
    });

**Example 1** : Seed only the `users` table with 20 entities and with refined seed logic for the `name` column

index.ts
    
    
    import { drizzle } from "drizzle-orm/node-postgres";
    import { seed } from "drizzle-seed";
    import * as schema from './schema.ts'
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
    
      await seed(db, { users: schema.users }).refine((f) => ({
        users: {
            columns: {
                name: f.fullName(),
            },
            count: 20
        }
      }));
    }
    
    main();

**Example 2** : Seed the `users` table with 20 entities and add 10 `posts` for each `user` by seeding the `posts` table and creating a reference from `posts` to `users`

index.ts
    
    
    import { drizzle } from "drizzle-orm/node-postgres";
    import { seed } from "drizzle-seed";
    import * as schema from './schema.ts'
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
    
      await seed(db, schema).refine((f) => ({
        users: {
            count: 20,
            with: {
                posts: 10
            }
        }
      }));
    }
    
    main();

**Example 3** : Seed the `users` table with 5 entities and populate the database with 100 `posts` without connecting them to the `users` entities. Refine `id` generation for `users` so that it will give any int from `10000` to `20000` and remains unique, and refine `posts` to retrieve values from a self-defined array

index.ts
    
    
    import { drizzle } from "drizzle-orm/node-postgres";
    import { seed } from "drizzle-seed";
    import * as schema from './schema.ts'
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
    
      await seed(db, schema).refine((f) => ({
        users: {
            count: 5,
            columns: {
                id: f.int({
                  minValue: 10000,
                  maxValue: 20000,
                  isUnique: true,
                }),
            }
        },
        posts: {
            count: 100,
            columns: {
                description: f.valuesFromArray({
                values: [
                    "The sun set behind the mountains, painting the sky in hues of orange and purple", 
                    "I can't believe how good this homemade pizza turned out!", 
                    "Sometimes, all you need is a good book and a quiet corner.", 
                    "Who else thinks rainy days are perfect for binge-watching old movies?", 
                    "Tried a new hiking trail today and found the most amazing waterfall!",
                    // ...
                ],
              })
            }
        }
      }));
    }
    
    main();

IMPORTANT

There are many more possibilities that we will define in these docs, but for now, you can explore a few sections in this documentation. Check the [Generators](/docs/seed-functions) section to get familiar with all the available generator functions you can use.

A particularly great feature is the ability to use weighted randomization, both for generator values created for a column and for determining the number of related entities that can be generated by `drizzle-seed`.

Please check Weighted Random docs for more info.

## Weighted Random

There may be cases where you need to use multiple datasets with a different priority that should be inserted into your database during the seed stage. For such cases, drizzle-seed provides an API called weighted random

The Drizzle Seed package has a few places where weighted random can be used:

  * Columns inside each table refinements
  * The `with` property, determining the amount of related entities to be created



Let’s check an example for both:

schema.ts
    
    
    import { pgTable, integer, text, varchar, doublePrecision } from "drizzle-orm/pg-core";
    
    export const orders = pgTable(
      "orders",
      {
        id: integer().primaryKey(),
        name: text().notNull(),
        quantityPerUnit: varchar().notNull(),
        unitPrice: doublePrecision().notNull(),
        unitsInStock: integer().notNull(),
        unitsOnOrder: integer().notNull(),
        reorderLevel: integer().notNull(),
        discontinued: integer().notNull(),
      }
    );
    
    export const details = pgTable(
      "details",
      {
        unitPrice: doublePrecision().notNull(),
        quantity: integer().notNull(),
        discount: doublePrecision().notNull(),
    
        orderId: integer()
          .notNull()
          .references(() => orders.id, { onDelete: "cascade" }),
      }
    );

**Example 1** : Refine the `unitPrice` generation logic to generate `5000` random prices, with a 30% chance of prices between 10-100 and a 70% chance of prices between 100-300

index.ts
    
    
    import { drizzle } from "drizzle-orm/node-postgres";
    import { seed } from "drizzle-seed";
    import * as schema from './schema.ts'
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
    
      await seed(db, schema).refine((f) => ({
        orders: {
           count: 5000,
           columns: {
               unitPrice: f.weightedRandom(
                   [
                       {
                           weight: 0.3,
                           value: funcs.int({ minValue: 10, maxValue: 100 })
                       },
                       {
                           weight: 0.7,
                           value: funcs.number({ minValue: 100, maxValue: 300, precision: 100 })
                       }
                   ]
               ),
           }
        }
      }));
    }
    
    main();

**Example 2** : For each order, generate 1 to 3 details with a 60% chance, 5 to 7 details with a 30% chance, and 8 to 10 details with a 10% chance

index.ts
    
    
    import { drizzle } from "drizzle-orm/node-postgres";
    import { seed } from "drizzle-seed";
    import * as schema from './schema.ts'
    
    async function main() {
      const db = drizzle(process.env.DATABASE_URL!);
    
      await seed(db, schema).refine((f) => ({
        orders: {
           with: {
               details:
                   [
                       { weight: 0.6, count: [1, 2, 3] },
                       { weight: 0.3, count: [5, 6, 7] },
                       { weight: 0.1, count: [8, 9, 10] },
                   ]
           }
        }
      }));
    }
    
    main();

## Complex example

main.ts

schema.ts
    
    
    import { seed } from "drizzle-seed";
    import * as schema from "./schema.ts";
    
    const main = async () => {
        const titlesOfCourtesy = ["Ms.", "Mrs.", "Dr."];
        const unitsOnOrders = [0, 10, 20, 30, 50, 60, 70, 80, 100];
        const reorderLevels = [0, 5, 10, 15, 20, 25, 30];
        const quantityPerUnit = [
            "100 - 100 g pieces",
            "100 - 250 g bags",
            "10 - 200 g glasses",
            "10 - 4 oz boxes",
            "10 - 500 g pkgs.",
            "10 - 500 g pkgs."
        ];
        const discounts = [0.05, 0.15, 0.2, 0.25];
    
        await seed(db, schema).refine((funcs) => ({
            customers: {
                count: 10000,
                columns: {
                    companyName: funcs.companyName(),
                    contactName: funcs.fullName(),
                    contactTitle: funcs.jobTitle(),
                    address: funcs.streetAddress(),
                    city: funcs.city(),
                    postalCode: funcs.postcode(),
                    region: funcs.state(),
                    country: funcs.country(),
                    phone: funcs.phoneNumber({ template: "(###) ###-####" }),
                    fax: funcs.phoneNumber({ template: "(###) ###-####" })
                }
            },
            employees: {
                count: 200,
                columns: {
                    firstName: funcs.firstName(),
                    lastName: funcs.lastName(),
                    title: funcs.jobTitle(),
                    titleOfCourtesy: funcs.valuesFromArray({ values: titlesOfCourtesy }),
                    birthDate: funcs.date({ minDate: "2010-12-31", maxDate: "2010-12-31" }),
                    hireDate: funcs.date({ minDate: "2010-12-31", maxDate: "2024-08-26" }),
                    address: funcs.streetAddress(),
                    city: funcs.city(),
                    postalCode: funcs.postcode(),
                    country: funcs.country(),
                    homePhone: funcs.phoneNumber({ template: "(###) ###-####" }),
                    extension: funcs.int({ minValue: 428, maxValue: 5467 }),
                    notes: funcs.loremIpsum()
                }
            },
            orders: {
                count: 50000,
                columns: {
                    shipVia: funcs.int({ minValue: 1, maxValue: 3 }),
                    freight: funcs.number({ minValue: 0, maxValue: 1000, precision: 100 }),
                    shipName: funcs.streetAddress(),
                    shipCity: funcs.city(),
                    shipRegion: funcs.state(),
                    shipPostalCode: funcs.postcode(),
                    shipCountry: funcs.country()
                },
                with: {
                    details:
                        [
                            { weight: 0.6, count: [1, 2, 3, 4] },
                            { weight: 0.2, count: [5, 6, 7, 8, 9, 10] },
                            { weight: 0.15, count: [11, 12, 13, 14, 15, 16, 17] },
                            { weight: 0.05, count: [18, 19, 20, 21, 22, 23, 24, 25] },
                        ]
                }
            },
            suppliers: {
                count: 1000,
                columns: {
                    companyName: funcs.companyName(),
                    contactName: funcs.fullName(),
                    contactTitle: funcs.jobTitle(),
                    address: funcs.streetAddress(),
                    city: funcs.city(),
                    postalCode: funcs.postcode(),
                    region: funcs.state(),
                    country: funcs.country(),
                    phone: funcs.phoneNumber({ template: "(###) ###-####" })
                }
            },
            products: {
                count: 5000,
                columns: {
                    name: funcs.companyName(),
                    quantityPerUnit: funcs.valuesFromArray({ values: quantityPerUnit }),
                    unitPrice: funcs.weightedRandom(
                        [
                            {
                                weight: 0.5,
                                value: funcs.int({ minValue: 3, maxValue: 300 })
                            },
                            {
                                weight: 0.5,
                                value: funcs.number({ minValue: 3, maxValue: 300, precision: 100 })
                            }
                        ]
                    ),
                    unitsInStock: funcs.int({ minValue: 0, maxValue: 125 }),
                    unitsOnOrder: funcs.valuesFromArray({ values: unitsOnOrders }),
                    reorderLevel: funcs.valuesFromArray({ values: reorderLevels }),
                    discontinued: funcs.int({ minValue: 0, maxValue: 1 })
                }
            },
            details: {
                columns: {
                    unitPrice: funcs.number({ minValue: 10, maxValue: 130 }),
                    quantity: funcs.int({ minValue: 1, maxValue: 130 }),
                    discount: funcs.weightedRandom(
                        [
                            { weight: 0.5, value: funcs.valuesFromArray({ values: discounts }) },
                            { weight: 0.5, value: funcs.default({ defaultValue: 0 }) }
                        ]
                    )
                }
            }
        }));
    }
    
    main();
    
    
    
    import type { AnyPgColumn } from "drizzle-orm/pg-core";
    import { integer, numeric, pgTable, text, timestamp, varchar } from "drizzle-orm/pg-core";
    
    export const customers = pgTable('customer', {
    	id: varchar({ length: 256 }).primaryKey(),
    	companyName: text().notNull(),
    	contactName: text().notNull(),
    	contactTitle: text().notNull(),
    	address: text().notNull(),
    	city: text().notNull(),
    	postalCode: text(),
    	region: text(),
    	country: text().notNull(),
    	phone: text().notNull(),
    	fax: text(),
    });
    
    export const employees = pgTable(
    	'employee',
    	{
    		id: integer().primaryKey(),
    		lastName: text().notNull(),
    		firstName: text(),
    		title: text().notNull(),
    		titleOfCourtesy: text().notNull(),
    		birthDate: timestamp().notNull(),
    		hireDate: timestamp().notNull(),
    		address: text().notNull(),
    		city: text().notNull(),
    		postalCode: text().notNull(),
    		country: text().notNull(),
    		homePhone: text().notNull(),
    		extension: integer().notNull(),
    		notes: text().notNull(),
    		reportsTo: integer().references((): AnyPgColumn => employees.id),
    		photoPath: text(),
    	},
    );
    
    export const orders = pgTable('order', {
    	id: integer().primaryKey(),
    	orderDate: timestamp().notNull(),
    	requiredDate: timestamp().notNull(),
    	shippedDate: timestamp(),
    	shipVia: integer().notNull(),
    	freight: numeric().notNull(),
    	shipName: text().notNull(),
    	shipCity: text().notNull(),
    	shipRegion: text(),
    	shipPostalCode: text(),
    	shipCountry: text().notNull(),
    
    	customerId: text().notNull().references(() => customers.id, { onDelete: 'cascade' }),
    
    	employeeId: integer().notNull().references(() => employees.id, { onDelete: 'cascade' }),
    });
    
    export const suppliers = pgTable('supplier', {
    	id: integer().primaryKey(),
    	companyName: text().notNull(),
    	contactName: text().notNull(),
    	contactTitle: text().notNull(),
    	address: text().notNull(),
    	city: text().notNull(),
    	region: text(),
    	postalCode: text().notNull(),
    	country: text().notNull(),
    	phone: text().notNull(),
    });
    
    export const products = pgTable('product', {
    	id: integer().primaryKey(),
    	name: text().notNull(),
    	quantityPerUnit: text().notNull(),
    	unitPrice: numeric().notNull(),
    	unitsInStock: integer().notNull(),
    	unitsOnOrder: integer().notNull(),
    	reorderLevel: integer().notNull(),
    	discontinued: integer().notNull(),
    
    	supplierId: integer().notNull().references(() => suppliers.id, { onDelete: 'cascade' }),
    });
    
    export const details = pgTable('order_detail', {
    	unitPrice: numeric().notNull(),
    	quantity: integer().notNull(),
    	discount: numeric().notNull(),
    
    	orderId: integer().notNull().references(() => orders.id, { onDelete: 'cascade' }),
    
    	productId: integer().notNull().references(() => products.id, { onDelete: 'cascade' }),
    });
    

## Limitations

#### Types limitations for `with`

Due to certain TypeScript limitations and the current API in Drizzle, it is not possible to properly infer references between tables, especially when circular dependencies between tables exist.

This means the `with` option will display all tables in the schema, and you will need to manually select the one that has a one-to-many relationship

warning

The `with` option works for one-to-many relationships. For example, if you have one `user` and many `posts`, you can use users `with` posts, but you cannot use posts `with` users

#### Type limitations for the third parameter in Drizzle tables:

Currently, we do not have type support for the third parameter in Drizzle tables. While it will work at runtime, it will not function correctly at the type level