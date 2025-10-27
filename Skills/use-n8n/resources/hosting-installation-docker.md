# hosting-installation-docker

**Source URL:** https://docs.n8n.io/hosting/installation/docker/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/installation/docker.md "Edit this page")

# Docker Installation#

n8n recommends using [Docker](https://www.docker.com/) for most self-hosting needs. It provides a clean, isolated environment, avoids operating system and tooling incompatibilities, and makes database and environment management simpler.

You can also use n8n in Docker with [Docker Compose](../server-setups/docker-compose/). You can find Docker Compose configurations for various architectures in the [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting).

Self-hosting knowledge prerequisites

Self-hosting n8n requires technical knowledge, including:

  * Setting up and configuring servers and containers
  * Managing application resources and scaling
  * Securing servers and applications
  * Configuring n8n



n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/).

You can also follow along with our video guide here:

## Prerequisites#

Before proceeding, install Docker:

  * [Docker Desktop](https://docs.docker.com/get-docker/) is available for Mac, Windows, and Linux. Docker Desktop includes the Docker Engine and Docker Compose.
  * [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/linux/) are also available as separate packages for Linux. Use this for Linux machines without a graphical environment or when you don't want the Docker Desktop UI.



Latest and Next versions

n8n releases a new minor version most weeks. The `latest` version is for production use. `next` is the most recent release. You should treat `next` as a beta: it may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12).

Current `latest`: 1.116.2  
Current `next`: 1.117.0

## Starting n8n#

From your terminal, run the following commands, replacing the `<YOUR_TIMEZONE>` placeholders with [your timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List):
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11

| 
    
    
    docker volume create n8n_data
    
    docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
     -e TZ="<YOUR_TIMEZONE>" \
     -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
     -e N8N_RUNNERS_ENABLED=true \
     -v n8n_data:/home/node/.n8n \
     docker.n8n.io/n8nio/n8n
      
  
---|---  
  
This command creates a volume to store persistent data, downloads the required n8n image, and starts the container with the following settings:

  * Maps and exposes port `5678` on the host.
  * Sets the timezone for the container:
    * the `TZ` environment variable sets the system timezone to control what scripts and commands like `date` return.
    * the [`GENERIC_TIMEZONE` environment variable](../../configuration/environment-variables/timezone-localization/) sets the correct timezone for schedule-oriented nodes like the [Schedule Trigger node](../../../integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/).
  * Enforces secure file permissions for the n8n configuration file.
  * Enables [task runners](../../configuration/task-runners/), the recommended way of executing tasks in n8n.
  * Mounts the `n8n_data` volume to the `/home/node/.n8n` directory to persist your data across container restarts.



Once running, you can access n8n by opening: <http://localhost:5678>

## Using with PostgreSQL#

By default, n8n uses SQLite to save [credentials](../../../glossary/#credential-n8n), past executions, and workflows. n8n also supports PostgreSQL, configurable using environment variables as detailed below.

Persisting the `.n8n` directory still recommended

When using PostgreSQL, n8n doesn't need to use the `.n8n` directory for the SQLite database file. However, the directory still contains other important data like encryption keys, instance logs, and source control feature assets. While you can work around some of these requirements, (for example, by setting the [`N8N_ENCRYPTION_KEY` environment variable](../../configuration/environment-variables/deployment/)), it's best to continue mapping a persistent volume for the directory to avoid potential issues.

To use n8n with PostgreSQL, execute the following commands, replacing the placeholders (depicted within angled brackets, for example `<POSTGRES_USER>`) with your actual values:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18

| 
    
    
    docker volume create n8n_data
    
    docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
     -e TZ="<YOUR_TIMEZONE>" \
     -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
     -e N8N_RUNNERS_ENABLED=true \
     -e DB_TYPE=postgresdb \
     -e DB_POSTGRESDB_DATABASE=<POSTGRES_DATABASE> \
     -e DB_POSTGRESDB_HOST=<POSTGRES_HOST> \
     -e DB_POSTGRESDB_PORT=<POSTGRES_PORT> \
     -e DB_POSTGRESDB_USER=<POSTGRES_USER> \
     -e DB_POSTGRESDB_SCHEMA=<POSTGRES_SCHEMA> \
     -e DB_POSTGRESDB_PASSWORD=<POSTGRES_PASSWORD> \
     -v n8n_data:/home/node/.n8n \
     docker.n8n.io/n8nio/n8n
      
  
---|---  
  
You can find a complete `docker-compose` file for PostgreSQL in the [n8n hosting repository](https://github.com/n8n-io/n8n-hosting/tree/main/docker-compose/withPostgres).

## Updating#

To update n8n, in Docker Desktop, navigate to the **Images** tab and select **Pull** from the context menu to download the latest n8n image:

![Docker Desktop](../../../_images/hosting/installation/docker/docker_desktop.png)

You can also use the command line to pull the latest, or a specific version:
    
    
    1
    2
    3
    4
    5
    6
    7
    8

| 
    
    
    # Pull latest (stable) version
    docker pull docker.n8n.io/n8nio/n8n
    
    # Pull specific version
    docker pull docker.n8n.io/n8nio/n8n:1.81.0
    
    # Pull next (unstable) version
    docker pull docker.n8n.io/n8nio/n8n:next
      
  
---|---  
  
After pulling the updated image, stop your n8n container and start it again. You can also use the command line. Replace `<container_id>` in the commands below with the container ID you find in the first command:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11

| 
    
    
    # Find your container ID
    docker ps -a
    
    # Stop the container with the `<container_id>`
    docker stop <container_id>
    
    # Remove the container with the `<container_id>`
    docker rm <container_id>
    
    # Start the container
    docker run --name=<container_name> [options] -d docker.n8n.io/n8nio/n8n
      
  
---|---  
  
### Updating Docker Compose#

If you run n8n using a Docker Compose file, follow these steps to update n8n:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11

| 
    
    
    # Navigate to the directory containing your docker compose file
    cd </path/to/your/compose/file/directory>
    
    # Pull latest version
    docker compose pull
    
    # Stop and remove older version
    docker compose down
    
    # Start the container
    docker compose up -d
      
  
---|---  
  
## n8n with tunnel#

Danger

Use this for local development and testing. It isn't safe to use it in production.

To use webhooks for trigger nodes of external services like GitHub, n8n has to be reachable from the web. n8n runs a [tunnel service](https://github.com/localtunnel/localtunnel) that can redirect requests from n8n's servers to your local n8n instance.

Start n8n with `--tunnel` by running:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12

| 
    
    
    docker volume create n8n_data
    
    docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
     -e TZ="<YOUR_TIMEZONE>" \
     -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
     -e N8N_RUNNERS_ENABLED=true \
     -v n8n_data:/home/node/.n8n \
     docker.n8n.io/n8nio/n8n \
     start --tunnel
      
  
---|---  
  
## Next steps#

  * Find more information about Docker setup in the README file for the [Docker image](https://github.com/n8n-io/n8n/tree/master/docker/images/n8n).
  * Learn more about [configuring](../../configuration/environment-variables/) and [scaling](../../scaling/overview/) n8n.
  * Or explore using n8n: try the [Quickstarts](../../../try-it-out/).



Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top