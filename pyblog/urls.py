from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Haystack
    url(r'^search/', include('haystack.urls')),

    #Blog URLs
    url(r'', include('blogengine.urls', namespace="blogengine")),

    #FlatPages
    url(r'', include('django.contrib.flatpages.urls')),



)
