#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='inkgrad',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Make gradients between 2 files unique",
    long_description="Make gradients between 2 files unique to overcome an annoying Inkscape bug.",
    scripts=['inkgrad'],
    data_files=[('share/man/man1', ['inkgrad.1'])],
)
