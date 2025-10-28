# changelog

**Source URL:** https://neon.com/docs/changelog

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/Changelog

# Changelog

The latest product updates from Neon

[RSS feed](/docs/changelog/rss.xml)

## Subscribe to our changelog.  
No spam, guaranteed.

Subscribe

## [Oct 24, 2025](/docs/changelog/2025-10-24)

## Claude Code plugin for Neon

We've launched a new plugin that brings Neon's capabilities directly into Claude Code. The new plugin includes:

  * **Claude Skills** to streamline key workflows:

    * **neon-drizzle** : Set up Drizzle ORM with Neon
    * **neon-serverless** : Configure connections with Neon's serverless Postgres driver
    * **neon-toolkit** : Manage databases, projects, and branches using the Neon API
    * **add-neon-knowledge** : Access Neon documentation snippets and usage examples
  * **Neon MCP server integration** that lets Claude interact with Neon in real time to query projects, manage databases and branches, and run SQL or migrations

  * **Context rules (.mdc files)** that can be used in other AI tools like Cursor




Install it from our marketplace:
    
    
    /plugin marketplace add neondatabase-labs/ai-rules
    /plugin install neon-plugin@neon

For more information, see [Claude Code plugin for Neon](/docs/ai/ai-claude-code-plugin).

## MCP server: Schema diff and migration generation

Our MCP server now supports schema diff generation and zero-downtime migration creation. Ask your AI assistant:
    
    
    Can you generate a schema diff for branch br-feature-auth in project my-app?

The assistant will compare the branch schema with its parent, show what changed, and offer to generate a zero-downtime migration to apply those changes to the parent branch.

This makes it easier to develop schema changes on feature branches and promote them when ready. For more information, see [Neon MCP Server](/docs/ai/neon-mcp-server).

## Storage quota doubled to 16TB

We've doubled our default storage quota from 8TB to 16TB. This means you can now run databases up to 16TB without contacting us to increase your limit. If you need to run larger databases, please [reach out to our team](https://neon.tech/contact-sales).

## Branch navigation improvements

We've added breadcrumb navigation to branch pages, making it easier to understand and navigate your branch hierarchy. When viewing a child branch, you'll now see the full lineage path (e.g., `production / development / feature-branch`) with visual branch indicators. The page heading has also been updated to "Child branch overview" for better clarity when working with nested branches.

