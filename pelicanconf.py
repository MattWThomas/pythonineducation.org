#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

''' Plugins to compile SCSS and include other files
PLUGIN_PATH = 'plugins'
PLUGINS = ['assets']

MARKDOWN = {
    'extensions': ['mdx_include']
}
'''

AUTHOR = 'PSF'
SITENAME = 'Python in Education'
SITEURL = ''

PATH = 'content'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DIRECT_TEMPLATES = ['index']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/pie'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True