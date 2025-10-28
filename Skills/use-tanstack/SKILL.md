---
name: use-tanstack
description: |
  Comprehensive guidance on using TanStack's suite of open-source libraries for frontend development, including React Query (TanStack Query), TanStack Table, TanStack Form, TanStack Router, TanStack Virtual, and TanStack Devtools. Use this skill when users ask about TanStack Query APIs, configuration options, React integration patterns, data fetching and caching strategies, table state management, form handling, routing, virtualization, or debugging with Devtools. Includes detailed coverage of version 5 React Query docs, config references, and advanced usage patterns.
---

# Instructions for Claude

This skill enables Claude to assist users with TanStack libraries, particularly React Query and related tools.

1. **Search and Read Documentation**
   - All supporting docs are located in the `resources/` folder.
   - When a user asks about a specific TanStack library or topic (e.g., React Query hooks, Table sorting, Router usage), search for relevant `.md` files in `resources/`.
   - Prioritize files with `-latest-docs.md` or `-v5.md` suffixes for the most current and authoritative info (e.g., `resources/query-v5.md`, `resources/config-latest-docs.md`).
   - For foundational concepts or overview, check `resources/index.md` or `resources/learn.md`.

2. **Use Tables of Contents for Long Files**
   - Some files exceed 100 lines and have a table of contents at the top (e.g., `resources/query-v5.md`). Use these to quickly locate sections relevant to the user query.

3. **Terminology Consistency**
   - Use consistent terms such as "API endpoint," "query key," "mutation," "cache," "hook," "configuration option," and "React integration."
   - Avoid mixing terms like "URL" for API endpoints or "route" for React Router unless referring specifically to TanStack Router.

4. **Answering User Questions**
   - Provide concrete examples from the docs when explaining how to use React Query hooks (`useQuery`, `useMutation`), configuration settings, or how to integrate with React components.
   - When multiple approaches exist, recommend the default or most commonly accepted pattern.
   - For deprecated or old usage, refer to "Old patterns" sections if present.
   - If the user asks about other TanStack libraries (Table, Form, Router, Virtual, Devtools), locate the specific docs in `resources/table.md`, `resources/form.md`, `resources/router.md`, `resources/virtual.md`, or `resources/devtools.md`.

5. **Progressive Disclosure**
   - Keep answers focused and to the point.
   - Provide links or references to resource files for deeper exploration if user requests more detail.

6. **Avoid Time-Sensitive Information**
   - Do not mention dates or version cutoffs.
   - Use version-specific docs (e.g., v5) as the default unless otherwise specified.

7. **File Reference Best Practices**
   - Always reference files directly from `resources/`.
   - Do not chain references through other resource files.


# Examples

**User:** How do I use React Query's `useQuery` hook in a React app?

**Claude:** React Query's `useQuery` hook fetches and caches data in React. You provide a unique query key and an async fetch function. For example, `useQuery(['todos'], fetchTodos)` fetches todos and manages loading and error states. Configure options like stale time or refetch intervals via the `useQuery` options object. See `resources/query-v5.md` for detailed usage patterns and configuration examples.

**User:** Can you explain how to configure TanStack Query's cache?

**Claude:** TanStack Query's cache can be configured globally or per query. Use the `QueryClient` to set default cache times, garbage collection, and retry behaviors. Per-query options include `staleTime`, `cacheTime`, and `retry`. For full configuration details, consult `resources/config-latest-docs.md` and `resources/query-v5.md` sections on caching.

**User:** What is TanStack Devtools and how do I integrate it?

**Claude:** TanStack Devtools is a tool for inspecting React Query's cache and queries in your app. To integrate, install the devtools package and add `<ReactQueryDevtools />` inside your React component tree. It helps monitor query status, cache contents, and query lifecycle events. See `resources/devtools.md` for setup and usage instructions.
