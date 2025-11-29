Title: Process wakeups on GNOME 2.18
Date: 2007-12-11 02:58
Author: liberforce
Category: Computers / Informatique
Tags: écologie, GNOME
Slug: process-wakeups-on-gnome-218
Status: published

# Learning from the past

Yesterday an old (1.5 year) blog entry of <a href="http://blogs.gnome.org/desrt/2006/07/27/burning-cpu-and-battery-on-the-gnome-desktop/" hreflang="en">Ryan Lortie on cpu and battery consumption</a> came to my mind. He tested some <a href="http://www.gnome.org" hreflang="en">GNOME</a> applications and saw that some of them caused way too many kernel wakeups, which prevents the CPU from entering in low consumption states. So, as just by curiosity (ang ecological concerns), I wanted to see if there's some improvements on this area on the GNOME desktop.

As Ryan talks about Ubuntu Dapper Drake in his post, I suppose he was testing ye old GNOME 2.14. As a comparison, I ran my tests on GNOME 2.18 under Mandriva 2007.1. I then will be able to compare the figures to GNOME 2.20 when I'll install Mandriva 2008.0 (I'm lacking some time for this at the moment).

Some stuff he pointed out:

> gnome-power-manager wakes up twice per second to do something  
> battery applet wakes up once per second to do something  
> clock-applet wakes up once per second to update the time even when seconds aren’t shown  
> gajim wakes up 10+ times per second for some unknown reason  
> at-spi-registryd wakes up more like 20+ times a second (?!?)  
> gss seems to talk to x11 once per second (presumably to ask if anything has happened). i don’t understand why it has to do this so often.

I don't use some of the stuff he tested. So I tested gnome-power-manager, the clock applet and gnome-screensaver (gss) as he did.

## The test method

A test that doesn't explain the test method is irrelevant. What I did is that I used strace for 10 seconds like Ryan did, but using an interesting option of strace (-c) to have a nice summary of the system calls that were used during the observation period. For example the gnome-screensaver process was spied using:

`strace -c -p $(pidof gnome-screensaver) & sleep 10; killall strace`

Strace is attached to the spied process in the background. We then wait for 10 seconds and stop strace so that it can give us the amount of systems calls performed during this timeframe. The application were not being actively used while the test was performed, and I stopped mouse/keyboard input during the test, just waiting until it ended.

## gnome-screensaver

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0         1           ioctl`  
`   nan    0.000000           0         2           gettimeofday`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                     3           total`  

<del>

~~We immediately can see that poll is still called once per second, so either this is a bug that has not been corrected, or this can't really be worked around.~~

</del>

**Update:** The previous numbers were wrong it seems (weird, I had tested it twice, but the numbers I get now are completely different). The problems reported by Ryan have already been <a href="http://bugzilla.gnome.org/show_bug.cgi?id=363436" hreflang="en">corrected</a>.

## gnome-panel

With the seconds in the clock applet **not** displayed:

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0         1           ioctl`  
`   nan    0.000000           0         2           gettimeofday`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                     3           total`  
  
With the seconds in the clock applet displayed:

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0        30           read`  
`   nan    0.000000           0        20           write`  
`   nan    0.000000           0        20           time`  
`   nan    0.000000           0        31           ioctl`  
`   nan    0.000000           0        62           gettimeofday`  
`   nan    0.000000           0        30           poll`  
`   nan    0.000000           0        10           stat64`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                   203           total`

It's easy to see that enabling the seconds on the applet causes an explosion of the number of calls. That's 3 poll calls per second ! Sound quite abnormal to me, especially the amount of other calls this option generated...

## gnome-session

Looks fine.

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0         1           ioctl`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                     1           total`

## devhelp

It was in the background, but there's still too many calls for an application that was not being used.

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0        11           read`  
`   nan    0.000000           0         1           write`  
`   nan    0.000000           0        32           ioctl`  
`   nan    0.000000           0         6           gettimeofday`  
`   nan    0.000000           0        11           poll`  
`   nan    0.000000           0         1           futex`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                    62           total`

## gnome-terminal

<del>

~~Waaaay too many calls. We here have 4 poll calls/second. The blinking cursor may be a cause (I'm aware a patch for this was made for <a href="http://laptop.org" hreflang="en">OLPC</a>). I also know <a href="http://mces.blogspot.com/" hreflang="en">Behdad</a> once committed a patch adding a timer to prevent gnome-terminal from trying to refresh too many times the screen. The goal was to accelerate the display of information. Don't know if the extra calls are related to this, however.~~

</del>

**Update:** ok, I must have been drinking, everything is normal.  
I tested the gnome-terminal that was running strace, so I was getting the calls for executing strace... The good way is for example to test it from an xterm. Another one like this and I jump out of the window.

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0         1           ioctl`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                     1           total`

## mixer_applet2

The mixer applet is one of the worst offenders! This is a <a href="http://bugzilla.gnome.org/show_bug.cgi?id=370937" hreflang="en">known bug</a> which is being worked on. Hope to see this included in GNOME 2.22.

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0        99        99 read`  
`   nan    0.000000           0       169           ioctl`  
`   nan    0.000000           0       296           gettimeofday`  
`   nan    0.000000           0       169           poll`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                   733        99 total`

## timer-applet

Even when not used, this applet does way too many calls... There's room for improvement here.  
`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0        34           ioctl`  
`   nan    0.000000           0        67           gettimeofday`  
`   nan    0.000000           0        34           poll`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                   135           total`

## trashapplet

Looks fine.

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0         1           ioctl`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                     1           total`

## mdkapplet

Mandriva's memory-hungry updates surveillance applet seems to be CPU friendly...

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`   nan    0.000000           0         2           ioctl`  
`   nan    0.000000           0         4           gettimeofday`  
`   nan    0.000000           0         1           poll`  
`   nan    0.000000           0         1         1 stat64`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                     8         1 total`

## gnome-power-manager

Ryan saw gnome-power-manager wake up twice per second in GNOME 2.14. It seems things got worse, as I had it wake up thrice per second, on AC power.

`% time     seconds  usecs/call     calls    errors syscall`  
`------ ----------- ----------- --------- --------- ----------------`  
`    nan    0.000000           0        40           read`  
`    nan    0.000000           0        40           write`  
`    nan    0.000000           0         2           time`  
`    nan    0.000000           0        29           ioctl`  
`    nan    0.000000           0        53           gettimeofday`  
`    nan    0.000000           0        29           poll`  
`------ ----------- ----------- --------- --------- ----------------`  
`100.00    0.000000                   193           total`

# Conclusion

Well, there's quite nothing to conclude. These numbers are just here so that people can easily test and compare with their GNOME version, and eventually find more culprits. I think I'll update them on each GNOME Release, so we can see if the plan to conquer the world with power-friendly software works out. Just as a remark, developers who use timers at the second scale should consider using the <a href="http://library.gnome.org/devel/glib/stable/glib-The-Main-Event-Loop.html#g-timeout-add-seconds" hreflang="en">g_timeout_add_seconds</a> call that was added in glib 2.14, as it allows to group processing of wakeup requests. So if your application can depend on glib 2.14, go for it.