![Branch breadcrumb navigation](/_next/image?url=%2Fdocs%2Fchangelog%2Fbranch-breadcrumbs-oct-2025.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## Postgres extension updates

We've expanded extension support for Postgres 18 and updated several extension versions.

**Now available on Postgres 18:**

Extension| Version  
---|---  
anon| 2.4.1  
address_standardizer| 3.6.0  
address_standardizer_data_us| 3.6.0  
h3| 4.2.3  
h3_postgis| 4.2.3  
pg_cron| 1.6  
pg_ivm| 1.12  
pg_uuidv7| 1.6  
pgrag| 0.0.0  
postgis_raster| 3.6.0  
postgis_sfcgal| 3.6.0  
postgis_tiger_geocoder| 3.6.0  
postgis_topology| 3.6.0  
postgres_fdw| 1.2  
  
**Version updates across all supported Postgres versions:**

Extension| Old Version| New Version  
---|---|---  
anon| 2.1.0| 2.4.1  
  
To upgrade from a previous version of an extension, follow the instructions in [Update an extension version](/docs/extensions/pg-extensions#update-an-extension-version).

For a complete list of Postgres extensions supported by Neon, see [Postgres extensions](/docs/extensions/pg-extensions).

**Fixes & improvements**

  * **Child branch storage now capped at logical data size**

We've introduced a storage billing cap for child branches. Previously, child branch storage cost was based on all data changes over time. Now, you're billed for the minimum of accumulated changes or your actual data size, ensuring you never pay more than the logical size of your data on a child branch. This change makes child branch storage costs more predictable and helps avoid charges from long-lived branches.

  * **Neon Launchpad packages renamed**

Neon Launchpad's packages were renamed: `neondb` → `get-db` (CLI) and `vite-plugin-postgres` → `vite-plugin-db` (Vite plugin). Use `npx get-db` to initiate Neon Launchpad.

_Neon Launchpad enables instant provisioning of a Postgres database without configuration or account creation. See[Neon Launchpad](/docs/reference/neon-launchpad) to learn more._




## [Oct 17, 2025](/docs/changelog/2025-10-17)

## Configure scale to zero in the console

Scale plan users can now adjust their scale to zero timeout directly in the Neon Console. Simply select **Edit compute** from the menu on the **Compute** tab to set a custom timeout. The Scale plan allows you to set this as low as 1 minute, a setting that was previously only available via the Neon API.

Scale to zero helps minimize costs by automatically placing inactive databases in an idle state. The timeout setting controls how fast that happens. To learn more, refer to our [Scale to zero](/docs/introduction/scale-to-zero) guide.

![Configure scale to zero time in the Console](/_next/image?url=%2Fdocs%2Fchangelog%2Fscale_to_zero_console.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## Quick presets for branch expiration

Managing your project's branches is now easier with convenient preset options. When creating or configuring a branch, choose to automatically expire it after 1 hour, 1 day, or a week. No need to manually calculate and select a specific date and time.

Setting branch expiration times can help reduce costs. To learn more, check out our [Branch expiration](/docs/guides/branch-expiration) guide.

![Branch expiration preset options](/_next/image?url=%2Fdocs%2Fchangelog%2Fbranch_expiration_presets.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## New NAT gateway IP addresses

We've added new NAT gateway IP addresses in the AWS US East (N. Virginia) region to expand infrastructure capacity. If you have external IP allow lists that enable connections from external services into Neon, **update those allow lists soon to include the new addresses** to avoid connectivity issues.

See our [Regions documentation](/docs/introduction/regions#aws-nat-gateway-ip-addresses) for the complete list of NAT gateway IPs for all regions.

## New VPC endpoint service for Private Networking

We've added a new VPC endpoint service address for Private Networking in the AWS US East (N. Virginia) region. If you're setting up Private Networking in the `us-east-1` region, you can now use the additional endpoint service address for enhanced infrastructure capacity and reliability.

For the complete list of VPC endpoint service addresses by region, see our [Private Networking guide](/docs/guides/neon-private-networking).

## E2E testing with Neon branches

Run end-to-end tests using isolated database branches. We've published guides showing how to use Neon's database branching with **Playwright** and **Cypress** to create isolated test environments for every pull request. Each PR gets its own database branch with automated schema migrations, ensuring your E2E tests run against the exact schema changes you're testing.

  * [Automated E2E Testing with Neon Branching and Playwright](https://neon.com/guides/e2e-playwright-tests-with-neon-branching)
  * [Automated E2E Testing with Neon Branching and Cypress](https://neon.com/guides/e2e-cypress-tests-with-neon-branching)

**Fixes & improvements**

  * **Postgres extension updates**

    * The [pg_graphql](/docs/extensions/pg_graphql) extension has been updated to version 1.5.11. This extension adds a GraphQL API layer directly to your Postgres database, allowing you to query your database using GraphQL.

To upgrade from a previous version of the extension, follow the instructions in [Update an extension version](/docs/extensions/pg-extensions#update-an-extension-version).

  * **Instant restore and snapshots**

    * Updated default instant restore settings for new projects. Instant restore lets you recover your database to any point in time within your configured window. Previously, new projects were set to the maximum restore window for their plan; now they default to 6 hours for Free plan projects and 1 day for paid plans. You can adjust your restore window anytime in your project settings.
    * Fixed an issue where selecting a restore time using the datepicker would unexpectedly include the current time's seconds and milliseconds. Restore times now set seconds and milliseconds to zero when specified to the minute.
    * Fixed an issue where the **Create snapshot** button incorrectly appeared on the Backup & Restore page when a non-root branch was selected. Snapshots can only be created from root branches (branches without a parent).
  * **Neon Launchpad**

    * Fixed an issue where usage limits for Neon projects created using Neon Launchpad ([neon.new](https://neon.new/)) were not reset after being claimed to a Neon account.
  * **Data API**

    * Data API and IP Allow cannot be used together. To enable Data API, you must first disable IP Allow on your project.



## [Oct 10, 2025](/docs/changelog/2025-10-10)

## Weekly Neon usage reports

Paid plan users will soon begin receiving weekly usage reports on Mondays. These reports provide month-to-date usage and costs across all billing metrics—including compute, storage, extra branches, and network transfer—helping you track spending and optimize costs before your monthly bill is finalized.

For cost optimization strategies for Neon, please refer to our [Cost optimization guide](/docs/introduction/cost-optimization).

![Weekly usage report email](/_next/image?url=%2Fdocs%2Fchangelog%2Fweekly_usage_report.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## pgvector v0.8.1 on Postgres 18

We've added support for [pgvector](/docs/extensions/pgvector) v0.8.1 on Postgres 18. This new version of `pgvector` adds support for Postgres 18 and improves `binary_quantize` function performance.

## Manage Neon with Pulumi

[Pulumi](https://www.pulumi.com), an open-source infrastructure-as-code (IaC) tool, can now be used to provision and manage your Neon projects as code. Using familiar programming languages or formats such as TypeScript, Python, Go, C#, Java, or YAML, you can define your Neon projects, branches, databases, compute endpoints, and roles alongside your other cloud resources. This integration uses a community-developed provider bridged from the Terraform provider for Neon.
    
    
    import * as neon from '@pulumi/neon';

To get started, see [Manage Neon with Pulumi](/guides/neon-pulumi).

## Manage Neon with SST

You can now use Neon with [SST](https://sst.dev/), an open-source framework for building full-stack applications on your own infrastructure. SST's support for Pulumi and Terraform providers enables you to manage Neon resources directly in your `sst.config.ts` alongside your serverless applications, with automated database provisioning for your deployments.
    
    
    npx sst add neon

To learn how, see [Manage Neon with SST](/guides/neon-sst).

**Fixes & improvements**

  * **Neon CLI**
    * We updated the Neon CLI to version 2.15.1, which adds support for numeric characters in parent branch names and fixes CSRF authentication errors experienced by some users. To upgrade your Neon CLI version, please refer to our [upgrade instructions](https://neon.com/docs/reference/cli-install#upgrade).
  * **Neon API**
    * Fixed an issue where database rename requests through the [Update branch](https://api-docs.neon.tech/reference/updateprojectbranchdatabase) endpoint could fail with a `could not configure compute node` error when the target database had active connections. The database rename operation now drops existing connections to the database before renaming, which allows rename requests to complete successfully.
  * **Postgres extension update**
    * The `neon` Postgres extension, which provides functions and views for gathering Neon-specific metrics, has been updated to version 1.9. To learn more about this extension, see [The neon extension](/docs/extensions/neon).
  * **Neon Console**
    * Fixed an issue that prevented creating Postgres 18 projects in HIPAA-enabled organizations. Note that HIPAA cannot be enabled on Postgres 18 projects, as Postgres 18 is currently in preview.
  * **Snapshot restore**
    * The [multi-step snapshot restore](/docs/guides/backup-restore#multi-step-restore) flow now includes **Restored to** and **Restored from** fields that show the target date/time and source snapshot for the restore operation. At the end of the restore flow, a **Go to branch** button lets you navigate directly to the backup branch created by the restore operation.



Was this page helpful?

YesNo

Thank you for your feedback!

## Subscribe to our changelog.  
No spam, guaranteed.

Subscribe

Neon Docs