# code-builtin-langchain-methods

**Source URL:** https://docs.n8n.io/code/builtin/langchain-methods/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/langchain-methods.md "Edit this page")

# LangChain Code node methods#

n8n provides these methods to make it easier to perform common tasks in the [LangChain Code node](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code/).

LangChain Code node only

These variables are for use in expressions in the LangChain Code node. You can't use them in other nodes.

Method | Description  
---|---  
`this.addInputData(inputName, data)` | Populate the data of a specified non-main input. Useful for mocking data.

  * `inputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`
  * `data` contains the data you want to add. Refer to [Data structure](../../../data/data-structure/) for information on the data structure expected by n8n.

  
`this.addOutputData(outputName, data)` | Populate the data of a specified non-main output. Useful for mocking data.

  * `outputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`
  * `data` contains the data you want to add. Refer to [Data structure](../../../data/data-structure/) for information on the data structure expected by n8n.

  
`this.getInputConnectionData(inputName, itemIndex, inputIndex?)` | Get data from a specified non-main input.

  * `inputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`
  * `itemIndex` should always be `0` (this parameter will be used in upcoming functionality)
  * Use `inputIndex` if there is more than one node connected to the specified input.

  
`this.getInputData(inputIndex?, inputName?)` | Get data from the main input.  
`this.getNode()` | Get the current node.  
`this.getNodeOutputs()` | Get the outputs of the current node.  
`this.getExecutionCancelSignal()` | Use this to stop the execution of a function when the workflow stops. In most cases n8n handles this, but you may need to use it if building your own chains or agents. It replaces the [Cancelling a running LLMChain](https://js.langchain.com/docs/modules/chains/foundational/llm_chain#cancelling-a-running-llmchain) code that you'd use if building a LangChain application normally.  
  
Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top