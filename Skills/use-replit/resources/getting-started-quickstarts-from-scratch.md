# getting-started-quickstarts-from-scratch

**Source URL:** https://docs.replit.com/getting-started/quickstarts/from-scratch

---

Skip to main content

[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

  * [Docs](/getting-started/intro-replit)
  * [Tutorials](/tutorials/vibe-coding-101)
  * [Trust & Billing](/category/billing)
  * [Teams and Enterprise](/category/teams)
  * [Changelog](/updates/2025/10/24/changelog)



##### Getting Started

  * [Introduction](/getting-started/intro-replit)
  * Quickstarts

    * [Remix](/getting-started/quickstarts/remix-an-app)
    * [Create with AI](/getting-started/quickstarts/ask-ai)
    * [Build from Scratch](/getting-started/quickstarts/from-scratch)
    * Import

  * [Replit Core](/replit-core/replit-core)



##### Replit Apps

  * [Overview](/category/replit-apps)
  * [Import](/replit-app/import-to-replit)
  * [Collaboration](/replit-app/collaborate)
  * [Visibility](/replit-app/visibility)
  * [Advanced Configuration](/replit-app/configuration)
  * [App Embed](/replit-app/app-embed)
  * [Developer Frameworks](/replit-workspace/templates)



##### Replit AI

  * [Overview](/category/replit-ai)
  * [Agent](/replitai/agent)
  * Autonomy & validation

  * Features

  * Integrations

  * Visual edits




##### Replit Workspace

  * [Overview](/category/replit-workspace)
  * Features

  * [Themes](/replit-workspace/replit-themes)



##### Publishing your App

  * [Overview](/category/replit-deployments)
  * Deployment Types

  * Advanced Configuration




##### Storage and Databases

  * [Overview](/category/storage-and-databases)
  * [Database](/cloud-services/storage-and-databases/sql-database)
  * [Production Databases](/cloud-services/storage-and-databases/production-databases)
  * App Storage

  * [Key-Value Store](/cloud-services/storage-and-databases/replit-database)



##### Platforms

  * [Mobile App](/platforms/mobile-app)
  * [Desktop App](/platforms/desktop-app)



##### Extensions

  * [Overview](/extensions/extensions)
  * Basics

  * Development

  * Examples

  * API Reference

  * [Overview](/extensions/publish)
  * [Overview](/extensions/faq)



##### Additional Resources

  * [CLUI](/additional-resources/clui-graphical-cli)
  * [Cheat Sheet](/additional-resources/cheat-sheet)
  * [FAQ](/faq)



  * [Start Building](https://replit.com/signup)
  * 


[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

Search...

Navigation

Quickstarts

Build from Scratch

## 

​

Create your app from a Template

⏰ _Estimated time: 15 minutes_ Learn how to create your Replit App from a **Template** in this guide. A Template is a set of ready-made setup and configuration files that get you coding faster. This tutorial demonstrates how to build a web app using a Replit Template for Express.js, a popular backend JavaScript framework. Templates provide ready-made project configuration files to get you coding faster, but exclude application logic to let you build your own ideas from scratch. For tutorials on building apps in other ways, see [Quickstart Guides](/getting-started/intro-replit#quickstart-guides). When you complete the tutorial, your app should resemble the following image:

![image of the Preview tool showing the finished app](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_aloha.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f361798d7adde0187c233a3ee4e977f5)

1

Create an App

Navigate to the Home screen and select **Create App** :![image of the Create App button](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_create_app_button.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2a49e7e011d640d210cb993637f6d148)

2

Choose a Template

Select the **Choose a Template** tab and enter “Express.js” in the search field to locate the corresponding Template as shown in the following image:

![image of the Template selection in the Create App dialog](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/quickstart_scratch_express_template.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ffc58dbee0c4416ff9399164adc8e897)

Set the App’s title in the **Title** field and make sure **Private** is selected. You can modify these values later.Select **Create App** to proceed.

3

Modify the app using Assistant

Navigate to the **Assistant** tab.Assistant is Replit’s AI-powered tool that specializes in building smaller changes to your app.Enter the following prompt in the text area and submit it to modify a specific file:

Copy

Ask AI
    
    
    Update the endpoint in index.js to say "Hello, Replit!" followed by a random cheerful emoji.
    

You can optionally refer to a specific filename by preceding it with the `@` character.

Select **Apply all** to accept changes or **Preview code changes** to view them.After applying the changes, you should see the updated message in the **Preview** tab as shown in the following image:

![image of the Preview tool showing the default endpoint](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/quickstart_scratch_hello.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=dde7eb7688f83f10abfd3c2c55ab5684)

4

Modify the code directly

Navigate to the **Files** tab to access your Replit App’s files.Select `index.js` to open a file editor tab.Locate the endpoint and change the message from “Hello, Replit!” to “Aloha, Replit!”If you’re unsure where to edit, replace the endpoint with the following code:

Copy

Ask AI
    
    
        app.get('/', (req, res) => {
            const emojis = ['😊', '🎉', '✨', '🌟', '💫', '🌈', '🎨', '🚀'];
            const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
            res.send(`<h1>Aloha, Replit! ${randomEmoji}</h1>`);
        });
    

Switch to the **Preview** tab and select the refresh button .After the browser reloads, the page should resemble the following image:

![image of the Preview tool showing the new message](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_aloha.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f361798d7adde0187c233a3ee4e977f5)

## 

​

Explore

Try the tasks in the following sections to build your knowledge of Replit.

### 

​

Add a dependency using Assistant

Follow these steps to add the `morgan` package, which lets you configure request logging for your Express.js server:

1

Craft a prompt

From the **All Tools** tab or search box, locate and select **Assistant**. Assistant is an AI chatbot that can modify your code to add new features or fix errors.Enter the following prompt in the text area and submit it:

Copy

Ask AI
    
    
    Add the morgan HTTP request logger
    

After analyzing the request and existing code, Assistant prompts you to view or accept its changes as shown in the following dialog:

![image of Assistant recommending installation of the morgan npm package](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/quickstart_scratch_morgan.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=bb0a2599addfca5a3e5b9aabbba277aa)

Select **Apply All** to add the dependency and update the configuration.

2

Verify the installation

Navigate to the **Dependencies** tab.The dependencies list should include the `morgan` package as shown in the following image:

![image of the Dependencies list including morgan](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_dependency_morgan.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6c80f72c83a1978cd4375617c3d60fc5)

### 

​

Add a dependency manually

You can edit the package manager configuration files or use the **Dependencies** tool to manage the frameworks and libraries your app uses.

1

Open the Dependencies tab

To access the tool, open the **All Tools** tab or search box, locate and select the **Dependencies** tab as shown in the following image:

![image of the Dependencies tab](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_dependencies_tab.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ce0d51ea0fbe412affbc4135866b77b1)

2

Add a package

In the **Imports** tab, select **Add new package** to open a dialog. Search for and add the “express-rate-limit” package as shown in the following image:

![image of adding the express-rate-limit dependency](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_dependency_search.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f38e8fee97680d7a856a076cff79f59e)

Alternatively, select **Open package.json** to open `package.json` in an editor tab, where you can add or edit dependencies.

### 

​

Try Assistant’s recommendations

In addition to adding or modifying features in your app, Assistant can provide suggestions or ideas to extend its functionality. Follow these steps to request a feature recommendation and implement it using Assistant:

1

Ask Assistant for recommendations

Navigate to the **Assistant** tab.Enter the following prompt in the text area and submit it:

Copy

Ask AI
    
    
    What features should I consider next?
    

Assistant might respond with the options shown in the following image:

![image of Assistant recommendations](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_assistant_recommendations.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=ff1f9ecd3c29dcd69456b7611f0266d5)

2

Request a feature

Enter the following prompt in the text area and submit it:

Copy

Ask AI
    
    
    Add API endpoints that let me modify the message
    

Assistant might respond with the implementation described in the following image:

![image of Assistant implementing API endpoints](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_assistant_api.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6614f13fccb9e6a568dfb168640fe45d)

Select **Apply all** to make the code changes.

3

Test the changes

Test the API endpoints by navigating to the **Shell** tab and running the shell commands recommended by Assistant.Alternatively, ask Assistant to test the endpoints. In the response, you should see action buttons such as **Run** and **Run in Shell** as shown in the following image:

![image of Assistant implementing API endpoints](https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/quickstart_scratch_assistant_api_test.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=56c3bcdbf9e0861a96efdf894592614a)

Select these to execute the commands to retrieve the current message and update it.Verify changes to the message by navigating to the **Preview** tab and selecting **Refresh** in the address toolbar.

### 

​

Customize the workflow

Replit Apps include a **workflow** , a customizable sequence of steps that execute when you select **Run**. Follow these steps to set up a new workflow using Assistant.

1

Customize the workflow

The Express.js Template includes a workflow that runs a command to start the Express.js server. However, the server requires a restart to view the latest changes to the files it serves which can inconvenience development.To avoid this repetitive task, you can ask Assistant to perform the following tasks:

  * Install the [nodemon](https://www.npmjs.com/package/nodemon) package which automatically restarts the Express.js server when it detects file changes
  * Update the workflow to manage the Express.js server using `nodemon`.

To request this change, navigate to the **Assistant** tab and enter the following prompt:

Copy

Ask AI
    
    
    Install nodemon and configure the app to automatically restart the Express server whenever I make changes
    

Assistant’s response should resemble the following image:

![image of Assistant recommending installation of the nodemon package](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/quickstart_scratch_nodemon.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3d81b0664303610e22c1982679adf2a8)

Select **Install** to add the dependencies, and **Apply All** to update the configuration.

2

Test the changes

To confirm the workflow updates, select the downward arrow next to the **Run** or **Stop** button and select **Manage Workflows** as shown in the following image:![image of the Manage Workflows button in the menu](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/quickstart_scratch_workflows.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=53b7bad7d5612bdd74616d996157529c)

The name of the workflow generated by the Assistant might vary.

Select the **Dev** workflow to view the details, which should resemble the following image:

![image of the Dev workflow that uses nodemon](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/quickstart_scratch_workflows_dev.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=8c9c17b437b16daa3afe8c45b81a6a5c)

To ensure your App runs using the selected workflow, select **Stop** and then **Run**.Try making a change to the message returned by the endpoint. After your update, you should see the updated message in the **Preview** tab.

## 

​

Continue your journey

Now that you’ve completed this tutorial, you’re ready to explore more possibilities with your Replit App. Try the following next steps to enhance your skills:

  * Browse the Replit Templates on the [Templates](https://replit.com/templates) page.
  * Start a Replit App using the [Blank Repl Template](https://replit.com/@replit/Blank-Repl?v=1#README.md) which omits language and framework setup.
  * Share your completed Replit App as a Template by following the steps in the [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public) guide.
  * Learn more about Assistant’s capabilities from the [Replit Assistant](/replitai/assistant) documentation.



Was this page helpful?

YesNo

[Previous](/getting-started/quickstarts/ask-ai)[Import from GitHubLearn how to import GitHub repositories into Replit using rapid import or guided import methods.Next](/getting-started/quickstarts/import-from-github)

⌘I

On this page

  * Create your app from a Template
  * Explore
  * Add a dependency using Assistant
  * Add a dependency manually
  * Try Assistant’s recommendations
  * Customize the workflow
  * Continue your journey