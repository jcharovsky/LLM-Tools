# buster-solvecaptcha

**Source URL:** https://hub.phantombuster.com/reference/buster-solvecaptcha

---

**DEPRECATED (see sidebar for details). Solves a CAPTCHA image.**

This method takes a screenshot of the area indicated by `selector` and sends it to one of our partners for solving.

If your CAPTCHA image is trivial, an OCR algorithm will quickly return the text, otherwise a human will solve it. This process generally takes less than 30 seconds and accuracy is >90%.

When a result string is returned, 1 is substracted from your daily CAPTCHA counter. In less than 10% of the cases the result will be incorrect — retry at will.

## 

— selector `(String)`

CSS path indicating which part of the page to take a screenshot of for solving. Be as precise as possible (sending a large image will fail). Often, a selector for the `<img>` tag works best.

## 

— casperInstance `(CasperJS)`

CasperJS instance that will be used for capturing the image. When using NickJS, simply put `nick.driver.casper` here.

## 

— callback `(Function(err, result))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`result (String)`** : the solved CAPTCHA text.



> ## ❗️
> 
> Deprecation notice
> 
> This method is deprecated, please use [solveCaptchaBase64()](/reference/buster-solvecaptchabase64) or [solveCaptchaImage()](/reference/buster-solvecaptchaimage) instead or [solveNoCaptcha()](/reference/solverecaptcha) for Google's noCAPTCHA/reCAPTCHA.

> ## 🚧
> 
> Warning
> 
> This method is only available when using the CasperJS driver as it uses its screenshot taking capabilities.

Async/AwaitPromisesCallbacks (ES5)
    
    
    const selector = "div.captcha"
    const casperInstance = tab.driver.casper
    
    try {
      const result = await buster.solveCaptcha(selector, casperInstance)
      console.log("The captcha text is:", result)
      //You can fill the input with result to access to the protected data
    } catch (err) {
      console.log("Could not solve captcha:", err)
    }
    
    
    
    const selector = "div.captcha"
    const casperInstance = tab.driver.casper
    
    buster.solveCaptcha(selector, casperInstance)
    .then((result) => {
      console.log("The captcha text is:", result)
      //You can fill the input with result to access to the protected data
    })
    .catch((err) => {
      console.log("Could not solve captcha:", err)
    })
    
    
    
    var selector = "div.captcha"
    var casperInstance = tab.driver.casper
    
    buster.solveCaptcha(selector, casperInstance, function(err, result) {
      if (err) {
        console.log("Could not solve captcha:", err)
      } else {
        console.log("The captcha text is:", result)
        //You can fill the input with result to access to the protected data
      }
    })