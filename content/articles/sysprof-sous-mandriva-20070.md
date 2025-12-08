---
title: "Sysprof sous Mandriva 2007.0"
date: "2007-03-28 00:58"
author: "liberforce"
category: "Computers / Informatique"
tags: "GNOME, mandriva"
slug: "sysprof-sous-mandriva-20070"
lang: "fr"
status: "published"
---
[Sysprof](http://live.gnome.org/Sysprof) est un logiciel de profiling: il
permet de voir les fonctions qui utilisent le plus de temps CPU dans un
programme. C'est le logiciel recommandé par GNOME pour vérifier les
performances d'une application. Malheureusement, il semble que le logiciel ne
peut être installé sous Mandriva 2007.0, à causes de problèmes de dépendances.

Pour ceux que cela intéresse, j'ai recompilé sysprof 1.0.8 à partir du RPM
source de la Mandriva 2007.1, pour qu'il soit utilisable sous Mandriva 2007.0.
N'oubliez pas aussi d'installer **dkms**, et les sources de *votre* version du
kernel (**kernel-source** ou **kernel-source-stripped**). Un petit `modprobe
sysprof-module` en root sera sans doute aussi nécessaire...

Vous trouverez là [sysprof 1.0.8 (i586) pour Mandriva
2007.0](http://liberforce.is.dreaming.org/tmp/sysprof-1.0.8-2mdv2007.0.i586.rpm).
