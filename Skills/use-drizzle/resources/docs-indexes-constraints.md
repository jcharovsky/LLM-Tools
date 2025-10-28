# indexes-constraints

**Source URL:** https://orm.drizzle.team/docs/indexes-constraints

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

Data types [ Indexes & Constraints ](/docs/indexes-constraints)

Constraints  Default  Not null  Unique  Check  Primary Key  Composite Primary Key  Foreign key  Indexes 

[ Sequences ](/docs/sequences)[ Views ](/docs/views)[ Schemas ](/docs/schemas)[ Row-Level Security (RLS) ](/docs/rls) Extensions [ Relations ](/docs/relations)

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

[ v1.0 75% ](/roadmap)

[ Benchmarks ](/benchmarks) [ Extension ](https://driz.link/extension) [ Studio ](/drizzle-studio/overview) [ Studio Package ](https://github.com/drizzle-team/drizzle-studio-npm) [ Gateway ](https://gateway.drizzle.team) [ Drizzle Run ](https://drizzle.run)

Our goodies!

[ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMTU0IiB2aWV3Qm94PSIwIDAgMjAwIDE1NCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICA8cGF0aCBkPSJNMCA2OC42QzAgOTAuNCAxNy44NDk5IDEwOCAzOS45NTk0IDEwOEM2MS44NjYxIDEwOCA3OS45MTg5IDkwLjQgNzkuOTE4OSA2OC42Qzc5LjkxODkgNDcgNjEuODY2MSAyOS4yIDM5Ljk1OTQgMjkuMkMxNy44NDk5IDI5LjIgMCA0NyAwIDY4LjZaTTE3MS4xOTcgMTRDMTcxLjE5NyA2LjYgMTc3LjQ4NSAwIDE4NS4zOTYgMEMxOTMuMzA2IDAgMjAwIDYuNiAyMDAgMTRWOTRDMjAwIDEwMS40IDE5My4zMDYgMTA4IDE4NS4zOTYgMTA4QzE3Ny40ODUgMTA4IDE3MS4xOTcgMTAxLjQgMTcxLjE5NyA5NFYxNFpNMTAuNTQ3NyAxMjcuNkMxMi4xNzA0IDE0MS40IDIzLjczMjMgMTU0IDM5Ljk1OTQgMTU0QzU1Ljk4MzggMTU0IDY3Ljk1MTMgMTQxLjQgNjkuNTc0IDEyNy42QzcxLjgwNTMgMTA3LjYgNTMuMzQ2OSAxMTQuMiAzOS45NTk0IDExNC4yQzI2LjU3MiAxMTQuMiA4LjMxNjQzIDEwNy42IDEwLjU0NzcgMTI3LjZaTTEzOS4zNTEgNzQuMkMxNDAuNzcxIDcxIDE0NC40MjIgNjkgMTUxLjUyMSA2OUMxNjIuNjc3IDY4LjggMTY3LjE0IDYxLjYgMTYxLjI1OCA1MC4yQzE1Ny4yMDEgNDIuNCAxNTAuOTEzIDM2LjQgMTQyLjM5NCAzMi42QzEyMi4zMTIgMjMuOCA5OC41ODAxIDMyLjggODkuNjU1MiA1Mi42QzgwLjczMDIgNzIuMiA4OS42NTUyIDk1LjYgMTA5LjkzOSAxMDQuNkMxMTguNDU4IDEwOC4yIDEyNi45NzggMTA4LjggMTM1LjcgMTA2LjZDMTQ4LjI3NiAxMDMuMiAxNTAuOTEzIDk1IDE0My40MDggODYuOEMxMzguNzQyIDgxLjQgMTM3LjcyOCA3Ny42IDEzOS4zNTEgNzQuMloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl81OV80NikiLz4KICAgICAgICAgIDxkZWZzPgogICAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzU5XzQ2IiB4MT0iMjUwLjI1NCIgeTE9IjAiIHgyPSIyNTAuMjU0IiB5Mj0iMTU0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CiAgICAgICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjRkZDODAwIi8+CiAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjQ4MDAiLz4KICAgICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICAgICAgICA8L2RlZnM+CiAgICAgICAgPC9zdmc+) ![Gel](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMTU0IiB2aWV3Qm94PSIwIDAgMjAwIDE1NCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICA8cGF0aCBkPSJNMCA2OC42QzAgOTAuNCAxNy44NDk5IDEwOCAzOS45NTk0IDEwOEM2MS44NjYxIDEwOCA3OS45MTg5IDkwLjQgNzkuOTE4OSA2OC42Qzc5LjkxODkgNDcgNjEuODY2MSAyOS4yIDM5Ljk1OTQgMjkuMkMxNy44NDk5IDI5LjIgMCA0NyAwIDY4LjZaTTE3MS4xOTcgMTRDMTcxLjE5NyA2LjYgMTc3LjQ4NSAwIDE4NS4zOTYgMEMxOTMuMzA2IDAgMjAwIDYuNiAyMDAgMTRWOTRDMjAwIDEwMS40IDE5My4zMDYgMTA4IDE4NS4zOTYgMTA4QzE3Ny40ODUgMTA4IDE3MS4xOTcgMTAxLjQgMTcxLjE5NyA5NFYxNFpNMTAuNTQ3NyAxMjcuNkMxMi4xNzA0IDE0MS40IDIzLjczMjMgMTU0IDM5Ljk1OTQgMTU0QzU1Ljk4MzggMTU0IDY3Ljk1MTMgMTQxLjQgNjkuNTc0IDEyNy42QzcxLjgwNTMgMTA3LjYgNTMuMzQ2OSAxMTQuMiAzOS45NTk0IDExNC4yQzI2LjU3MiAxMTQuMiA4LjMxNjQzIDEwNy42IDEwLjU0NzcgMTI3LjZaTTEzOS4zNTEgNzQuMkMxNDAuNzcxIDcxIDE0NC40MjIgNjkgMTUxLjUyMSA2OUMxNjIuNjc3IDY4LjggMTY3LjE0IDYxLjYgMTYxLjI1OCA1MC4yQzE1Ny4yMDEgNDIuNCAxNTAuOTEzIDM2LjQgMTQyLjM5NCAzMi42QzEyMi4zMTIgMjMuOCA5OC41ODAxIDMyLjggODkuNjU1MiA1Mi42QzgwLjczMDIgNzIuMiA4OS42NTUyIDk1LjYgMTA5LjkzOSAxMDQuNkMxMTguNDU4IDEwOC4yIDEyNi45NzggMTA4LjggMTM1LjcgMTA2LjZDMTQ4LjI3NiAxMDMuMiAxNTAuOTEzIDk1IDE0My40MDggODYuOEMxMzguNzQyIDgxLjQgMTM3LjcyOCA3Ny42IDEzOS4zNTEgNzQuMloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl81OV80NikiLz4KICAgICAgICAgIDxkZWZzPgogICAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzU5XzQ2IiB4MT0iMjUwLjI1NCIgeTE9IjAiIHgyPSIyNTAuMjU0IiB5Mj0iMTU0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CiAgICAgICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjRkZDODAwIi8+CiAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjQ4MDAiLz4KICAgICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICAgICAgICA8L2RlZnM+CiAgICAgICAgPC9zdmc+) ](https://driz.link/edgedb)

[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Turso](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) 🚀 Drizzle is giving you 10% off Turso Scaler and Pro for 1 Year 🚀 ](https://driz.link/turso)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Payload](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/payload)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMDU0LjM1IDM3OS4xNEMxMDU0LjI0IDQ2OS4xMzcgMTAxOC4zNSA1NTUuNDA4IDk1NC41NiA2MTguOTcxVjYxOC45NjRMNzI4LjI3MyA4NDQuNDVDNzIwLjQzMiA4NTIuMjcgNzA3LjY5MyA4NTIuMjkgNzAwLjM0NiA4NDQuMDFDNjQ1LjMzMSA3ODIuMDE4IDYxNC43NTggNzAxLjgzOCA2MTQuODU2IDYxOC41MzVDNjE0Ljk2MSA1MjguNTM4IDY1MC44NTYgNDQyLjI2OCA3MTQuNjQzIDM3OC43MDVMNzE0LjY1IDM3OC43MTFMOTIxLjM5IDE3Mi42OTdDOTQwLjAyIDE1NC4xMjggOTcwLjUxIDE1My45OTYgOTg2LjMxIDE3NS4wMjJDMTAzMC4zIDIzMy41NDcgMTA1NC40NCAzMDUuMTEgMTA1NC4zNSAzNzkuMTRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMjAyXzcxKSIvPjxwYXRoIGQ9Ik0yNDQuNzg2IDYyMC4zNDVDMTgwLjk5OSA1NTYuNzgyIDE0NS4xMDUgNDcwLjUxMiAxNDUgMzgwLjUxNUMxNDQuOTEzIDMwNi40ODUgMTY5LjA0OCAyMzQuOTIxIDIxMy4wMzUgMTc2LjM5NkMyMjguODM4IDE1NS4zNyAyNTkuMzI4IDE1NS41MDMgMjc3Ljk2MyAxNzQuMDcyTDQ4NC43MDMgMzgwLjA4OEw0ODQuNzEgMzgwLjA4MUM1NDguNDk3IDQ0My42NDUgNTg0LjM5MSA1MjkuOTE0IDU4NC40OTcgNjE5LjkxMkM1ODQuNTk0IDcwMy4yMTQgNTU0LjAyMiA3ODMuMzk1IDQ5OS4wMDcgODQ1LjM4QzQ5MS42NTkgODUzLjY2IDQ3OC45MiA4NTMuNjQgNDcxLjA4IDg0NS44M0wyNDQuNzkzIDYyMC4zMzlMMjQ0Ljc4NiA2MjAuMzQ1WiIgZmlsbD0idXJsKCNwYWludDFfbGluZWFyXzIwMl83MSkiLz48cGF0aCBkPSJNOTQ2LjA1IDEwMjMuODNDOTI5LjQyIDEwNDQuMjIgODk5LjAyIDEwNDQuMDQgODgwLjQyIDEwMjUuNDJMNzUyLjcyNyA4OTcuNThDNzQ0Ljg5MSA4ODkuNzMgNzQ0LjkwNiA4NzcuMDIgNzUyLjc2IDg2OS4xOUw5NjQuODUgNjU3Ljg0OEM5NzIuNjkgNjUwLjAzNSA5ODUuNDggNjQ5Ljk4OSA5OTIuMzkgNjU4LjYzMkMxMDI5LjIgNzA0LjYyOCAxMDQzLjY4IDc2OC4xOTggMTAzMi43NCA4MzguMThDMTAyMi43MiA5MDIuMjQgOTkyLjA4IDk2Ny4zNyA5NDYuMDUgMTAyMy44M1oiIGZpbGw9InVybCgjcGFpbnQyX2xpbmVhcl8yMDJfNzEpIi8+PHBhdGggZD0iTTMxOC45MzEgMTAyNi44QzMwMC4zMzcgMTA0NS40MSAyNjkuOTI5IDEwNDUuNTkgMjUzLjMwNSAxMDI1LjJDMjA3LjI2OSA5NjguNzQgMTc2LjYzMyA5MDMuNjIgMTY2LjYxNyA4MzkuNTZDMTU1LjY3NSA3NjkuNTcxIDE3MC4xNDkgNzA2LjAwMSAyMDYuOTU5IDY2MC4wMDVDMjEzLjg3NiA2NTEuMzYzIDIyNi42NjMgNjUxLjQwOCAyMzQuNTA0IDY1OS4yMjFMNDQ2LjU5NSA4NzAuNTdDNDU0LjQ0OSA4NzguMzkgNDU0LjQ2NCA4OTEuMTEgNDQ2LjYyOSA4OTguOTVMMzE4LjkzMSAxMDI2LjhaIiBmaWxsPSJ1cmwoI3BhaW50M19saW5lYXJfMjAyXzcxKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU4Ljk5OSIgeDI9IjU5OS42NzYiIHkyPSI4NTkuNCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiM5Rjg3RkYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM4NTY2RkYiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU5IiB4Mj0iNTk5LjY3NiIgeTI9Ijg1OS40IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzlGODdGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg1NjZGRiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzIwMl83MSIgeDE9IjU5OS42NzYiIHkxPSI2NDMuNzY2IiB4Mj0iNTk5LjY3NiIgeTI9IjEwMzkuOTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjREU5OUY2Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRDY2OUZDIi8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9InBhaW50M19saW5lYXJfMjAyXzcxIiB4MT0iNTk5LjY3NiIgeTE9IjY0My43NjYiIHgyPSI1OTkuNjc2IiB5Mj0iMTAzOS45MyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNERTk5RjYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNENjY5RkMiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=) ![Xata](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMDU0LjM1IDM3OS4xNEMxMDU0LjI0IDQ2OS4xMzcgMTAxOC4zNSA1NTUuNDA4IDk1NC41NiA2MTguOTcxVjYxOC45NjRMNzI4LjI3MyA4NDQuNDVDNzIwLjQzMiA4NTIuMjcgNzA3LjY5MyA4NTIuMjkgNzAwLjM0NiA4NDQuMDFDNjQ1LjMzMSA3ODIuMDE4IDYxNC43NTggNzAxLjgzOCA2MTQuODU2IDYxOC41MzVDNjE0Ljk2MSA1MjguNTM4IDY1MC44NTYgNDQyLjI2OCA3MTQuNjQzIDM3OC43MDVMNzE0LjY1IDM3OC43MTFMOTIxLjM5IDE3Mi42OTdDOTQwLjAyIDE1NC4xMjggOTcwLjUxIDE1My45OTYgOTg2LjMxIDE3NS4wMjJDMTAzMC4zIDIzMy41NDcgMTA1NC40NCAzMDUuMTEgMTA1NC4zNSAzNzkuMTRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMjAyXzcxKSIvPjxwYXRoIGQ9Ik0yNDQuNzg2IDYyMC4zNDVDMTgwLjk5OSA1NTYuNzgyIDE0NS4xMDUgNDcwLjUxMiAxNDUgMzgwLjUxNUMxNDQuOTEzIDMwNi40ODUgMTY5LjA0OCAyMzQuOTIxIDIxMy4wMzUgMTc2LjM5NkMyMjguODM4IDE1NS4zNyAyNTkuMzI4IDE1NS41MDMgMjc3Ljk2MyAxNzQuMDcyTDQ4NC43MDMgMzgwLjA4OEw0ODQuNzEgMzgwLjA4MUM1NDguNDk3IDQ0My42NDUgNTg0LjM5MSA1MjkuOTE0IDU4NC40OTcgNjE5LjkxMkM1ODQuNTk0IDcwMy4yMTQgNTU0LjAyMiA3ODMuMzk1IDQ5OS4wMDcgODQ1LjM4QzQ5MS42NTkgODUzLjY2IDQ3OC45MiA4NTMuNjQgNDcxLjA4IDg0NS44M0wyNDQuNzkzIDYyMC4zMzlMMjQ0Ljc4NiA2MjAuMzQ1WiIgZmlsbD0idXJsKCNwYWludDFfbGluZWFyXzIwMl83MSkiLz48cGF0aCBkPSJNOTQ2LjA1IDEwMjMuODNDOTI5LjQyIDEwNDQuMjIgODk5LjAyIDEwNDQuMDQgODgwLjQyIDEwMjUuNDJMNzUyLjcyNyA4OTcuNThDNzQ0Ljg5MSA4ODkuNzMgNzQ0LjkwNiA4NzcuMDIgNzUyLjc2IDg2OS4xOUw5NjQuODUgNjU3Ljg0OEM5NzIuNjkgNjUwLjAzNSA5ODUuNDggNjQ5Ljk4OSA5OTIuMzkgNjU4LjYzMkMxMDI5LjIgNzA0LjYyOCAxMDQzLjY4IDc2OC4xOTggMTAzMi43NCA4MzguMThDMTAyMi43MiA5MDIuMjQgOTkyLjA4IDk2Ny4zNyA5NDYuMDUgMTAyMy44M1oiIGZpbGw9InVybCgjcGFpbnQyX2xpbmVhcl8yMDJfNzEpIi8+PHBhdGggZD0iTTMxOC45MzEgMTAyNi44QzMwMC4zMzcgMTA0NS40MSAyNjkuOTI5IDEwNDUuNTkgMjUzLjMwNSAxMDI1LjJDMjA3LjI2OSA5NjguNzQgMTc2LjYzMyA5MDMuNjIgMTY2LjYxNyA4MzkuNTZDMTU1LjY3NSA3NjkuNTcxIDE3MC4xNDkgNzA2LjAwMSAyMDYuOTU5IDY2MC4wMDVDMjEzLjg3NiA2NTEuMzYzIDIyNi42NjMgNjUxLjQwOCAyMzQuNTA0IDY1OS4yMjFMNDQ2LjU5NSA4NzAuNTdDNDU0LjQ0OSA4NzguMzkgNDU0LjQ2NCA4OTEuMTEgNDQ2LjYyOSA4OTguOTVMMzE4LjkzMSAxMDI2LjhaIiBmaWxsPSJ1cmwoI3BhaW50M19saW5lYXJfMjAyXzcxKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU4Ljk5OSIgeDI9IjU5OS42NzYiIHkyPSI4NTkuNCIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiM5Rjg3RkYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM4NTY2RkYiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl8yMDJfNzEiIHgxPSI1OTkuNjc2IiB5MT0iMTU5IiB4Mj0iNTk5LjY3NiIgeTI9Ijg1OS40IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzlGODdGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzg1NjZGRiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzIwMl83MSIgeDE9IjU5OS42NzYiIHkxPSI2NDMuNzY2IiB4Mj0iNTk5LjY3NiIgeTI9IjEwMzkuOTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjREU5OUY2Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRDY2OUZDIi8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9InBhaW50M19saW5lYXJfMjAyXzcxIiB4MT0iNTk5LjY3NiIgeTE9IjY0My43NjYiIHgyPSI1OTkuNjc2IiB5Mj0iMTAzOS45MyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNERTk5RjYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNENjY5RkMiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48L3N2Zz4=) ](https://driz.link/xataio)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Neon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/neon)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Nuxt](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://hub.nuxt.com/?utm_source=drizzle-docs)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQiIGhlaWdodD0iNTQiIHZpZXdCb3g9IjAgMCA1NCA1NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQ4LjQ2MDggMjdDNDguNDYwOCAzOC44Nzc5IDM4Ljg0IDQ4LjUgMjYuOTgwNCA0OC41QzE1LjEyMDkgNDguNSA1LjUgMzguODc3OSA1LjUgMjdDNS41IDE1LjEyMjEgMTUuMTIwOSA1LjUgMjYuOTgwNCA1LjVDMzguODQgNS41IDQ4LjQ2MDggMTUuMTIyMSA0OC40NjA4IDI3WiIgZmlsbD0iI0NGRTJGOCIgc3Ryb2tlPSIjQ0ZFMkY4IiBzdHJva2Utd2lkdGg9IjExIj48L3BhdGg+CjxwYXRoIGQ9Ik0yNC42Nzk2IDEyLjQ3NzVDMjcuMTkxNiA4LjM0MDQ5IDMyLjU3OTEgNy4wMjQ1NSAzNi43MTI4IDkuNTM4MjFDNDAuODQ2NiAxMi4wNTE5IDQyLjE2MTIgMTcuNDQzMyAzOS42NDkyIDIxLjU4MDNMMzEuNjcyNCAzNC43MTY5QzI5LjE2MDMgMzguODUzOCAyMy43NzI4IDQwLjE2OTggMTkuNjM5MSAzNy42NTYxQzE1LjUwNTMgMzUuMTQyNSAxNC4xOTA3IDI5Ljc1MSAxNi43MDI3IDI1LjYxNDFMMjQuNjc5NiAxMi40Nzc1WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zMC4yODkyIDMzLjg3NThMMzguMjY2IDIwLjczOTJDNDAuMzEzOCAxNy4zNjY3IDM5LjI0MjEgMTIuOTcxNiAzNS44NzIzIDEwLjkyMjVDMzIuNTAyNSA4Ljg3MzM1IDI4LjExMDYgOS45NDYxMSAyNi4wNjI3IDEzLjMxODZMMTguMDg1OSAyNi40NTUyQzE2LjAzODEgMjkuODI3NiAxNy4xMDk4IDM0LjIyMjcgMjAuNDc5NiAzNi4yNzE4QzIzLjg0OTUgMzguMzIxIDI4LjI0MTQgMzcuMjQ4MiAzMC4yODkyIDMzLjg3NThaTTM2LjcxMjggOS41MzgyMUMzMi41NzkxIDcuMDI0NTUgMjcuMTkxNiA4LjM0MDQ5IDI0LjY3OTYgMTIuNDc3NUwxNi43MDI3IDI1LjYxNDFDMTQuMTkwNyAyOS43NTEgMTUuNTA1MyAzNS4xNDI1IDE5LjYzOTEgMzcuNjU2MUMyMy43NzI4IDQwLjE2OTggMjkuMTYwMyAzOC44NTM4IDMxLjY3MjQgMzQuNzE2OUwzOS42NDkyIDIxLjU4MDNDNDIuMTYxMiAxNy40NDMzIDQwLjg0NjYgMTIuMDUxOSAzNi43MTI4IDkuNTM4MjFaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMxLjQzODkgMTkuNjczN0MzMS44MTcgMTkuOTEyMiAzMS45MzA0IDIwLjQxMjIgMzEuNjkyMSAyMC43OTA3TDE2LjExOTIgNDUuNTIzMkMxNS44ODEgNDUuOTAxNyAxNS4zODEzIDQ2LjAxNTEgMTUuMDAzMSA0NS43NzY3QzE0LjYyNSA0NS41MzgzIDE0LjUxMTYgNDUuMDM4MiAxNC43NDk5IDQ0LjY1OThMMzAuMzIyOCAxOS45MjcyQzMwLjU2MSAxOS41NDg4IDMxLjA2MDcgMTkuNDM1MyAzMS40Mzg5IDE5LjY3MzdaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMzLjEwNTEgMzAuOTk0OUMzMy4xNzc1IDMxLjM2MDYgMzIuOTQgMzEuNzE1OCAzMi41NzQ2IDMxLjc4ODJDMjcuNzM0NyAzMi43NDc4IDI1LjMxMyAzMi4xMzk0IDI0LjI2ODcgMzEuNDA0NEMyMy45NjQxIDMxLjE5IDIzLjg5MDggMzAuNzY4OSAyNC4xMDUgMzAuNDY0QzI0LjMxOTMgMzAuMTU5IDI0Ljc0IDMwLjA4NTcgMjUuMDQ0NyAzMC4zMDAxQzI1LjYyNzEgMzAuNzEgMjcuNTgxMSAzMS40MDIxIDMyLjMxMjYgMzAuNDY0QzMyLjY3NzkgMzAuMzkxNSAzMy4wMzI4IDMwLjYyOTIgMzMuMTA1MSAzMC45OTQ5WiIgZmlsbD0iYmxhY2siPjwvcGF0aD4KPC9zdmc+) ![SQLite Cloud](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTQiIGhlaWdodD0iNTQiIHZpZXdCb3g9IjAgMCA1NCA1NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQ4LjQ2MDggMjdDNDguNDYwOCAzOC44Nzc5IDM4Ljg0IDQ4LjUgMjYuOTgwNCA0OC41QzE1LjEyMDkgNDguNSA1LjUgMzguODc3OSA1LjUgMjdDNS41IDE1LjEyMjEgMTUuMTIwOSA1LjUgMjYuOTgwNCA1LjVDMzguODQgNS41IDQ4LjQ2MDggMTUuMTIyMSA0OC40NjA4IDI3WiIgZmlsbD0iI0NGRTJGOCIgc3Ryb2tlPSIjQ0ZFMkY4IiBzdHJva2Utd2lkdGg9IjExIj48L3BhdGg+CjxwYXRoIGQ9Ik0yNC42Nzk2IDEyLjQ3NzVDMjcuMTkxNiA4LjM0MDQ5IDMyLjU3OTEgNy4wMjQ1NSAzNi43MTI4IDkuNTM4MjFDNDAuODQ2NiAxMi4wNTE5IDQyLjE2MTIgMTcuNDQzMyAzOS42NDkyIDIxLjU4MDNMMzEuNjcyNCAzNC43MTY5QzI5LjE2MDMgMzguODUzOCAyMy43NzI4IDQwLjE2OTggMTkuNjM5MSAzNy42NTYxQzE1LjUwNTMgMzUuMTQyNSAxNC4xOTA3IDI5Ljc1MSAxNi43MDI3IDI1LjYxNDFMMjQuNjc5NiAxMi40Nzc1WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zMC4yODkyIDMzLjg3NThMMzguMjY2IDIwLjczOTJDNDAuMzEzOCAxNy4zNjY3IDM5LjI0MjEgMTIuOTcxNiAzNS44NzIzIDEwLjkyMjVDMzIuNTAyNSA4Ljg3MzM1IDI4LjExMDYgOS45NDYxMSAyNi4wNjI3IDEzLjMxODZMMTguMDg1OSAyNi40NTUyQzE2LjAzODEgMjkuODI3NiAxNy4xMDk4IDM0LjIyMjcgMjAuNDc5NiAzNi4yNzE4QzIzLjg0OTUgMzguMzIxIDI4LjI0MTQgMzcuMjQ4MiAzMC4yODkyIDMzLjg3NThaTTM2LjcxMjggOS41MzgyMUMzMi41NzkxIDcuMDI0NTUgMjcuMTkxNiA4LjM0MDQ5IDI0LjY3OTYgMTIuNDc3NUwxNi43MDI3IDI1LjYxNDFDMTQuMTkwNyAyOS43NTEgMTUuNTA1MyAzNS4xNDI1IDE5LjYzOTEgMzcuNjU2MUMyMy43NzI4IDQwLjE2OTggMjkuMTYwMyAzOC44NTM4IDMxLjY3MjQgMzQuNzE2OUwzOS42NDkyIDIxLjU4MDNDNDIuMTYxMiAxNy40NDMzIDQwLjg0NjYgMTIuMDUxOSAzNi43MTI4IDkuNTM4MjFaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMxLjQzODkgMTkuNjczN0MzMS44MTcgMTkuOTEyMiAzMS45MzA0IDIwLjQxMjIgMzEuNjkyMSAyMC43OTA3TDE2LjExOTIgNDUuNTIzMkMxNS44ODEgNDUuOTAxNyAxNS4zODEzIDQ2LjAxNTEgMTUuMDAzMSA0NS43NzY3QzE0LjYyNSA0NS41MzgzIDE0LjUxMTYgNDUuMDM4MiAxNC43NDk5IDQ0LjY1OThMMzAuMzIyOCAxOS45MjcyQzMwLjU2MSAxOS41NDg4IDMxLjA2MDcgMTkuNDM1MyAzMS40Mzg5IDE5LjY3MzdaIiBmaWxsPSJibGFjayI+PC9wYXRoPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMzLjEwNTEgMzAuOTk0OUMzMy4xNzc1IDMxLjM2MDYgMzIuOTQgMzEuNzE1OCAzMi41NzQ2IDMxLjc4ODJDMjcuNzM0NyAzMi43NDc4IDI1LjMxMyAzMi4xMzk0IDI0LjI2ODcgMzEuNDA0NEMyMy45NjQxIDMxLjE5IDIzLjg5MDggMzAuNzY4OSAyNC4xMDUgMzAuNDY0QzI0LjMxOTMgMzAuMTU5IDI0Ljc0IDMwLjA4NTcgMjUuMDQ0NyAzMC4zMDAxQzI1LjYyNzEgMzAuNzEgMjcuNTgxMSAzMS40MDIxIDMyLjMxMjYgMzAuNDY0QzMyLjY3NzkgMzAuMzkxNSAzMy4wMzI4IDMwLjYyOTIgMzMuMTA1MSAzMC45OTQ5WiIgZmlsbD0iYmxhY2siPjwvcGF0aD4KPC9zdmc+) ](https://driz.link/sqlitecloud)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Upstash](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/upstash)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Lokalise](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/lokalise)[ ![](data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJBcnR3b3JrIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNzkzLjggODcxLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDc5My44IDg3MS41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0Y1NjQwQzt9Cjwvc3R5bGU+CjxnPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM5Ni45LDM1Ni4xSDIyNy4yYy0xNi42LDAtMzAtMTMuNC0zMC0zMHYtOTkuOGMwLTE2LjYsMTMuNC0zMCwzMC0zMGgxMzkuN2MxNi42LDAsMzAsMTMuNCwzMCwzMFYzNTYuMXoiLz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik01NjYuNiw1MTUuOEgzOTYuOVYzNTYuMWgxNjkuN2MxNi41LDAsMjkuOSwxMy40LDI5LjksMjkuOXY5OS44QzU5Ni41LDUwMi40LDU4My4xLDUxNS44LDU2Ni42LDUxNS44eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM2Ni45LDY3NS42SDIyNy4yYy0xNi41LDAtMjkuOS0xMy40LTI5LjktMjkuOXYtOTkuOGMwLTE2LjUsMTMuNC0yOS45LDI5LjktMjkuOWgxNjkuN3YxMjkuOAoJCUMzOTYuOSw2NjIuMSwzODMuNSw2NzUuNiwzNjYuOSw2NzUuNnoiLz4KPC9nPgo8L3N2Zz4=) ![Replit](data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJBcnR3b3JrIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNzkzLjggODcxLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDc5My44IDg3MS41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0Y1NjQwQzt9Cjwvc3R5bGU+CjxnPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM5Ni45LDM1Ni4xSDIyNy4yYy0xNi42LDAtMzAtMTMuNC0zMC0zMHYtOTkuOGMwLTE2LjYsMTMuNC0zMCwzMC0zMGgxMzkuN2MxNi42LDAsMzAsMTMuNCwzMCwzMFYzNTYuMXoiLz4KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik01NjYuNiw1MTUuOEgzOTYuOVYzNTYuMWgxNjkuN2MxNi41LDAsMjkuOSwxMy40LDI5LjksMjkuOXY5OS44QzU5Ni41LDUwMi40LDU4My4xLDUxNS44LDU2Ni42LDUxNS44eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTM2Ni45LDY3NS42SDIyNy4yYy0xNi41LDAtMjkuOS0xMy40LTI5LjktMjkuOXYtOTkuOGMwLTE2LjUsMTMuNC0yOS45LDI5LjktMjkuOWgxNjkuN3YxMjkuOAoJCUMzOTYuOSw2NjIuMSwzODMuNSw2NzUuNiwzNjYuOSw2NzUuNnoiLz4KPC9nPgo8L3N2Zz4=) ](https://driz.link/replit)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![Sentry](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/sentry)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQuNzIwNDcgMEMyLjExMzQ0IDAgMCAyLjExMzQ0IDAgNC43MjA0N1YxOS4yNzk1QzAgMjEuODg2NiAyLjExMzQ0IDI0IDQuNzIwNDcgMjRIMTkuMjc5NUMyMS44ODY2IDI0IDI0IDIxLjg4NjYgMjQgMTkuMjc5NVY0LjcyMDQ3QzI0IDIuMTEzNDQgMjEuODg2NiAwIDE5LjI3OTUgMEg0LjcyMDQ3Wk05LjMwMjA0IDUuMDE1NjNWNy44NDM2N0g2Ljc0OTk4VjEwLjMyNjhDNi43NDk5OCAxMC44NDg3IDYuOTQzNzMgMTEuMDEzNCA3LjA2OTUxIDExLjEyMDRDNy4xMDI4NSAxMS4xNDg3IDcuMTMxMzkgMTEuMTczIDcuMTUwMzEgMTEuMTk4OEw5LjI3NzAyIDEzLjM4MTRINi43NDk5OFYxNi4xNzk4SDkuMjc3MDJWMTkuMDA3OEgxNC43MDYzVjE2LjE3OThIOS4yNzcwMlYxMy4zODE0SDE0LjAzNUMxNC42OTM4IDEzLjM4MTQgMTQuNjkzOCAxNC4xNzk1IDE0LjY5MzggMTQuNTQ0MVYxNi4xNzk4SDE3LjI0NThWMTMuNjk2N0MxNy4yNDU4IDEzLjE3NDggMTcuMDUyMSAxMy4wMTAxIDE2LjkyNjMgMTIuOTAzMUMxNi44OTMgMTIuODc0NyAxNi44NjQ0IDEyLjg1MDUgMTYuODQ1NSAxMi44MjQ3TDE0LjY5MzggMTAuNjQyMUgxNy4yNUwxNy4yNDU4IDcuODQzNjdIMTQuNzA2M0wxNC42OTM4IDEwLjY0MjFIOS45NjA4OEM5LjMwMjA0IDEwLjY0MjEgOS4zMDIwNCA5Ljg0Mzk1IDkuMzAyMDQgOS40NzkzNVY3Ljg0MzY3SDE0LjcwNjNWNS4wMTU2M0g5LjMwMjA0WiIgZmlsbD0iI0Y5NzMxNiIvPjwvc3ZnPg==) ![Sevalla](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTQuNzIwNDcgMEMyLjExMzQ0IDAgMCAyLjExMzQ0IDAgNC43MjA0N1YxOS4yNzk1QzAgMjEuODg2NiAyLjExMzQ0IDI0IDQuNzIwNDcgMjRIMTkuMjc5NUMyMS44ODY2IDI0IDI0IDIxLjg4NjYgMjQgMTkuMjc5NVY0LjcyMDQ3QzI0IDIuMTEzNDQgMjEuODg2NiAwIDE5LjI3OTUgMEg0LjcyMDQ3Wk05LjMwMjA0IDUuMDE1NjNWNy44NDM2N0g2Ljc0OTk4VjEwLjMyNjhDNi43NDk5OCAxMC44NDg3IDYuOTQzNzMgMTEuMDEzNCA3LjA2OTUxIDExLjEyMDRDNy4xMDI4NSAxMS4xNDg3IDcuMTMxMzkgMTEuMTczIDcuMTUwMzEgMTEuMTk4OEw5LjI3NzAyIDEzLjM4MTRINi43NDk5OFYxNi4xNzk4SDkuMjc3MDJWMTkuMDA3OEgxNC43MDYzVjE2LjE3OThIOS4yNzcwMlYxMy4zODE0SDE0LjAzNUMxNC42OTM4IDEzLjM4MTQgMTQuNjkzOCAxNC4xNzk1IDE0LjY5MzggMTQuNTQ0MVYxNi4xNzk4SDE3LjI0NThWMTMuNjk2N0MxNy4yNDU4IDEzLjE3NDggMTcuMDUyMSAxMy4wMTAxIDE2LjkyNjMgMTIuOTAzMUMxNi44OTMgMTIuODc0NyAxNi44NjQ0IDEyLjg1MDUgMTYuODQ1NSAxMi44MjQ3TDE0LjY5MzggMTAuNjQyMUgxNy4yNUwxNy4yNDU4IDcuODQzNjdIMTQuNzA2M0wxNC42OTM4IDEwLjY0MjFIOS45NjA4OEM5LjMwMjA0IDEwLjY0MjEgOS4zMDIwNCA5Ljg0Mzk1IDkuMzAyMDQgOS40NzkzNVY3Ljg0MzY3SDE0LjcwNjNWNS4wMTU2M0g5LjMwMjA0WiIgZmlsbD0iI0Y5NzMxNiIvPjwvc3ZnPg==) ](https://driz.link/sevalla)[ ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ![GibsonAI](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIwMCIgaGVpZ2h0PSIxMjAwIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjwvc3ZnPg==) ](https://driz.link/gibsonai)

Product by Drizzle Team 

[ One Dollar Stats $1 per mo web analytics christmas   
deal  ](https://driz.link/onedollarstats)

# Indexes & Constraints

## Constraints

SQL constraints are the rules enforced on table columns. They are used to prevent invalid data from being entered into the database.

This ensures the accuracy and reliability of your data in the database.

### Default

The `DEFAULT` clause specifies a default value to use for the column if no value provided by the user when doing an `INSERT`. If there is no explicit `DEFAULT` clause attached to a column definition, then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`, a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { sql } from "drizzle-orm";
    import { integer, uuid, pgTable } from "drizzle-orm/pg-core";
    
    const table = pgTable('table', {
      integer1: integer('integer1').default(42),
      integer2: integer('integer2').default(sql`'42'::integer`),
      uuid1: uuid('uuid1').defaultRandom(),
      uuid2: uuid('uuid2').default(sql`gen_random_uuid()`),
    });
    
    
    CREATE TABLE IF NOT EXISTS "table" (
      "integer1" integer DEFAULT 42,
      "integer2" integer DEFAULT '42'::integer,
      "uuid1" uuid DEFAULT gen_random_uuid(),
      "uuid2" uuid DEFAULT gen_random_uuid()
    );
    
    
    import { sql } from "drizzle-orm";
    import { int, time, mysqlTable } from "drizzle-orm/mysql-core";
    
    const table = mysqlTable("table", {
      int: int("int").default(42),
      time: time("time").default(sql`cast("14:06:10" AS TIME)`),
    });
    
    
    CREATE TABLE `table` (
      `int` int DEFAULT 42,
      `time` time DEFAULT cast("14:06:10" AS TIME)
    );
    
    
    import { sql } from "drizzle-orm";
    import { integer, sqliteTable } from "drizzle-orm/sqlite-core";
    
    const table = sqliteTable('table', {
      int1: integer('int1').default(42),
      int2: integer('int2').default(sql`(abs(42))`)
    });
    
    
    
    CREATE TABLE `table` (
      `int1` integer DEFAULT 42
      `int2` integer DEFAULT (abs(42))
    );
    
    
    import { sql } from "drizzle-orm";
    import { int, time, singlestoreTable } from "drizzle-orm/singlestore-core";
    
    const table = singlestoreTable("table", {
      int: int("int").default(42),
      time: time("time").default(sql`cast("14:06:10" AS TIME)`),
    });
    
    
    CREATE TABLE `table` (
      `int` int DEFAULT 42,
      `time` time DEFAULT cast("14:06:10" AS TIME)
    );

### Not null

By default, a column can hold **NULL** values. The `NOT NULL` constraint enforces a column to **NOT** accept **NULL** values.

This enforces a field to always contain a value, which means that you cannot insert a new record, or update a record without adding a value to this field.

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { integer, pgTable } from "drizzle-orm/pg-core";
    
    const table = pgTable('table', {
      integer: integer('integer').notNull(),
    });
    
    
    CREATE TABLE IF NOT EXISTS "table" (
      "integer" integer NOT NULL
    );
    
    
    import { int, mysqlTable } from "drizzle-orm/mysql-core";
    
    const table = mysqlTable('table', {
      int: int('int').notNull(),
    });
    
    
    CREATE TABLE `table` (
      `int` int NOT NULL
    );
    
    
    const table = sqliteTable('table', { 
      numInt: integer('numInt').notNull() 
    });
    
    
    CREATE TABLE table (
      `numInt` integer NOT NULL
    );
    
    
    import { int, singlestoreTable } from "drizzle-orm/singlestore-core";
    
    const table = singlestoreTable('table', {
      int: int('int').notNull(),
    });
    
    
    CREATE TABLE `table` (
      `int` int NOT NULL
    );

### Unique

The `UNIQUE` constraint ensures that all values in a column are different.

Both the `UNIQUE` and `PRIMARY KEY` constraints provide a guarantee for uniqueness for a column or set of columns.

A `PRIMARY KEY` constraint automatically has a `UNIQUE` constraint.

You can have many `UNIQUE` constraints per table, but only one `PRIMARY KEY` constraint per table.

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { integer, text, unique, pgTable } from "drizzle-orm/pg-core";
    
    export const user = pgTable('user', {
      id: integer('id').unique(),
    });
    
    export const table = pgTable('table', {
      id: integer('id').unique('custom_name'),
    });
    
    export const composite = pgTable('composite_example', {
      id: integer('id'),
      name: text('name'),
    }, (t) => [
      unique().on(t.id, t.name),
      unique('custom_name').on(t.id, t.name)
    ]);
    
    // In Postgres 15.0+ NULLS NOT DISTINCT is available
    // This example demonstrates both available usages
    export const userNulls = pgTable('user_nulls_example', {
      id: integer('id').unique("custom_name", { nulls: 'not distinct' }),
    }, (t) => [
      unique().on(t.id).nullsNotDistinct()
    ]);
    
    
    CREATE TABLE IF NOT EXISTS "composite_example" (
        "id" integer,
      "name" text,
      CONSTRAINT "composite_example_id_name_unique" UNIQUE("id","name"),
      CONSTRAINT "custom_name" UNIQUE("id","name")
    );
    
    CREATE TABLE IF NOT EXISTS "table" (
    	"id" integer,
    	CONSTRAINT "custom_name" UNIQUE("id")
    );
    
    CREATE TABLE IF NOT EXISTS "user" (
    	"id" integer,
    	CONSTRAINT "user_id_unique" UNIQUE("id")
    );
    
    CREATE TABLE IF NOT EXISTS "user_nulls_example" (
      "id" integer,
      CONSTRAINT "custom_name" UNIQUE NULLS NOT DISTINCT("id"),
      CONSTRAINT "user_nulls_example_id_unique" UNIQUE NULLS NOT DISTINCT("id")
    );
    
    
    import { int, varchar, unique, mysqlTable } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable('user', {
      id: int('id').unique(),
    });
    
    export const table = mysqlTable('table', {
      id: int('id').unique('custom_name'),
    });
    
    export const composite = mysqlTable('composite_example', {
      id: int('id'),
      name: varchar('name', { length: 256 }),
    }, (t) => [
      unique().on(t.id, t.name),
      unique('custom_name').on(t.id, t.name)
    ]);
    
    
    CREATE TABLE `user` (
    	`id` int,
    	CONSTRAINT `user_id_unique` UNIQUE(`id`)
    );
    
    CREATE TABLE `table` (
    	`id` int,
    	CONSTRAINT `custom_name` UNIQUE(`id`)
    );
    
    CREATE TABLE `composite_example` (
      `id` int,
      `name` varchar(256),
      CONSTRAINT `composite_example_id_name_unique` UNIQUE(`id`,`name`),
      CONSTRAINT `custom_name` UNIQUE(`id`,`name`)
    );
    
    
    import { int, text, unique, sqliteTable } from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable('user', {
      id: int('id').unique(),
    });
    
    export const table = sqliteTable('table', {
      id: int('id').unique('custom_name'),
    });
    
    export const composite = sqliteTable('composite_example', {
      id: int('id'),
      name: text('name'),
    }, (t) => [
      unique().on(t.id, t.name),
      unique('custom_name').on(t.id, t.name)
    ]);
    
    
    CREATE TABLE `user` (
        `id` integer
    );
    
    CREATE TABLE `table` (
    	`id` integer
    );
    
    CREATE TABLE `composite_example` (
    	`id` integer,
    	`name` text
    );
    
    CREATE UNIQUE INDEX `composite_example_id_name_unique` ON `composite_example` (`id`,`name`);
    CREATE UNIQUE INDEX `custom_name` ON `composite_example` (`id`,`name`);
    CREATE UNIQUE INDEX `custom_name` ON `table` (`id`);
    CREATE UNIQUE INDEX `user_id_unique` ON `user` (`id`);
    
    
    import { int, varchar, unique, singlestoreTable } from "drizzle-orm/singlestore-core";
    
    export const user = singlestoreTable('user', {
      id: int('id').unique(),
    });
    
    export const table = singlestoreTable('table', {
      id: int('id').unique('custom_name'),
    });
    
    export const composite = singlestoreTable('composite_example', {
      id: int('id'),
      name: varchar('name', { length: 256 }),
    }, (t) => [
      unique().on(t.id, t.name),
      unique('custom_name').on(t.id, t.name)
    ]);
    
    
    CREATE TABLE `user` (
    	`id` int,
    	CONSTRAINT `user_id_unique` UNIQUE(`id`)
    );
    
    CREATE TABLE `table` (
    	`id` int,
    	CONSTRAINT `custom_name` UNIQUE(`id`)
    );
    
    CREATE TABLE `composite_example` (
      `id` int,
      `name` varchar(256),
      CONSTRAINT `composite_example_id_name_unique` UNIQUE(`id`,`name`),
      CONSTRAINT `custom_name` UNIQUE(`id`,`name`)
    );

### Check

The `CHECK` constraint is used to limit the value range that can be placed in a column.

If you define a `CHECK` constraint on a column it will allow only certain values for this column.

If you define a `CHECK` constraint on a table it can limit the values in certain columns based on values in other columns in the row.

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { sql } from "drizzle-orm";
    import { check, integer, pgTable, text, uuid } from "drizzle-orm/pg-core";
    
    export const users = pgTable(
      "users",
      {
        id: uuid().defaultRandom().primaryKey(),
        username: text().notNull(),
        age: integer(),
      },
      (table) => [
        check("age_check1", sql`${table.age} > 21`),
      ]
    );
    
    
    CREATE TABLE IF NOT EXISTS "users" (
        "id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
        "username" text NOT NULL,
        "age" integer,
        CONSTRAINT "age_check1" CHECK ("users"."age" > 21)
    );
    
    
    import { sql } from "drizzle-orm";
    import { check, int, mysqlTable, text } from "drizzle-orm/mysql-core";
    
    export const users = mysqlTable(
      "users",
      {
        id: int().primaryKey(),
        username: text().notNull(),
        age: int(),
      },
      (table) => [
        check("age_check1", sql`${table.age} > 21`)
      ]
    );
    
    
    CREATE TABLE `users` (
        `id` int NOT NULL,
        `username` text NOT NULL,
        `age` int,
        CONSTRAINT `users_id` PRIMARY KEY(`id`),
        CONSTRAINT `age_check1` CHECK(`users`.`age` > 21)
    );
    
    
    import { sql } from "drizzle-orm";
    import { check, int, sqliteTable, text } from "drizzle-orm/sqlite-core";
    
    export const users = sqliteTable(
      "users",
      {
        id: int().primaryKey(),
        username: text().notNull(),
        age: int(),
      },
      (table) => [
        check("age_check1", sql`${table.age} > 21`)
      ]
    );
    
    
    CREATE TABLE `users` (
        `id` integer PRIMARY KEY NOT NULL,
        `username` text NOT NULL,
        `age` integer,
        CONSTRAINT "age_check1" CHECK("users"."age" > 21)
    );

Currently not supported in SingleStore

### Primary Key

The `PRIMARY KEY` constraint uniquely identifies each record in a table.  
Primary keys must contain `UNIQUE` values, and cannot contain `NULL` values.

A table can have only **ONE** primary key; and in the table, this primary key can consist of single or multiple columns (fields).

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { serial, text, pgTable } from "drizzle-orm/pg-core";
    
    const user = pgTable('user', {
      id: serial('id').primaryKey(),
    });
    
    const table = pgTable('table', {
      id: text('cuid').primaryKey(),
    });
    
    
    CREATE TABLE IF NOT EXISTS "user" (
      "id" serial PRIMARY KEY
    );
    
    CREATE TABLE IF NOT EXISTS "table" (
      "cuid" text PRIMARY KEY
    );
    
    
    import { int, text, mysqlTable } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable("user", {
      id: int("id").autoincrement().primaryKey(),
    })
    
    export const table = mysqlTable("table", {
      cuid: text("cuid").primaryKey(),
    })
    
    
    CREATE TABLE `user` (
      `id` int AUTO_INCREMENT PRIMARY KEY NOT NULL
    );
    
    CREATE TABLE `table` (
      `cuid` text PRIMARY KEY NOT NULL
    );
    
    
    import { integer, sqliteTable } from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey(),
    })
    
    export const pet = sqliteTable("pet", {
      id: integer("id").primaryKey(),
    })
    
    
    CREATE TABLE `user` (
      `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL
    );
    
    CREATE TABLE `pet` (
      `id` integer PRIMARY KEY AUTOINCREMENT
    )
    
    
    import { int, text, singlestoreTable } from "drizzle-orm/singlestore-core";
    
    export const user = singlestoreTable("user", {
      id: int("id").autoincrement().primaryKey(),
    })
    
    export const table = singlestoreTable("table", {
      cuid: text("cuid").primaryKey(),
    })
    
    
    CREATE TABLE `user` (
      `id` int AUTO_INCREMENT PRIMARY KEY NOT NULL
    );
    
    CREATE TABLE `table` (
      `cuid` text PRIMARY KEY NOT NULL
    );

### Composite Primary Key

Just like `PRIMARY KEY`, composite primary key uniquely identifies each record in a table using multiple fields.

Drizzle ORM provides a standalone `primaryKey` operator for that:

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { serial, text, integer, primaryKey, pgTable } from "drizzle-orm/pg-core";
    
    export const user = pgTable("user", {
      id: serial("id").primaryKey(),
      name: text("name"),
    });
    
    export const book = pgTable("book", {
      id: serial("id").primaryKey(),
      name: text("name"),
    });
    
    export const booksToAuthors = pgTable("books_to_authors", {
      authorId: integer("author_id"),
      bookId: integer("book_id"),
    }, (table) => [
      primaryKey({ columns: [table.bookId, table.authorId] }),
      // Or PK with custom name
      primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] }),
    ]);
    
    
    ...
    
    CREATE TABLE IF NOT EXISTS "books_to_authors" (
      "author_id" integer,
      "book_id" integer,
      PRIMARY KEY("book_id","author_id")
    );
    
    ALTER TABLE "books_to_authors" ADD CONSTRAINT "custom_name" PRIMARY KEY("book_id","author_id");
    
    
    import { int, text, primaryKey, mysqlTable } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable("user", {
      id: int("id").autoincrement().primaryKey(),
      name: text("name"),
    });
    
    export const book = mysqlTable("book", {
      id: int("id").autoincrement().primaryKey(),
      name: text("name"),
    });
    
    export const booksToAuthors = mysqlTable("books_to_authors", {
      authorId: int("author_id"),
      bookId: int("book_id"),
    }, (table) => [
      primaryKey({ columns: [table.bookId, table.authorId] }),
      // Or PK with custom name
      primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] })
    ]);
    
    
    ...
    
    CREATE TABLE `books_to_authors` (
      `author_id` int,
      `book_id` int,
      PRIMARY KEY(`book_id`,`author_id`)
    );
    
    
    import { integer, text, primaryKey, sqliteTable} from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
    });
    
    export const book = sqliteTable("book", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
    });
    
    export const bookToAuthor = sqliteTable("book_to_author", {
      authorId: integer("author_id"),
      bookId: integer("book_id"),
    }, (table) => [
      primaryKey({ columns: [table.bookId, table.authorId] }),
      // Or PK with custom name
      primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] })
    ]);
    
    
    ...
    
    CREATE TABLE `book_to_author` (
      `author_id` integer,
      `book_id` integer,
      PRIMARY KEY(`book_id`, `author_id`)
    );
    
    
    import { int, text, primaryKey, mysqlTable } from "drizzle-orm/singlestore-core";
    
    export const user = singlestoreTable("user", {
      id: int("id").autoincrement().primaryKey(),
      name: text("name"),
    });
    
    export const book = singlestoreTable("book", {
      id: int("id").autoincrement().primaryKey(),
      name: text("name"),
    });
    
    export const booksToAuthors = singlestoreTable("books_to_authors", {
      authorId: int("author_id"),
      bookId: int("book_id"),
    }, (table) => [
      primaryKey({ columns: [table.bookId, table.authorId] }),
      // Or PK with custom name
      primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] }),
    ]);
    
    
    ...
    
    CREATE TABLE `books_to_authors` (
      `author_id` int,
      `book_id` int,
      PRIMARY KEY(`book_id`,`author_id`)
    );

