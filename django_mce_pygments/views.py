from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

def pygments(request, template_name="pygments/pygments.html"):
    if request.method == "POST":
        lang = request.POST.get('lang', 'python')
        code = request.POST.get('code', '')
        code = highlight(code, get_lexer_by_name(lang),
                            HtmlFormatter(
                                cssclass="pygments pygments_%s" % lang,
                                full=False, style="friendly", noclasses=True),
                            )
        return HttpResponse(code)
    else:
        return render_to_response(template_name, {},
                                   context_instance=RequestContext(request))
