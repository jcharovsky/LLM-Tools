# data-data-structure

**Source URL:** https://docs.n8n.io/data/data-structure/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-structure.md "Edit this page")

# Data structure#

In n8n, all data passed between nodes is an array of objects. It has the following structure:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24

| 
    
    
    [
    	{
    		// For most data:
    		// Wrap each item in another object, with the key 'json'
    		"json": {
    			// Example data
    			"apple": "beets",
    			"carrot": {
    				"dill": 1
    			}
    		},
    		// For binary data:
    		// Wrap each item in another object, with the key 'binary'
    		"binary": {
    			// Example data
    			"apple-picture": {
    				"data": "....", // Base64 encoded binary data (required)
    				"mimeType": "image/png", // Best practice to set if possible (optional)
    				"fileExtension": "png", // Best practice to set if possible (optional)
    				"fileName": "example.png", // Best practice to set if possible (optional)
    			}
    		}
    	},
    ]
      
  
---|---  
  
Skipping the `json` key and array syntax

From 0.166.0 on, when using the Function node or Code node, n8n automatically adds the `json` key if it's missing. It also automatically wraps your items in an array (`[]`) if needed. This is only the case when using the Function or Code nodes. When building your own nodes, you must still make sure the node returns data with the `json` key.

## Data item processing#

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