# buster-argument

**Source URL:** https://hub.phantombuster.com/reference/buster-argument

---

On Phantombuster, each agent receives a JSON object as an argument, which can be set each time they are launched.

JavaScript: get arguments with buster.argument
    
    
    /*Bot launched with argument:
    {
      "name": "nick",
      "age": 2 
    }
    */
    
    const arg = buster.argument
    
    console.log("The name is", arg.name, "and the age is", arg.age)
    //This will print "The name is nick and the age is 2"