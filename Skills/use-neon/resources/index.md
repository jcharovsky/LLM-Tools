# index

**Source URL:** https://neon.com/

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

# Ship faster with Postgres

The database developers trust, on a serverless platform designed to help you build reliable and scalable applications faster.

[Start for Free](https://console.neon.tech/signup)[Talk to Us](/contact-sales)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggc3Ryb2tlPSIjZmZmIiBzdHJva2UtbGluZWNhcD0ic3F1YXJlIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNCAyNy4zMzFINC42Njd2LTkuMzMzTTI3LjMzMyAxMy45OThWNC42NjVIMThNNS4yMzggMjYuNzYgMjYuNzYyIDUuMjM2Ii8+PC9zdmc+)

## Scaling

### Scaling

Focus on building applications with time and money-saving features like instant provisioning, autoscaling according to load, and scale to zero.

[Discover Autoscaling](/docs/introduction/autoscaling)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgZmlsbD0ibm9uZSI+PHBhdGggc3Ryb2tlPSIjZmZmIiBzdHJva2UtbGluZWNhcD0ic3F1YXJlIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0yLjUgMjIuNWgyMk0xOS41IDEwLjVoLTVhNSA1IDAgMCAwLTUgNXY3Ii8+PGNpcmNsZSBjeD0iMjgiIGN5PSIyMi41IiByPSIzIiBzdHJva2U9IiNmZmYiIHN0cm9rZS13aWR0aD0iMiIvPjxjaXJjbGUgY3g9IjIzIiBjeT0iMTAuNSIgcj0iMyIgc3Ryb2tlPSIjZmZmIiBzdHJva2Utd2lkdGg9IjIiLz48L3N2Zz4=)

## Branching

### Branching

Instantly branch your data and schema to access isolated DB copies for development, CI/CD, and schema migrations with copy-on-write storage.

[Explore Branching](/docs/introduction/branching)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg.3d093f83.jpg&w=3840&q=100&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## Trusted in production by thousands of teams.

  * ![Pepsi](/_next/static/svgs/81880c06f0017bb1727dced789f3342e.svg)
  * ![Zimmer Biomet](/_next/static/svgs/7f02b9671daf78d29a1aff9900c27428.svg)
  * ![Retool](/_next/static/svgs/784a74e2862af9f295d83c6460a25ea3.svg)
  * ![Boston Consulting Group](/_next/static/svgs/0ec024e581a9ad1a8fd4067237130f92.svg)
  * ![Outfront Media](/_next/static/svgs/357153973509682f51a32c7f5829b2d8.svg)
  * ![Replit](/_next/static/svgs/bc51018c075b240eb3bd1032ea0c8b3b.svg)



## Instant Provisioning

No waiting. No config.

Provisioned in 300ms

postgresql://example@ep-938132.eu-central-1.aws.neon.tech/primary

## Works with   
your stack

Integrate it into your language or framework within minutes and unlock a simpler developer workflow.

[See all examples](/docs/guides/guides-intro)

![](/_next/static/svgs/10dc59376dbc4407529140b059de0c37.svg)Next.js![](/_next/static/svgs/f586b4ee268939235809c4f8e9634251.svg)Drizzle![](/_next/static/svgs/6ade259658926475c0eb792e61111c98.svg)Prisma![](/_next/static/svgs/bee5282584f26a60944dfc6f92efb527.svg)Python![](/_next/static/svgs/f1fc4356fcf3e301a0b84466845bbe8f.svg)Ruby![](/_next/static/svgs/39d40e4342ea5abb651ec618fd159053.svg)Rust![](/_next/static/svgs/4914c82061c06def4904591775d95785.svg)Go
    
    
    import { neon } from '@neondatabase/serverless';
    
    export async function GET() {
        const sql = neon(process.env.DATABASE_URL);
    
        const rows = await sql`SELECT * FROM posts`;
    
        return Response.json({ rows })
    }

## Lightning fast. Edge ready.

