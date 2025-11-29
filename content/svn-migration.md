Title: SVN migration
Date: 2007-01-05 02:51
Author: liberforce
Category: Computers / Informatique
Tags: Unclassified
Slug: svn-migration
Status: published

I see [lots](http://blogs.gnome.org/view/mortenw/2006/12/26/0) [of](http://blogs.gnome.org/view/ryanl/2006/12/25/0) [people](http://tw.apinc.org/weblog/2006/12/26#christmas-evening-thoughts) complaining about the GNOME servers migration from CVS to SVN. Hey guys, what's the point? That's not a big step enough for you? This has been talked about for a long time now.  
  
I'm personnaly using SVN at work, and, even if I don't use advanced features (i'm the only developer on the project), i've been pretty happy with it. The features I liked the most:

- *svn move* can move or rename files, without losing their history
- *svn diff* output is format-ready for patch. No need to specify weird options for the output format (*cvs diff -up*)
- svn keeps permissions on files
- svn keeps only stores modifications of binary files, and not the full file each time.
- the [SVN documentation](http://svnbook.red-bean.com/en/1.2/index.html) is great!

Yes. I'm a really basic user of SVN. Sure. So may be the average GNOME contributors-wanabe.  
Yes, I know that commiting modifications offline is great. But I mostly see the CVS-\>SVN migration as a first step.  
  
It's good for conservative people because is very close to CVS. It's good for newcommers because it hasn't the CVS headaches (mostly the file renaming issue, and lack of directory versionning).  
  
And i'm really happy **I will finallly be able to browse online the GNOME source code without having to figure out which directory contains the source** because the hierarchy of the project once changed and it only contains dead code o/. All this crap will finally be removed, and that's a good thing.  
  
SVN is a big step forward. Maybe it's not as big as some may want, but it's for sure enough for me. And it surely will be better than the current situation.  
  
\[Edit\]:  
The comment here will also give lots of good reasons: think of casual contributors, translators, etc. who just don't want to learn a new bleeding-edge revision system. SVN addresses the problems we have **now**.  
<http://blogs.gnome.org/view/ryanl/2006/12/25/0#comments>  
  
\[Edit 2\]: This may help too  
[Why GNOME migrated from CVS to Subversion ?](http://live.gnome.org/SubversionFAQ#Why_Subversion)
