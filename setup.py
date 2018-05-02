#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='wagtailbookmarklet',
    version='0.1.2',
    description="Gives Wagtail editors an 'edit this page' bookmarklet",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/torchbox/wagtail-bookmarklet',
    author='Tom Dyson',
    author_email='tom+wagtailbookmarklet@torchbox.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "wagtail>=1.12"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
)
