---
title: Example Post
date: 2025-02-11
draft: true
tags:
  - draft
description: This post is for demo purposes
---

## This is an example post

[[Board configuration in Jira Cloud Business Projects]]

http://localhost:1313/posts/board-configuration-in-jira-cloud-business-projects/

[Internal Link](/posts/board-configuration-in-jira-cloud-business-projects)

[example](https://example.com)

## Lists

* Item 1
* Item 2
  * Item 3
    * Item 4

- Item A
- Item B

## Code

```go
func getCookie(name string, r interface{}) (*http.Cookie, error) {
	rd := r.(*http.Request)
	cookie, err := rd.Cookie(name)
	if err != nil {
		return nil, err
	}
	return cookie, nil
}

func setCookie(cookie *http.Cookie, w interface{}) error {
	// Get write interface registered using `Acquire` method in handlers.
	wr := w.(http.ResponseWriter)
	http.SetCookie(wr, cookie)
	return nil
}
```

## Callouts

### Note

{{< callout emoji="📝️" text="A note." >}}

### Original

{{< callout emoji="⚡️" text="Original callout." >}}

### Alert

{{< callout type="alert" text="This is an alert callout." >}}

### Custom

{{< callout type="custom" emoji="⚡️" title="Custom callout" text="This is custom text for a custom callout." style="background-color: transparent; border: 3px solid #d340e0;" >}}

### Tip

{{< callout type="tip" text="This is a tip callout." >}}

### Warning

{{< callout type="warning" text="This is a warning callout." >}}
