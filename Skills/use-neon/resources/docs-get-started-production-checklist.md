# get-started-production-checklist

**Source URL:** https://neon.com/docs/get-started/production-checklist

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/4 - Ready for production

# Getting ready for production

A checklist of recommended settings to optimize performance, security, and reliability

## Production checklist

0%

  * ### 1\. Set a compute size that can handle production traffic

Make sure your default branch can handle production traffic. A higher minimum compute can help you avoid performance bottlenecks.

  * ### 2\. Enable autoscaling to handle usage spikes

Set your compute to automatically scale up, allowing your app to handle traffic surges and stay performant without manual scaling.

  * ### 3\. Disable scale to zero

Scale to zero turns off your compute after a period of inactivity. Ideal for development or other environments with bursty usage.

  * ### 4\. Use a pooled connection

Increase your database's ability to handle concurrent connections by using connection pooling.

  * ### 5\. Increase your project's restore window to 7 days

Protect your production data from accidental loss. Keep at least a 7-day restore window for quick data recovery and analysis.

  * ### 6\. Restrict database access to trusted IPs

Secure your database by limiting connections to trusted IP addresses.

  * ### 7\. Set up metrics export

Export Neon metrics to Datadog or any OTEL-compatible platform like Grafana Cloud or New Relic to centralize database monitoring with your existing observability stack.

  * ### 8\. Install pg_stat_statements

Enable query performance monitoring to track execution times and frequency.

  * ### 9\. Ensure your app reconnects after your database restarts

Verify your application handles compute restarts gracefully.

  * ### 10\. Upgrade to get priority support

Get support for your production database with a Scale plan.

  * ### 11\. Advanced: Set up cross-region replication

For added resilience, replicate your data to a Neon project in another region. This helps prepare for regional outages, making it possible to failover to a copy of your database in a different region, if necessary.




  1. ## Set a compute size that can handle production traffic

