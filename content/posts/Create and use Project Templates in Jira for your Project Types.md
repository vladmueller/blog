---
date: 2025-02-27
title: Create and use Project Templates in Jira for your Project Types
description: TODO
draft: true
tags:
  - draft
---

## Create a template for your projects types

1. `Projects` > `Create project` 

> [!warning] #todo Explain and link to difference between business and software project

### Option A: Use a business project

2. (a) Select `Work management` + `Blank project` (if you want a *business project*)

![jira-template-work-management-blank-project.png](/images/jira-template-work-management-blank-project.png)

1. Click on `Show more` and select `Company-managed` project with key `PMTEMPLATE`
   and for Name: "Template Project Management"

![jira-template-blank-business-project-use-company-managed.png](/images/jira-template-blank-business-project-use-company-managed.png)

1. Click on `Create project`

### Option B: Use a software project

1. (b) Select `Software development` + `Scrum` OR `Kanban` (if you want a `software project`)
   and Click on `Use template`

![jira-template-use-scrum-template.png](/images/jira-template-use-scrum-template.png)

> [!warning] #todo Note that a Scrum or Kanban board is not part of the template

1. Select `Company-managed` project with key `PMTEMPLATE`
   and for Name: "Template Project Management"

![jira-template-software-project-use-company-managed.png](/images/jira-template-software-project-use-company-managed.png)

1. Click on `Create project`

![jira-template-software-project-after-creation.png](/images/jira-template-software-project-after-creation.png)

> [!NOTE] When you create a project, it will automatically create the following elements:
>
> - Issue type schemes -> `PMTEMPLATE: Scrum Issue Type Scheme`
> - Issue type screen schemes -> `PMTEMPLATE: Scrum Issue Type Screen Scheme`
> - Workflow schemes -> `PMTEMPLATE: Software Simplified Workflow Scheme`
> - Workflows -> `Software Simplified Workflow for Project PMTEMPLATE`
> - Screen schemes -> `PMTEMPLATE: Scrum Default Screen Scheme`, `PMTEMPLATE: Scrum Bug Screen Scheme`
> - Screens -> `PMTEMPLATE: Scrum Default Issue Screen`, `PMTEMPLATE: Scrum Bug Screen`

## Adjust our newly created project template to follow some best practices

> [!warning] #todo
