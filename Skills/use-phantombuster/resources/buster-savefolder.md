# buster-savefolder

**Source URL:** https://hub.phantombuster.com/reference/buster-savefolder

---

**Saves a`folder` from your agent's disk to your persistent storage.**

## 

— path `(String)`

Path of the `folder` to save (optional, defaults to `.`).

  * `.` (everything from your current working directory)
  * `any/sub/../sub/directory`



Each file has it [MIME type](https://en.wikipedia.org/wiki/Internet_media_type) guessed from its extension (if this fails, no MIME type is set).

## 

— saveAs `(String)`

Where to put the `folder` on your persistent storage (_optional_).  
By default, the folder will be saved at the root of your agent's folder in your persistent storage.  
If files with the same name already exist, they are overwritten.

  * `/` or empty string (root of your agent's folder in your persistent storage)
  * `any/sub/directory`
  * `dir/foo.txt` (this will create a directory named `foo.txt`, obviously not recommended)



_You do not need to create any intermediate directory (a/b/c/d will work)._

## 

— callback `(Function(err, url))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong (typically if there was a network error or timeout).
  * **`url (String)`** : the full `URL` to the folder on your persistent storage.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const path = "screenshots"
    const saveAs = "agent_screenshots"
    
    try {
      const url = await buster.saveFolder(path, saveAs)
      console.log("Folder successfully at url:", url)
      // The folder is permanently saved at this url you can access
    } catch (err) {
      console.log("Could not save folder:", err)
    }
    
    
    
    const path = "screenshots"
    const saveAs = "agent_screenshots"
    
    buster.saveFolder(path, saveAs)
    .then((url) => {
      console.log("Folder successfully at url:", url)
      // The folder is permanently saved at this url you can access
    })
    .catch((err) => {
      console.log("Could not save folder:", err)
    })
    
    
    
    var path = "screenshots"
    var saveAs = "agent_screenshots"
    
    buster.saveFolder(path, saveAs, function(err, url) {
      if (err) {
        console.log("Could not save folder:", err)
      } else {
        console.log("Folder successfully at url:", url)
        // The folder is permanently saved at this url you can access
      }
    })
    

> ## 📘
> 
> Tips
> 
> If you take many screenshots or save many text files with nick rather than calling buster.save() for each file, just do a buster.saveFolder() at the end of your script.