# hosting-scaling-binary-data

**Source URL:** https://docs.n8n.io/hosting/scaling/binary-data/

---

Skip to content 

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/binary-data.md "Edit this page")

# Binary data#

Binary data is any file-type data, such as image files or documents generated or processed during the execution of a workflow. 

## Enable filesystem mode#

When handling binary data, n8n keeps the data in memory by default. This can cause crashes when working with large files. 

To avoid this, change the `N8N_DEFAULT_BINARY_DATA_MODE` [environment variable](../../configuration/environment-variables/binary-data/) to `filesystem`. This causes n8n to save data to disk, instead of using memory.

If you're using queue mode, keep this to `default`. n8n doesn't support filesystem mode with queue mode.

## Binary data pruning#

n8n executes binary data pruning as part of execution data pruning. Refer to [Execution data | Enable executions pruning](../execution-data/#enable-executions-pruning) for details. 

If you configure multiple binary data modes, binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. Refer to [External storage](../external-storage/#usage) for details. 

Chat with the docs

This page was ![Thumbs up](/_images/assets/thumb_up.png)Helpful  ![Thumbs down](/_images/assets/thumb_down.png)Not helpful 

Thanks for your feedback! 

Submit 

Back to top