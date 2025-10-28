# cloud-services-storage-and-databases-replit-database

**Source URL:** https://docs.replit.com/cloud-services/storage-and-databases/replit-database

---

Skip to main content

[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

  * [Docs](/getting-started/intro-replit)
  * [Tutorials](/tutorials/vibe-coding-101)
  * [Trust & Billing](/category/billing)
  * [Teams and Enterprise](/category/teams)
  * [Changelog](/updates/2025/10/24/changelog)



##### Getting Started

  * [Introduction](/getting-started/intro-replit)
  * Quickstarts

  * [Replit Core](/replit-core/replit-core)



##### Replit Apps

  * [Overview](/category/replit-apps)
  * [Import](/replit-app/import-to-replit)
  * [Collaboration](/replit-app/collaborate)
  * [Visibility](/replit-app/visibility)
  * [Advanced Configuration](/replit-app/configuration)
  * [App Embed](/replit-app/app-embed)
  * [Developer Frameworks](/replit-workspace/templates)



##### Replit AI

  * [Overview](/category/replit-ai)
  * [Agent](/replitai/agent)
  * Autonomy & validation

  * Features

  * Integrations

  * Visual edits




##### Replit Workspace

  * [Overview](/category/replit-workspace)
  * Features

  * [Themes](/replit-workspace/replit-themes)



##### Publishing your App

  * [Overview](/category/replit-deployments)
  * Deployment Types

  * Advanced Configuration




##### Storage and Databases

  * [Overview](/category/storage-and-databases)
  * [Database](/cloud-services/storage-and-databases/sql-database)
  * [Production Databases](/cloud-services/storage-and-databases/production-databases)
  * App Storage

  * [Key-Value Store](/cloud-services/storage-and-databases/replit-database)



##### Platforms

  * [Mobile App](/platforms/mobile-app)
  * [Desktop App](/platforms/desktop-app)



##### Extensions

  * [Overview](/extensions/extensions)
  * Basics

  * Development

  * Examples

  * API Reference

  * [Overview](/extensions/publish)
  * [Overview](/extensions/faq)



##### Additional Resources

  * [CLUI](/additional-resources/clui-graphical-cli)
  * [Cheat Sheet](/additional-resources/cheat-sheet)
  * [FAQ](/faq)



  * [Start Building](https://replit.com/signup)
  * 


[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

Search...

Navigation

Storage and Databases

Key-Value Store

Replit Key-Value Store provides a simple, user-friendly database inside every Replit App. No configuration required—just import and start storing data immediately.

## 

​

Features

  * **Zero configuration** : Start using the database right away with no setup required
  * **Simple API** : Store and retrieve data with an interface similar to Python dictionaries
  * **Multiple data types** : Store strings, numbers, lists, dictionaries, and other Python objects
  * **Prefix filtering** : Query for keys that share common prefixes
  * **Built-in access** : Access your database from the Replit workspace sidebar



## 

​

Getting started

### 

​

Accessing your key-value store

How to access the Key-Value Store tool

From the left **Tool dock** :

  1. Select the second-to-last icon in the sidebar
  2. The Key-Value Store interface will appear with instructions and current data

You can also use the **Search bar** :

  1. Select the ![magnifying glass icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30) magnifying glass at the top
  2. Type “Key-Value” to locate the tool



### 

​

Importing the database

importing.py

importing.js

Copy

Ask AI
    
    
    from replit import db
    

If you encounter publishing errors in Python, ensure you’re using `replit` version 3.3.0 or above. Check your version with `pip show replit`. Upgrade with `upm add 'replit>=3.3.0'`.For Node.js, make sure to install the package with `pnpm add @replit/database`.

## 

​

Using the key-value store

### 

​

Creating and storing data

The Key-Value Store works similar to a dictionary in Python or an object in JavaScript. Here’s how to add data:

basic_storage.py

basic_storage.js

Copy

Ask AI
    
    
    from replit import db
    
    # Add a key and value to the database
    db["key1"] = "value1"
    

#### 

​

Storing different data types

data_types.py

data_types.js

Copy

Ask AI
    
    
    from replit import db
    
    # Store different data types
    db["string_key"] = "text value"
    db["integer_key"] = 100
    db["float_key"] = 9.99
    db["list_key"] = [1, 2, 3]
    db["dict_key"] = {"name": "user", "role": "admin"}
    db["none_key"] = None
    

Use 2D arrays/lists to create table-like structures:

table_structure.py

table_structure.js

Copy

Ask AI
    
    
    from replit import db
    
    db["users"] = [["id", "name"], [1, "James"], [2, "Angel"]]
    
    for row in db["users"]:
        print(row)
    

### 

​

Reading data

Retrieve data by referencing the key:

reading_data.py

reading_data.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create example data
    db["username"] = "developer123"
    db["user_info"] = {"email": "dev@example.com", "plan": "Pro"}
    
    # Read the data
    print(db["username"])                   # Outputs: developer123
    print(db["user_info"]["email"])         # Outputs: dev@example.com
    

For safer access that won’t raise an error if the key doesn’t exist:

safe_access.py

safe_access.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create example data
    db["count"] = 42
    
    # Access with get() method
    print(db.get("count"))                  # Outputs: 42
    print(db.get("missing_key", "Not found")) # Outputs: Not found
    

### 

​

Listing and searching keys

Access all keys in the database:

list_keys.py

list_keys.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create some sample data first
    db["user1"] = "Alice"
    db["user2"] = "Bob"
    db["setting1"] = "enabled"
    
    # Print all keys
    print(db.keys())  # Outputs something like: {'user1', 'user2', 'setting1'}
    
    # Loop through keys and print values
    for key in db:
        print(f"{key}: {db.get(key)}")
    

Find keys with a specific prefix:

prefix_search.py

prefix_search.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create data
    db["user_id"] = 1001
    db["user_name"] = "Alex"
    db["item_id"] = 5001
    
    # Find all keys starting with "user"
    user_keys = db.prefix("user")
    print(user_keys)  # Outputs: ('user_id', 'user_name')
    

### 

​

Updating data

Update stored values by assigning new values to existing keys:

update_data.py

update_data.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create and display data
    db["score"] = 95
    print(db["score"])  # Outputs: 95
    
    # Update the value
    db["score"] = 98
    print(db["score"])  # Outputs: 98
    

Perform operations on stored values:

modify_values.py

modify_values.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create numeric data
    db["counter"] = 10
    
    # Increment the value
    db["counter"] += 5
    print(db["counter"])  # Outputs: 15
    

### 

​

Deleting data

Remove key-value pairs:

delete_data.py

delete_data.js

Copy

Ask AI
    
    
    from replit import db
    
    # Create data
    db["temporary"] = "will be deleted"
    
    # Delete the data
    del db["temporary"]
    
    # Verify deletion
    if "temporary" not in db:
        print("Value deleted successfully.")
    

### 

​

Complete example

Here’s a complete example of using the Key-Value Store for a simple task list:

task_list.py

task_list.js

Copy

Ask AI
    
    
    from replit import db
    import time
    
    def add_task(title, description=""):
        task_id = int(time.time())  # Use timestamp as ID
        db[f"task_{task_id}"] = {
            "id": task_id,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": time.time()
        }
        return task_id
    
    def complete_task(task_id):
        key = f"task_{task_id}"
        if key in db:
            task = db[key]
            task["completed"] = True
            db[key] = task
            return True
        return False
    
    def list_tasks(show_completed=True):
        tasks = []
        for key in db.prefix("task_"):
            task = db[key]
            if show_completed or not task["completed"]:
                tasks.append(task)
        return tasks
    
    # Usage example
    add_task("Buy groceries", "Milk, eggs, bread")
    add_task("Call dentist")
    task_id = add_task("Finish project", "Complete documentation")
    
    # Mark a task as complete
    complete_task(task_id)
    
    # List all tasks
    all_tasks = list_tasks()
    for task in all_tasks:
        status = "✓" if task["completed"] else "☐"
        print(f"{status} {task['title']}: {task.get('description', '')}")
    

## 

​

Use cases

The Key-Value Store is ideal for:

  * **User preferences** : Store user settings and preferences
  * **Game state** : Save game progress and high scores
  * **Caching** : Store temporary data to speed up your application
  * **Simple configuration** : Maintain configuration values across app restarts
  * **Session data** : Track user sessions without complex database setup



## 

​

FAQs

### 

​

Where can I find my store?

Finding your Key-Value Store

When viewing your Replit App:

  1. Look for the Key-Value Store icon toward the bottom of the sidebar (second from last)
  2. Select it to open the database interface



### 

​

How can I access my store programmatically?

Replit provides official clients for multiple languages:

  * [Python](https://pypi.org/project/replit/)
  * [Node.js](https://www.npmjs.com/package/@replit/database)
  * [Go](https://github.com/replit/database-go)



Basic usage in different languages

basic_usage.py

basic_usage.js

basic_usage.go

Copy

Ask AI
    
    
    from replit import db
    db["key"] = "value"
    print(db["key"])
    

### 

​

What if my language doesn’t have a client?

If your Replit App is in a language without an official client, you can use HTTP requests to interact with the database:

HTTP API usage for custom clients

**Set a key-value pair:**

Copy

Ask AI
    
    
    curl $REPLIT_DB_URL -d '<key>=<value>'
    

**Alternative set method (for safe characters):**

Copy

Ask AI
    
    
    curl -XPOST $REPLIT_DB_URL/<key>=<value>
    

**Get a value:**

Copy

Ask AI
    
    
    curl $REPLIT_DB_URL/<key>
    

**Delete a key:**

Copy

Ask AI
    
    
    curl -XDELETE $REPLIT_DB_URL/<key>
    

**List keys with a prefix:**

Copy

Ask AI
    
    
    curl "$REPLIT_DB_URL?prefix=<key>"
    

### 

​

What is REPLIT_DB_URL?

`REPLIT_DB_URL` is an environment variable created with your Replit App. It’s the connection string that enables database access.

`REPLIT_DB_URL` provides full access to your database. Never expose it publicly or share it with untrusted parties.

How to access REPLIT_DB_URL

get_db_url.py

get_db_url.js

Copy

Ask AI
    
    
    import os
    print(os.getenv("REPLIT_DB_URL"))
    

**In Deployments:** For published apps, the URL is stored in `/tmp/replitdb` instead of the environment variable. If writing a client, first check `/tmp/replitdb` and fall back to the environment variable.

### 

​

What are the storage limits?

The Key-Value Store has the following limits:

  * 50 MiB per store (sum of keys and values)
  * 5,000 keys per store
  * 1,000 bytes per key
  * 5 MiB per value



Rate limits apply to all operations. If exceeded, you’ll receive an HTTP 429 response. Implement exponential retry with gradual delays to handle rate limiting.

### 

​

How can I check my storage usage?

Checking storage usage

  1. Open the Key-Value Store tool from the sidebar
  2. At the top of the interface, you’ll see your current usage:
     * Number of keys in your store
     * Total storage used by keys and values



### 

​

Is my store private?

Yes, each store is private and isolated. Every Replit App has its own database that is not shared with other Replit Apps.

### 

​

How do I share a database across multiple Replit Apps?

Creating a shared database service

To share data between Replit Apps:

  1. Designate one Replit App as the primary database service
  2. Create an API in this app that allows other apps to interact with its database
  3. Have other Replit Apps send requests to this API

[View an example Replit App in Python](https://replit.com/@util/Replit-Database-proxy)

## 

​

Next steps

To learn about other storage options available in Replit:

  * [SQL Database](/cloud-services/storage-and-databases/sql-database) \- For relational data with SQL queries
  * [Object Storage](/cloud-services/storage-and-databases/object-storage) \- For storing larger files and assets
  * [Secrets](/replit-workspace/workspace-features/secrets) \- For storing sensitive credentials securely



Was this page helpful?

YesNo

[Previous](/reference/object-storage-javascript-sdk)[Mobile AppThe Replit Mobile App for iOS and Android lets you create apps using all of Replit's tools on the go.Next](/platforms/mobile-app)

⌘I

On this page

  * Features
  * Getting started
  * Accessing your key-value store
  * Importing the database
  * Using the key-value store
  * Creating and storing data
  * Storing different data types
  * Reading data
  * Listing and searching keys
  * Updating data
  * Deleting data
  * Complete example
  * Use cases
  * FAQs
  * Where can I find my store?
  * How can I access my store programmatically?
  * What if my language doesn’t have a client?
  * What is REPLIT_DB_URL?
  * What are the storage limits?
  * How can I check my storage usage?
  * Is my store private?
  * How do I share a database across multiple Replit Apps?
  * Next steps