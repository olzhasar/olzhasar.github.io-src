#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

AUTHOR = 'Olzhas Arystanov'
SITENAME = 'Olzhas Arystanov'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['projects']

THEME = os.path.join(BASE_DIR, 'theme')

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}.html'

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
TAG_URL = 'tag/{slug}'

TIMEZONE = 'Asia/Almaty'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
