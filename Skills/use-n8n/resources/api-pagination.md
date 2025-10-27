# api-pagination

**Source URL:** https://docs.n8n.io/api/pagination/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/api/pagination.md "Edit this page")

# API pagination#

The default page size is 100 results. You can change the page size limit. The maximum permitted size is 250.

When a response contains more than one page, it includes a cursor, which you can use to request the next pages.

For example, say you want to get all active workflows, 150 at a time.

Get the first page:
    
    
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

| 
    
    
    # For a self-hosted n8n instance
    curl -X 'GET' \
      '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \
      -H 'accept: application/json' \
      -H 'X-N8N-API-KEY: <your-api-key>'
    
    # For n8n Cloud
    curl -X 'GET' \
      '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \
      -H 'accept: application/json' \
      -H 'X-N8N-API-KEY: <your-api-key>'
      
  
---|---  
  
The response is in JSON format, and includes a `nextCursor` value. This is an example response.
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9

| 
    
    
    {
      "data": [
        // The response contains an object for each workflow
        {
          // Workflow data
        }
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }
      
  
---|---  
  
Then to request the next page:
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9

| 
    
    
    # For a self-hosted n8n instance
    curl -X 'GET' \
      '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
      -H 'accept: application/json'
    
    # For n8n Cloud
    curl -X 'GET' \
      '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
      -H 'accept: application/json'
      
  
---|---  
  
Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top