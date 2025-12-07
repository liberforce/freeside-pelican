---
title: "Pidgin connection errors with jabber"
date: "2008-04-01 21:50"
author: "liberforce"
category: "Computers / Informatique"
tags: "bug, mandriva, pidgin"
slug: "pidgin-connection-errors-with-jabber"
status: "published"
---
I barely use pidgin (and jabber even less), but today, I was just fed up of having the same connection error. I'm using the 2.2.1 version, shipped with on Mandriva 2008.0. The problem is that I had an SSL certificate error each time I would try to connect to jabber.org. The solution from the french Ubuntu forums I found was overkill: recompile and install pidgin 2.4.0. Fortunately, I found on the [Arch Linux forums](http://bbs.archlinux.org/viewtopic.php?pid=319192){hreflang="en"} a much better solution, which might be helpful for people having the same problem :


    rm ~/.purple/certificates/x509/tls_peers

Enjoy :)
