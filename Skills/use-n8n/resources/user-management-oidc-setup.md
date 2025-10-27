# user-management-oidc-setup

**Source URL:** https://docs.n8n.io/user-management/oidc/setup/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/user-management/oidc/setup.md "Edit this page")

# Set up OIDC#

Feature availability

  * Available on Enterprise plans.
  * You need to be an instance owner or admin to enable and configure OIDC.



## Setting up and enabling OIDC#

  1. In n8n, go to **Settings** > **SSO**.
  2. Under **Select Authentication Protocol** , choose **OIDC** from the dropdown.
  3. Copy the **redirect URL** shown (for example, `https://yourworkspace.app.n8n.cloud/rest/sso/oidc/callback`).

Extra configuration for load balancers or proxies

If you are running n8n behind a load balancer, make sure you set the [`N8N_EDITOR_BASE_URL` environment variable](../../../hosting/configuration/environment-variables/deployment/).

  4. Set up OIDC with your identity provider (IdP). You'll need to:

     * Create a new OIDC client/application in your IdP.
     * Configure the redirect URL from the previous step.
     * Note down the **Client ID** and **Client Secret** provided by your IdP.
  5. In your IdP, locate the **Discovery Endpoint** (also called the well-known configuration endpoint). It typically has the following format: 
         
         1

| 
         
         https://your-idp-domain/.well-known/openid-configuration
           
  
---|---  
  
  6. In n8n, complete the OIDC configuration:
     * **Discovery Endpoint** : Enter the discovery endpoint URL from your IdP.
     * **Client ID** : Enter the client ID you received when registering your application with your IdP.
     * **Client Secret** : Enter the client secret you received when registering your application with your IdP.
  7. Select **Save settings**.
  8. Set OIDC to **Activated**.



## Provider-specific OIDC setup#

### Auth0#

  1. **Create an application in Auth0** :
     * Log in to your Auth0 Dashboard.
     * Go to **Applications** > **Applications**.
     * Click **Create Application**.
     * Enter a name (for example, "n8n SSO") and select **Regular Web Applications**.
     * Click **Create**.
  2. **Configure the application** :
     * Go to the **Settings** tab of your new application.
     * **Allowed Callback URLs** : Add your n8n redirect URL from **Settings** > **SSO** > **OIDC**.
     * **Allowed Web Origins** : Add your n8n base URL (for example, `https://yourworkspace.app.n8n.cloud`).
     * Click **Save Changes**.
  3. **Get your credentials** :
     * **Client ID** : Found in the **Settings** tab.
     * **Client Secret** : Found in the **Settings** tab.
     * **Discovery Endpoint** : `https://{your-auth0-domain}.auth0.com/.well-known/openid-configuration`.
  4. **In n8n, complete the OIDC configuration:**
     * **Discovery Endpoint** : Enter the discovery endpoint URL from Auth0.
     * **Client ID** : Enter the client ID you found in your Auth0 settings.
     * **Client Secret** : Enter the client secret you found in your Auth0 settings.
  5. Select **Save settings**.
  6. Set OIDC to **Activated**.



## Discovery endpoints reference#

  * **Google discovery endpoint example** : 
        
        1

| 
        
        https://accounts.google.com/.well-known/openid-configuration
          
  
---|---  
  
  * **Microsoft Azure AD discovery endpoint example** : 
        
        1

| 
        
        https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration
          
  
---|---  
  
  * **Auth0 discovery endpoint example** : 
        
        1

| 
        
        https://{your-domain}.auth0.com/.well-known/openid-configuration
          
  
---|---  
  
  * **Okta discovery endpoint example** : 
        
        1

| 
        
        https://{your-domain}.okta.com/.well-known/openid-configuration
          
  
---|---  
  
  * **Amazon Cognito discovery endpoint example** : 
        
        1

| 
        
        https://cognito-idp.{region}.amazonaws.com/{user-pool-id}/.well-known/openid-configuration
          
  
---|---  
  



Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top