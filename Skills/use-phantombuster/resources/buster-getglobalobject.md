# buster-getglobalobject

**Source URL:** https://hub.phantombuster.com/reference/buster-getglobalobject

---

**Gets the global object of your account.** [What is the global object?](/docs/the-agent-and-global-object)

## 

— callback `(Function(err, object))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`object (PlainObject)`** : the content of your globalObject, if the globalObject is not filled then `object` will be an empty object `{}`.



Async/AwaitPromisesCallbacks (ES5)
    
    
    /*Bot launched with globalObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    try {
      const object = await buster.getGlobalObject()
      console.log("The name is", object.name, "and the age is", object.age)
      //This will print "The name is nick and the age is 2"
    } catch (err) {
      console.log("Could not get the global object:", err)
    }
    
    
    
    /*Bot launched with globalObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    buster.getGlobalObject()
    .then((object) => {
      console.log("The name is", object.name, "and the age is", object.age)
      //This will print "The name is nick and the age is 2"
    })
    .catch((err) => {
      console.log("Could not get the global object:", err)
    })
    
    
    
    /*Bot launched with globalObject:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    buster.getGlobalObject(function(err, object) {
      if (err) {
        console.log("Could not get the global object:", err)
      } else {
        console.log("The name is", object.name, "and the age is", object.age)
        //This will print "The name is nick and the age is 2"
      }
    })