![](data:image/svg+xml;charset=utf-8,%3Csvg width='828' height='684' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![](data:image/svg+xml;charset=utf-8,%3Csvg width='828' height='684' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![](data:image/svg+xml;charset=utf-8,%3Csvg width='351' height='298' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

The Neon serverless driver, designed for fast queries over HTTP

`import { neon } from '@neondatabase/ serverless';const sql = neon('postgresql:// usr:pass@proj.us-east-2.aws.neon.tech/db');const posts = await sql('SELECT * FROM posts');`[Get the Serverless Driver](/docs/serverless/serverless-driver)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fphone-camera.27658a1d.png&w=384&q=100&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## Better database.  
For modern workflows.

![](data:image/svg+xml;charset=utf-8,%3Csvg width='960' height='384' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

**Boost your performance with instant [read replicas](/docs/introduction/read-replicas).** They scale down to zero when idle and don't use additional storage.

**Easy database ops via the [API](https://api-docs.neon.tech/reference/getting-started-with-neon-api) and [CLI](/docs/reference/neon-cli).** Manage thousands of databases programmatically.

**Instant [Point-in-time recovery](/blog/point-in-time-recovery-in-postgres).** Up to 30 days granularity down to the transaction or second.

## Unleashing Cutting-  
Edge AI Applications.

The HNSW index algorithm streamlines performance, making high-dimensional vector search remarkably efficient.

[Power your AI apps with Postgres](/ai)

![](data:image/svg+xml;charset=utf-8,%3Csvg width='1160' height='1160' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

ReliableScalabilityHigh compatibilityBlazingly fast searchWorks with PGVECTORWorks with langchain;

## Thousands of databases.  
Zero overhead.

![](data:image/svg+xml;charset=utf-8,%3Csvg width='1920' height='474' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

Use the Neon API to deploy [database-per-tenant architectures](/blog/how-retool-uses-retool-and-the-neon-api-to-manage-300k-postgres-databases). Scale to fleets of thousands of databases without touching a server. Rest easy knowing scale to zero keeps costs low.

## Industry leaders  
trust Neon

[Dive into success stories](/case-studies)

![Supergood.ai](/_next/static/svgs/03731b59b0dbf4dc3b09def19e5d25ec.svg)

> Neon allows us to develop much faster than we’ve even been used to

![Alex Klarfeld](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Falex-klarfeld.b8bd71ba.jpg&w=64&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

Alex Klarfeld – CEO and co-founder of Supergood.ai

![Koyeb](/_next/static/svgs/db1030bbd306eba437adb54691e31dea.svg)

> Neon's serverless philosophy is aligned with our vision: no infrastructure to manage, no servers to provision, no database cluster to maintain

![Edouard Bonlieu](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fedouard-bonlieu.d69ae917.jpg&w=64&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

Edouard Bonlieu – Co-founder at Koyeb

![Topo.io](/_next/static/svgs/f232265d4bedb9cce70f66a4838ee013.svg)

> The killer feature that convinced us to use Neon was branching: it keeps our engineering velocity high

![Léonard Henriquez](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fleonard-henriquez.1ab5608f.jpg&w=64&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

Léonard Henriquez – Co-founder and CTO, Topo.io

![Retool](/_next/static/svgs/5e43faa91c0e64a308dad433f12b6cc7.svg)

> We've been able to automate virtually all database tasks via the Neon API, saving us a tremendous amount of time and engineering effort

![Himanshu Bhandoh](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhimanshu-bhandoh.95baee7b.jpg&w=64&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

Himanshu Bhandoh – Software Engineer at Retool

## Trusted Postgres

[![](/_next/static/media/github.e7e489f2.jpg)neondatabase/neon](https://github.com/neondatabase/neon)

![](/_next/static/media/digit.d4d71d86.jpg)

**Databases under management.** Postgres for the World.

![](/_next/static/media/elephant.c07449d7.jpg)

**100% Postgres.** Not a fork, not a rewrite.

[![](/_next/static/media/soc.bf1f4421.jpg)![](/_next/static/media/soc-md.43810ef9.jpg)SOC2 Compliance](/blog/soc2-type2)

## Features of tomorrow.  
Available today.

[Get Started](https://console.neon.tech/signup)