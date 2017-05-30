import datetime
from haystack import indexes
from announcement.models import Notification

class NotificationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content = indexes.CharField(model_attr='content')
    title = indexes.CharField(model_attr='title')
    created_date = indexes.DateTimeField(model_attr='created_date')

    def get_model(self):
        return Notification

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(created_date__lte=datetime.datetime.now())
        return self.get_model().objects.all()