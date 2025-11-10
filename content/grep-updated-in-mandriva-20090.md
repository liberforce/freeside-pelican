Title: Grep updated in Mandriva 2009.0
Date: 2008-10-22 16:16
Author: liberforce
Category: Computers / Informatique
Tags: mandriva, grep
Slug: grep-updated-in-mandriva-20090
Status: published

Funny thing I saw today : grep version jumped from 2.5.1a in 2008.1 to 2.5.3in 2009.0. Sounds useless, huh, grep does its stuff, so this should only be abugfix or code cleaning release, don't you think ?

Well in fact, its not. Grep 2.5.3 introduces the long awaited option`--exclude-dir`. You can now just grep your version control tree forsome stuff and easily exclude your .cvs/.svn/whatever directory, without havingto resort to a big fat `find` command with `xargs`.

Before :

<span id="\"hidsubpartcontentdiscussion\"">`find .`</span> <span id="\"hidsubpartcontentdiscussion\"">`-type f`</span> <span id="\"hidsubpartcontentdiscussion\"">`! -path '*/.svn/*' -print0 | xargs -0 grepfoo`</span>

<span id="\"hidsubpartcontentdiscussion\"">After :</span>

<span id="\"hidsubpartcontentdiscussion\"">`grep -R --exclude-dir=.svn foo*`</span>

<span id="\"hidsubpartcontentdiscussion\"">It's sad that this option tookseveral years to enter the code base (at least 2.5 years) and was first refused(this bug report is an <a href="\%22http://savannah.gnu.org/patch/?3521\%22" hreflang="\&quot;en\&quot;">example of how not to reply tousers</a>). Also, this new version of grep landed in 2009.0, but grep 2.5.3 wasreleased</span> <span id="\"hidsubpartcontentdiscussion\"">in august2007...</span>

Mandriva Linux 2008.1 users interested by this feature can install the2009.0 version of grep from their closest miror :

`urpmiftp://ftp.proxad.net/pub/Distributions_Linux/MandrivaLinux/official/2009.0/i586/media/main/release/grep-2.5.3-6mdv2009.0.i586.rpm`

**Update :** Don't do that at home kids if you're not sure,because mixing software from different releases can sometimes lead to nastybugs

</p>
