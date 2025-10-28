# get-started-workflow-primer

**Source URL:** https://neon.com/docs/get-started/workflow-primer

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/3 - Branching

# Database branching workflow primer

An introduction to integrating Postgres branching into your development workflow

With Neon, you can work with your data just like you work with your code. The key is Neon's database [branching](/docs/guides/branching-intro) feature, which lets you instantly create branches of your data that you can include in your workflow — as many branches as you need.

Neon branches are:

  * **Isolated** : changes made to a branch don't affect its parent.
  * **Fast to create** : creating a branch takes ~1 second, regardless of the size of your database.
  * **Cost-effective** : you're only billed for unique data across all branches, and they scale to zero when not in use (you can configure this behavior for every branch).
  * **Ready to use** : branches will have the parent branch's schema and all its data (you can also include data up to a certain point in time). If you're working with sensitive data, Neon also supports a [schema-only branching](/docs/guides/branching-schema-only) option.



Every Neon branch has a unique Postgres connection string, so they're completely isolated from one another.
    
    
    # Branch 1
    postgresql://database_name_owner:AbC123dEf@ep-shiny-cell-a5y2zuu0.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require
    
    # Branch 2
    postgresql://database_name_owner:AbC123dEf@ep-hidden-hall-a5x58cuv.us-east-2.aws.neon.tech/dbname?sslmode=require&channel_binding=require

You can create all of your branches from the default branch, or set up a dedicated branch that you use as a base. The first approach is simpler, while the second provides greater data isolation.

![database workflow A B](/_next/image?url=%2Fdocs%2Fget-started%2Fdatabase_workflow_AB.jpg&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## Create branch methods

You can use either the Neon CLI or GitHub actions to incorporate branching into your workflow.

### Neon CLI

Using the [Neon CLI](/docs/reference/neon-cli), you can create branches without leaving your editor or automate branch creation in your CI/CD pipeline.

And here are the key CLI actions you can use:
    
    
    # Create branch
    neon branches create [options]
    
    # Get Connection string
    neon connection-string [branch] [options]
    
    # Delete branch
    neon branches delete <id|name> [options]

For more information, see:

  * ### [Branching with the Neon CLILearn about branching with the Neon CLI](/docs/guides/branching-neon-cli)
  * ### [Neon CLI ReferenceReference for all commands in the Neon CLI](/docs/reference/neon-cli)



### GitHub Actions

If you're using GitHub Actions for your CI workflows, Neon provides GitHub Actions for [creating](/docs/guides/branching-github-actions#create-branch-action), [deleting](/docs/guides/branching-github-actions#delete-branch-action), and [resetting](/docs/guides/branching-github-actions#reset-from-parent-action) branches — and there's also a [schema diff action](/docs/guides/branching-github-actions#schema-diff-action).

Create branchDelete branch

Here is an example of what a create branch action might look like:
    
    
    name: Create Neon Branch with GitHub Actions Demo
    run-name: Create a Neon Branch 🚀
    jobs:
      Create-Neon-Branch:
        uses: neondatabase/create-branch-action@v5
        with:
          project_id: rapid-haze-373089
          parent_id: br-long-forest-224191
          branch_name: from_action_reusable
          api_key: {{ secrets.NEON_API_KEY }}
        id: create-branch
      - run: echo project_id ${{ steps.create-branch.outputs.project_id}}
      - run: echo branch_id ${{ steps.create-branch.outputs.branch_id}}

You can find these GitHub Actions here:

  * ### [Create branch ActionCreate Neon Branch GitHub Action](https://github.com/neondatabase/create-branch-action)
  * ### [Delete Branch ActionDelete Neon Branch GitHub Action](https://github.com/neondatabase/delete-branch-action)
  * ### [Reset Branch ActionReset Neon Branch GitHub Action](https://github.com/neondatabase/reset-branch-action)
  * ### [Schema Diff ActionNeon Schema Diff GitHub Action](https://github.com/neondatabase/schema-diff-action)



For more detailed documentation, see [Automate branching with GitHub Actions](/docs/guides/branching-github-actions).

## A branch for every environment

Here's how you can integrate Neon branching into your workflow:

### Development

You can create a Neon branch for every developer on your team. This ensures that every developer has an isolated environment that includes schemas and data. These branches are meant to be long-lived, so each developer can tailor their branch based on their needs. With Neon's [branch reset capability](/docs/manage/branches#reset-a-branch-from-parent), developers can refresh their branch with the latest schemas and data anytime they need.

#### tip

To easily identify branches dedicated to development, we recommend prefixing the branch name with `dev/<developer-name>` or `dev/<feature-name>` if multiple developers collaborate on the same development branch.

Examples:
    
    
    dev/alice             dev/new-onboarding

### Preview environments

Whenever you create a pull request, you can create a Neon branch for your preview deployment. This allows you to test your code changes and SQL migrations against production-like data.

#### tip

We recommend following this naming convention to identify these branches easily:
    
    
    preview/pr-<pull_request_number>-<git_branch_name>

Example:
    
    
    preview/pr-123-feat/new-login-screen

You can also automate branch creation for every preview. These example applications show how to create Neon branches with GitHub Actions for every preview environment.

  * ### [Preview branches with Fly.ioSample project showing you how to create a branch for every Fly.io preview deployment](https://github.com/neondatabase/preview-branches-with-fly)
  * ### [Preview branches with VercelSample project showing you how to create a branch for every Vercel preview deployment](https://github.com/neondatabase/preview-branches-with-vercel)



### Testing

When running automated tests that require a database, each test run can have its branch with its own compute resources. You can create a branch at the start of a test run and delete it at the end.

#### tip

We recommend following this naming convention to identify these branches easily:
    
    
    test/<git_branch_name-test_run_name-commit_SHA-time_of_the_test_execution>

The time of the test execution can be an epoch UNIX timestamp (e.g., 1704305739). For example:
    
    
    test/feat/new-login-loginPageFunctionality-1a2b3c4d-20240211T1530

You can create test branches from the same date and time or Log Sequence Number (LSN) for tests requiring static or deterministic data.

## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[Previous2 - Connect](/docs/get-started/connect-neon)[Next4 - Ready for production](/docs/get-started/production-checklist)

Last updated on August 2, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Create branch methods
  * A branch for every environment
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/get-started/workflow-primer.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/get-started/workflow-primer.md)

Neon Docs