#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

setup(
    name='reverse',
    version='0.1.0',
    description='Reverse a file',
    long_description='Reverse the content of a file, write into another file.',
    url='https://github.com/physacco/reverse',
    author='physacco',
    author_email='physacco@gmail.com',
    license='MIT',
    py_modules=['reverse'],
    entry_points={
        'console_scripts': [
            'reverse = reverse:main',
        ],
    },
)
