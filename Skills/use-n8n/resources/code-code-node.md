# code-code-node

**Source URL:** https://docs.n8n.io/code/code-node/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/code-node.md "Edit this page")

# Using the Code node#

Use the Code node to write custom JavaScript or Python and run it as a step in your workflow.

Coding in n8n

This page gives usage information about the Code node. For more guidance on coding in n8n, refer to the [Code](../) section. It includes:

  * Reference documentation on [Built-in methods and variables](../builtin/overview/)
  * Guidance on [Handling dates](../cookbook/luxon/) and [Querying JSON](../cookbook/jmespath/)
  * A growing collection of examples in the [Cookbook](../cookbook/code-node/)



Examples and templates

For usage examples and templates to help you get started, refer to n8n's [Code integrations](https://n8n.io/integrations/code/) page.

Function and Function Item nodes

The Code node replaces the Function and Function Item nodes from version 0.198.0. If you're using an older version of n8n, you can still view the [Function node documentation](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.function.md) and [Function Item node documentation](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.functionItem.md).

## Usage#

How to use the Code node.

### Choose a mode#

There are two modes:

  * **Run Once for All Items** : this is the default. When your workflow runs, the code in the code node executes once, regardless of how many input items there are.
  * **Run Once for Each Item** : choose this if you want your code to run for every input item.



## JavaScript#

The Code node supports Node.js.

### Supported JavaScript features#

The Code node supports:

  * Promises. Instead of returning the items directly, you can return a promise which resolves accordingly.
  * Writing to your browser console using `console.log`. This is useful for debugging and troubleshooting your workflows.



### External libraries#

If you self-host n8n, you can import and use built-in and external npm modules in the Code node. To learn how to enable external modules, refer to the [Enable modules in Code node](../../hosting/configuration/configuration-examples/modules-in-code-node/) guide.

If you use n8n Cloud, you can't import external npm modules. n8n makes two modules available for you:

  * [crypto Node.js module](https://nodejs.org/docs/latest-v18.x/api/crypto.html)
  * [moment npm package](https://www.npmjs.com/package/moment)



### Built-in methods and variables#

n8n provides built-in methods and variables for working with data and accessing n8n data. Refer to [Built-in methods and variables](../builtin/overview/) for more information.

The syntax to use the built-in methods and variables is `$variableName` or `$methodName()`. Type `$` in the Code node or expressions editor to see a list of suggested methods and variables.

### Keyboard shortcuts#

The Code node editing environment supports time-saving and useful keyboard shortcuts for a range of operations from autocompletion to code-folding and using multiple-cursors. See the full list of [keyboard shortcuts](../../integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts/).

## Python (Pyodide - legacy)#

Pyodide is a legacy feature. Future versions of n8n will no longer support this feature.

n8n added Python support in version 1.0. It doesn't include a Python executable. Instead, n8n provides Python support using [Pyodide](https://pyodide.org/en/stable/), which is a port of CPython to WebAssembly. This limits the available Python packages to the [Packages included with Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide). n8n downloads the package automatically the first time you use it.

Slower than JavaScript

The Code node takes longer to process Python than JavaScript. This is due to the extra compilation steps.

### Built-in methods and variables#

n8n provides built-in methods and variables for working with data and accessing n8n data. Refer to [Built-in methods and variables](../builtin/overview/) for more information.

The syntax to use the built-in methods and variables is `_variableName` or `_methodName()`. Type `_` in the Code node to see a list of suggested methods and variables.

### Keyboard shortcuts#

The Code node editing environment supports time-saving and useful keyboard shortcuts for a range of operations from autocompletion to code-folding and using multiple-cursors. See the full list of [keyboard shortcuts](../../integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts/).

## File system and HTTP requests#

You can't access the file system or make HTTP requests. Use the following nodes instead:

  * [Read/Write File From Disk](../../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/)
  * [HTTP Request](../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)



## Python (Native - beta)#

n8n added native Python support using task runners (beta) in version 1.111.0. 

Main differences from Pyodide:

  * Native Python supports only `_items` in all-items mode and `_item` in per-item mode. It doesn't support other n8n built-in methods and variables.
  * Native Python supports importing native Python modules from the standard library and from third-parties, if the `n8nio/runners` image includes them and explicitly allowlists them. See [adding extra dependencies for task runners](../../hosting/configuration/task-runners/#adding-extra-dependencies) for more details.
  * Native Python denies insecure built-ins by default. See [task runners environment variables](../../hosting/configuration/environment-variables/task-runners/) for more details.
  * Unlike Pyodide, which accepts dot access notation, for example, `item.json.myNewField`, native Python only accepts bracket access notation, for example, `item["json"]["my_new_field"]`. There may be other minor syntax differences where Pyodide accepts constructs that aren't legal in native Python.



Keep in mind upgrading to native Python is a breaking change, so you may need to adjust your Python scripts to use the native Python runner. 

This feature is in beta and is subject to change. As it becomes stable, n8n will roll it out progressively to n8n cloud users during 2025. Self-hosting users can [try it out](../../hosting/configuration/task-runners/) and provide feedback.

## Coding in n8n#

There are two places where you can use code in n8n: the Code node and the expressions editor. When using either area, there are some key concepts you need to know, as well as some built-in methods and variables to help with common tasks.

### Key concepts#

When working with the Code node, you need to understand the following concepts:

  * [Data structure](../../data/data-structure/): understand the data you receive in the Code node, and requirements for outputting data from the node.
  * [Item linking](../../data/data-mapping/data-item-linking/): learn how data items work, and how to link to items from previous nodes. You need to handle item linking in your code when the number of input and output items doesn't match.



### Built-in methods and variables#

n8n includes built-in methods and variables. These provide support for:

  * Accessing specific item data
  * Accessing data about workflows, executions, and your n8n environment
  * Convenience variables to help with data and time



Refer to [Built-in methods and variables](../builtin/overview/) for more information.

## Use AI in the Code node#

Feature availability

AI assistance in the Code node is available to Cloud users. It isn't available in self-hosted n8n.

AI generated code overwrites your code

If you've already written some code on the **Code** tab, the AI generated code will replace it. n8n recommends using AI as a starting point to create your initial code, then editing it as needed.

To use ChatGPT to generate code in the Code node:

  1. In the Code node, set **Language** to **JavaScript**.
  2. Select the **Ask AI** tab.
  3. Write your query.
  4. Select **Generate Code**. n8n sends your query to ChatGPT, then displays the result in the **Code** tab.



Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top