# workflows-executions-single-workflow-executions

**Source URL:** https://docs.n8n.io/workflows/executions/single-workflow-executions/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/workflows/executions/single-workflow-executions.md "Edit this page")

# Workflow-level executions list#

The **Executions** list in a workflow shows all executions for that workflow.

Deleted workflows

When you delete a workflow, n8n deletes its execution history as well. This means you can't view executions for deleted workflows.

Execution history and workflow history

Don't confuse the execution list with [Workflow history](../../history/).

Executions are workflow runs. With the executions list, you can see previous runs of the current version of the workflow. You can copy previous executions into the editor to [Debug and re-run past executions](../debug/) in your current workflow.

Workflow history is previous versions of the workflow: for example, a version with a different node, or different parameters set.

## View executions for a single workflow#

In the workflow, select the **Executions** tab in the top menu. You can preview all executions of that workflow.

## Filter executions#

You can filter the executions list.

  1. In your workflow, select **Executions**. 
  2. Select **Filters**.
  3. Enter your filters. You can filter by:
     * **Status** : choose from **Failed** , **Running** , **Success** , or **Waiting**.
     * **Execution start** : see executions that started in the given time.
     * **Saved custom data** : this is data you create within the workflow using the Code node. Enter the key and value to filter. Refer to [Custom executions data](../custom-executions-data/) for information on adding custom data.

Feature availability

Custom executions data is available on:

       * Cloud: Pro, Enterprise
       * Self-Hosted: Enterprise, registered Community




## Retry failed workflows#

If your workflow execution fails, you can retry the execution. To retry a failed workflow:

  1. Open the **Executions** list.
  2. For the workflow execution you want to retry, select **Refresh** ![Refresh icon](../../../_images/common-icons/refresh.png).
  3. Select either of the following options to retry the execution:
     * **Retry with currently saved workflow** : Once you make changes to your workflow, you can select this option to execute the workflow with the previous execution data.
     * **Retry with original workflow** : If you want to retry the execution without making changes to your workflow, you can select this option to retry the execution with the previous execution data.



Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top