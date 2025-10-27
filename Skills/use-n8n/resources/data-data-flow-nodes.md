# data-data-flow-nodes

**Source URL:** https://docs.n8n.io/data/data-flow-nodes/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-flow-nodes.md "Edit this page")

# Data flow within nodes#

Nodes can process multiple items.

For example, if you set the Trello node to `Create-Card`, and create an expression that sets `Name` using a property called `name-input-value` from the incoming data, the node creates a card for each item, always choosing the `name-input-value` of the current item.

For example, this input will create two cards. One named `test1` the other one named `test2`:
    
    
    1
    2
    3
    4
    5
    6
    7
    8

| 
    
    
    [
    	{
    		name-input-value: "test1"
    	},
    	{
    		name-input-value: "test2"
    	}
    ]
      
  
---|---  
  
Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top