# hosting-installation-npm

**Source URL:** https://docs.n8n.io/hosting/installation/npm/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/npm.md "Edit this page")

# npm#

npm is a quick way to get started with n8n on your local machine. You must have [Node.js](https://nodejs.org/en/) installed. n8n requires a Node.js version between 20.19 and 24.x, inclusive.

Latest and Next versions

n8n releases a new minor version most weeks. The `latest` version is for production use. `next` is the most recent release. You should treat `next` as a beta: it may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

Current `latest`: 1.116.2  
Current `next`: 1.117.0

## Try n8n with npx#

You can try n8n without installing it using npx.

From the terminal, run:
    
    
    1

| 
    
    
    npx n8n
      
  
---|---  
  
This command will download everything that's needed to start n8n. You can then access n8n and start building workflows by opening <http://localhost:5678>.

## Install globally with npm#

To install n8n globally, use npm:
    
    
    1

| 
    
    
    npm install n8n -g
      
  
---|---  
  
To install or update to a specific version of n8n use the `@` syntax to specify the version. For example:
    
    
    1

| 
    
    
    npm install -g [[email protected]](/cdn-cgi/l/email-protection)
      
  
---|---  
  
To install `next`:
    
    
    1

| 
    
    
    npm install -g n8n@next
      
  
---|---  
  
After the installation, start n8n by running:
    
    
    1
    2
    3

| 
    
    
    n8n
    # or
    n8n start
      
  
---|---  
  
### Next steps#

Try out n8n using the [Quickstarts](../../../try-it-out/).

## Updating#

To update your n8n instance to the `latest` version, run:
    
    
    1

| 
    
    
    npm update -g n8n
      
  
---|---  
  
To install the `next` version:
    
    
    1

| 
    
    
    npm install -g n8n@next
      
  
---|---  
  
## n8n with tunnel#

Danger

Use this for local development and testing. It isn't safe to use it in production.

To use webhooks for trigger nodes of external services like GitHub, n8n has to be reachable from the web. n8n runs a [tunnel service](https://github.com/localtunnel/localtunnel) that can redirect requests from n8n's servers to your local n8n instance.

Start n8n with `--tunnel` by running:
    
    
    1

| 
    
    
    n8n start --tunnel
      
  
---|---  
  
## Reverting an upgrade#

Install the older version that you want to go back to.

If the upgrade involved a database migration:

  1. Check the feature documentation and release notes to see if there are any manual changes you need to make.
  2. Run `n8n db:revert` on your current version to roll back the database. If you want to revert more than one database migration, you need to repeat this process.



## Windows troubleshooting#

If you are experiencing issues running n8n on Windows, make sure your Node.js environment is correctly set up. Follow Microsoft's guide to [Install NodeJS on Windows](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top