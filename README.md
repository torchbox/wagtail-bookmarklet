# Wagtail Bookmarklet

This simple app gives Wagtail editors an 'edit this page' bookmarklet, for scenarios where the [User Bar](http://docs.wagtail.io/en/stable/topics/writing_templates.html#wagtail-user-bar) isn't available, e.g. when the site has been statically generated.

## Installation

1. `pip install wagtailbookmarklet`
2. Add `'wagtailbookmarklet'` to your `INSTALLED_APPS`
3. Check `BASE_URL` is correctly configured in settings.

## Usage

Go to 'Bookmarklet' in the Wagtail admin settings menu. Drag the link to your bookmarks bar.

![Screencast demo](https://tom.s3.amazonaws.com/wagtail-edit-bookmarklet.gif)
