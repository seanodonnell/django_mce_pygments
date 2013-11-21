from django.conf.urls.defaults import url, patterns 

urlpatterns = patterns('mce_pygments.views',
    url(r'^$', 'pygments', name='pygments'),
)
