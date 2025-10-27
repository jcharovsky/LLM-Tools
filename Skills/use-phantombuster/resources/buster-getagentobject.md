# buster-getagentobject

**Source URL:** https://hub.phantombuster.com/reference/buster-getagentobject

---

**Gets the object of an agent.** [What are agent objects?](/docs/the-agent-and-global-object)

## 

— agentId `(Number)`

ID of the agent from which to get the object (_optional_).  
By default, this is the ID of the currently running agent.

## 

— callback `(Function(err, object))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`object (PlainObject)`** : the content of your agentObject, if the agentObject is not filled then `object` will be an empty object `{}`.



Async/AwaitPromisesCallbacks (ES5)
    
    
    /*Bot launched with agentObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    const agentId = buster.agentId //Useless
    
    try {
      const object = await buster.getAgentObject(agentId)
      console.log("The name is", object.name, "and the age is", object.age)
      //This will print "The name is nick and the age is 2"
    } catch (err) {
      console.log("Could not get agent object:", err)
    }
    
    
    
    /*Bot launched with agentObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    const agentId = buster.agentId //Useless
    
    buster.getAgentObject(agentId)
    .then((object) => {
      console.log("The name is", object.name, "and the age is", object.age)
      //This will print "The name is nick and the age is 2"
    })
    .catch((err) => {
      console.log("Could not get agent object:", err)
    })
    
    
    
    /*Bot launched with agentObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    var agentId = buster.agentId //Useless
    
    buster.getAgentObject(agentId, function(err, object) {
      if (err) {
        console.log("Could not get agent object:", err)
      } else {
        console.log("The name is", object.name, "and the age is", object.age)
        //This will print "The name is nick and the age is 2"
      }
    })
    

> ## 🚧
> 
> Note
> 
> The `agentId` argument should be used just in case you want another agent's object.  
>  To get the current agent object just call `buster.getAgentObject()`.