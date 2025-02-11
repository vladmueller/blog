---
title: No Board configuration in Jira Cloud Business Projects
date: 2025-01-29
draft: true
tags:
  - atlassian
  - jira
  - problem
  - draft
---

## Problem 

You want track some tasks and work which has to be done ..
introduce a higher level hierarchy
but then you realize that you can not configure the board

![jira-cloud-no-board-configuration-in-jira-workmanagement-projects.png](/images/jira-cloud-no-board-configuration-in-jira-workmanagement-projects.png)

Basically the initial board setup is different for every project type:

|                         | Jira Software | Jira Business Project | Jira Service Management |
| ----------------------- | ------------- | --------------------- | ----------------------- |
| **Bulit-in board**      | ✅             | ✅                     | ❌                       |
| **Board configuration** | ✅             | ❌                     | ❌                       |

## Solution

Create a second Kanban board manually and create a link to it in your business project. We start with the filter first.

1. Create a new filter: `Filters > View all filters > Create filter` 
   Type in the following JQL: `project = <YOUR-PROJECT_KEY> ORDER BY Rank ASC`

> Note to `Rank`: **TODO**

![Pasted image 20250129154619.png](/images/Pasted image 20250129154619.png)

2. Click on `Save filter` and name it: `Filter for <YOUR-PROJECT_KEY> board` (which is the default naming convention for boards in Jira, if you want to stick to it) 

![Pasted image 20250129155041.png](/images/Pasted image 20250129155041.png)

It is also important to set the viewers and editors permission accordingly, otherwise your team member in this project won't see anything on the board.

3. Create a new Kanban board: `Your work > Boards > View all boards > Create board > Create a Kanban board > Board from an existing Saved Filter > Create board` 

![Pasted image 20250129160145.png](/images/Pasted image 20250129160145.png)

> [!warning] Select your personal user for `Location`, as you can not select other project types than Jira Software projects - but that's ok in this workaround

The result will be this new board, which we can configure now as we are used to from classical Jira Software projects:

![Pasted image 20250129160712.png](/images/Pasted image 20250129160712.png)

> [!NOTE] One more note to this workaround:
> This board won't show up per default in your business project, but you can add a shortcut to it in your project menu bar: 
> 
> ![Pasted image 20250129161305.png](/images/Pasted image 20250129161305.png)

## Summary

If you know in first place, that you are going to use many boards with flexible configurations, which should live under the same project, then you might consider to create a Jira Software project, even when the tasks/issues are more business and less software related (just remove not need issue types `Story`, `Bug` etc.) ✌





---

- [How to access Board Settings IN Work Management Pr...](https://community.atlassian.com/t5/Jira-questions/How-to-access-Board-Settings-IN-Work-Management-Project/qaq-p/2340344)
- [Creating a Second Agile Board for Team-Managed or ... - Atlassian Community](https://community.atlassian.com/t5/Jira-articles/Creating-a-Second-Agile-Board-for-Team-Managed-or-JIra-Work/ba-p/2115018)
- [Solved: How do I create an empty project?](https://community.atlassian.com/t5/Jira-questions/How-do-I-create-an-empty-project/qaq-p/2906807)
