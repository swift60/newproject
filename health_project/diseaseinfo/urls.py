from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect

urlpatterns = patterns('diseaseinfo.views',
    url(r'^$', lambda x: HttpResponseRedirect('/home/index')),
    url(r'^index/$','search_disease', name='index'),
    url(r'^search_ajax/$','search_ajax'),
    url(r'^search/$', 'disease',name='search'),
)
