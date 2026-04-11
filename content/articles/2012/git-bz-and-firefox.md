---
title: "git-bz and Firefox"
date: "2012-07-30 17:50"
author: "liberforce"
category: "Computers / Informatique"
tags: "git, gnome"
slug: "git-bz-and-firefox"
lang: "en"
status: "published"
---
[git-bz](http://git.fishsoup.net/cgit/git-bz/) is a utility written by [Owen
Taylor](http://blog.fishsoup.net) to ease the workflow between git and the
patches living in a bugzilla bugtracker. It allows uploading, applying patches
to/from bugzilla from the command line.

As it's the second time I'm bitten by that problem, I'll write it here as a
memo. The way git-bz communicates with bugzilla is by reusing the bugzilla
cookie from your browser. You just tell it which browser you're using, and it
will get the cookie at the right location. When this fail however, I tend to
check if I configured the right browser, or if I'm logged on
bugzilla.gnome.org. And I am, but it still fails.

```
Error getting login cookie from browser:    You don't appear to be signed
into bugzilla.gnome.org; please log in with Firefox

Configured browser: firefox3 (change with 'git config --global bz.browser
<value>') Possible browsers: chromium, epiphany, firefox3, galeon,
google-chrome
```

The problem is that with that message, I tend to focus on the configured
browser, not in the cookie itself. And the problem is in the cookie. In fact my
Firefox is configured to delete cookies each time I close it. The problem with
that configuration is that even if I log into bugzilla, the cookie will not be
written on disk in the cookies.sqlite file, it will just be kept in memory. To
fix that:

- go in Firefox Preferences, in Privacy settings
- add an exception on cookies management for the bugzilla instance of your
  choice, like bugzilla.gnome.org by allowing it
- log in your bugzilla instance

That way the cookie will be kept, and added to cookies.sqlite where git-bz will
find it.
