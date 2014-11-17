import datetime
from haystack import indexes
from blogengine.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='author')
    pub_date = indexes.CharField(model_attr='pub_date')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        '''return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())'''
        return self.get_model().objects.all()