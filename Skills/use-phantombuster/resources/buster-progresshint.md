# buster-progresshint

**Source URL:** https://hub.phantombuster.com/reference/buster-progresshint

---

**Reports the progress state of the agent.**

This affects the width and content of the progress bar displayed in the agent console on Phantombuster.

This is useful for debugging purposes and is not required for the agent to function properly. Sometimes it's just nice to see the progress of your agent in real-time.

## 

— progress `(Number)`

Progress float value between `0` and `1`.

  * `1` means 100% of the work was completed.
  * `0` means 0% of the work was completed.



## 

— label `(String)`

Optional textual description of the state of your agent (clipped to 50 characters).  
This shows up as a text inside the progress bar displayed in the agent console.

Use of progressHint()
    
    
    buster.progressHint(0.25, "First action") //25% of the work done
    buster.progressHint(0.5, "Second action") //50% of the work done
    buster.progressHint(0.75, "Third action") //75% of the work done
    buster.progressHint(1, "End of the script") //100% of the work done
    

> ## 🚧
> 
> No callback
> 
> This method does not have a callback. Using await is unnecessary.

> ## 📘
> 
> Tip
> 
> When using the standard JSON output from the Phantombuster API to get the console output, the progress object shows up like this:  
>  {  
>  label: "First action",  
>  progress: 0.25  
>  }