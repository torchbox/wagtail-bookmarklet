from django.conf import settings
from django.utils.translation import ugettext_lazy as _

try:
    from wagtail.core import hooks
    from wagtail.admin.menu import MenuItem
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailcore import hooks
    from wagtail.wagtailadmin.menu import MenuItem

try:
    from django.urls import re_path, include
except ImportError:  # fallback for Django <2.0
    from django.conf.urls import url as re_path
    from django.conf.urls import include

try:
    from django.urls import reverse
except ImportError:  # fallback for Django <1.9
    from django.core.urlresolvers import reverse

from . import urls
from . import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^bookmarklet/', include(urls)),
    ]

@hooks.register('register_settings_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Bookmarklet'),
        reverse('bookmarklet'),
        classnames='icon icon-link',
        order=1000
    )