# buster-setresultobject

**Source URL:** https://hub.phantombuster.com/reference/buster-setresultobject

---

**Sets (in fact,** replaces**) the result object of your agent.**

Think of the result object as the output value of your agent.  
This is useful for returning a small set of JSON fields containing whatever your agent might want to return when it exits.

Use this method in conjunction with the launch `<launch-an-agent>` API endpoint (with `output` set to `result-object`) to launch and get the result of your agent in one single HTTP request.

## 

— object `(PlainObject)`

Object to set as result object.

## 

— callback `(Function(err))`

Function called when finished(optional).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const object = {
      name: "Nick",
      age: 1,
      url: "nickjs.org"
    }
    
    try {
      await buster.setResultObject(object)
      //curl -i -H 'X-Phantombuster-Key-1: API_KEY' -X POST -d 'output=first-result-object' https://phantombuster.com/api/v1/agent/AGENT_ID/launch
      //You can get your result object at the url with the API
    } catch (err) {
    	console.log("Could not set the result object:", err)
    }
    
    
    
    const object = {
      name: "Nick",
      age: 1,
      url: "nickjs.org"
    }
    
    buster.setResultObject(object)
    .then(() => {
      //curl -i -H 'X-Phantombuster-Key-1: API_KEY' -X POST -d 'output=first-result-object' https://phantombuster.com/api/v1/agent/AGENT_ID/launch
      //You can get your result object at the url with the API
    })
    .catch((err) => {
    	console.log("Could not set the result object:", err)
    })
    
    
    
    var object = {
      name: "Nick",
      age: 1,
      url: "nickjs.org"
    }
    
    buster.setResultObject(object, function(err) {
      if (err) {
        console.log("Could not set the result object:", err)
      } else {
        //curl -i -H 'X-Phantombuster-Key-1: API_KEY' -X POST -d 'output=first-result-object' https://phantombuster.com/api/v1/agent/AGENT_ID/launch
        //You can get your result object at the url with the API
      }
    })
    

> ## 📘
> 
> Tips
> 
> Thanks to this function, you can create an endpoint to your bot.  
>  You can integrate this in your own network.

> ## ❗️
> 
> Careful
> 
> Never share your API Key, anyone with this key could change code, call bots and mess with your work.