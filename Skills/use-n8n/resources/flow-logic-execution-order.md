# flow-logic-execution-order

**Source URL:** https://docs.n8n.io/flow-logic/execution-order/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/execution-order.md "Edit this page")

# Execution order in multi-branch workflows#

n8n's node execution order depends on the version of n8n you're using:

  * For workflows created before version 1.0: n8n executes the first node of each branch, then the second node of each branch, and so on.
  * For workflows created in version 1.0 and above: executes each branch in turn, completing one branch before starting another. n8n orders the branches based on their position on the [canvas](../../glossary/#canvas-n8n), from topmost to bottommost. If two branches are at the same height, the leftmost branch executes first.



You can change the execution order in your [workflow settings](../../workflows/settings/).

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top