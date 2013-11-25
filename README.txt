django app and tiny_mce extension to add syntax highlighted source code in tiny_mce

some settings you can define

MCE_DEFAULT_LEXERS - languages in this list will be the first in the dropdown 
MCE_DEFAULT_STYLE - the default style to have selected in the pygments dialog
SOURCE_CODE_FILE_DIR - the location to store raw source code used in blog posts
                       default is static/source, make sure it exists and is
                       writable

The template pygments/source_link.html can be overridden or customized to change how the download link for source code is presented.
