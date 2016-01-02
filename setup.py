"""Python Tools.

This is a meta-package providing an easy way to initialize a python
distribution to have the tools I commonly use.

**Source:**
  https://bitbucket.org/mforbes/python_setup
**Issues:**
  https://bitbucket.org/mforbes/python_setup/issues
"""
import os.path
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as original_test

NAME = "mmf_setup"

install_requires = []

test_requires = []

# Get the long description from the README.rst file
_HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_HERE, 'README.rst')) as _f:
    LONG_DESCRIPTION = _f.read()


setup(name=NAME,
      version='0.1.0',
      packages=find_packages(exclude=['tests']),

      install_requires=install_requires,
      tests_require=test_requires,
      extras_require={},
      setup_requires=[],

      # Metadata
      author='Michael McNeil Forbes',
      author_email='michael.forbes+bitbucket@gmail.com',
      url='https://bitbucket.org/mforbes/python_setup',
      description="Python Tools",
      long_description=LONG_DESCRIPTION,

      license='GPL',

      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ],

      keywords='ipython jupyter notebook setup',
      )