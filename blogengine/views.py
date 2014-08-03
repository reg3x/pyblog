from django.views.generic import ListView, DetailView
from blogengine.models import Category, Post, Tag
from django.contrib.syndication.views import Feed


class SideBarMixin(object):
    def get_context_data(self, **kwargs):
        context = super(SideBarMixin, self).get_context_data(**kwargs)
        context['categories'] = self.cat_list_sorted()
        context['tags'] = self.tag_list_sorted()
        context['archives'] = Post.objects.order_by('pub_date')[:3] #consider to put this on a method
        return context

    def cat_list_sorted(self):
        cat_list = []
        for category in Category.objects.all():
            # count number of posts with the category
            count = category.post_set.all().count()
            # append dictionaries in a list
            cat_list.append({'name': category.name, 'count': count, 'url': category.get_absolute_url()})
        # returns a sorted list of dictionaries in reverse using 'count' as the sorting key
        return sorted(cat_list, key=lambda foo: foo['count'], reverse=True)

    def tag_list_sorted(self):
        tag_list = []
        for tag in Tag.objects.all():
            # count number of posts with the tag
            count = tag.post_set.all().count()
            # append dictionaries in a list
            tag_list.append({'name': tag.name, 'count': count, 'url': tag.get_absolute_url()})
        # returns a sorted list of dictionaries in reverse using 'count' as the sorting key
        return sorted(tag_list, key=lambda foo: foo['count'], reverse=True)


class BaseView(SideBarMixin, ListView):
    model = Post
    paginate_by=5
    name='home'


class SingleView(SideBarMixin, DetailView):
    model = Post
    paginate_by=5


class CategoryListView(SideBarMixin, ListView):
    model = Category
    paginate_by=5

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()


class TagListView(SideBarMixin, ListView):
    model = Tag
    paginate_by=5

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()


class PostsFeed(Feed):
    title = "RSS feed - posts"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Post.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