### Foreign key

The `FOREIGN KEY` constraint is used to prevent actions that would destroy links between tables. A `FOREIGN KEY` is a field (or collection of fields) in one table, that refers to the `PRIMARY KEY` in another table. The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table.

Drizzle ORM provides several ways to declare foreign keys. You can declare them in a column declaration statement:

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { serial, text, integer, pgTable } from "drizzle-orm/pg-core";
    
    export const user = pgTable("user", {
      id: serial("id"),
      name: text("name"),
    });
    
    export const book = pgTable("book", {
      id: serial("id"),
      name: text("name"),
      authorId: integer("author_id").references(() => user.id)
    });
    
    
    import { int, text, mysqlTable } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
    });
    
    export const book = mysqlTable("book", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      authorId: int("author_id").references(() => user.id)
    });
    
    
    import { integer, text, sqliteTable } from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
    });
    
    export const book = sqliteTable("book", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      authorId: integer("author_id").references(() => user.id)
    });

Currently not supported in SingleStore

If you want to do a self reference, due to a TypeScript limitations you will have to either explicitly set return type for reference callback or use a standalone `foreignKey` operator.

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { serial, text, integer, foreignKey, pgTable, AnyPgColumn } from "drizzle-orm/pg-core";
    
    export const user = pgTable("user", {
      id: serial("id"),
      name: text("name"),
      parentId: integer("parent_id").references((): AnyPgColumn => user.id)
    });
    
    // or
    export const user = pgTable("user", {
      id: serial("id"),
      name: text("name"),
      parentId: integer("parent_id"),
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    
    
    import { int, text, foreignKey, AnyMySqlColumn, mysqlTable } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      parentId: int("parent_id").references((): AnyMySqlColumn => user.id),
    });
    
    // or
    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      parentId: int("parent_id")
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    
    
    import { integer, text, foreignKey, sqliteTable, AnySQLiteColumn } from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      parentId: integer("parent_id").references((): AnySQLiteColumn => user.id)
    });
    
    //or
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      parentId: integer("parent_id"),
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);

