from django.conf.urls import patterns, url
from blogengine.views import CategoryListView, TagListView, PostsFeed, BaseView, SingleView

urlpatterns = patterns('',
    # Index
    url(r'^(?P<page>\d+)?/?$', BaseView.as_view(),
        name='home'),

    # Individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', SingleView.as_view()),

    # Categories
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryListView.as_view()),

    # Tags
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagListView.as_view()),

    # Post RSS feed
    url(r'^feeds/posts/$', PostsFeed()),

)