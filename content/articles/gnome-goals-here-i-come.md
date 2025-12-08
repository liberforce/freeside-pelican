---
title: "GNOME Goals, here I come !"
date: "2008-12-04 03:02"
author: "liberforce"
category: "Computers / Informatique"
tags: "GNOME Goals, GNOME"
slug: "gnome-goals-here-i-come"
lang: "en"
status: "published"
---
A few weeks ago, some new [GNOME
Goals](http://live.gnome.org/GnomeGoals){hreflang="en"} were open. I've worked
on the guidelines of some of them. Some of these goals are paving the road
towards GNOME 3.0. My first task has been to [detect the deprecated GLib
symbols](http://live.gnome.org/GnomeGoals/RemoveDeprecatedSymbols/Glib){hreflang="en"}
used within the GNOME stack, to let other people submit simple patches. This is
a nice way to have newcommers get into the GNOME stuff. This work included
basic grep searching in C/C++ source files of each GNOME module, in order to
find these symbols.

Tonight, I've been working on using
[jhbuild](http://live.gnome.org/Jhbuild){hreflang="en"} and compiling the whole
stuff disabling deprecated Glib symbols, and [forbiding gtk/gdk/gdk-pixbuf
sub-headers direct
inclusion](http://live.gnome.org/GnomeGoals/CleanupGTKIncludes){hreflang="en"}.
This is easy, but lenghty work. Especialy compiling the whole GNOME stack.
gnome-vfs in particular was a pain in the ass to migrate, because it heavily
relied on sub-headers inclusion.

Expect a few bug reports and patches until the end of the week. Now if only I
could have commit rights... Does anyone know who I'm supposed to contact for
this ?

If you want to give it a try too, or just want to check progress, just add this
to your `~/.jhbuildrc` file

`makeargs='CFLAGS="-g -O2 -DG_DISABLE_DEPRECATED -DG_DISABLE_SINGLE_INCLUDES
-DGDK_PIXBUF_DISABLE_SINGLE_INCLUDES -DGTK_DISABLE_SINGLE_INCLUDES"'`

The next step towards world domination will be the [removal of deprecated GTK+
symbols](http://live.gnome.org/GnomeGoals/RemoveDeprecatedSymbols/GTK%2B){hreflang="en"},
wich is longer and more complicated, as it required more testing.