Currently not supported in SingleStore

To declare multicolumn foreign keys you can use a dedicated `foreignKey` operator:

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { serial, text, foreignKey, pgTable, AnyPgColumn } from "drizzle-orm/pg-core";
    
    export const user = pgTable("user", {
      firstName: text("firstName"),
      lastName: text("lastName"),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);
    
    export const profile = pgTable("profile", {
      id: serial("id").primaryKey(),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_fk"
      })
    ])
    
    
    import { int, text, primaryKey, foreignKey, mysqlTable, AnyMySqlColumn } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable("user", {
      firstName: text("firstName"),
      lastName: text("lastName"),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);
    
    export const profile = mysqlTable("profile", {
      id: int("id").autoincrement().primaryKey(),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_name"
      })
    ]);
    
    
    import { integer, text, primaryKey, foreignKey, sqliteTable, AnySQLiteColumn } from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable("user", {
      firstName: text("firstName"),
      lastName: text("lastName"),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);
    
    export const profile = sqliteTable("profile", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_name"
      })
    ]);

Currently not supported in SingleStore

## Indexes

Drizzle ORM provides API for both `index` and `unique index` declaration:

PostgreSQL 

MySQL 

SQLite 

SingleStore 
    
    
    import { serial, text, index, uniqueIndex, pgTable } from "drizzle-orm/pg-core";
    
    export const user = pgTable("user", {
      id: serial("id").primaryKey(),
      name: text("name"),
      email: text("email"),
    }, (table) => [
      index("name_idx").on(table.name),
      uniqueIndex("email_idx").on(table.email)
    ]);
    
    
    CREATE TABLE "user" (
      ...
    );
    
    CREATE INDEX "name_idx" ON "user" ("name");
    CREATE UNIQUE INDEX "email_idx" ON "user" ("email");

