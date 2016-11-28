#!/usr/bin/env python

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kyle thomas'
SITENAME = u'command build'
SITEURL = 'tkthomas27.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

BROWSER_COLOR = '#f4f9f9'
PYGMENTS_STYLE = 'monokai'
SITESUBTITLE = 'a temporary blog'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'http://google.com/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#MARKUP = ('md')

PLUGIN_PATH = ['/users/kthomas1/pelican-plugins']
PLUGINS = ['render_math']

# theme
THEME = "/users/kthomas1/pelican-themes/Flex"
