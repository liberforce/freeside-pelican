---
title: "Lazyweb: of the good usage of GSource..."
date: "2008-02-21 19:19"
author: "liberforce"
category: "Computers / Informatique"
tags: "glib, GNOME"
slug: "lazyweb-of-the-good-usage-of-gsource"
status: "published"
---
I'm currently writing an application that has two backends.

- In *live* mode, I acquire images from several cameras.
- In *replay* mode, I read pre-recorded images from the hard drive.

As I want to switch between these 2 backends transparently, I thought of using two implementations of a [custom GSource](http://library.gnome.org/devel/glib/2.10/glib-The-Main-Event-Loop.html#id3126598){hreflang="en"}. It seemed to be what I need: a way to send and react to asynchonous events. In my case, I want to notify the application that the images are in the memory, and ready to be processed.

However I'm a still a bit puzzled about how GSource works, and I found the documentation a bit obscure to people unfamiliar with the arcanes of the glib main loop. The timeout and idle sources don't give me enough information. The other examples use polling of file descriptors, but I have nothing to poll here. I've even checked out [The Official GNOME 2 Developper's Guide](http://nostarch.com/frameset.php?startat=gnome){hreflang="en"}, but no GSource there. I had [not much result](http://mail.gnome.org/archives/gtk-app-devel-list/2008-February/msg00050.html){hreflang="en"} in the gtk-apps-devel mailing list, nor the [french GTK forums](http://forum.gtk-fr.org/viewtopic.php?id=4529){hreflang="fr"}.

I'm at the point where I'm not even sure that GSource meets my needs, but I wanted to avoid as much as possible exposing the acquisition backend. There will be multi-threaded stuff for live acquisition (the cameras I'm using only provide a blocking API, sigh..), but they're not required for the replay mode.

Do you think a custom GSource is the way to go ? It seems it's the only way I can connect to glib's main loop to receive asynchronous events (excepted from timeout and idle sources). Could someone please explain me a bit in which case(s) using GSource is recommended ? Thanks for reading.
