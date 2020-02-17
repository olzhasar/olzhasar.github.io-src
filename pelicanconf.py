#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

AUTHOR = "Olzhas Arystanov"
SITENAME = "Olzhas Arystanov"
SITEURL = ""

PATH = "content"
STATIC_PATHS = ["projects"]

THEME = os.path.join(BASE_DIR, "theme")

CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}.html"

ARTICLE_URL = "{category}/{slug}"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
TAG_URL = "tag/{slug}"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

TIMEZONE = "Asia/Almaty"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

GITHUB_URL = "https://github.com/olzhasar"
STACKOVERFLOW_URL = "https://stackoverflow.com/users/4154360/olzhas-arystanov"

CONTACTS = (
    ("Email", "mailto:o.arystanov@gmail.com", "o.arystanov@gmail.com"),
    ("Mobile", "callto:+77017367551", "+77017367551"),
    ("Telegram", "https://t.me/olzhasar", "olzhasar"),
)

EMAIL = "o.arystanov@gmail.com"


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
