#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime

AUTHOR = "liberforce"
SITENAME = "Greetings From The Free Side!"

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "http://www.freeside.fr"

PATH = "content"

TIMEZONE = "Europe/Paris"

############################
# Languages and translations
############################
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GNOME", "http://www.gnome.org"),
    ("Mageia", "http://www.mageia.org"),
)

# Social widget
SOCIAL = (("Mastodon", "https://framapiaf.org/@liberforce"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

###############
# File location
###############
# Articles
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.{lang}.html"
ARTICLE_SAVE_AS = ARTICLE_URL

# Translated articles
ARTICLE_LANG_URL = ARTICLE_URL
ARTICLE_LANG_SAVE_AS = ARTICLE_URL

########
# Themes
########
# Theme to use
THEME = "themes/Flex"

#########
# License
#########
COPYRIGHT_YEAR = datetime.now().year
