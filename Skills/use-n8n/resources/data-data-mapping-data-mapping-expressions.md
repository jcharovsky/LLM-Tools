# data-data-mapping-data-mapping-expressions

**Source URL:** https://docs.n8n.io/data/data-mapping/data-mapping-expressions/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-mapping/data-mapping-expressions.md "Edit this page")

# Mapping in the expressions editor#

These examples show how to access linked items in the expressions editor. Refer to [expressions](../../../code/expressions/) for more information on expressions, including built in variables and methods.

For information on errors with mapping and linking items, refer to [Item linking errors](../data-item-linking/item-linking-errors/).

## Access the linked item in a previous node's output#

When you use this, n8n works back up the item linking chain, to find the parent item in the given node.
    
    
    1
    2

| 
    
    
    // Returns the linked item
    {{$("<node-name>").item}}
      
  
---|---  
  
As a longer example, consider a scenario where a node earlier in the workflow has the following output data:
    
    
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

| 
    
    
    [
      {
        "id": "23423532",
        "name": "Jay Gatsby",
      },
      {
        "id": "23423533",
        "name": "José Arcadio Buendía",
      },
      {
        "id": "23423534",
        "name": "Max Sendak",
      },
      {
        "id": "23423535",
        "name": "Zaphod Beeblebrox",
      },
      {
        "id": "23423536",
        "name": "Edmund Pevensie",
      }
    ]
      
  
---|---  
  
To extract the name, use the following expression:
    
    
    1

| 
    
    
    {{$("<node-name>").item.json.name}}
      
  
---|---  
  
### Access the linked item in the current node's input#

In this case, the item linking is within the node: find the input item that the node links to an output item.
    
    
    1
    2

| 
    
    
    // Returns the linked item
    {{$input.item}}
      
  
---|---  
  
As a longer example, consider a scenario where the current node has the following input data:
    
    
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

| 
    
    
    [
      {
        "id": "23423532",
        "name": "Jay Gatsby",
      },
      {
        "id": "23423533",
        "name": "José Arcadio Buendía",
      },
      {
        "id": "23423534",
        "name": "Max Sendak",
      },
      {
        "id": "23423535",
        "name": "Zaphod Beeblebrox",
      },
      {
        "id": "23423536",
        "name": "Edmund Pevensie",
      }
    ]
      
  
---|---  
  
To extract the name, you'd normally use drag-and-drop [Data mapping](../), but you could also write the following expression:
    
    
    1

| 
    
    
    {{$input.item.json.name}}
      
  
---|---  
  
Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top