IMPORTANT

For versions before `[[email protected]](/cdn-cgi/l/email-protection)` and `[[email protected]](/cdn-cgi/l/email-protection)` `drizzle-kit` only supports index `name` and `on()` param.

After versions `[[email protected]](/cdn-cgi/l/email-protection)` and `[[email protected]](/cdn-cgi/l/email-protection)` all fields are supported in drizzle-kit!

Starting from 0.31.0 a new index api for Drizzle ORM provides set of all params for index creation:
    
    
    // First example, with `.on()`
    index('name')
      .on(table.column1.asc(), table.column2.nullsFirst(), ...) or .onOnly(table.column1.desc().nullsLast(), table.column2, ...)
      .concurrently()
      .where(sql``)
      .with({ fillfactor: '70' })
    
    // Second Example, with `.using()`
    index('name')
      .using('btree', table.column1.asc(), sql`lower(${table.column2})`, table.column1.op('text_ops'))
      .where(sql``) // sql expression
      .with({ fillfactor: '70' })
    
    
    import { int, text, index, uniqueIndex, mysqlTable } from "drizzle-orm/mysql-core";
    
    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      email: text("email"),
    }, (table) => [
      index("name_idx").on(table.name),
      uniqueIndex("email_idx").on(table.email),
    ]);
    
    
    CREATE TABLE `user` (
      ...
    );
    
    CREATE INDEX `name_idx` ON `user` (`name`);
    CREATE UNIQUE INDEX `email_idx` ON `user` (`email`);

