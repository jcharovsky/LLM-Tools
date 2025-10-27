# buster-solvecaptchabase64

**Source URL:** https://hub.phantombuster.com/reference/buster-solvecaptchabase64

---

**Solves a CAPTCHA image.**

This method takes a Base64 encoded image and sends it to one of our partners for solving.

If your CAPTCHA image is trivial, an OCR algorithm will quickly return the text, otherwise a human will solve it. This process generally takes less than 30 seconds and accuracy is >90%.

When a result string is returned, 1 is substracted from your daily CAPTCHA counter. In less than 10% of the cases the result will be incorrect — retry at will.

This method is asynchronous and returns nothing.  
Use the callback to know when it has finished.

## 

— base64String `(String)`

CAPTCHA image to solve.  
Can be pure Base64 or a Data URI Scheme string starting with `data:`.

## 

— callback `(Function(err, result))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`result (String)`** : the solved CAPTCHA text.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const base64String = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4AoTFC0xuFcAiwAAAgtJREFUOMuVk81rE1EUxX9v5iUzaZKxaWM/UqxV0BZFEUF041ZEBMWFH3t10UX/guIfIHTptijFRaEuXLnrwkWlIii6kGIQ7Efa0urMYJJpk8xcF2PbiRaxZ/O4F95595zzrrrw+ovwBwTQSmGquA4FWiIo/oZOFpFAylAM5ywuFTo4mU0jwEK1wRu3RrnWoBkJRoJJ7UwQCWRMxf3BLu4MdGIb7e/Vw4ipZY+pZZetcI9EJ8ceHerm3kAn+6HDNHh4tItIhMkld7dvQKzvYqGDK4fz/AsKuNF/iOGcRZQkMFGcd2y60yZzbp0HH1d4XN6gJbG0RwvrjH6qMO/WKVmakayFuUNQsjW3BzopWrGap0suT86UOJGzeO8HzLk1zjo2E6f6ma74APTZmuu9DsW0Ro8dKzKSs5j3AgBu9jnMVHxMFOccGwGer3i8XPe52pPfjXXseJHLfoBeDJqcduzfNsK1njyLQZNyrcHE100i4FafQ9Y0OJJJJcxTVFsRenLxB7Pfq9wt7bk/mEmR1wa9dixrKJPGNvdizZoG4wtrfPAD9FYkfKs3YzcTKKRMCilz3zS0Urzz6vGn2olHcTCoZIwASh2UIkEQihCJ/PclQZAkQRAKrzZ+4jUjni25rG23mFn1eevV+VzdZrri4zVDXqz6eK2Q2c0qjUjal0kAEVCq/YzltfeSe/YL9WDOKpeKAEQAAAAASUVORK5CYII="
    
    try {
      const result = await buster.solveCaptchaBase64(base64String)
      console.log("The captcha text is:", result)
      //You can fill the input with result to access to the protected data
    } catch (err) {
      console.log("Could not solve the captcha base 64:", err)
    }
    
    
    
    const base64String = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4AoTFC0xuFcAiwAAAgtJREFUOMuVk81rE1EUxX9v5iUzaZKxaWM/UqxV0BZFEUF041ZEBMWFH3t10UX/guIfIHTptijFRaEuXLnrwkWlIii6kGIQ7Efa0urMYJJpk8xcF2PbiRaxZ/O4F95595zzrrrw+ovwBwTQSmGquA4FWiIo/oZOFpFAylAM5ywuFTo4mU0jwEK1wRu3RrnWoBkJRoJJ7UwQCWRMxf3BLu4MdGIb7e/Vw4ipZY+pZZetcI9EJ8ceHerm3kAn+6HDNHh4tItIhMkld7dvQKzvYqGDK4fz/AsKuNF/iOGcRZQkMFGcd2y60yZzbp0HH1d4XN6gJbG0RwvrjH6qMO/WKVmakayFuUNQsjW3BzopWrGap0suT86UOJGzeO8HzLk1zjo2E6f6ma74APTZmuu9DsW0Ro8dKzKSs5j3AgBu9jnMVHxMFOccGwGer3i8XPe52pPfjXXseJHLfoBeDJqcduzfNsK1njyLQZNyrcHE100i4FafQ9Y0OJJJJcxTVFsRenLxB7Pfq9wt7bk/mEmR1wa9dixrKJPGNvdizZoG4wtrfPAD9FYkfKs3YzcTKKRMCilz3zS0Urzz6vGn2olHcTCoZIwASh2UIkEQihCJ/PclQZAkQRAKrzZ+4jUjni25rG23mFn1eevV+VzdZrri4zVDXqz6eK2Q2c0qjUjal0kAEVCq/YzltfeSe/YL9WDOKpeKAEQAAAAASUVORK5CYII="
    
    buster.solveCaptchaBase64(base64String)
    .then((result) => {
      console.log("The captcha text is:", result)
      //You can fill the input with result to access to the protected data
    })
    .catch((err) => {
      console.log("Could not solve the captcha base 64:", err)
    })
    
    
    
    var base64String = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4AoTFC0xuFcAiwAAAgtJREFUOMuVk81rE1EUxX9v5iUzaZKxaWM/UqxV0BZFEUF041ZEBMWFH3t10UX/guIfIHTptijFRaEuXLnrwkWlIii6kGIQ7Efa0urMYJJpk8xcF2PbiRaxZ/O4F95595zzrrrw+ovwBwTQSmGquA4FWiIo/oZOFpFAylAM5ywuFTo4mU0jwEK1wRu3RrnWoBkJRoJJ7UwQCWRMxf3BLu4MdGIb7e/Vw4ipZY+pZZetcI9EJ8ceHerm3kAn+6HDNHh4tItIhMkld7dvQKzvYqGDK4fz/AsKuNF/iOGcRZQkMFGcd2y60yZzbp0HH1d4XN6gJbG0RwvrjH6qMO/WKVmakayFuUNQsjW3BzopWrGap0suT86UOJGzeO8HzLk1zjo2E6f6ma74APTZmuu9DsW0Ro8dKzKSs5j3AgBu9jnMVHxMFOccGwGer3i8XPe52pPfjXXseJHLfoBeDJqcduzfNsK1njyLQZNyrcHE100i4FafQ9Y0OJJJJcxTVFsRenLxB7Pfq9wt7bk/mEmR1wa9dixrKJPGNvdizZoG4wtrfPAD9FYkfKs3YzcTKKRMCilz3zS0Urzz6vGn2olHcTCoZIwASh2UIkEQihCJ/PclQZAkQRAKrzZ+4jUjni25rG23mFn1eevV+VzdZrri4zVDXqz6eK2Q2c0qjUjal0kAEVCq/YzltfeSe/YL9WDOKpeKAEQAAAAASUVORK5CYII="
    
    buster.solveCaptchaBase64(base64String, function(err, result) {
      if (err) {
        console.log("Could not solve the captcha base 64:", err)
      } else {
        console.log("The captcha text is:", result)
        //You can fill the input with result to access to the protected data
      }
    })