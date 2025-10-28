# introduction-status

**Source URL:** https://neon.com/docs/introduction/status

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/Status

# Neon status

Stay informed about the performance and availability of Neon

To stay informed about Neon's status, we provide a dedicated status page for each region that Neon supports. To view the Neon Status page, navigate to <https://neonstatus.com/>[](https://neonstatus.com/).

Remember to bookmark the Neon Status page for easy access.

![Neon status page](/_next/image?url=%2Fdocs%2Fintroduction%2Fneon_status_page.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

For status information applicable to your Neon project, monitor the status page for the region where your Neon project resides. If you don't know the region, you can find it on the **Project Dashboard** in the Neon Console.

Status pages provide status for:

  * Database Connectivity
  * Database Operations
  * Console and API Requests



#### platform maintenance notices

You can monitor or subscribe to your region's [status page](/docs/manage/platform-maintenance) to stay informed about upcoming platform maintenance. See Subscribing to Neon status pages below.

Neon also applies regular updates to your project's computes, but these updates are not posted to regional status pages since they are specific to your Neon project. To stay informed about these updates, watch for update notices in your project's settings in the Neon Console. See [Updates](/docs/manage/updates) for details.

## Subscribing to Neon status pages

Follow the instructions from the **Subscribe to updates** link on a regional status page to subscribe to updates via email, RSS, or Slack.

![Neon status page](/_next/image?url=%2Fdocs%2Fintroduction%2Fneon_status_subscribe.png&w=1920&q=75&dpl=dpl_BWMnjAnsz5e4vCV8rVKCfZ67QP1V)

## Access Neon status via API

The [Neon status page](https://neonstatus.com), powered by [incident.io](https://incident.io/), is also accessible via API. You can use these endpoints to check the status of the Neon Console and Neon-supported regions.

> For more about the incident.io API that supports the Neon status API, including incident.io API rate limits, refer to the [incident.io API docs](https://api-docs.incident.io/).

Endpoint responses include the following attributes:
    
    
    {
      "page_title": "AWS - Europe (Frankfurt) - eu-central-1",
      "page_url": "https://neonstatus.com/aws-europe-frankfurt",
      "ongoing_incidents": [],
      "in_progress_maintenances": [],
      "scheduled_maintenances": []
    }

### Neon status endpoints

Region| Endpoint  
---|---  
Neon Console| <https://neonstatus.com/console/api/v1/summary>[](https://neonstatus.com/console/api/v1/summary)  
Neon Console and all regions| <https://neonstatus.com/api/v1/summary>[](https://neonstatus.com/api/v1/summary)  
AWS - Asia Pacific (Singapore)| <https://neonstatus.com/aws-asia-pacific-singapore/api/v1/summary>[](https://neonstatus.com/aws-asia-pacific-singapore/api/v1/summary)  
AWS - Asia Pacific (Sydney)| <https://neonstatus.com/aws-asia-pacific-sydney/api/v1/summary>[](https://neonstatus.com/aws-asia-pacific-sydney/api/v1/summary)  
AWS - Europe (Frankfurt)| <https://neonstatus.com/aws-europe-frankfurt/api/v1/summary>[](https://neonstatus.com/aws-europe-frankfurt/api/v1/summary)  
AWS - Europe (London)| <https://neonstatus.com/aws-europe-london/api/v1/summary>[](https://neonstatus.com/aws-europe-london/api/v1/summary)  
AWS - South America (São Paulo)| <https://neonstatus.com/aws-south-america-sao-paulo/api/v1/summary>[](https://neonstatus.com/aws-south-america-sao-paulo/api/v1/summary)  
AWS - US East (N. Virginia)| <https://neonstatus.com/aws-us-east-n-virginia/api/v1/summary>[](https://neonstatus.com/aws-us-east-n-virginia/api/v1/summary)  
AWS - US East (Ohio)| <https://neonstatus.com/aws-us-east-ohio/api/v1/summary>[](https://neonstatus.com/aws-us-east-ohio/api/v1/summary)  
AWS - US West (Oregon)| <https://neonstatus.com/aws-us-west-oregon/api/v1/summary>[](https://neonstatus.com/aws-us-west-oregon/api/v1/summary)  
Azure - Germany West Central (Frankfurt)| <https://neonstatus.com/azure-germanywestcentral-frankfurt/api/v1/summary>[](https://neonstatus.com/azure-germanywestcentral-frankfurt/api/v1/summary)  
Azure East US 2 (Virginia)| <https://neonstatus.com/azure-east-us-2-virginia-eastus-2/api/v1/summary>[](https://neonstatus.com/azure-east-us-2-virginia-eastus-2/api/v1/summary)  
Azure West US 3 (Arizona)| <https://neonstatus.com/azure-westus3-arizona/api/v1/summary>[](https://neonstatus.com/azure-westus3-arizona/api/v1/summary)  
  
## Need help?

Join our [Discord Server](https://discord.gg/92vNTzKDGp) to ask questions or see what others are doing with Neon. For paid plan support options, see [Support](/docs/introduction/support).

[PreviousPostgreSQL Tutorial](https://neon.com/postgresql/tutorial)[NextSupport](/docs/introduction/support)

Last updated on June 4, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * Subscribing to Neon status pages
  * Access Neon status via API
  * Need help?



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/introduction/status.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/introduction/status.md)

Neon Docs