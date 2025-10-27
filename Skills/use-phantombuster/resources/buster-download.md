# buster-download

**Source URL:** https://hub.phantombuster.com/reference/buster-download

---

**Downloads a distant file to your agent's disk (not to your persistent storage).**

If you do not save the file to your persistent storage (see [buster.save()](/reference/buster-save) or [buster.saveFolder()](/reference/buster-savefolder)), **it will be lost when your agent exits**.

## 

— url `(String)`

URL of the file to be downloaded.

  * `https://www.google.com/images/srpr/logo11w.png`
  * `http://soundcloud.com/` (you'll get the HTML content of their homepage)



## 

— saveAs `(String)`

Where to put the file on your agent's disk (_optional_).  
By default, the name will be taken from url and the file will be saved in the current working directory on your agent's disk.  
If a file with the same name already exists, it is overwritten.

  * `foo/ (saves http://example.com/baz/bar.png as foo/bar.png)`
  * `null (saves http://example.com/foo/bar.png as bar.png)`
  * `foo/ (fails on http://example.com/ with could not determine filename)`
  * `foo/a (saves http://example.com/bar.png as foo/a)`



**Intermediate directories are not created automatically on your agent's disk.** When using NodeJS, create directories beforehand with [require('fs').mkdirSync()](https://nodejs.org/api/fs.html#fs_fs_mkdirsync_path_mode).

## 

— headers `(Plain Object)`

HTTP headers to use when requesting the file (_optional_).  
Cookies are automatically set when using CasperJS or PhantomJS.

## 

— callback `(Function(err, path))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong (typically if there was a network error or timeout).
  * **`path (String)`** : the path to the file on your agent's disk. 



> ## 📘
> 
> Using NodeJS?
> 
> When running NodeJS within Phantombuster (the recommended binary), you also have access to common HTTP request modules such as `request`, `needle` and `fetch`. They can come in handy! See [packages & modules](/docs/packages).

Async/AwaitPromisesCallbacks (ES5)
    
    
    const url = "https://phantombuster.com"
    const saveAs = "phantombuster.html"
    const headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    try {
      const path = await buster.download(url, saveAs, headers)
      console.log("File successfully download here:", path)
      //The file is saved on the disk at this path, you can only access it inside the script
    } catch (err) {
    	console.log("Could not download the file:", err)
    }
    
    
    
    const url = "https://phantombuster.com"
    const saveAs = "phantombuster.html"
    const headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    await buster.download(url, saveAs, headers)
    .then((path) => {
      console.log("File successfully download here:", path)
      //The file is saved on the disk at this path, you can only access it inside the script
    })
    .catch((err) => {
    	console.log("Could not download the file:", err)
    })
    
    
    
    var url = "https://phantombuster.com"
    var saveAs = "phantombuster.html"
    var headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    await buster.download(url, saveAs, headers, function(err, path) {
    	if (err) {
        console.log("Could not download the file:", err)
      } else {
        console.log("File successfully download here:", path)
        //The file is saved on the disk at this path, you can only access it inside the script
      }
    })
    

> ## 🚧
> 
> Note
> 
> This file will be only accessible from your script when it is running. If you want to keep the file in your persistent storage, use buster.save() or [buster.saveFolder()](/reference/buster-savefolder) or similar.