# replitai-agent

**Source URL:** https://docs.replit.com/replitai/agent

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

Replit AI

Replit Agent

Agent uses powerful AI technology to transform your ideas into applications and seamlessly add new features by describing what you want.

**New with Agent 3** \- Extended autonomous builds with minimal supervision, App Testing for self-validation, two ways to start an app (design-first vs. full app first), and Agents & Automations for building your own autonomous systems.

## 

​

Features

Agent uses powerful AI technology to create your apps, leveraging industry-leading models to deliver the best results.

Chat with Agent in your Replit App to receive the following support:

  * Create full-stack apps from scratch
  * Add advanced features and integrate complex APIs
  * Design, create, and modify database structures
  * Streamline environment setup and dependency management



## 

​

Build Modes

**New in Agent 3** : Choose between two distinct build approaches to match your development style and project needs.

When you submit your initial prompt to create an app, Agent creates a feature list based on your request. You’ll then see the question “How do you want to continue?” with two build options:

![Agent build mode selection interface showing 'Build the full app' and 'Start with a design' options](https://mintcdn.com/replit/fq3p5W3K0mVwvlo1/images/replitai/agent-build-modes-selection.png?fit=max&auto=format&n=fq3p5W3K0mVwvlo1&q=85&s=9b3798227f9a1da43b50a9395272d338)

You can also choose to “continue planning” if you want to refine the feature list before building begins.

### 

​

Start with a design

Perfect for seeing visual results first:

  * **Quick design phase** : Agent creates a clickable front-end prototype in ~3 minutes
  * **Visual-first approach** : See how your app will look and feel before building functionality
  * **Flexible continuation** : Press “Build functionality” to have Agent complete a full working version of your app
  * **User-controlled pacing** : You decide when to move from visual prototyping to a finished application

After the design phase, you’ll see options to continue:

![Interface showing 'Keep iterating on design' and 'Build functionality' options after design phase](https://mintcdn.com/replit/pnpczhK4itt7pXl2/images/replitai/keep-iterating-design-or-build-functionality.png?fit=max&auto=format&n=pnpczhK4itt7pXl2&q=85&s=de99d5fe3010980b7af6043df5baf070)

### 

​

Build the full app

Ideal for comprehensive application development:

  * **Complete functionality** : Agent builds out the full functionality of your app from the start
  * **Initial build** : Agent creates an initial working application in ~10 minutes
  * **Comprehensive scope** : Full-stack development with frontend, backend, and integrations

After the initial build phase, you can:

  * **Review the full task list** : See exactly what Agent plans to build next
  * **Accept or modify** : Approve the plan or request changes before full implementation
  * **Complete the build** (New in Agent 3): Let Agent finish the comprehensive development (can run for up to 200 minutes)

After creating an MVP, you’ll see options to continue building:

![Interface showing 'Dismiss' and 'Continue building' options after MVP creation](https://mintcdn.com/replit/fq3p5W3K0mVwvlo1/images/replitai/continue-building-or-dismiss.png?fit=max&auto=format&n=fq3p5W3K0mVwvlo1&q=85&s=0d46c6d59a763e2cd2ba1400c2447470)

## 

​

Autonomous Features (New in Agent 3)

Agent 3 introduces powerful autonomous capabilities that enable extended, self-supervised development with minimal human intervention.

### 

​

App Testing

**Automated browser testing** \- Agent tests itself using an actual browser, navigating through your application like a real user would. **Key capabilities:**

  * **Real user simulation** : Agent clicks through your app, testing functionality and user workflows
  * **Automatic issue detection** : Identifies problems and fixes them during development
  * **Visual feedback** : Provides video replays of testing sessions for review
  * **Intelligent timing** : Agent decides when testing would be most valuable

**Usage** : Toggle “App testing” in the Agent Tools panel. When enabled, Agent intelligently decides when testing adds the most value.

![Agent Tools interface showing App testing toggle enabled with description](https://mintcdn.com/replit/fq3p5W3K0mVwvlo1/images/replitai/app-testing-toggle-on.png?fit=max&auto=format&n=fq3p5W3K0mVwvlo1&q=85&s=c5d005615afe2475bb061ebd2b77746b)

Learn more about [App Testing](/replitai/app-testing) capabilities and troubleshooting.

### 

​

Max Autonomy (Beta)

**Extended autonomous development** \- Agent works for much longer periods with minimal supervision. Learn more about [Autonomy Level settings](/replitai/autonomy-level) and how to choose the right level for your project. **Key benefits:**

  * **Extended work sessions** : Agent can work much longer without requiring input
  * **Longer-tasklist handling** : Creates much longer task lists to complete more functionality
  * **Reduced supervision** : Agent will supervise itself, so you don’t have to (runs up to 200 minutes)

**Usage** : Turn on “Max autonomy” in the Agent Tools panel under the Autonomy Level based on your comfort level with autonomous development. This feature is currently in Beta.

![Agent Tools interface showing Max autonomy toggle enabled with Beta label](https://mintcdn.com/replit/YBG_cdNEwjn6sUBd/images/replitai/max-autonomy-level.png?fit=max&auto=format&n=YBG_cdNEwjn6sUBd&q=85&s=ee206296f46a60e96dd8766665ff5c41)

### 

​

Agents & Automations

**Beyond traditional apps** \- Build intelligent agents, chatbots, and automated workflows that interact with external services.

Agents & Automations is currently in beta. Your automation must be deployed to function with external triggers like Slack or Telegram.

**Supported use cases:**

  * **Slack Agents** : Intelligent Slackbots for research, Q&A, and task automation
  * **Telegram Bots** : Customer service, scheduling, and entertainment bots
  * **Timed Automations** : Scheduled workflows for reports, summaries, and monitoring

**Getting started** : Select “Agents & Automations” from the Replit homepage app type selector to begin building automated systems.

![Replit homepage showing Agents & Automations selection with Beta label and prompt input area](https://mintcdn.com/replit/fq3p5W3K0mVwvlo1/images/replitai/agents-automations-homepage-2.png?fit=max&auto=format&n=fq3p5W3K0mVwvlo1&q=85&s=ec25b745f7f0e9d95e0af74d2dcb6515)

Learn more about [Agents & Automations](/replitai/agents-and-automations) use cases and setup.

## 

​

Usage

You can access Agent in your Replit App workspace by selecting the Agent tool.

How to access Agent

From the **Create a new App** screen, select the **Replit Agent** tab to enter a description of the app you want as shown in the following animation:

![animation showing Agent in the Create a new App screen](https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-start-building.avif?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=132104b9caa4c832a48387532886f51e)

If viewing a Replit App started by Agent, you can locate the Agent tool in your workspace in one of the following locations:From the left tool dock, select ![Agent icon](https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent_icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=4aaa46ea144fd055c19515360c3e54e0) **Agent** as shown in the following animation:

![animation showing Agent selection from the dock](https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-from-dock.avif?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=0368c2ee2414d7c5715f243205af38be)

From the **Search bar** :

  1. Select the ![magnifying glass icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30) magnifying glass at the top to open the search tool
  2. Type “Agent” to locate the Agent tool and select it from the results



From the Agent tool, you can perform the following actions:

  * **Chat** : Describe your app or feature in the text area and respond to Agent’s follow-up questions
  * **Add detailed requests** : Upload files or import content from URLs to give Agent more information
  * **Manage conversations** : Select **New chat** or select previous conversations from the ![menu icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/manage-chats-menu.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f2f1a6e7b1f15d5b2872e17c3f20c225) menu icon to start or resume a conversation
  * **Track usage** : Select the ![usage icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=afedaf18cbe1d4549be6e7833c88c269) usage icon at the top right to view your billing page
  * **Reverse changes** : Undo changes made by Agent by selecting ![rollback icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/rollback-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=34791076a8d31ed55a923fff97179a6f) **Rollback to here**



### 

​

Chat prompts

![Agent chat interface with Make, test, iterate header and build options](https://mintcdn.com/replit/pnpczhK4itt7pXl2/images/replitai/updated-v3-chat-window.png?fit=max&auto=format&n=pnpczhK4itt7pXl2&q=85&s=2b71a7e363837be3f9466a9c7c0a6e67) To communicate your request to Agent, enter a **prompt** in the text area. A prompt is a natural language instruction that describes the task you want Agent to perform. In addition to text, you can include the following data in your prompt:

  * **File attachments** : Drag a file into the text area or select the ![Paperclip icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/paperclip-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=45949f269700584b5abce83018948efd) paperclip icon
  * **Web content** : Include text data from a webpage by entering a URL and selecting **Copy page content**
  * **Webpage screenshots** : Include a screenshot of a webpage by entering a URL and selecting **Take screenshot**

Agent operates in three distinct modes to support different types of work:

  * **Build mode** (default): Agent writes code, modifies files, and implements features directly in your project
  * **Plan mode** : Brainstorm ideas, plan development work, and collaborate on project architecture without modifying code. Learn more about [Plan mode](/replitai/plan-mode)
  * **Edit mode** : Make targeted changes to specific files or code sections with precise control

**All Agent interactions are billable** \- whether Agent responds with text guidance or makes code changes, there is always a charge, though smaller requests cost less.

### 

​

Checkpoints

![Agent checkpoint with interactive map and rollback options](https://mintcdn.com/replit/pnpczhK4itt7pXl2/images/replitai/updated-v3-checkpoint.png?fit=max&auto=format&n=pnpczhK4itt7pXl2&q=85&s=1cf06bf550cc671d1c29677309d7e1c9) A **checkpoint** is a comprehensive snapshot of your Replit App that captures completed work from Agent, including workspace contents, AI conversation context, and connected databases. Agent creates checkpoints when it finishes implementing your request, ensuring you only pay for completed functionality.

#### 

​

How checkpoints work with effort-based pricing

Agent’s new effort-based pricing creates checkpoints that reflect the actual work performed:

  * **One checkpoint per request** : Agent bundles all work for your request into a single, meaningful checkpoint
  * **Variable pricing** : Simple changes cost less, while complex builds cost more based on the effort required
  * **Transparent costs** : Each checkpoint shows exactly what you’re paying for that completed work
  * **No intermediate billing** : You’re not charged for Agent’s thinking or planning process

Each checkpoint lets you perform the following actions:

  * **Rollback** : Undo changes made by Agent and return to the state of the previous checkpoint, including workspace contents and AI memory; connected databases can also be restored when selected
  * **Track usage** : Hover over the ![usage icon](https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/usage-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=afedaf18cbe1d4549be6e7833c88c269) usage icon in a checkpoint to view the amount billed for that checkpoint



For comprehensive details about what checkpoints capture and how rollbacks work across your entire development environment, see [Checkpoints and Rollbacks](/replitai/checkpoints-and-rollbacks).

Agent uses effort-based pricing where you pay based on the complexity and scope of your request. Simple changes typically cost less than complex builds. Initial planning and proposal stages are free - you only pay when Agent implements approved changes. Learn more about [Agent billing](/billing/ai-billing#agent-billing).

### 

​

Advanced capabilities

For complex projects, you can enable additional Agent capabilities through toggles in the chat toolbar: **Extended Thinking** : Instructs Agent to analyze your request more thoroughly, considering multiple approaches and edge cases. Best for architectural decisions or when you need comprehensive solutions. **High Power mode** : Uses more sophisticated AI models for advanced problem-solving. Ideal for complex integrations, performance optimizations, or unfamiliar technologies. Learn more about when and how to use these advanced features in the [Dynamic Intelligence documentation](/replitai/dynamic-intelligence).

### 

​

Progress tab

The **Progress** tab shows a record of Agent’s actions in real-time. Access it through the Tools dock or search bar to monitor Agent’s progress and navigate directly to relevant files. **Key features:**

  * **Real-time updates** : Monitor Agent’s progress with live activity feed
  * **Chronological history** : Review Agent’s activities to understand changes and troubleshoot issues
  * **File navigation** : Click links to jump directly to files Agent is working on



## 

​

Getting the most from Agent

### 

​

Best practices for prompts

  * **Be specific** : Describe exactly what you want your app to do
  * **Provide context** : Include relevant files, URLs, or examples
  * **Start simple** : Begin with basic functionality and add complexity gradually
  * **Use examples** : Show Agent similar apps or features you want to emulate
  * **Choose your mode thoughtfully** : Consider your timeline, certainty about requirements, and development style



### 

​

Managing costs effectively

  * **Start with free planning** : Review Agent’s implementation plan before approving work
  * **Use simple requests** : Break complex projects into smaller, focused tasks
  * **Set spending limits** : Configure [usage alerts and budgets](/billing/managing-spend) to control costs
  * **Monitor usage** : Track checkpoint costs to understand pricing patterns



## 

​

Next steps

Ready to start building with Agent? Here’s how to begin:

  1. **Create your first app** : Use the [Create with AI quickstart](/getting-started/quickstarts/ask-ai)
  2. **Choose your build mode** : Start with a design for visual-first development or build the full app for comprehensive functionality
  3. **Learn effective prompting** : Follow our [vibe coding guide](/tutorials/how-to-vibe-code)
  4. **Set up billing controls** : Configure [spending management](/billing/managing-spend)
  5. **Explore Agent 3 features** : Try [App Testing](/replitai/app-testing) for self-validation, [Autonomy Level](/replitai/autonomy-level) for customized workflows, and [Agents & Automations](/replitai/agents-and-automations) for building intelligent systems

Learn more about [Agent pricing](/billing/ai-billing#agent-billing) or explore other [Replit AI tools](/category/replit-ai).

Was this page helpful?

YesNo

[Previous](/category/replit-ai)[App TestingAgent's self-testing feature that validates your app's functionality using an actual browser, with visual feedback and automatic issue resolution.Next](/replitai/app-testing)

⌘I

On this page

  * Features
  * Build Modes
  * Start with a design
  * Build the full app
  * Autonomous Features (New in Agent 3)
  * App Testing
  * Max Autonomy (Beta)
  * Agents & Automations
  * Usage
  * Chat prompts
  * Checkpoints
  * How checkpoints work with effort-based pricing
  * Advanced capabilities
  * Progress tab
  * Getting the most from Agent
  * Best practices for prompts
  * Managing costs effectively
  * Next steps