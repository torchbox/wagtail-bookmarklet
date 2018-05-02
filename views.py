# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import Http404

try:
    from wagtail.core.sites import get_site_for_hostname
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailcore.sites import get_site_for_hostname

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

def bookmarklet(request):
    return render(request, 'wagtailbookmarklet/bookmarklet.html', {
        'BASE_URL': settings.BASE_URL
    })

def bookmarklet_redirect(request):
    url = request.GET['url']
    parsed_url = urlparse(url)
    host = parsed_url.hostname
    port = parsed_url.port or 80
    site = get_site_for_hostname(host, port)
    path = parsed_url.path
    path_components = [component for component in path.split('/') if component]
    try:
        page, args, kwargs = site.root_page.specific.route(request, path_components)
    except Http404:
        return redirect(url)
    edit_url = "/admin/pages/%s/edit/" % page.id
    return redirect(edit_url)