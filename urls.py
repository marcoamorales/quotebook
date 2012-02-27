__author__ = 'marco'
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^quotebooks/(?P<user>\w+)/$', 'quotebook.views.quotebooks', name='quotebooks'),
    url(r'^quotebooks/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'quotebook.views.book', name='book'),
#    url(r'^quotebooks/(?P<user>[-/w]+)/(?P<slug>[-\w]+', )
    url(r'^quotebooks/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/addquote/$', 'quotebook.views.add_quote', name='add_quote'),
)