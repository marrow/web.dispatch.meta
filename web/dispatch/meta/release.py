# encoding: utf-8

"""Release information about WebCore."""

from __future__ import unicode_literals

from collections import namedtuple


version_info = namedtuple('version_info', ('major', 'minor', 'micro', 'releaselevel', 'serial'))(1, 0, 0, 'alpha', 1)
version = ".".join([str(i) for i in version_info[:3]]) + ((version_info.releaselevel[0] + str(version_info.serial)) if version_info.releaselevel != 'final' else '')

author = namedtuple('Author', ['name', 'email'])("Alice Bevan-McGregor", 'alice@gothcandy.com')
description = "A collection of common dispatch protocol middleware."
copyright = "2009-2015, Alice Bevan-McGregor and contributors"
url = 'https://docs.webcore.io/dispatch/meta'
