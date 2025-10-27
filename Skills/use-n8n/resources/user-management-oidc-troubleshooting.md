# user-management-oidc-troubleshooting

**Source URL:** https://docs.n8n.io/user-management/oidc/troubleshooting/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/user-management/oidc/troubleshooting.md "Edit this page")

# Troubleshooting OIDC SSO#

## Known issues#

### State parameter not supported#

When using OIDC providers that enforce the use of the `state` CSRF token parameter, authentication fails with the error:
    
    
    1

| 
    
    
    {"code":0,"message":"authorization response from the server is an error"}
      
  
---|---  
  
n8n's current OIDC implementation doesn't handle the `state` parameter that some OIDC providers send as a security measure against CSRF attacks.

For now, the only work around is to configure your OIDC provider to disable the `state` parameter if possible.

n8n is working on adding full support for the OIDC `state` parameter in a future release.

### PKCE not supported#

OIDC providers that require PKCE (Proof Key for Code Exchange) may fail authentication or reject n8n's authorization requests. n8n's current OIDC implementation doesn't support PKCE.

The only work around is to configure your OIDC provider to not require PKCE for the n8n client if this option is available in your providers settings. 

n8n plans on adding PKCE support in a future release

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top