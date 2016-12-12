#!/usr/bin/env python

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kyle thomas'
SITENAME = u'cmd+build'
SITEURL = 'tkthomas27.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

BROWSER_COLOR = '#f4f9f9'
PYGMENTS_STYLE = 'native'
SITESUBTITLE = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
SOCIAL = (('github', 'https://github.com/tkthomas27'),
         ('linkedin', 'https://www.linkedin.com/in/timothy-thomas-6206134a'),
          ('twitter', 'https://twitter.com/tkylethomas27'),
         ('youtube', 'https://www.linkedin.com/in/timothy-thomas-6206134a'))

MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
            ('Tags', '/tags.html'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md','rmd')
#MD_EXTENSIONS = (['toc'])

#PLUGINS
PLUGIN_PATHS = ['/users/kthomas1/pelican-plugins']
PLUGINS = ['render_math','section_number','rmd_reader']

# theme
THEME = "/users/kthomas1/pelican-themes/Flex"
