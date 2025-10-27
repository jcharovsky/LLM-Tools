# buster-setglobalobject

**Source URL:** https://hub.phantombuster.com/reference/buster-setglobalobject

---

**Sets (** in fact, replaces**) the global object of your account.** [What is the global object?](/docs/the-agent-and-global-object)

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
> It's recommended to first fetch the global object with getGlobalObject() (to update it) because **this method overwrites the whole object**.

Async/AwaitPromisesCallbacks (ES5)
    
    
    /*Bot launched with globalObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    try {
      const object = await buster.getGlobalObject(agentId)
      object.password = "pass"
      
      await buster.setGlobalObject(agentId, object)
      
      const newObject = await buster.getGlobalObject(agentId)
      console.log("The name is", newObject.name, ", the age is", newObject.age "and the password is", newObject.password)
      //This will print "The name is nick , the age is 2 and the password is pass"
    } catch (err) {
      console.log("Could not change global object:", err)
    }
    
    
    
    /*Bot launched with globalObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    buster.getGlobalObject(agentId)
    .then((object) => {
      object.password = "pass"
      return buster.setGlobalObject(agentId, object)
    })
    .then(() => {
      return buster.getGlobalObject(agentId)
    })
    .then((newObject) => {
      console.log("The name is", newObject.name, ", the age is", newObject.age "and the password is", newObject.password)
      //This will print "The name is nick , the age is 2 and the password is pass"
    })
    .catch((err) => {
      console.log("Could not change global object:", err)
    })
    
    
    
    /*Bot launched with globalObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    buster.getGlobalObject(agentId, function(err, object) {
      if (err) {
        console.log("Could not get global object:", err)
      } else {
        object.password= "pass"
        buster.setGlobalObject(agentId, object, function(err) {
          if (err) {
            console.log("Could not set global object:", err)
          } else {
            buster.getGlobalObject(agentId, function(err, newObject) {
              if (err) {
                console.log("Could not get global object:", err)
              } else {
                console.log("The name is", newObject.name, ", the age is", newObject.age "and the password is", newObject.password)
                //This will print "The name is nick , the age is 2 and the password is pass"
              }
            })
          }
        })
      }
    })