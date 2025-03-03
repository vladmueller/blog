---
date: 2025-02-14
title: Imports in Python are executed immediately
description: Beware that Python executes code from imports directly.
draft: false
tags:
  - python
  - unexpected-behavior
---

## Problem

> [!warning] Python directly executes top-level code from imported files.

If you come from a compiled language, like I do, you are probably used to creating an instance of your imports or calling a static method directly.
In both cases, we must take explicit action in our code - nothing happens automatically.

I was unaware of this, and it led to unexpected side effects in my Python script, which imported files from my other directories and packages.

## Solution

> [!tip] To avoid side effects, only define functions and methods in the Python files you intend to import.
