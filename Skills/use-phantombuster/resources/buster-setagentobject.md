# buster-setagentobject

**Source URL:** https://hub.phantombuster.com/reference/buster-setagentobject

---

**Sets (** in fact, replaces**) the object of an agent.** [What are agent objects?](/docs/the-agent-and-global-object)

## 

— agentId `(Number)`

ID of the agent from which to get the object (_optional_).  
By default, this is the ID of the currently running agent.

## 

— object `(PlainObject)`

Object to save.

## 

— callback `(Function(err))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.



> ## ❗️
> 
> Warning
> 
> It's recommended to first fetch the object with getAgentObject() (to update it) because **this method overwrites the whole object**.

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
      object.password = "pass"
      
      await buster.setAgentObject(agentId, object)
      
      const newObject = await buster.getAgentObject(agentId)
      console.log("The name is", newObject.name, ", the age is", newObject.age "and the password is", newObject.password)
      //This will print "The name is nick , the age is 2 and the password is pass"
    } catch (err) {
      console.log("Could not change agent object:", err)
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
      object.password = "pass"
      return buster.setAgentObject(agentId, object)
    })
    .then(() => {
      return buster.getAgentObject(agentId)
    })
    .then((newObject) => {
      console.log("The name is", newObject.name, ", the age is", newObject.age "and the password is", newObject.password)
      //This will print "The name is nick , the age is 2 and the password is pass"
    })
    .catch((err) => {
      console.log("Could not change agent object:", err)
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
        object.password= "pass"
        buster.setAgentObject(agentId, object, function(err) {
          if (err) {
            console.log("Could not set agent object:", err)
          } else {
            buster.getAgentObject(agentId, function(err, newObject) {
              if (err) {
                console.log("Could not get agent object:", err)
              } else {
                console.log("The name is", newObject.name, ", the age is", newObject.age "and the password is", newObject.password)
                //This will print "The name is nick , the age is 2 and the password is pass"
              }
            })
          }
        })
      }
    })