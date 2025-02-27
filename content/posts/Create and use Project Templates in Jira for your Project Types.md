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
> - *Issue type schemes* -> `PMTEMPLATE: Scrum Issue Type Scheme`
> - *Issue type screen schemes* -> `PMTEMPLATE: Scrum Issue Type Screen Scheme`
> - *Workflow schemes* -> `PMTEMPLATE: Software Simplified Workflow Scheme`
> - *Workflows* -> `Software Simplified Workflow for Project PMTEMPLATE`
> - *Screen schemes* -> `PMTEMPLATE: Scrum Default Screen Scheme`, `PMTEMPLATE: Scrum Bug Screen Scheme`
> - *Screens* -> `PMTEMPLATE: Scrum Default Issue Screen`, `PMTEMPLATE: Scrum Bug Screen`

## Adjust our newly created project template to follow some best practices

For *Issue type schemes* and *Issue type screen schemes* we follow this naming convention:

```
<PROJECT-KEY> - Issue Type Scheme
```

- `PMTEMPLATE: Scrum Issue Type Scheme` -> `PMTEMPLATE - Issue Type Scheme`
- `PMTEMPLATE: Scrum Issue Type Screen Scheme` -> `PMTEMPLATE - Issue Type Screen Scheme`

For *Screen schemes* we follow this naming convention:

```
<PROJECT-KEY> - <Issue Type> - Screen Scheme
```

- `PMTEMPLATE: Scrum Default Issue Screen` -> `PMTEMPLATE - Default - Screen Scheme`
- `PMTEMPLATE: Scrum Bug Screen` -> `PMTEMPLATE - Bug - Screen Scheme`

For Workflows and Workflow Schemes it is a bit more tricky - we could either use the **Simplified Workflow** and just rename it according to our naming convention:

> [!warning] #todo Explain Simplified Workflows

- `PMTEMPLATE: Software Simplified Workflow Scheme` -> `PMTEMPLATE - Workflow Scheme`
- `Software Simplified Workflow for Project PMTEMPLATE` -> `PMTEMPLATE - Simplified - Workflow`

Or what I would recommend to have the maximum flexibility, we are going to create our own Workflow scheme and Workflows, according to our naming convention.

```
<PROJECT-KEY> - <ISSUE TYPE> - Workflow - <VERSION>
```

1. Create a new workflow for the beginning: `Cog wheel` > `Issues` > `Workflows` > `Add workflow` > `Create new`
2. Name the workflow `PMTEMPLATE - Default - Workflow - 1.0` > Click on `Create`
3. `Cog wheel` > `Issues` > `Workflows schemes` > `Add workflow scheme`
4. Name the workflow scheme `PMTEMPLATE - Workflow scheme` > Click on `Add`
5. *In the newly added workflow scheme* click on `Add workflow` > `Add Existing` > Select `PMTEMPLATE - Default - Workflow - 1.0` > Click on `Next` > Select `All Unassigned Issue Types` > Click on `Finish`

Now we need to switch the *workflow scheme* which is used by our `PMTEMPLATE` project

1. `Cog wheel` > `Projects` > Search for PMTEMPLATE > Click on `...` > `Project settings` > `Workflows` > `Switch scheme` > Select `PMTEMPLATE - Workflow scheme` > Click on `Associate` > `Associate` (there shouldn't be any tickets to migrate)

Then our initial setup for our project template should look like this:

![jira-template-first-setup-summary.png](/images/jira-template-first-setup-summary.png)

## Next steps

- Adjust our workflows for each issue type
- Use another notification scheme, which uses [Jira Notification Best Practices](/posts/jira-notification-best-practices)
- Define Roles for our project type
- Set up a permission scheme for our roles
- Create groups for each role
