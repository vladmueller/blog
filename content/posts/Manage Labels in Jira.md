---
date: 2025-02-12
title: Manage Labels in Jira
description: TODO
draft: true
tags:
  - draft
---

#todo [3 Essential Ways for Product Owners to Manage BAU Without Killing Innovation | Scrum.org](https://www.scrum.org/resources/blog/3-essential-ways-product-owners-manage-bau-without-killing-innovation)

- [collectivemind.atlassian.net/rest/api/3/label](https://collectivemind.atlassian.net/rest/api/3/label)
- https://collectivemind.atlassian.net/rest/api/2/search?jql=&fields=labels

How to delete a Label -> [Delete a label in Jira | Jira | Atlassian Documentation](https://confluence.atlassian.com/jirakb/how-to-delete-a-label-in-jira-297667646.html)

> if you simply want to remove a label then use JQL to find all issues where the label is used and manually remove from each issue at which point the label will disappear from the drop-down.

## Remove a label

1. List all labels via JQL `labels = "your-label"`
2. Click on `... > Bulk change all n issues`
3. *Select all issues* > Click on `Next`
4. Select `Edit issues`
5. Select `Change Labels` + Select `Find and remove these` from drop-down list + *Type in* `your-label`

![jira-remove-label.png](/images/jira-remove-label.png)

6. Click on `Next`
7. Click on `Confirm`
8. Click on `Acknowledge`


#todo All labels which are found are also used. There are not "unsed" labels.
