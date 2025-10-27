# buster-mail

**Source URL:** https://hub.phantombuster.com/reference/buster-mail

---

**Sends an email from your agent and substracts 1 to your daily email counter.**

## 

— subject `(String)`

Subject of the email.

## 

— text `(String)`

Plain text contents of the email.

## 

— to `(String)`

Where to send the email (optional).  
When omitted, the email will be sent to the address associated with your Phantombuster account.

## 

— callback `(Function(err))`

Function called when finished(optional).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const subject = "Mail subject"
    const text = "This a sample text for an email."
    const to = "[[email protected]](/cdn-cgi/l/email-protection)"
    
    try {
      await buster.mail(subject, text, to)
      //The mail is send to [[email protected]](/cdn-cgi/l/email-protection)
    } catch (err) {
    	console.log("Could not send the mail:", err)
    }
    
    
    
    const subject = "Mail subject"
    const text = "This a sample text for an email."
    const to = "[[email protected]](/cdn-cgi/l/email-protection)"
    
    buster.mail(subject, text, to)
    .then(() => {
      //The mail is send to [[email protected]](/cdn-cgi/l/email-protection)
    })
    .catch((err) => {
    	console.log("Could not send the mail:", err)
    })
    
    
    
    var subject = "Mail subject"
    var text = "This a sample text for an email."
    var to = "[[email protected]](/cdn-cgi/l/email-protection)"
    
    buster.mail(subject, text, to, function(err) {
      if (err) {
        console.log("Could not send the mail:", err)
      } else {
        //The mail is send to [[email protected]](/cdn-cgi/l/email-protection)
      }
    })
    

![238](https://files.readme.io/07da56e-Capture_decran_2017-04-21_a_1.42.26_PM.png)