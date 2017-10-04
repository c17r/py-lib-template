import os
import sys
from importlib import import_module


_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SRC = os.path.join(_ROOT, 'src')


def make_readme(name, repo):
    readme = os.path.join(_ROOT, 'README.rst')
    with open(readme, 'w') as f:
        f.write('''.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |coveralls|
    * - package
      - |travis|

.. |travis| image:: https://travis-ci.org/{name}/{repo}.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/{name}/{repo}

.. |coveralls| image:: https://coveralls.io/repos/github/{name}/{repo}/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/repos/github/{name}/{repo}

.. end-badges
'''.format(name=name, repo=repo))
        for mod in _get_modules():
            f.write(mod.__doc__)
            f.write('')


def make_long_description():
    return '\n'.join((mod.__doc__ for mod in _get_modules()))


def _get_modules():
    folders = (f.name for f in os.scandir(_SRC) if f.is_dir() and 'egg-info' not in f.name)
    for mod in (import_module('src.' + folder) for folder in folders):
        yield mod


def _get_setup():
    sys.path.insert(0, _ROOT)
    mod = import_module('setup')
    return mod
