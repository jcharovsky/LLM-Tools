# buster-savebase64

**Source URL:** https://hub.phantombuster.com/reference/buster-savebase64

---

**Saves a`Base64 encoded file` to your persistent storage.**

## 

— base64String `(String)`

Contents of the `file` to save. Can be pure Base64 or a [Data URI Scheme](https://en.wikipedia.org/wiki/Data_URI_scheme) string starting with `data:`.

## 

— saveAs `(String)`

Where to put the `file` on your persistent storage.  
If a file with the same name already exists, it is overwritten.

  * `file.jpg`
  * `any/sub/directory/file.png`
  * `dir/` (fails because no file name was given)



_You do not need to create any intermediate directory (a/b/c/d/e.jpg will work)._

## 

— mime `(String)`

MIME type of the file being saved (optional).  
By default, it is guessed either from the Data URI Scheme string or from the file extension of the `saveAs` parameter (if this fails, no MIME type is set).

  * `image/jpeg`
  * `image/png`
  * `image/svg+xml`



## 

— callback `(Function(err, url))`

Function called when finished.

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong (typically if there was a network error or timeout).
  * **`url (String)`** : the full `url` to the file on your persistent storage.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const base64String = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4AoTFC0xuFcAiwAAAgtJREFUOMuVk81rE1EUxX9v5iUzaZKxaWM/UqxV0BZFEUF041ZEBMWFH3t10UX/guIfIHTptijFRaEuXLnrwkWlIii6kGIQ7Efa0urMYJJpk8xcF2PbiRaxZ/O4F95595zzrrrw+ovwBwTQSmGquA4FWiIo/oZOFpFAylAM5ywuFTo4mU0jwEK1wRu3RrnWoBkJRoJJ7UwQCWRMxf3BLu4MdGIb7e/Vw4ipZY+pZZetcI9EJ8ceHerm3kAn+6HDNHh4tItIhMkld7dvQKzvYqGDK4fz/AsKuNF/iOGcRZQkMFGcd2y60yZzbp0HH1d4XN6gJbG0RwvrjH6qMO/WKVmakayFuUNQsjW3BzopWrGap0suT86UOJGzeO8HzLk1zjo2E6f6ma74APTZmuu9DsW0Ro8dKzKSs5j3AgBu9jnMVHxMFOccGwGer3i8XPe52pPfjXXseJHLfoBeDJqcduzfNsK1njyLQZNyrcHE100i4FafQ9Y0OJJJJcxTVFsRenLxB7Pfq9wt7bk/mEmR1wa9dixrKJPGNvdizZoG4wtrfPAD9FYkfKs3YzcTKKRMCilz3zS0Urzz6vGn2olHcTCoZIwASh2UIkEQihCJ/PclQZAkQRAKrzZ+4jUjni25rG23mFn1eevV+VzdZrri4zVDXqz6eK2Q2c0qjUjal0kAEVCq/YzltfeSe/YL9WDOKpeKAEQAAAAASUVORK5CYII="
    const saveAs = "img/phantom.png"
    const mime = "image/png"
    
    try {
      const url = await buster.saveBase64(base64Image, saveAs, mime)
      console.log("File successfully saved at:", url)
      // The file is permanently saved at this url you can access
    } catch (err) {
      console.log("Could not save the file:", err)
    }
    
    
    
    const base64String = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4AoTFC0xuFcAiwAAAgtJREFUOMuVk81rE1EUxX9v5iUzaZKxaWM/UqxV0BZFEUF041ZEBMWFH3t10UX/guIfIHTptijFRaEuXLnrwkWlIii6kGIQ7Efa0urMYJJpk8xcF2PbiRaxZ/O4F95595zzrrrw+ovwBwTQSmGquA4FWiIo/oZOFpFAylAM5ywuFTo4mU0jwEK1wRu3RrnWoBkJRoJJ7UwQCWRMxf3BLu4MdGIb7e/Vw4ipZY+pZZetcI9EJ8ceHerm3kAn+6HDNHh4tItIhMkld7dvQKzvYqGDK4fz/AsKuNF/iOGcRZQkMFGcd2y60yZzbp0HH1d4XN6gJbG0RwvrjH6qMO/WKVmakayFuUNQsjW3BzopWrGap0suT86UOJGzeO8HzLk1zjo2E6f6ma74APTZmuu9DsW0Ro8dKzKSs5j3AgBu9jnMVHxMFOccGwGer3i8XPe52pPfjXXseJHLfoBeDJqcduzfNsK1njyLQZNyrcHE100i4FafQ9Y0OJJJJcxTVFsRenLxB7Pfq9wt7bk/mEmR1wa9dixrKJPGNvdizZoG4wtrfPAD9FYkfKs3YzcTKKRMCilz3zS0Urzz6vGn2olHcTCoZIwASh2UIkEQihCJ/PclQZAkQRAKrzZ+4jUjni25rG23mFn1eevV+VzdZrri4zVDXqz6eK2Q2c0qjUjal0kAEVCq/YzltfeSe/YL9WDOKpeKAEQAAAAASUVORK5CYII="
    const saveAs = "img/phantom.png"
    const mime = "image/png"
    
    await buster.saveBase64(base64Image, saveAs, mime)
    .then((url) => {
      console.log("File successfully saved at:", url)
      // The file is permanently saved at this url you can access
    })
    .catch((err) => {
      console.log("Could not save the file:", err)
    })
    
    
    
    var base64String = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4AoTFC0xuFcAiwAAAgtJREFUOMuVk81rE1EUxX9v5iUzaZKxaWM/UqxV0BZFEUF041ZEBMWFH3t10UX/guIfIHTptijFRaEuXLnrwkWlIii6kGIQ7Efa0urMYJJpk8xcF2PbiRaxZ/O4F95595zzrrrw+ovwBwTQSmGquA4FWiIo/oZOFpFAylAM5ywuFTo4mU0jwEK1wRu3RrnWoBkJRoJJ7UwQCWRMxf3BLu4MdGIb7e/Vw4ipZY+pZZetcI9EJ8ceHerm3kAn+6HDNHh4tItIhMkld7dvQKzvYqGDK4fz/AsKuNF/iOGcRZQkMFGcd2y60yZzbp0HH1d4XN6gJbG0RwvrjH6qMO/WKVmakayFuUNQsjW3BzopWrGap0suT86UOJGzeO8HzLk1zjo2E6f6ma74APTZmuu9DsW0Ro8dKzKSs5j3AgBu9jnMVHxMFOccGwGer3i8XPe52pPfjXXseJHLfoBeDJqcduzfNsK1njyLQZNyrcHE100i4FafQ9Y0OJJJJcxTVFsRenLxB7Pfq9wt7bk/mEmR1wa9dixrKJPGNvdizZoG4wtrfPAD9FYkfKs3YzcTKKRMCilz3zS0Urzz6vGn2olHcTCoZIwASh2UIkEQihCJ/PclQZAkQRAKrzZ+4jUjni25rG23mFn1eevV+VzdZrri4zVDXqz6eK2Q2c0qjUjal0kAEVCq/YzltfeSe/YL9WDOKpeKAEQAAAAASUVORK5CYII="
    var saveAs = "img/phantom.png"
    var mime = "image/png"
    
    await buster.saveBase64(base64Image, saveAs, mime, function (err, url) {
      if (err) {
        console.log("Could not save the file:", err)
      } else {
        console.log("File successfully saved at:", url)
        // The file is permanently saved at this url you can access
      }
    })