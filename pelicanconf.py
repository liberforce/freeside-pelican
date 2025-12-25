#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime

AUTHOR = "liberforce"
SITENAME = "Greetings From The Free Side!"
SITEURL = "https://www.freeside.fr/blog"

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
    ("GNOME", "https://www.gnome.org"),
    ("Mageia", "https://www.mageia.org"),
)

# Social widget
SOCIAL = (
    ("mastodon", "https://framapiaf.org/@liberforce"),
    ("github", "https://github.com/liberforce"),
)

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

# Categories
CATEGORY_URL = "categories/{slug}.html"
CATEGORY_SAVE_AS = CATEGORY_URL

# Tags
TAG_URL = "tags/{slug}.html"
TAG_SAVE_AS = TAG_URL

########
# Themes
########
# Theme to use
THEME = "themes/Flex"

#######
# Menus
#######
MAIN_MENU = True

# These paths are implied as absolute in the Flex theme
SITELOGO = "/images/hackergotchi.png"
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

#######
# Fonts
#######
USE_GOOGLE_FONTS = False

#########
# License
#########
COPYRIGHT_YEAR = datetime.now().year
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

#########
# Caching
#########
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

#########
# Plugins
#########
PLUGINS = [
    "pelican.plugins.pandoc_reader",
    "pelican.plugins.minify",
]
