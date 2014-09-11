import factory
from blogengine.models import Post, Category, Tag
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = (
            'username',
            'email',
            'password'
        )

    username = 'testuser'
    email = 'user@example.com'
    password = 'password'


class SiteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Site
        django_get_or_create = (
            'name',
            'domain'
        )

    name = 'example.com'
    domain = 'example.com'


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = (
            'name',
            'description',
            'slug'
        )

    name = 'python'
    description = 'The Python programming language'
    slug = slugify(name)


class TagFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = (
            'name',
            'description',
            'slug'
        )

    name = 'python'
    description = 'The Python programming language'
    slug = slugify(name)


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = (
            'title',
            'pub_date',
            'text'
        )

    title = 'My first post'
    slug = slugify(title)
    pub_date = timezone.now()
    text = 'This is my first blog post'
    author = factory.SubFactory(AuthorFactory)
    site = factory.SubFactory(SiteFactory)
    category = factory.SubFactory(CategoryFactory)
