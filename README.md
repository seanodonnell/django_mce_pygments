# django_mce_pygments

## Description

[Django](http://www.djangoproject.com) app and [tinymce](http://www.tinymce.com/) extension that allows you to insert syntax highlighted sourcecode. It is configured to work by default with a [Mezzanine](https://github.com/stephenmcd/mezzanine) installation. Syntax highlighting is provided by [pygments](http://pygments.org/). You can adjust line numbering, highlighted ranges, styles and every language your version of pygments supports is selectable. You can optionally select to have a link to download the unformatted source code inserted, in which case a text file containing the source is saved to your server. The default paths for tinymce and jquery are designed for a mezzanine installation, but can be customized in settings.py.

This project is based on https://github.com/fruitschen/django_mce_pygments

## Screenshots
![alt text](https://github.com/seanodonnell/django_mce_pygments/master/screenshots/django_mce_pygments_1.png "Logo Title Text 1")

The pygments icon in tinymce:

![The pygments icon](https://raw.github.com/seanodonnell/django_mce_pygments/master/screenshots/django_mce_pygments_1.png)

The dialog:

![The Dialog](https://raw.github.com/seanodonnell/django_mce_pygments/master/screenshots/django_mce_pygments_2.png)

The preview tab:

![The Preview Tab](https://raw.github.com/seanodonnell/django_mce_pygments/master/screenshots/django_mce_pygments_3.png)

The inserted source with download link:

![The inserted source with download link](https://raw.github.com/seanodonnell/django_mce_pygments/master/screenshots/django_mce_pygments_4.png)

## Requirements

[pygments](http://pygments.org/)
it is assumed you are using django.contril.staticfiles (https://docs.djangoproject.com/en/dev/howto/static-files/) to manage static media
File path defaults assume a [Mezzanine](https://github.com/stephenmcd/mezzanine) installation but this can be easily overridden in your settings.py

## INSTALLATION

Place the app on your python path
Add django_mce_pygments to your INSTALLED APPS
Check that the paths below for jquery and tinymce are correct, and override
in your settings file if neccessary
Make sure the SOURCE_CODE_FILE_DIR exists and is writable

## Configuration

The following can be set in your settings.py. All are optional, but the first two probably need adjustment if you are not using Mezzanine.

'''MCE_POPUP_LOCATION''' - The location of your tiny_mce_popup.js file, defaults to  'grappelli/tinymce/jscripts/tiny_mce/tiny_mce_popup.js'. This assumes you are using static files, so this url will be passed through the static template tag, and probably resolve to /staticgrappelli/tinymce/jscripts/tiny_mce/tiny_mce_popup.js.

'''JQUERY_LOCATION''' - The location of your jquery library. Defaults to 'mezzanine/js/jquery-1.7.1.min.js'. This assumes you are using static files, so this url will be passed through the static template tag, and probably resolve to /static/mezzanine/js/jquery-1.7.1.min.js 

'''MCE_DEFAULT_LEXERS''' - Languages in this list will be the first in the dropdown in the pygments dialog to save you time hunting. Defaults to an empty list, an example would be:

    MCE_DEFAULT_LEXERS = ['Python', 'Javascript']
 
'''MCE_DEFAULT_STYLE''' - The default style to have selected in the pygments dialog. This defaults to None. An example of its use:

    MCE_DEFAULT_STYLE = 'pastie'

'''SOURCE_CODE_FILE_DIR''' - The location to store raw source code files used for lines.  The default is static/source, make sure it exists and is writable.

The template pygments/source_link.html can be overridden or customized to change how the download link for source code is presented.

## AUTHORS
[seanodonnell](https://github.com/seanodonnell/)
[fruitschen](https://github.com/fruitschen/)

