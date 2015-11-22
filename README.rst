=================
web.dispatch.meta
=================

    © 2015 Alice Bevan-McGregor and contributors.

..

    https://github.com/marrow/web.dispatch.meta

..

    |latestversion| |downloads| |masterstatus| |mastercover| |issuecount|



Introduction
============

Dispatch is the process of taking some starting point and a path, then resolving the object that path refers to. This
process is common to almost every web application framework (transforming URLs into controllers), RPC system, and even
filesystem shell. Other terms for this process include: "traversal", "routing", or "lookup".




This package speaks a standardized `dispatch protocol <https://github.com/marrow/WebCore/wiki/Dispatch-Protocol>`_ and
is not entirely intended for direct use by most developers. The target audience is instead the authors of frameworks
that may require such modular dispatch for use by their own users.


Installation
============

Installing ``web.dispatch.meta`` is easy, just execute the following in a terminal::

    pip install web.dispatch.meta

**Note:** We *strongly* recommend always using a container, virtualization, or sandboxing environment of some kind when
developing using Python; installing things system-wide is yucky (for a variety of reasons) nine times out of ten.  We
prefer light-weight `virtualenv <https://virtualenv.pypa.io/en/latest/virtualenv.html>`_, others prefer solutions as
robust as `Vagrant <http://www.vagrantup.com>`_.

If you add ``web.dispatch.meta`` to the ``install_requires`` argument of the call to ``setup()`` in your
application's ``setup.py`` file, this dispatcher will be automatically installed and made available when your own
application or library is installed.  We recommend using "less than" version numbers to ensure there are no
unintentional side-effects when updating.  Use ``web.dispatch.meta<1.1`` to get all bugfixes for the current release,
and ``web.dispatch.meta<2.0`` to get bugfixes and feature updates while ensuring that large breaking changes are not
installed.


Development Version
-------------------

    |developstatus| |developcover|

Development takes place on `GitHub <https://github.com/>`_ in the 
`web.dispatch.meta <https://github.com/marrow/web.dispatch.meta/>`_ project.  Issue tracking, documentation, and
downloads are provided there.

Installing the current development version requires `Git <http://git-scm.com/>`_, a distributed source code management
system.  If you have Git you can run the following to download and *link* the development version into your Python
runtime::

    git clone https://github.com/marrow/web.dispatch.meta.git
    (cd web.dispatch.meta; python setup.py develop)

You can then upgrade to the latest version at any time::

    (cd web.dispatch.meta; git pull; python setup.py develop)

If you would like to make changes and contribute them back to the project, fork the GitHub project, make your changes,
and submit a pull request.  This process is beyond the scope of this documentation; for more information see
`GitHub's documentation <http://help.github.com/>`_.


Usage
=====




Version History
===============

Version 1.0
-----------

* Initial extract from WebCore 2.


License
=======

web.dispatch.meta has been released under the MIT Open Source license.

The MIT License
---------------

Copyright © 2015 Alice Bevan-McGregor and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


.. |masterstatus| image:: http://img.shields.io/travis/marrow/web.dispatch.meta/master.svg?style=flat
    :target: https://travis-ci.org/marrow/web.dispatch.meta
    :alt: Release Build Status

.. |developstatus| image:: http://img.shields.io/travis/marrow/web.dispatch.meta/develop.svg?style=flat
    :target: https://travis-ci.org/marrow/web.dispatch.meta
    :alt: Development Build Status

.. |latestversion| image:: http://img.shields.io/pypi/v/web.dispatch.meta.svg?style=flat
    :target: https://pypi.python.org/pypi/web.dispatch.meta
    :alt: Latest Version

.. |downloads| image:: http://img.shields.io/pypi/dw/web.dispatch.meta.svg?style=flat
    :target: https://pypi.python.org/pypi/web.dispatch.meta
    :alt: Downloads per Week

.. |mastercover| image:: http://img.shields.io/coveralls/marrow/web.dispatch.meta/master.svg?style=flat
    :target: https://travis-ci.org/marrow/web.dispatch.meta
    :alt: Release Test Coverage

.. |developcover| image:: http://img.shields.io/coveralls/marrow/web.dispatch.meta/develop.svg?style=flat
    :target: https://travis-ci.org/marrow/web.dispatch.meta
    :alt: Development Test Coverage

.. |issuecount| image:: http://img.shields.io/github/issues/marrow/web.dispatch.meta.svg?style=flat
    :target: https://github.com/marrow/web.dispatch.meta/issues
    :alt: Github Issues

.. |cake| image:: http://img.shields.io/badge/cake-lie-1b87fb.svg?style=flat
