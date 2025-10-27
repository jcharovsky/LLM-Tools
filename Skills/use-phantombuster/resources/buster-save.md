# buster-save

**Source URL:** https://hub.phantombuster.com/reference/buster-save

---

**Saves a distant or local`file` to your persistent storage.**

## 

— urlOrPath `(String)`

URL or path of the file to be saved.

  * `https://www.google.com/images/srpr/logo11w.png` (from the web)
  * `foo/my_screenshot.jpg` (from your agent's disk)
  * `http://soundcloud.com/` (you'll get the HTML content of their homepage)



When saving a distant file, the MIME type is taken from the Content-Type HTTP header (if present).  
When saving a local file, the MIME type is guessed from the file extension (if this fails, no MIME type is set).

## 

— saveAs `(String)`

Where to put the `file` on your persistent storage (_optional_).  
By default, the name will be taken from `urlOrPath` and the file will be saved at the root of your agent's folder in your persistent storage.  
If a file with the same name already exists, it is overwritten.

  * `foo/ (saves http://example.com/baz/bar.png as foo/bar.png)`
  * `null (saves http://example.com/foo/bar.png as bar.png)`
  * `foo/ (fails on http://example.com/ with could not determine filename)`
  * `foo/a (saves http://example.com/bar.png as foo/a)`



_You do not need to create any intermediate directory (a/b/c/d/e.jpg will work)._

## 

— headers `(Plain Object)`

HTTP headers to use when requesting the file (_optional_).  
Cookies are automatically set when using CasperJS or PhantomJS.

## 

— callback `(Function(err, url))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong (typically if there was a network error or timeout).
  * **`url (String)`** : the full `URL` to the file on your persistent storage.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const urlOrPath = "screenshot.jpg"
    const saveAs = "screenshots/"
    
    
    try {
      const url = await buster.save(urlOrPath, saveAs)
      console.log("File successfully saved at url:", url)
      // The file is permanently saved at this url you can access
    } catch (err) {
      console.log("Could not save file:", err)
    }
    
    
    
    const urlOrPath = "screenshot.jpg"
    const saveAs = "screenshots/"
    
    buster.save(urlOrPath, saveAs)
    .then((url) => {
      console.log("File successfully save at url:", url)
      // The file is permanently saved at this url you can access
    })
    .catch((err) => {
      console.log("Could not save file:", err)
    })
    
    
    
    var urlOrPath = "screenshot.jpg"
    var saveAs = "screenshots/"
    
    buster.save(urlOrPath, saveAs, function(err, url) {
      if (err) {
        console.log("Could not save file:", err)
      } else {
        console.log("File successfully save at url:", url)
        // The file is permanently saved at this url you can access
      }
    })
    

Async/AwaitPromisesCallbacks (ES5)
    
    
    const urlOrPath = "https://phantombuster.com"
    const saveAs = "phantombuster.html"
    const headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    try {
      const url = await buster.save(urlOrPath, saveAs, headers)
      console.log("File successfully saved at url:", url)
      // The file is permanently saved at this url you can access
    } catch (err) {
      console.log("Could not save file:", err)
    }
    
    
    
    const urlOrPath = "https://phantombuster.com"
    const saveAs = "phantombuster.html"
    const headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    buster.save(urlOrPath, saveAs, headers)
    .then((url) => {
      console.log("File successfully saved at url:", url)
      // The file is permanently saved at this url you can access
    })
    .catch((err) => {
      console.log("Could not save file:", err)
    })
    
    
    
    var urlOrPath = "https://phantombuster.com"
    var saveAs = "phantombuster.html"
    var headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    buster.save(urlOrPath, saveAs, headers, function (err, url) {
      if (err) {
        console.log("Could not save file:", err)
      } else {
        console.log("File successfully saved at url:", url)
        // The file is permanently saved at this url you can access
      }
    })
    

> ## 🚧
> 
> Specify the right url
> 
> Since save() can either save local and distant files, you must specify the exact URL if you want to save a distant file.  
>  ~~"phantombuster.com"~~ -bad  
>  "[https://phantombuster.com"](https://phantombuster.com%22) -good