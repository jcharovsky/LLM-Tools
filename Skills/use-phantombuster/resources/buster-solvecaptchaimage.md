# buster-solvecaptchaimage

**Source URL:** https://hub.phantombuster.com/reference/buster-solvecaptchaimage

---

**Solves a CAPTCHA image.**

This method takes an URL or a path of an image and sends it to one of our partners for solving.

If your CAPTCHA image is trivial, an OCR algorithm will quickly return the text, otherwise a human will solve it. This process generally takes less than 30 seconds and accuracy is >90%.

When a result string is returned, 1 is substracted from your daily CAPTCHA counter. In less than 10% of the cases the result will be incorrect — retry at will.

This method is asynchronous and returns nothing.  
Use the callback to know when it has finished.

## 

— urlOrPath `(String)`

URL or path of the CAPTCHA image to be solved.

## 

— headers `(CasperJS)`

HTTP headers to use when fetching the image (_optional_).  
Cookies are automatically set to get the image when using CasperJS or PhantomJS.

## 

— callback `(Function(err, result))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`result (String)`** : the solved CAPTCHA text.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const urlOrPath = "https://phantombuster.com/img/logo3-header.png"
    const headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    try {
      const result = await buster.solveCaptchaImage(urlOrPath, headers)
      console.log("The captcha text is:", result)
      //You can fill the input with result to access to the protected data
    } catch (err) {
      console.log("Could not solve the captcha image:", err)
    }
    
    
    
    const urlOrPath = "https://phantombuster.com/img/logo3-header.png"
    const headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    buster.solveCaptchaImage(urlOrPath, headers)
    .then((result) => {
      console.log("The captcha text is:", result)
      //You can fill the input with result to access to the protected data
    })
    .catch((err) => {
      console.log("Could not solve the captcha image:", err)
    })
    
    
    
    var urlOrPath = "https://phantombuster.com/img/logo3-header.png"
    var headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
    }
    
    buster.solveCaptchaImage(urlOrPath, headers, function(err, result) {
      if (err) {
        console.log("Could not solve the captcha image:", err)
      } else {
        console.log("The captcha text is:", result)
        //You can fill the input with result to access to the protected data
      }
    })