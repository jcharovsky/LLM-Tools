# code-builtin-date-time

**Source URL:** https://docs.n8n.io/code/builtin/date-time/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/date-time.md "Edit this page")

# Built-in date and time methods#

Methods for working with date and time. 

Python support

You can use Python in the Code node. It isn't available in expressions.

JavaScriptPython

Method | Description | Available in Code node?  
---|---|---  
`$now` | A Luxon object containing the current timestamp. Equivalent to `DateTime.now()`. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg)  
`$today` | A Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg)  
  
Method | Description  
---|---  
`_now` | A Luxon object containing the current timestamp. Equivalent to `DateTime.now()`.  
`_today` | A Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`.  
  
Don't mix native JavaScript and Luxon dates

While you can use both native JavaScript dates and Luxon dates in n8n, they aren't directly interoperable. It's best to [convert JavaScript dates to Luxon](../../cookbook/luxon/#convert-javascript-dates-to-luxon) to avoid problems.

n8n provides built-in convenience functions to support data transformation in expressions for dates. Refer to [Data transformation functions | Dates](../data-transformation-functions/dates/) for more information.

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top