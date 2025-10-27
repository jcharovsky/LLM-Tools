# buster-pushover

**Source URL:** https://hub.phantombuster.com/reference/buster-pushover

---

**Sends a push notification to your device(s) using Pushover.**

For this call to work, you must have set a Pushover `user key` in your settings and have installed a Pushover client on at least one of your devices.

## 

— message `(String)`

Text contents of the notification.

## 

— options `(PlainObject)`

Additionnal parameters to send to Pushover. Get the full details at the [Pushover API documentation](https://pushover.net/api).

  * `device` \- your device name to send the message directly to that device, rather than all of your devices (multiple devices may be separated by a comma).
  * `title` \- your message's title, otherwise `Phantombuster` is used.
  * `url` \- a supplementary URL to show with your message.
  * `url_title` \- a title for your supplementary URL, otherwise just the URL is shown.
  * `priority` \- send as `-2` to generate no notification/alert, `-1` to always send as a quiet notification or `1` to display as high-priority and bypass your quiet hours.
  * `timestamp` \- a Unix timestamp of your message's date and time to display, rather than the time the message is received by Pushover.
  * `sound` \- the name of one of the sounds supported by device clients to override your `default sound` choice.



_Note: at the moment this method does not support the receipt system of Pushover (priority set to`2`)._

## 

— callback `(Function(err))`

Function called when finished(optional).

  * **`err (String)`** : `null` or a description of what went wrong if something went wrong.



Async/AwaitPromisesCallbacks (ES5)
    
    
    const message = "This is a sample message for a Pushover notification"
    const options = {
      device: "my_device",
      title: "Sample notification",
      url: "https://phantombuster.com",
      url_title: "Phantombuster",
      priority: 1,
      timestamp: 1331249662, //March 8, 2011 17:34:22 CST 
      sound: "magic"
    }
    
    try {
      await buster.pushover(message, options)
      //The notification is send with your Pushover settings
    } catch (err) {
    	console.log("Could not send the notification:", err)
    }
    
    
    
    const message = "This is a sample message for a Pushover notification"
    const options = {
      device: "my_device",
      title: "Sample notification",
      url: "https://phantombuster.com",
      url_title: "Phantombuster",
      priority: 1,
      timestamp: 1331249662, //March 8, 2011 17:34:22 CST 
      sound: "magic"
    }
    
    buster.pushover(message, options)
    .then(() => {
      //The notification is send with your Pushover settings
    })
    .catch((err) => {
    	console.log("Could not send the notification:", err)
    })
    
    
    
    var message = "This is a sample message for a Pushover notification"
    var options = {
      device: "my_device",
      title: "Sample notification",
      url: "https://phantombuster.com",
      url_title: "Phantombuster",
      priority: 1,
      timestamp: 1331249662, //March 8, 2011 17:34:22 CST 
      sound: "magic"
    }
    
    buster.pushover(message, options, function(err) {
      if (err) {
        console.log("Could not send the notification:", err)
      } else {
        //The notification is send with your Pushover settings
      }
    })