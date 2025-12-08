---
title: "Common mistakes writing GTK code"
date: "2012-08-25 00:58"
author: "liberforce"
category: "Computers / Informatique"
tags: "gtk"
slug: "common-mistakes-writing-gtk-code"
lang: "en"
status: "published"
---

I give a hand in several computing forums (mainly nowadays [developpez.net](https://www.developpez.net) in french, and [stackoverflow.com](https://stackoverflow.com) in english), mostly about GNOME, GTK, or C programming.

Let's focus on GTK. People asking some advice on these sites are often starting to learn GTK. From my experience, the root causes of most of their problems are often the same:

1. Not respecting the prototype of a signal's callback
2. Failing to understand how a message pump works
