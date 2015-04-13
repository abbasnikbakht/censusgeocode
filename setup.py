#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of censusgeocode.
# https://github.com/fitnr/censusgeocode

# Licensed under the General Public License (version 3)
# http://opensource.org/licenses/LGPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup

setup(
    name='censusgeocode',
    version='0.1.0',
    description='Thin Python wrapper for the US Census Geocoder',
    long_description=open('readme.rst').read(),
    keywords='census geocode api',
    author='Neil Freeman',
    author_email='contact@fakeisthenewreal.org',
    url='https://github.com/fitnr/censusgeocode',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=['censusgeocode'],
    install_requires=[
        'poster'
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            # 'censusgeocode=censusgeocode.cli:main',
        ],
    },
)
