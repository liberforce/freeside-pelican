Title: Lazyweb: of the good usage of GSource...
Date: 2008-02-21 19:19
Author: LM2153-GANDI
Category: Computers / Informatique
Tags: glib, GNOME
Slug: lazyweb-of-the-good-usage-of-gsource
Status: published

I'm currently writing an application that has two backends.

- In *live* mode, I acquire images from several cameras.
- In *replay* mode, I read pre-recorded images from the harddrive.

As I want to switch between these 2 backends transparently, I thought ofusing two implementations of a <a href="http://library.gnome.org/devel/glib/2.10/glib-The-Main-Event-Loop.html#id3126598" hreflang="en">custom GSource</a>. It seemed to be what I need: a way to sendand react to asynchonous events. In my case, I want to notify the applicationthat the images are in the memory, and ready to be processed.

However I'm a still a bit puzzled about how GSource works, and I found thedocumentation a bit obscure to people unfamiliar with the arcanes of the glibmain loop. The timeout and idle sources don't give me enough information. Theother examples use polling of file descriptors, but I have nothing to pollhere. I've even checked out <a href="http://nostarch.com/frameset.php?startat=gnome" hreflang="en">The OfficialGNOME 2 Developper's Guide</a>, but no GSource there. I had <a href="http://mail.gnome.org/archives/gtk-app-devel-list/2008-February/msg00050.html" hreflang="en">not much result</a> in the gtk-apps-devel mailing list, nor the<a href="http://forum.gtk-fr.org/viewtopic.php?id=4529" hreflang="fr">frenchGTK forums</a>.

I'm at the point where I'm not even sure that GSource meets my needs, but Iwanted to avoid as much as possible exposing the acquisition backend. Therewill be multi-threaded stuff for live acquisition (the cameras I'm using onlyprovide a blocking API, sigh..), but they're not required for the replaymode.

Do you think a custom GSource is the way to go ? It seems it's the only wayI can connect to glib's main loop to receive asynchronous events (excepted fromtimeout and idle sources). Could someone please explain me a bit in whichcase(s) using GSource is recommended ? Thanks for reading.

</p>
