from django.conf.urls import patterns, include, url
from health_project import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls
from django.http import HttpResponseRedirect
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponseRedirect('/home/index')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'home/',include('diseaseinfo.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    (r'^admin/lookups/', include(ajax_select_urls)),
)
if settings.DEBUG :
   urlpatterns += patterns("django.views",
       url(r'^stat(?P<path>.*)/$',"static.serve", {"document_root": settings.MEDIA_ROOT,}),
       url(r'^static(?P<path>.*)/$',"static.serve", {"document_root": settings.STATIC_ROOT,})
   )