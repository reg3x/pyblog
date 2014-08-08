from django.conf.urls import patterns, url
from blogengine.views import CategoryListView, TagListView, PostsFeed, BaseView,\
    SingleView, AddPost, UpdatePost, DeletePost, DashBoardView

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

    # Log in
    url(
        regex=r'^login/$',
        view='django.contrib.auth.views.login'),

    # Log out
    url(
        regex=r'^logout/$',
        view='django.contrib.auth.views.logout'),

    # Dashboard
    url(
        regex=r'^dashboard/$',
        view=DashBoardView.as_view(),
        name='dashboard'),

    # Add Post
    url(
        regex=r'^post/add/$',
        view=AddPost.as_view(),
        name='addpost'),

    # Update Post
    url(
        regex=r'^post/update/(?P<slug>[a-zA-Z0-9-]+)?$',
        view=UpdatePost.as_view(),
        name='updatepost'),

    # Delete Post
    url(
        regex=r'^post/delete/(?P<slug>[a-zA-Z0-9-]+)?$',
        view=DeletePost.as_view(),
        name='deletepost'),

)