from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.text import slugify
from datetime import datetime


class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Tag, self).save()

    def get_absolute_url(self):
        return "/tag/%s/" % (self.slug)

    def count_posts(self):
        return Post.objects.filter(tags__name=self.name).count()

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Category, self).save()

    def get_absolute_url(self):
        return "/category/%s/" % (self.slug)

    def __unicode__(self):
        return self.name

    def count_posts(self):
        return Post.objects.filter(category__name=self.name).count()

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(verbose_name='Post Title', max_length=200)
    pub_date = models.DateTimeField(verbose_name='Publication Date', default=datetime.now)
    text = models.TextField(verbose_name='Text')
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)
    site = models.ForeignKey(Site)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connexion = models.DateTimeField(verbose_name="Date of last connexion", null=True, default=None, blank=True)

    def __unicode__(self):
        return self.user_auth.username