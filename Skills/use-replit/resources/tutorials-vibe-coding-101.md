# tutorials-vibe-coding-101

**Source URL:** https://docs.replit.com/tutorials/vibe-coding-101

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



##### Vibe Coding & Prompting

  * [Vibe coding 101](/tutorials/vibe-coding-101)
  * [Efficient prompting](/tutorials/effective-prompting)
  * [How to vibe code effectively](/tutorials/how-to-vibe-code)
  * [Advanced AI features](/tutorials/advanced-ai-features)



##### Agent & Assistant

  * [Notion-powered website](/tutorials/build-a-notion-powered-website)
  * [Create mobile apps with Replit](/tutorials/expo-on-replit)
  * [Create a cat image generator](/getting-started/quickstarts/no-code-cat-image-generator)
  * [Create a file converter with AI](/getting-started/quickstarts/build-with-ai)



##### Security

  * [Built-in security features](/tutorials/vibe-code-securely)
  * [Security checklist](/tutorials/vibe-code-security-checklist)



##### MCP

  * [Learn about MCP in 3 minutes](/tutorials/mcp-in-3)



##### Deployments

  * [Publish a Grok 3 app on Replit](/tutorials/create-apps-with-grok-3)



##### Start from a template

  * [Create a Google Sheets integration](/getting-started/quickstarts/google-sheets-integration)
  * [Create a Discord bot](/getting-started/quickstarts/discord-bot)
  * [Create a Next.js app](/getting-started/quickstarts/next-js-app)
  * [Create a Flask app](/getting-started/quickstarts/flask-app)
  * [Create a FastAPI service](/getting-started/quickstarts/fastapi-service)
  * [Create a static blog with Astro](/getting-started/quickstarts/static-blog-astro)
  * [Create a HackerNews Slack bot](/getting-started/quickstarts/webscrape-and-slack-notifications)
  * [Create a Slack channel summarizer](/getting-started/quickstarts/ai-slack-channel-summarizer)



##### Data storage

  * [Add a SQL database](/getting-started/quickstarts/database-connection)
  * [App Storage in Python](/getting-started/quickstarts/object-storage-python)
  * [App Storage in JavaScript](/getting-started/quickstarts/object-storage-javascript)



