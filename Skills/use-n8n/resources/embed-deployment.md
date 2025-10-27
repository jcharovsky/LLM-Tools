# embed-deployment

**Source URL:** https://docs.n8n.io/embed/deployment/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/embed/deployment.md "Edit this page")

# Deployment#

Feature availability

Embed requires an embed license. For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/) on the n8n website.

See the [hosting documentation](../../hosting/installation/server-setups/) for detailed setup options.

## User data#

n8n recommends that you follow the same or similar practices used internally for n8n Cloud: Save user data using [Rook](https://rook.io/) and, if an n8n server goes down, a new instance starts on another machine using the same data.

Due to this, you don't need to use backups except in case of a catastrophic failure, or when a user wants to reactivate their account within your prescribed retention period (two weeks for n8n Cloud).

## Backups#

n8n recommends creating nightly backups by attaching another container, and copying all data to this second container. In this manner, RAM usage is negligible, and so doesn't impact the amount of users you can place on the server.

## Restarting#

If your instance is down or restarting, missed executions (for example, Cron or Webhook nodes) during this time aren't recoverable. If it's important for you to maintain 100% uptime, you need to build another proxy in front of it which caches the data.

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top