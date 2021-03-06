from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogengine.models import Category, Post, Tag
from django.contrib.syndication.views import Feed
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

'''
class TitleSearchMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TitleSearchMixin, self).get_context_data(**kwargs)
        q = self.request.GET.get("q")
        if q:
            result = SearchQuerySet().filter(content=q)
            print 'el resultado es: ' + result
            context['post_list'] = result
            return context
            #return queryset.filter(title__icontains=q)
            #return SearchQuerySet().filter(content=q)
            #we need to check this cause it is not returning what expected
        return context
'''

class SideBarMixin(object):
    def get_context_data(self, **kwargs):
        context = super(SideBarMixin, self).get_context_data(**kwargs)
        context['categories'] = self.get_category_list()
        context['tags'] = self.get_tag_list()
        context['archives'] = self.get_archive_list()
        return context

    def get_category_list(self):
        cat_list = []
        for category in Category.objects.all():
            # count number of posts with the category
            count = category.post_set.all().count()
            # append dictionaries in a list
            cat_list.append({'name': category.name, 'count': count, 'url': category.get_absolute_url()})
        # returns a sorted list of dictionaries in reverse using 'count' as the sorting key
        return sorted(cat_list, key=lambda foo: foo['count'], reverse=True)

    def get_tag_list(self):
        tag_list = []
        for tag in Tag.objects.all():
            # count number of posts with the tag
            count = tag.post_set.all().count()
            # append dictionaries in a list
            tag_list.append({'name': tag.name, 'count': count, 'url': tag.get_absolute_url()})
        # returns a sorted list of dictionaries in reverse using 'count' as the sorting key
        return sorted(tag_list, key=lambda foo: foo['count'], reverse=True)

    def get_archive_list(self):
        archive_list = []
        for post in Post.objects.all().order_by('-pub_date'):
            archive_list.append({'title': post.title, 'year': post.pub_date.year,
                                 'month': post.pub_date.month, 'day': post.pub_date.day,
                                 'url': post.get_absolute_url()})
        return archive_list


class BaseView(SideBarMixin, ListView):
    model = Post
    paginate_by = 5


class SingleView(SideBarMixin, DetailView):
    model = Post
    paginate_by = 5


class CategoryListView(SideBarMixin, ListView):
    model = Category
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()


class TagListView(SideBarMixin, ListView):
    model = Tag
    paginate_by = 5

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


class AddPost(LoggedInMixin, CreateView):
    model = Post
    success_url = reverse_lazy('dashboard')


class UpdatePost(LoggedInMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('dashboard')


class DeletePost(LoggedInMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')


class DashBoardView(LoggedInMixin, ListView):
    model = Post
    template_name = 'blogengine/dashboard.html'