Before your application goes to production, make sure your database has enough vCPU and memory to handle expected production load. See [How to size your compute](/docs/manage/computes#how-to-size-your-compute).

**Recommendation**

We recommend that you **fit your data in memory** and use Neon **autoscaling** :

     * Start with a compute size that can hold all your data in memory. Or try to fit at least your most frequently accessed data (your [working set](/docs/reference/glossary#working-set)).
     * Once you determine the [right size](/docs/manage/computes#how-to-size-your-compute) for your compute, use that as the **minimum compute size** for Autoscaling).

**About compute size**

A Compute Unit (CU) in Neon measures the processing power or "size" of a Neon compute. One CU includes 1 vCPU and 4 GB of RAM. Neon computes can range from **0.25** CUs to **56** CUs, depending on your [Neon plan](/docs/introduction/plans).

  2. ## Enable autoscaling to handle usage spikes

Use Neon's [autoscaling](/docs/guides/autoscaling-algorithm) feature to dynamically adjust your compute resources based on your current workload. This means you don't need to scale manually during traffic surges.

**Recommendation**

     * **Minimum compute size** : Autoscaling works best if your data can be fully cached in memory.
     * **Maximum compute size** : Set this to as a high a limit as your plan allows. You only pay for what you use.

![Autoscaling control](/_next/image?url=%2Fdocs%2Fget-started%2Fautoscaling_control.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

To get started with Autoscaling, read:

     * [Enable Autoscaling in Neon](/docs/guides/autoscaling-guide)
     * [How to size your compute](/docs/manage/computes#how-to-size-your-compute), including the [Autoscaling considerations](/docs/manage/computes#autoscaling-considerations) section.

  3. ## Disable scale to zero

Scale to zero turns off your compute after a period of inactivity. Ideal for development or other environments with bursty usage.

**Recommendation**

Disable scale to zero for production workloads. This ensures your compute is always active, preventing delays and session context resets caused by cold starts.

**Session and latency considerations**

By default, your compute scales to zero after 5 minutes. Restarts are nearly instant, but there may still be some latency (around 500 milliseconds depending on the region). Restarts will reset your session context, affecting in-memory statistics and temporary tables. While typical production loads might never go idle long enough to scale to zero, disabling this feature prevents any possible issues from cold starts or session loss.

Disabling scale to zero is available on paid plans only. See [Configuring Scale to Zero for Neon computes](/docs/guides/scale-to-zero-guide) for more detail.

  4. ## Use a pooled connection

Connection pooling with [PgBouncer](https://www.pgbouncer.org/) allows your database to handle up to 10,000 concurrent connections, reducing connection overhead and improving performance.

**Recommendation**

For production environments, enable connection pooling. This increases the number of simultaneous connections your database can handle and optimizes resource usage.

**Connection details**

Use a pooled connection string by adding `-pooler` to your endpoint ID, or simply copy the pooled connection string from the **Connect** widget in your **Project Dashboard**. Use this string as your database connection in your application's environment variables. For more information, see [Connection pooling](/docs/connect/connection-pooling).

Example connection string:
         
         postgresql://alex:AbC123dEf@ep-cool-darkness-123456-pooler.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require

  5. ## Increase your project's restore window to 7 days

Neon retains a history of changes for all branches, enabling instant restore and time travel queries. This history acts as a backup strategy, allowing recovery of lost data and viewing past database states.

**Recommendation**

Set your restore window to 7 days to ensure data integrity and quick recovery.

**Restore window details**

By default, Neon's restore window is set to **1 day**. Extending it to 7 days helps protect you against data loss, letting you recover from human or application errors that may go unnoticed for days. It can also help you comply with any industry regulations that need longer retention periods. While a longer restore window can increase storage costs, it provides exta security and recoverability for production data.

![Restore window setting](/_next/image?url=%2Fdocs%2Fget-started%2Fhistory_retention_setting.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

For more info, see [Instant restore](/docs/introduction/branch-restore).

  6. ## Restrict database access to trusted IPs

Neon's IP Allow feature ensures that only trusted IP addresses can connect to your database, preventing unauthorized access and enhancing security.

**Recommendation**

Combine an allowlist with protected branches for enhanced security. This setup ensures that only trusted IPs can access critical data, reducing the risk of unauthorized access and safeguarding data integrity.

**Configuration details**

     * **IP Allow** : Restricts access to specific, trusted IP addresses, preventing unauthorized connections.
     * **Protected branch** : Safeguards critical data from accidental deletions or modifications by designating branches as protected.

You can configure **IP Allow** and protected branches in your Neon project's settings. For more information, see [Configure IP Allow](/docs/manage/projects#configure-ip-allow) and [Protected branches guide](/docs/guides/protected-branches).

![IP allow setting settings](/_next/image?url=%2Fdocs%2Fget-started%2Fip_allow_settings.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

  7. ## Set up metrics export

Export Neon metrics to your preferred observability platform and centralize your database monitoring with your existing stack.

**Recommendation**

Set up integration with your observability platform to monitor and set alerts for key metrics:

     * Connection counts (active and idle database connections)
     * Database size (total size of all databases)
     * Replication delay (lag in bytes and seconds)
     * Compute metrics (CPU and memory usage)

**Available integrations:**

     * **[Grafana Cloud](/docs/guides/grafana-cloud)** : Native OTLP integration with automatic routing to Mimir, Loki, and Tempo
     * **[Datadog](/docs/guides/datadog)** : Direct integration with Datadog's observability platform
     * **[OpenTelemetry](/docs/guides/opentelemetry)** : Export to any OTLP-compatible platform, including self-hosted Grafana and Tempo

Choose the platform that best fits your existing monitoring infrastructure.

  8. ## Ensure your app reconnects after your database restarts

Verify your application handles compute restarts gracefully. Neon occasionally restarts computes for updates and maintenance.

**Recommendation**

Most database drivers and connection pools handle reconnection automatically, but it's important to test this behavior. You can use the Neon API to trigger a restart and watch your application reconnect:
         
         curl --request POST \
           --url https://console.neon.tech/api/v2/projects/your_project_id/endpoints/your_endpoint_id/restart \
           --header 'accept: application/json' \
           --header 'authorization: Bearer $NEON_API_KEY'

See [Restart compute endpoint](https://api-docs.neon.tech/reference/restartprojectendpoint) for details.

For more information:

     * [Build connection timeout handling into your application](/docs/connect/connection-latency#build-connection-timeout-handling-into-your-application)
     * [Maintenance & updates overview](/docs/manage/maintenance-updates-overview)

  9. ## Install pg_stat_statements

Enable query performance monitoring to track execution times and frequency.

**Recommendation**

Install the `pg_stat_statements` extension to monitor query performance and identify potential bottlenecks.

**Usage**
         
         CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

The statistics gathered by this extension require little overhead and let you quickly access metrics like:

     * [Most frequently executed queries](/docs/postgresql/query-performance#most-frequently-executed-queries)
     * [Longest running queries](/docs/postgresql/query-performance#long-running-queries)
     * [Queries that return the most rows](/docs/postgresql/query-performance#queries-that-return-the-most-rows)

You can also use the **Monitoring Dashboard** in the Neon Console to view live graphs for system and database metrics like CPU, RAM, and connections.

![Monitoring page connections graph](/_next/image?url=%2Fdocs%2Fintroduction%2Fmonitor_connections.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

For more information, see [Query performance](/docs/postgresql/query-performance) and [Monitoring](/docs/introduction/monitoring).

  10. ## Upgrade to a Neon Scale plan for priority support

Scale plan customers can open support tickets with the Neon Support team.

**Recommendation**

Upgrade to a [Scale plan](/docs/introduction/plans) to get both [priority support](/docs/introduction/support#prioritized-support-tickets) and acccess to SLAs.

For more information, see the [Support documentation](/docs/introduction/support).

  11. ## Advanced: Set up cross-region replication

Cross-region replication can provide an added layer of resilience for production environments. It allows you to replicate data from one Neon project to another in a different region — helping you prepare for unlikely regional outages or implement failover strategies.

**Recommendation**

Set up cross-region replication if your app requires high availability across regions or if you're building a disaster recovery plan.

**How it works**

Neon uses [logical replication](/docs/guides/logical-replication-neon-to-neon) to replicate data between Neon projects. You can replicate from a source project in one region to a destination project in another region, creating a near real-time copy of your data.

**Steps to get started**

     * Set up a publication on your source database
     * Create matching tables and a subscription on your destination database
     * Test the replication and monitor for consistency

For full details, see [Replicate data from one Neon project to another](/docs/guides/logical-replication-neon-to-neon).




## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[Previous3 - Branching](/docs/get-started/workflow-primer)[NextOverview](/docs/import/migrate-intro)

Last updated on August 18, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * 1Set a compute size that can handle production traffic
  * 2Enable autoscaling to handle usage spikes
  * 3Disable scale to zero
  * 4Use a pooled connection
  * 5Increase your project's restore window to 7 days
  * 6Restrict database access to trusted IPs
  * 7Set up metrics export
  * 8Ensure your app reconnects after your database restarts
  * 9Install pg_stat_statements
  * 10Upgrade to a Neon Scale plan for priority support
  * 11Advanced: Set up cross-region replication
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/get-started/production-checklist.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/get-started/production-checklist.md)

Neon Docs