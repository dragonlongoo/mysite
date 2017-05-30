import datetime
from haystack import indexes
from wiki.models import Chapter

class NotificationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content = indexes.CharField(model_attr='content')
    subject = indexes.CharField(model_attr='subject')

    def get_model(self):
        return Chapter

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(created_date__lte=datetime.datetime.now())
        return self.get_model().objects.all()