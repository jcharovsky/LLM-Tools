# buster-overridetimelimit

**Source URL:** https://hub.phantombuster.com/reference/buster-overridetimelimit

---

**Overrides the execution time limit of the agent.**

When the execution time reaches the specified number of seconds, the agent is stopped.

## 

— seconds `(Number)`

New time limit of the agent in seconds (_integer_). Setting this parameter to `0` will change the limit to the maximum allowed execution time of an agent.  
If the specified number of seconds is already lower than the current execution time, the agent is stopped right away.

## 

— callback `(Function(err))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.



Async/AwaitPromisesCallbacks (ES5)
    
    
    try {
      await buster.overrideTimeLimit(60)
      // Set the time limit at 1 minute
    } catch (err) {
      console.log("Could not override the time limit:", err)
    }
    
    
    
    buster.overrideTimeLimit(60)
    .then(() => {
      // Set the time limit at 1 minute
    })
    .catch((err) => {
      console.log("Could not override the time limit:", err)
    })
    
    
    
    buster.overrideTimeLimit(60, function(err) {
      if (err) {
        console.log("Could not override the time limit:", err)
      } else {
        // Set the time limit at 1 minute
      }
    })