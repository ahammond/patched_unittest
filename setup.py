#!/usr/bin/env python

from distutils.core import setup

setup(name='patched_unittest',
      version='1.2',
      description='Automatically manage house-keeping for class level patching.',
      install_requires=['mock'],
      author='Andrew Hammond',
      author_email='andrew.george.hammond@gmail.com',
      url='https://github.com/ahammond/patched_unittest',
      py_modules=['patched_unittest'])