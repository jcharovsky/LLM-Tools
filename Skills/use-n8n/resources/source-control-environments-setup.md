# source-control-environments-setup

**Source URL:** https://docs.n8n.io/source-control-environments/setup/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/source-control-environments/setup.md "Edit this page")

# Set up source control for environments#

Link a Git repository to an n8n instance and configure your source control.

n8n uses source control to provide environments. Refer to [Environments in n8n](../understand/environments/) for more information.

## Prerequisites#

To use source control with n8n, you need a Git repository with either:

  * SSH access (using deploy keys), or 
  * HTTPS access (using Personal Access Tokens)



This document assumes you are familiar with Git and your Git provider.

## Step 1: Set up your repository and branches#

For a new setup:

  1. Create a new repository for use with n8n. 
  2. Create the branches you need. For example, if you plan to have different environments for test and production, set up a branch for each.



To help decide what branches you need for your use case, refer to [Branch patterns](../understand/patterns/).

## Step 2: Configure Git in n8n#

  1. Go to **Settings** > **Environments**.
  2. Choose your connection method:
     * **SSH** : In **Git repository URL** , enter the SSH URL for your repository (for example, `[[email protected]](/cdn-cgi/l/email-protection):username/repo.git`).
     * **HTTPS** : In **Git repository URL** enter the HTTPS URL for your repository (for example, `https://github.com/username/repo.git`).
  3. Configure authentication based on your connection method:
     * **For SSH** : n8n supports ED25519 and RSA public key algorithms. ED25519 is the default. Select **RSA** under **SSH Key** if your git host requires RSA. Copy the SSH key.
     * **For HTTPS** : Enter your credentials:
       * **Username** : Your Git provider username.
       * **Token** : Your Personal Access Token (PAT) from your Git provider.



## Step 3: Set up authentication#

Configure authentication based on your chosen connection method.

### SSH authentication (using deploy keys)#

Set up SSH access by creating a deploy key for the repository using the SSH key from n8n. The key must have write access.

The steps depend on your Git provider. Help links for common providers:

  * [GitHub | Managing deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)
  * [GitLab | Deploy keys](https://docs.gitlab.com/ee/user/project/deploy_keys/)



### HTTPS authentication (using Personal Access Tokens)#

Create a Personal Access Token (PAT) with repository access permissions.

Help links for creating PATs with common providers:

  * [GitHub | Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
  * [GitLab | Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
  * [Bitbucket | App passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)



Required permissions for your token:

  * Repository read/write access
  * Contents read/write (for GitHub)
  * Source code pull/push (for GitLab)



## Step 4: Connect n8n and configure your instance#

  1. In **Settings** > **Environments** in n8n, select **Connect**. n8n connects to your Git repository.
  2. Under **Instance settings** , choose which branch you want to use for the current n8n instance.
  3. **Optional** : select **Protected instance** to prevent users editing workflows in this instance. This is useful for protecting production instances.
  4. **Optional** : choose a custom color for the instance. This will appear in the menu next to the source control push and pull buttons. It helps users know which instance they're in.
  5. Select **Save settings**.



Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top