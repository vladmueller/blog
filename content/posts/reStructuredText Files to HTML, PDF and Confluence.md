---
date: 2025-04-23
title: reStructuredText Files to HTML, PDF and Confluence
description: Create different output formats from one single reStructuredText files source
draft: true
tags:
  - draft
---

```
.rst-files -> Sphinx
                |
                +---> HTML
                +-(SimplePDF)--> PDF
                +-(confluencebuilder)-> Confluence
```

- [Sphinx-SimplePDF — Sphinx-SimplePDF documentation](https://sphinx-simplepdf.readthedocs.io/en/latest/)
- [Resolving the Python WeasyPrint Error: "Cannot Load Library '‌gobject-2.0-0'" - YouTube](https://www.youtube.com/watch?v=dYR75vxY1ho&ab_channel=blogize)

---

[GitHub Container Registry: BETTER Than Docker Hub? - YouTube](https://www.youtube.com/watch?v=WjzA9dfk5w4)

```
ghcr.io/OWNER/IMAGE_NAME:version
```

[Push Docker Images to GitHub Container Registry - YouTube](https://www.youtube.com/watch?v=RgZyX-e6W9E)

Ein personal access token verwenden, um uns in GitHub Packages (GHCR) einzuloggen.
`Settings -> Developer Settings -> Personal access tokens -> Tokens (classic)`

```
docker login --username vladmueller --password <PASSWORD> ghcr.io
```

---

> [!important]- SVG Exports von draw.io müssen bestimmte Einstellungen haben
> Sonst werden sie nur schwarz in der generierten PDF von simplepdf angezeigt 
> ![drawio-svg-compatible-settings-for-simplepdf.png](/images/drawio-svg-compatible-settings-for-simplepdf.png)
