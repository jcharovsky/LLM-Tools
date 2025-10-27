# flow-logic-splitting

**Source URL:** https://docs.n8n.io/flow-logic/splitting/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/splitting.md "Edit this page")

# Splitting workflows with conditional nodes#

Splitting uses the [IF](../../integrations/builtin/core-nodes/n8n-nodes-base.if/) or [Switch](../../integrations/builtin/core-nodes/n8n-nodes-base.switch/) nodes. It turns a single-branch workflow into a multi-branch workflow. This is a key piece of representing complex logic in n8n.

Compare these workflows:

!["Diagram representing two workflows. One has three steps and follows a linear process, with a user submitting a bug, and the workflow emailing a support team. The second workflow starts the same way, but then splits depending on whether the user marked the issue as urgent. It then splits again depending on the user's support plan"](../../_images/flow-logic/splitting/single-multi-branch-workflow.png)

This is the power of splitting and conditional nodes in n8n.

Refer to the [IF](../../integrations/builtin/core-nodes/n8n-nodes-base.if/) or [Switch](../../integrations/builtin/core-nodes/n8n-nodes-base.switch/) documentation for usage details.

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top