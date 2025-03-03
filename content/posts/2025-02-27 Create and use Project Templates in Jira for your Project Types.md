---
date: 2025-02-27
title: Create and use Project Templates in Jira for your Project Types
description: Use project templates for your project types to avoid wild growth of elements in Jira and reduce maintenance effort in the future.
draft: false
tags:
  - atlassian
  - jira
  - best-practices
  - jira-administration
  - project-management
  - cloud
---

It is a good practice to create project templates for you different project types, which you are going to use. This way you don't have to create every new project from scratch and every new project follows a standardized structure which helps to avoid wild growth of elements in Jira and reduces maintenance effort in the future.

> [!tip] Remember to follow these two rules, regardless of what you are doing in Jira:
> 
> - **#1 Less is more**
> - **#2 Always use Company-managed projects**

## Create a template for your projects types

**1**: `Projects` > `Create project` 

> [!warning] #todo Explain and link to difference between business and software project

### Option A: Use a business project

**2a**: Select `Work management` + `Blank project` (if you want a *business project*)

![jira-template-work-management-blank-project.png](/images/jira-template-work-management-blank-project.png)

**3a**: Click on `Show more` and select `Company-managed` project with key `PMTEMPLATE`
   and for Name: "Template Project Management"

![jira-template-blank-business-project-use-company-managed.png](/images/jira-template-blank-business-project-use-company-managed.png)

**4a**: Click on `Create project`

### Option B: Use a software project

**2b**: Select `Software development` + `Scrum` OR `Kanban` (if you want a `software project`)
and Click on `Use template`

![jira-template-use-scrum-template.png](/images/jira-template-use-scrum-template.png)

> [!note] Although we have to select a Scrum or Kanban board setup here, it will not be part of the template -  this means, if we create a new project from our template, we have to create the Kanban or Scrum board manually again.

**3b**: Select `Company-managed` project with key `PMTEMPLATE`
   and for Name: "Template Project Management"

![jira-template-software-project-use-company-managed.png](/images/jira-template-software-project-use-company-managed.png)

**4b**: Click on `Create project`

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

> [!note] [What is a simplified Jira workflow? | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/what-is-a-simplified-jira-workflow/)

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

6. `Cog wheel` > `Projects` > Search for PMTEMPLATE > Click on `...` > `Project settings` > `Workflows` > `Switch scheme` > Select `PMTEMPLATE - Workflow scheme` > Click on `Associate` > `Associate` (there shouldn't be any tickets to migrate)

Then our initial setup for our project template should look like this:

![jira-template-first-setup-summary.png](/images/jira-template-first-setup-summary.png)

## Next steps

- Use another notification scheme, which uses [Jira Notification Best Practices](/posts/jira-notification-best-practices)
- Define Roles for our project type
- Create groups for each role
- Set up a permission scheme for our roles
- Adjust our workflows for each issue type

## Use a reduced notification scheme

As described in [Jira Notification Best Practices](/posts/jira-notification-best-practices), we are going to use a reduced "watcher-only" notification scheme. Otherwise Jira is very talkative, which leads to unnecessary noise.

`Cog wheel` > `Projects` > Search for PMTEMPLATE > Click on `...` > `Project settings` > `Notifications` > `Settings` > Click on `Actions` > `Use a different scheme` > Select `Reduced Notification Scheme`

![jira-reduced-notification-scheme-watcher-only.png](/images/jira-reduced-notification-scheme-watcher-only.png)

## Define the roles for your project

For a classical project management context, I would suggest the following roles:

| Role            | Permissions                                                   |
| --------------- | ------------------------------------------------------------- |
| Project Admin   | *can access the* `Project settings` *and do everything else*  |
| Project Manager | *can do everything but can not access the* `Project settings` |
| User            | *can do the same as the project manager or less*              |
| Read-only       | *can only read information and add comments*                  |

We have to create our needed roles globally in the system settings:

`Cog wheel` > `System` > `Project roles`

### Create groups based on our roles

For each role we are going to create a group in our directory with the following convention:

```
JIRA_<PROJECT-KEY>_<ROLE>s
```

So for our template project, this will result in these groups:

- `JIRA_PMTEMPLATE_PROJECT_ADMINS`
- `JIRA_PMTEMPLATE_PROJECT_MANAGERS`
- `JIRA_PMTEMPLATE_USERS`
- `JIRA_PMTEMPLATE_READ_ONLY`

### Assign groups and roles

> [!tip] Each role is assigned to exactly one group in the project settings

![jira-assign-each-role-to-one-group.png](/images/jira-assign-each-role-to-one-group.png)

## Create a permission scheme

Check which *permission scheme* is used by our template project and make a copy of it:

- `Cog wheel` > `Issues` > `Permission schemes`, find `Default software scheme` and click on `Copy`
- Then find `Copy of Default software scheme` and click on `Edit`
- Rename it to `PMTEMPLATE - Permission scheme`

Then navigate to the `Project settings` of our template project > `Permissions` > `Actions` > `Use a different scheme` > Select `PMTEMPLATE - Permission scheme`

Adjust the permission scheme based on our roles, which could look something like this:

![jira-template-permission-scheme.png](/images/jira-template-permission-scheme.png)
