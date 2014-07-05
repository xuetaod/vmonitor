from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vmonitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': './media'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('website.urls')),
)
