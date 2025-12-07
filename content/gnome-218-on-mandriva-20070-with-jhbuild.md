---
title: "GNOME 2.18 on Mandriva 2007.0 with jhbuild"
date: "2007-03-20 01:09"
author: "liberforce"
category: "Computers / Informatique"
tags: "mandriva, GNOME"
slug: "gnome-218-on-mandriva-20070-with-jhbuild"
status: "published"
---
[GNOME 2.18](http://www.gnome.org/start/2.18/) has been released a few days ago. However, I still haven't seen it running.... I'm too lazy to download [Foresight Linux](http://www.rpath.org/rbuilder/project/foresight/release?id=5451), and it seems that the Mandriva One with GNOME 2.18 is only available for x86_64 users... Too bad for my Athlon XP 3000+.  
  
Anyway, I just achieved to compile almost the whole GNOME desktop from jhbuild tonight. Only a few modules are missing, some because they are hard to compile with 2007.0 (NetworkManager, network-manager-applet), others just because I just don't care about them (mozilla, evolution-exchange, libexchange). Mozilla in particular is so huge that I just always skip it.  
  
For the braves that will dare to compile the GNOME desktop on their Mandriva 2007.0, I have just updated my guidelines about the [jhbuild dependencies for GNOME on Mandriva Linux](http://live.gnome.org/JhbuildDependencies/MandrivaLinux).  
  
Enjoy.
