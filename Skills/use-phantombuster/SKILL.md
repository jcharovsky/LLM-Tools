---
name: use-phantombuster
description: |
  Comprehensive guidance for using the Phantombuster API and agent scripting environment. This skill helps with Phantombuster API endpoints, agent lifecycle management, scripting commands, data fetching, and automation workflows. Use when users ask about launching, aborting, or saving agents; managing agent and global objects; handling proxies; downloading files; sending emails from agents; solving captchas; or integrating with Phantombuster's automation platform.

  Trigger terms include "Phantombuster API", "Phantombuster agents", "buster-agentid", "launchagent", "abortagent", "buster-download", "buster-mail", "proxyaddress", "agent object", "global object", "captcha solver", and "automation workflow".
---

# Instructions for Claude

1. Always search for relevant information by reading the Markdown files in the `resources/` subdirectory.

2. The documentation is split into many focused files named after API endpoints or functions (e.g., `launchagent-1.md`, `buster-download.md`, `post_agents-save.md`). Use the filenames and content headings to locate the best match for the user's query.

3. For any large or complex files (over ~100 lines), a table of contents is provided at the top to quickly identify sections.

4. Focus on providing clear, actionable answers referencing the Phantombuster API endpoints and agent scripting functions. Avoid generic or vague explanations.

5. Use consistent terminology such as "API endpoint" when referring to HTTP calls, and "agent" when referring to Phantombuster automation scripts or processes.

6. When multiple methods exist, recommend the most common or default approach unless the user specifically requests alternatives.

7. Avoid mentioning time-sensitive information such as version numbers or dates.

8. Include code examples or parameter explanations from the resources when relevant to improve clarity.

9. If the user asks about deprecated or old patterns, refer to the "Old patterns" sections if available.

10. Keep responses concise but thorough, ensuring you address the user's specific question about Phantombuster's API or automation capabilities.

# Examples

**User:** How do I launch a Phantombuster agent using the API?

**Claude:** To launch an agent, use the POST `/agents/launch` API endpoint described in `resources/post_agents-launch.md`. You need to provide the agent ID and optional parameters such as arguments or execution limits. This starts the agent's execution immediately.

---

**User:** How can I save data from within a Phantombuster agent script?

**Claude:** Within an agent script, you can use the `Buster.save()` function documented in `resources/buster-save.md` to save data to the agent's storage. This allows you to persist results that you can later fetch via the API.

---

**User:** What is the difference between the agent object and the global object in Phantombuster?

**Claude:** The agent object (see `resources/buster-getagentobject.md`) stores data local to a specific agent run, while the global object (`resources/buster-getglobalobject.md`) stores data shared across all agent executions in your account. Use the global object for shared state and the agent object for per-run data.