IMPORTANT

As of now `drizzle-kit` only supports index `name` and `on()` param.

Drizzle ORM provides set of all params for index creation:
    
    
    // Index declaration reference
    index("name")
      .on(table.name)
      .algorythm("default") // "default" | "copy" | "inplace"
      .using("btree") // "btree" | "hash"
      .lock("default") // "none" | "default" | "exclusive" | "shared"
    
    
    import { integer, text, index, uniqueIndex, sqliteTable } from "drizzle-orm/sqlite-core";
    
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      email: text("email"),
    }, (table) => [
      index("name_idx").on(table.name),
      uniqueIndex("email_idx").on(table.email),
    ]);
    
    
    CREATE TABLE `user` (
      ...
    );
    
    CREATE INDEX `name_idx` ON `user` (`name`);
    CREATE UNIQUE INDEX `email_idx` ON `user` (`email`);

Drizzle ORM provides set of all params for index creation:
    
    
    // Index declaration reference
    index("name")
      .on(table.name)
      .where(sql`...`)
    
    
    import { int, text, index, uniqueIndex, singlestoreTable } from "drizzle-orm/singlestore-core";
    
    export const user = singlestoreTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      email: text("email"),
    }, (table) => [
      index("name_idx").on(table.name),
      uniqueIndex("email_idx").on(table.email),
    ]);
    
    
    CREATE TABLE `user` (
      ...
    );
    
    CREATE INDEX `name_idx` ON `user` (`name`);
    CREATE UNIQUE INDEX `email_idx` ON `user` (`email`);