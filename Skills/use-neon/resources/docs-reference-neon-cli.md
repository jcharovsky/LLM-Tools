# neon-cli

**Source URL:** https://neon.com/docs/reference/neon-cli

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/[Dev tools (API, CLI, SDKs)](/docs/reference/api-reference)/Overview

# Neon CLI

Use the Neon CLI to manage Neon directly from the terminal

The Neon CLI is a command-line interface that lets you manage Neon directly from the terminal. This documentation references all commands and options available in the Neon CLI.

🚀 Get set up in just a few steps with the [CLI Quickstart](/docs/reference/cli-quickstart).

## Install

macOSWindowsLinux

**Install with[Homebrew](https://formulae.brew.sh/formula/neonctl)**
    
    
    brew install neonctl

**Install via[npm](https://www.npmjs.com/package/neonctl)**
    
    
    npm i -g neonctl

Requires [Node.js 18.0](https://nodejs.org/en/download/) or higher.

**Install with bun**
    
    
     bun install -g neonctl

**macOS binary**

Download the binary. No installation required.
    
    
    curl -sL https://github.com/neondatabase/neonctl/releases/latest/download/neonctl-macos -o neonctl

Run the CLI from the download directory:
    
    
    neon <command> [options]

For more about installing, upgrading, and connecting, see [Neon CLI — Install and connect](/docs/reference/cli-install).

#### Use the Neon CLI without installing

You can run the Neon CLI without installing it using **npx** (Node Package eXecute) or the `bun` equivalent, **bunx**. For example:
    
    
    # npx
    npx neonctl <command>
    
    # bunx
    bunx neonctl <command>

## Synopsis
    
    
    neon --help
    usage: neon <command> [options]                               [aliases: neonctl]
    
    Commands:
      neon auth                        Authenticate                      [aliases: login]
      neon me                          Show current user
      neon orgs                        Manage organizations                [aliases: org]
      neon projects                    Manage projects                 [aliases: project]
      neon ip-allow                    Manage IP Allow
      neon vpc                         Manage VPC endpoints and project VPC restrictions
      neon branches                    Manage branches                   [aliases: branch]
      neon databases                   Manage databases            [aliases: database, db]
      neon roles                       Manage roles                        [aliases: role]
      neon operations                  Manage operations               [aliases: operation]
      neon connection-string [branch]  Get connection string                  [aliases: cs]
      neon set-context                 Set the current context
      neon completion                  generate completion script
    
    Global options:
      -o, --output      Set output format
                      [string] [choices: "json", "yaml", "table"] [default: "table"]
      --config-dir      Path to config directory [string] [default: ""]
      --api-key         API key  [string] [default: ""]
      --analytics       Manage analytics. Example: --no-analytics, --analytics false
                                                           [boolean] [default: true]
      -v, --version     Show version number                                [boolean]
      -h, --help        Show help                                          [boolean]
    
    Options:
    --context-file      Context file [string] [default: (current-context-file)]

## Commands

Command| Subcommands| Description  
---|---|---  
[auth](/docs/reference/cli-auth)| | Authenticate  
[me](/docs/reference/cli-me)| | Show current user  
[orgs](/docs/reference/cli-orgs)| `list`| Manage organizations  
[projects](/docs/reference/cli-projects)| `list`, `create`, `update`, `delete`, `get`| Manage projects  
[ip-allow](/docs/reference/cli-ip-allow)| `list`, `add`, `remove`, `reset`| Manage IP Allow  
[vpc](/docs/reference/cli-vpc)| `endpoint`, `project`| Manage VPC endpoints and project VPC restrictions  
[branches](/docs/reference/cli-branches)| `list`, `create`, `reset`, `restore`, `rename`, `schema-diff`, `set-default`, `add-compute`, `delete`, `get`| Manage branches  
[databases](/docs/reference/cli-databases)| `list`, `create`, `delete`| Manage databases  
[roles](/docs/reference/cli-roles)| `list`, `create`, `delete`| Manage roles  
[operations](/docs/reference/cli-operations)| `list`| Manage operations  
[connection-string](/docs/reference/cli-connection-string)| | Get connection string  
[set-context](/docs/reference/cli-set-context)| | Set context for session  
[completion](/docs/reference/cli-completion)| | Generate a completion script  
  
## Global options

Global options are supported with any Neon CLI command.

Option| Description| Type| Default  
---|---|---|---  
-o, --output| Set the Neon CLI output format (`json`, `yaml`, or `table`)| string| table  
\--config-dir| Path to the Neon CLI configuration directory| string| `/home/<user>/.config/neonctl`  
\--api-key| Neon API key| string| `NEON_API_KEY` environment variable  
\--color| Colorize the output. Example: `--no-color`, `--color false`| boolean| true  
\--analytics| Manage analytics| boolean| true  
-v, --version| Show the Neon CLI version number| boolean| -  
-h, --help| Show the Neon CLI help| boolean| -  
  
  * `-o, --output`

Sets the output format. Supported options are `json`, `yaml`, and `table`. The default is `table`. Table output may be limited. The `json` and `yaml` output formats show all data.
        
        neon me --output json

  * `--config-dir`

Specifies the path to the `neonctl` configuration directory. To view the default configuration directory containing you `credentials.json` file, run `neon --help`. The credentials file is created when you authenticate using the `neon auth` command. This option is only necessary if you move your `neonctl` configuration file to a location other than the default.
        
        neon projects list --config-dir /home/<user>/.config/neonctl

  * `--api-key`

Specifies your Neon API key. You can authenticate using a Neon API key when running a Neon CLI command instead of using `neon auth`. For information about obtaining an Neon API key, see [Create an API key](/docs/manage/api-keys#create-an-api-key).
        
        neon <command> --api-key <neon_api_key>

To avoid including the `--api-key` option with each CLI command, you can export your API key to the `NEON_API_KEY` environment variable.
        
        export NEON_API_KEY=<neon_api_key>

The authentication flow for the Neon CLI follows this order:

    * If the `--api-key` option is provided, it takes precedence and is used for authentication.
    * If the `--api-key` option is not provided, the `NEON_API_KEY` environment variable is used if it is set.
    * If both `--api-key` option and `NEON_API_KEY` environment variable are not provided or set, the CLI falls back to the `credentials.json` file created by the `neon auth` command.
    * If the credentials file is not found, the Neon CLI initiates the `neon auth` web authentication process.
  * `--color`

Colorize the output. This option is enabled by default, but you can disable it by specifying `--no-color` or `--color false`, which is useful when using Neon CLI commands in your automation pipelines.

  * `--analytics`

Analytics are enabled by default to gather information about the CLI commands and options that are used by our customers. This data collection assists in offering support, and allows for a better understanding of typical usage patterns so that we can improve user experience. Neon does not collect user-defined data, such as project IDs or command payloads. To opt-out of analytics data collection, specify `--no-analytics` or `--analytics false`.

  * `-v, --version`

Shows the Neon CLI version number.
        
        $ neon --version
        1.15.0

  * `-h, --help`

Shows the `neon` command-line help. You can view help for `neon`, a `neon` command, or a `neon` subcommand, as shown in the following examples:
        
        neon --help
        
        neon branches --help
        
        neon branches create --help




## Options

Option| Description| Type| Default  
---|---|---|---  
\--context-file| The context file for CLI sessions| string| current-context-file  
  
  * `--context-file`

Sets a background context for your CLI sessions, letting you perform organization, project, or branch-specific actions without having to specify the relevant id in every command. For example, this command lists all branches using the `branches list` command. No need to specify the project since the context file provides it.
        
        neon branches list --context-file path/to/context_file_name

To define a context file, see [Neon CLI commands — set-context](/docs/reference/cli-set-context).




## GitHub repository

The GitHub repository for the Neon CLI is found [here](https://github.com/neondatabase/neonctl).

[PreviousNeon API](/docs/reference/api-reference)[NextQuickstart](/docs/reference/cli-quickstart)

Last updated on August 21, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Install
  * Synopsis
  * Commands
  * Global options
  * Options
  * GitHub repository



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/reference/neon-cli.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/reference/neon-cli.md)

Neon Docs