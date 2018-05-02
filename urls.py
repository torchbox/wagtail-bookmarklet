from __future__ import absolute_import, unicode_literals
from wagtailbookmarklet.views import bookmarklet, bookmarklet_redirect

try:
    from django.urls import re_path
except ImportError:  # fallback for Django <2.0
    from django.conf.urls import url as re_path

urlpatterns = [
    re_path(r'^$', bookmarklet, name='bookmarklet'),
    re_path(r'^redirect$', bookmarklet_redirect, name='bookmarklet_redirect'),
]