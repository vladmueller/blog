---
date: 2025-03-05
title: Publish Markdown files to Confluence (Cloud)
description: TODO
draft: true
tags:
  - draft
---

- [markdown-confluence/markdown-confluence: Publish your Markdown Files to Confluence](https://github.com/markdown-confluence/markdown-confluence)

> [!fail] 2025-03-05: No such file error when .md file contains a reference to an image.
> 
> I tried different variations, according to this documentation: [Image Upload - Markdown Confluence Tools](https://markdown-confluence.com/features/image-upload.html) - but without success.

## Create some Markdown files on your local machine

![example-some-markdown-files.png](/images/example-some-markdown-files.png)

## Prepare Confluence

Create a new space for testing purpose:

![confluence-create-space-for-markdown-to-confluence-1.png](/images/confluence-create-space-for-markdown-to-confluence-1.png)

![confluence-create-space-for-markdown-to-confluence-2.png](/images/confluence-create-space-for-markdown-to-confluence-2.png)

## Set up markdown-confluence

Add this `.markdown-confluence.json` to your project folder with your markdown files:

```json
{
    "confluenceBaseUrl": "https://<YOUR-INSTANCE>.atlassian.net",
    "confluenceParentId": "430473218",
    "atlassianUserName": "mail@example.com",
    "folderToPublish": "."
}
```

## Publish to Confluence

### Generate an API token for Confluence

You can generate tokens for your account under [Atlassian account](https://id.atlassian.com/manage-profile/security/api-tokens).

### Set up environment variables (Windows)

```powershell
$env:ATLASSIAN_API_TOKEN = "ATATT..."
```

```powershell
echo $env:ATLASSIAN_API_TOKEN
```

### Execute the CLI

```shell
npx @markdown-confluence/cli
```

## Result

![confluence-markdown-to-confluence-result.png](/images/confluence-markdown-to-confluence-result.png)
