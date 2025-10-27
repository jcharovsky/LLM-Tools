# gettimeleft

**Source URL:** https://hub.phantombuster.com/reference/gettimeleft

---

**Returns the number of seconds left before the agent is killed for time limit reasons.**

This is very useful for saving data and exiting properly **before** being killed by Phantombuster for time limit reasons. Simply call this method regularly from your "main loop" and check if you have more than 60 seconds left (for example).

In addition, Phantombuster will detect when you use `buster.getTimeLeft()` and show an _ABORT_ button instead of a _STOP_ button in your agent's console. When _ABORT_ is clicked, all subsequent calls to `buster.getTimeLeft()` will return the sentinel value `-1`. That way, your agent can save its data and do other specific actions before exiting gracefully instead of being immediately killed as is the case for a regular click on the _STOP_ button.

> ## ❗️
> 
> The recommended way to use this method is to call it regularly, from your "main loop". Calling it once does not really make sense. We recommend calling it about once per minute.

> ## 📘
> 
> This method will find the lowest possible time limit, which can be either the agent's own time limit, your account global time limit (according to your plan) or the maximum allowed Phantombuster agent run time.

> ## 📘
> 
> This method's result is cached for 10 seconds. You can call this method any number of times but the result will only change every 10 seconds.

## 

— callback `(Function(err, timeLeft))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`timeLeft (Number)`** : the number of seconds left before the agent is killed or `-1` if the _ABORT_ button was clicked.



Async/AwaitPromisesCallbacks (ES5)
    
    
    try {
      const timeLeft = await buster.getTimeLeft()
      console.log(`I have ${timeLeft} seconds before being killed`)
    } catch (err) {
      console.log("Could not get time left:", err)
    }
    
    
    
    buster.getTimeLeft()
    .then((timeLeft) => {
      console.log(`I have ${timeLeft} seconds before being killed`)
    })
    .catch((err) => {
      console.log("Could not get time left:", err)
    })
    
    
    
    buster.getTimeLeft(function(err, timeLeft) {
      if (err) {
        console.log("Could not get time left:", err)
      } else {
        console.log("Number of seconds left before being killed:", timeLeft)
      }
    })