# retrycount

**Source URL:** https://hub.phantombuster.com/reference/retrycount

---

When the agent is configured to retry on failure ("Number of retries" Phantombuster option in the agent settings), this `Number` indicates on which retry run the bot is. The first run is `0`.

JavaScript: use of buster.retryCount
    
    
    if (buster.retryCount > 0) {
      console.log("The previous bot has failed, this is run number", buster.retryCount+1)
    } else {
      console.log("This is the first run")
    }