---
title: "Recycling an old machine for gcompris - part 1"
date: "2007-01-09 02:54"
author: "liberforce"
category: "Computers / Informatique"
tags: "recyclage, matériel"
slug: "recycling-an-old-machine-for-gcompris-part-1"
lang: "en"
status: "published"
---
I'm currently trying to convert my sister's old computer to Linux (guess what ?
Mandriva 2007). That way my 8 years old niece will be able to have her computer
to play with [gcompris](http://gcompris.net/).  Hardware specs of the beast:

- Celeron 366
- 160MB SDRAM (PC66 I presume)
- 4GB hard drive

It was running Windows 98, but running out of space. 2 years ago, when I
reinstalled Win98 on it, the HD had some failures and bad blocks, and I
couldn't use all the disk space, dur to Windows patition creation tool. Only
1GB could be partitioned, and I didn't have at that moment a Linux Live CD to
do it. Now that my sister has a more recent computer, this one can be recycled.

To have it working, I'm doing the following.

**Step 1:** Recover existing personal data using the excellent [Slax Popcorn
Live CD](http://www.slax.org/), and copy it on my USB key.  **Step 2:** Send
her the 60MB file backup file using the free (of charge) service
[Savefile.com](http://savefile.com/) to avoid blowing her mailbox **Step 3:**
Run [badblocks
-sw](http://man.linuxquestions.org/?query=badblocks&section=0&type=2) from the
[System Rescue CD.](http://www.sysresccd.org/) Note that these options will
erase all the data on disk, as this is a destructive test.

Let's see tomorrow how this is doing. Badblocks is now running, even if
painfully slow.
