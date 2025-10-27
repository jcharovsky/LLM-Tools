# solverecaptcha

**Source URL:** https://hub.phantombuster.com/reference/solverecaptcha

---

**Solves a Google noCAPTCHA/reCAPTCHA.**

This method sends the required tokens to one of our partners so that a human can solve a Google noCAPTCHA/reCAPTCHA challenge.

`buster.solveNoCaptcha()` calls will take about 30 to 60+ seconds to return a response token. It mainly depends on the availability of human workers in the queue and their ability to quickly solve the challenges from Google.

When a result token is returned, 2 is substracted from your daily CAPTCHA counter. Contrary to standard image CAPTCHA solving methods, when returned, this token is always valid.

## 

— siteUrl `(String)`

URL of the page or website where the noCAPTCHA/reCAPTCHA widget is found.  
When using NickJS, simply use the return value from `tab.getUrl()`.

## 

— captchaToken `(String)`

Token of the noCAPTCHA/reCAPTCHA widget. This token is generally found in the `data-sitekey` attribute of the `<div class="g-recaptcha">` element. However, some site administrators use the widget differently and you might have to find this token somewhere else, for example in the `&k=<TOKEN>` parameter of the URL of the widget's `<iframe>`.

## 

— secret `(String)`

Second token from the noCAPTCHA/reCAPTCHA widget (_optional_).  
Almost all websites do not use this token anymore, it is only for deprecated noCAPTCHA/reCAPTCHA versions. If present, it's generally found in the `data-stoken` attribute of the widget's `<div>`.

## 

— callback `(Function(err, result))`

Function called when finished (_optional_).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.
  * **`result (String)`** : the response token, put this as a value in the `<textarea id="g-recaptcha-response">` element and submit the form.



> ## 🚧
> 
> Custom noCAPTCHA/reCAPTCHA installations
> 
> Not all websites use this CAPTCHA system the same way. The widget supports custom JavaScript integration, as you can see in its [official documentation](https://developers.google.com/recaptcha/docs/display). If that's the case on your target website (not common), you'll first have to understand how the widget is integrated to get its token and to submit the result.

> ## 📘
> 
> Also supports "invisible" noCAPTCHA!
> 
> The new "invisible" noCAPTCHA is basically the same widget but hidden in the page and automatically activated. Check its [official documentation](https://developers.google.com/recaptcha/docs/invisible) to understand how your target website might integrate it.

Async/AwaitPromisesCallbacks (ES5)
    
    
    const siteUrl = "https://www.google.com/recaptcha/api2/demo"
    const captchaToken = await tab.evaluate((args, callback) => {
      const token = document.querySelector(".g-recaptcha[data-sitekey]").dataset.sitekey
      callback(null, token)
    }, null)
    
    try {
      const result = await buster.solveNoCaptcha(siteUrl, captchaToken)
      console.log("The reCAPTCHA response token is:", result)
      //You can fill the g-recaptcha-response <textarea> with result to access to the protected data
    } catch (err) {
      console.log("Could not solve reCAPTCHA:", err)
    }
    
    
    
    const siteUrl = "https://www.google.com/recaptcha/api2/demo"
    const captchaToken = "reC4PTCH4_token"
    
    buster.solveNoCaptcha(siteUrl, captchaToken)
    .then((result) => {
      console.log("The reCAPTCHA text is:", result)
      //You can fill the input with result to access to the protected data
    })
    .catch((err) => {
      console.log("Could not solve reCAPTCHA:", err)
    })
    
    
    
    const siteUrl = "https://www.google.com/recaptcha/api2/demo"
    const captchaToken = "reC4PTCH4_token"
    
    buster.solveCaptcha(siteUrl, captchaToken, function(err, result) {
      if (err) {
        console.log("Could not solve reCAPTCHA:", err)
      } else {
        console.log("The reCAPTCHA text is:", result)
        //You can fill the input with result to access to the protected data
      }
    })