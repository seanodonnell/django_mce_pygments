from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from pygments import highlight
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

def pygments(request, template_name="pygments/pygments.html"):
    if request.method == "POST":
        lang = request.POST.get('lang', 'python')
        style = request.POST.get('style', 'default')
        code = request.POST.get('code', '')
        linenos = request.POST.get('linenos', False)
        linenostart = int(request.POST.get('linenostart', 1))
        highlight_lines = request.POST.get('highlight', '').split(',')
        if linenos == 'true':
            linenos = 'inline'
        else:
            linenos = False
             
        code = highlight(code, get_lexer_by_name(lang),
                            HtmlFormatter(
                                cssclass="pygments pygments_%s" % lang,
                                full=False, style=style, noclasses=True,
                                linenos=linenos,
				linenostart=linenostart,
                                hl_lines=highlight_lines),
                            )
        return HttpResponse(code)
    else:
        styles = list(get_all_styles())
        styles.sort()
        
        langs = [(l[0].strip(), l[1][0].strip()) for l in get_all_lexers()]
        langs.sort()
        
        default_lexers = settings.MCE_DEFAULT_LEXERS
        
	for index, lexer in enumerate(default_lexers):
        	for lang in langs:
                    if lang[0] == lexer:
			langs.remove(lang)
			default_lexers[index] = lang

        langs = default_lexers + langs

        default_style = settings.MCE_DEFAULT_STYLE
        styles.insert(0, styles.pop(styles.index(default_style)))

        context = {"styles": styles, "langs": langs,}
        return render_to_response(template_name, context,
                                   context_instance=RequestContext(request))
