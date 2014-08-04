from django.conf.urls import patterns, url
from blogengine.views import CategoryListView, TagListView, PostsFeed, BaseView, SingleView

urlpatterns = patterns('',
    # Index
    url(
        regex=r'^(?P<page>\d+)?/?$',
        view=BaseView.as_view(),
        name='home'),

    # Individual posts
    url(
        regex=r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
        view=SingleView.as_view()),

    # Categories
    url(
        regex=r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$',
        view=CategoryListView.as_view()),

    # Tags
    url(
        regex=r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$',
        view=TagListView.as_view()),

    # Post RSS feed
    url(
        regex=r'^feeds/posts/$',
        view=PostsFeed()),

)