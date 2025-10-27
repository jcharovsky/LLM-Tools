# buster-savetext

**Source URL:** https://hub.phantombuster.com/reference/buster-savetext

---

**Saves a`string` to a `file` in your persistent storage.**

## 

— text `(String)`

Contents of the `file` to save. Can be anything, really.

## 

— saveAs `(String)`

Where to put the `file` on your persistent storage.  
If a file with the same name already exists, it is overwritten.

  * `file.txt`
  * `any/sub/directory/file.json`
  * `dir/` (fails because no file name was given)



_You do not need to create any intermediate directory (a/b/c/d/e.jpg will work)._

## 

— mime `(String)`

MIME type of the file being saved (optional).  
By default, it is guessed either from the Data URI Scheme string or from the file extension of the `saveAs` parameter (if this fails, no MIME type is set).

  * `application/json`
  * `text/csv`
  * `text/html`



## 

— callback `(Function(err, url))`

Function called when finished.

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong (typically if there was a network error or timeout).
  * **`url (String)`** : the full `url` to the file on your persistent storage.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const text   = "This a sample text."
    const saveAs = "texts/sample.txt"
    const mime   = "text/plain"
    
    try {
      const url = await buster.saveText(text, saveAs, mime)
      console.log("File successfully saved at:", url)
      // The file is permanently saved at this url you can access
    } catch (err) {
      console.log("Could not save file:", err)
    }
    
    
    
    const text   = "This a sample text."
    const saveAs = "texts/sample.txt"
    const mime   = "text/plain"
    
    buster.save(text, saveAs, mime)
    .then(() => {
      console.log("File successfully saved at:", url)
      // The file is permanently saved at this url you can access
    })
    .catch((err) =>{
      console.log("Could not save file:", err)
    })
    
    
    
    var text = "This a sample text."
    var saveAs = "texts/sample.txt"
    var mime = "text/plain"
    
    buster.save(text, saveAs, mime, function(err, url) {
      if (err) {
        console.log("Could not save file:", err)
      } else {
        console.log("File successfully saved at:", url)
        // The file is permanently saved at this url you can access
      }
    })