##### Additional Resources

  * [Add a Replit Badge](/additional-resources/add-a-made-with-replit-badge-to-your-app)



  * [Start Building](https://replit.com/signup)
  * 


[Replit home page![light logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/light.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=7eae80cd046605cac4b4a6e7eb48369f)![dark logo](https://mintcdn.com/replit/9NKf1XREDj9JhKJb/logo/dark.svg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bcbac9afa58f8a51aa123f848bc8d7cd)](/)

Search...

⌘K

Search...

Navigation

Vibe Coding & Prompting

Vibe coding 101: from idea to published app

[![Matt Palmer](https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg)Matt PalmerHead of Developer Relations](https://youtube.com/@mattpalmer) This tutorial walks you through the “vibe coding” process on Replit—taking an idea from concept to a fully published application. This tutorial will build an interactive map visualization of San Francisco parks, pulling in external data and using modern frameworks. You’ll see how to leverage [Replit Agent](/replitai/agent) for initial development and [Replit Assistant](/replitai/assistant) for refinements and debugging.

## 

​

The vibe coding philosophy

Vibe coding is less about writing every line of code and more about guiding AI tools with your vision and domain knowledge. It’s an iterative process of prompting, reviewing, and refining. Key takeaways from the video:

  * **Conceptualize First** : Start with a clear idea of what you want to build. Visualizing the end product helps, especially when prompting AI.
  * **Domain Knowledge is Power** : Knowing relevant frameworks (like Leaflet.js for maps) or data sources (like OpenStreetMap) significantly improves AI-generated results.
  * **Iterative Development** : Expect to debug and refine. AI tools are powerful, but they’re collaborators, not magic wands.



## 

​

Project: San Francisco parks map

The goal is to build an interactive map displaying parks and public spaces in San Francisco. **Problem Statement** : The goal is an interactive map to discover parks and public spaces in San Francisco. **Solution** : An interactive tool using Leaflet.js and OpenStreetMap data. **Key lessons** :

  * Prompting AI effectively.
  * Processing external data.
  * Debugging and handling errors.



## 

​

Building with Replit Agent

Replit Agent can scaffold entire projects, set up environments, and generate initial code.

1

Crafting the Initial Prompt

A good prompt is specific. We tell Agent:

  * The goal: “Help me create a minimalist maps app to visualize San Francisco’s parks.”
  * Key technologies: “You should use leaflet for map visualization and fetch data from OpenStreetMap.”
  * Specific data types from OpenStreetMap (after research): Natural formations (woods, beaches, islets, cave entrances) and leisure locations (parks, gardens).



Copy

Ask AI
    
    
    Help me create a minimalist maps app to visualize San Francisco’s parks. You should use leaflet for map visualization and fetch data from OpenStreetMap. Include the following OpenStreetMap data types for San Francisco: natural formations (woods, beaches, islet, cave entrance) and leisure (park, gardens).

To learn more about how to write effective prompts, check out [this article](tutorials/effective-prompting).

2

Attaching a Mockup

Visual aids help Agent understand the desired layout and features. A simple sketch or mockup can be attached directly to the prompt.

![Wireframe sketch of the maps app](https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c67dc8c30de1d2fe85de17a49b8a9ec1)

3

Agent's Process

  1. **Plan Creation** : [Agent](/replitai/agent) outlines the steps it will take. Review and approve this plan.

![Replit Agent plan creation](https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e25c35ce8054f2ccb02bc8eeb607c23e)

  2. **Visual Preview** : Agent streams a visual preview of the app’s UI.

![Replit Agent visual preview](https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1d3fc339176c1fdf0cc73621109c162b)

  3. **Environment Setup** : Agent configures the development environment, installing necessary languages and packages—no manual setup required.
  4. **Building the App** : Agent writes the code for the front end and back end.
  5. **Checkpoints** : Agent creates checkpoints ([Git commits](/replit-workspace/workspace-features/version-control)) so you can roll back if something goes wrong.



4

Debugging with Agent

Errors happen. Use the browser’s DevTools (specifically the Console and Network tabs) to find error messages.

  * **Observe** : The map loaded, but no data points appeared.
  * **Investigate** : The console showed an error: “Failed to fetch map features error cannot read properties of undefined reading natural.”
  * **Inform Agent** : Paste the error message directly into the chat with Agent. Agent will attempt to debug and fix the issue.

![Browser console showing an error](https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b21be49b94e56aea8b6e15ceabd55926)


In the video, Agent identified an issue with parsing the Overpass API response and added robust error handling, which resolved the problem.

## 

​

Refining with Replit Assistant

Once Agent builds the MVP, switch to Replit Assistant for smaller, more targeted edits and refinements. Assistant is generally faster for these tasks.

Improving Map Styling

The initial map was functional but could look better. **Prompt to Assistant** : “Can you use a more minimalist carto style for OpenStreetMap? Carto lite.”This relies on knowing that “Carto lite” is a known theme for Leaflet maps.

Adding Dark Mode

A common refinement is adding a dark mode. **Prompt to Assistant** : “Can you add a dark mode to my app and use, carto dark for the map in the dark mode?”

![Replit Assistant implementing dark mode](https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/dark-mode-assistant.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=30c79e86c302549d9f683124261dad71)

Assistant will:

  * Read files for context.
  * Make changes to necessary files (e.g., theme providers, styles).
  * Restart the app to apply changes.



Iterative Debugging with Assistant

Adding dark mode involved several iterations:

  1. Initial implementation had a toggle that worked for the map but then disappeared. **Feedback** : “The toggle theme button works for the map, but it disappears when clicked. The theme toggle should be in the side nav and the theme should be applied to the side nav.”
  2. Issues with multiple toggle buttons and incorrect component references (`side nav` vs. `sidebar`). **Feedback & Guidance**: “Now there are two toggle themes. One controls the map, the other controls the side nav. Make them into one in the side. Now and update the CSS.” When Assistant made an incorrect assumption (e.g. `SideNav` component), explicitly pointing it to the correct file (`@Sidebar`) helps.
  3. Final fix to ensure the dark mode toggle in the sidebar correctly toggled the map theme to Carto Dark. **Feedback** : “Now the dark mode toggle in @Sidebar does not toggle the map to carto dark.”

This process highlights the “conversation” aspect of vibe coding. Be descriptive and guide the AI.

## 

​

Publishing your application

Replit makes publishing straightforward.

  1. Select the **[Publish](/cloud-services/deployments/about-deployments)** button.
  2. Agent suggests a publishing configuration (e.g., app name, build and run commands). Review and confirm.
  3. If your app uses API keys or other sensitive information, store them in **[Secrets](replit-workspace/workspace-features/secrets)**. Agent will use these securely.
  4. Select **Publish**. Replit bundles your app and makes it live on the web.

![Replit deployment screen](https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9634d8cb1f712a5f12be15989d690fdb)


Your published app will have a public URL (e.g., `park-mapper.replit.app`). Changes made in your development environment won’t affect the published version until you click **Republish**.

## 

​

Recap and next steps

This tutorial went from an idea to a published interactive map application without writing a single line of code manually. Replit Agent was used for the heavy lifting and Replit Assistant for refinements, leveraging domain knowledge and an iterative debugging process. **Potential Next Steps for the Park Mapper App** :

  * Add a [database](category/storage-and-databases) to store park data persistently (avoiding re-fetch on every load).
  * Allow users to save or favorite parks.
  * Implement advanced filtering.
  * Improve styling and add custom icons for map markers.
  * Enhance mobile responsiveness (e.g., ensuring filters are accessible on mobile).

Vibe coding is about iterating, experimenting, and guiding AI to bring your ideas to life. Don’t be afraid of errors; they are part of the process!

Was this page helpful?

YesNo

[Efficient promptingLearn principles and see examples for writing effective prompts when using AI development tools like Replit Agent and Assistant.Next](/tutorials/effective-prompting)

⌘I

On this page

  * The vibe coding philosophy
  * Project: San Francisco parks map
  * Building with Replit Agent
  * Refining with Replit Assistant
  * Publishing your application
  * Recap and next steps