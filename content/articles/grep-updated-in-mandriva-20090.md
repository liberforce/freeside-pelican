---
title: "Grep updated in Mandriva 2009.0"
date: "2008-10-22 18:16"
author: "liberforce"
category: "Computers / Informatique"
tags: "mandriva, grep"
slug: "grep-updated-in-mandriva-20090"
status: "published"
---
Funny thing I saw today : grep version jumped from 2.5.1a in 2008.1 to 2.5.3 in 2009.0. Sounds useless, huh, grep does its stuff, so this should only be a bugfix or code cleaning release, don't you think ?

Well in fact, its not. Grep 2.5.3 introduces the long awaited option `--exclude-dir`. You can now just grep your version control tree for some stuff and easily exclude your .cvs/.svn/whatever directory, without having to resort to a big fat `find` command with `xargs`.

Before :

[`find .`]{#hidsubpartcontentdiscussion} [`-type f`]{#hidsubpartcontentdiscussion} [`! -path '*/.svn/*' -print0 | xargs -0 grep foo`]{#hidsubpartcontentdiscussion}

[After :]{#hidsubpartcontentdiscussion}

[`grep -R --exclude-dir=.svn foo *`]{#hidsubpartcontentdiscussion}

[It's sad that this option took several years to enter the code base (at least 2.5 years) and was first refused (this bug report is an [example of how not to reply to users](http://savannah.gnu.org/patch/?3521){hreflang="en"}). Also, this new version of grep landed in 2009.0, but grep 2.5.3 was released]{#hidsubpartcontentdiscussion} [in august 2007...]{#hidsubpartcontentdiscussion}

Mandriva Linux 2008.1 users interested by this feature can install the 2009.0 version of grep from their closest miror :

`urpmi ftp://ftp.proxad.net/pub/Distributions_Linux/MandrivaLinux/official/2009.0/i586/media/main/release/grep-2.5.3-6mdv2009.0.i586.rpm`

**Update :** Don't do that at home kids if you're not sure, because mixing software from different releases can sometimes lead to nasty bugs
