# maxretries

**Source URL:** https://hub.phantombuster.com/reference/maxretries

---

When the agent is configured to retry on failure ("Number of retries" Phantombuster option in the agent settings), this `Number` indicates how many times the agent will automatically be restarted in case of failure (exit code different than `0`). In case this option is left at its default value (no retries), `maxRetries` is set to `0`.

JavaScript: use of buster.maxRetries
    
    
    if (buster.maxRetries === buster.retryCount) {
      console.log("This is the last chance for the bot to work!")
    } else {
      console.log("We still have " + (buster.maxRetries - buster.retryCount) + " retries left")
    }