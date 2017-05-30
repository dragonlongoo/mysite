from django.conf.urls import *
from haystack import urls
import views

urlpatterns = [
    url(r'^index/$', views.get_home_page, name="wiki_index"),
    url(r'^(?P<category>\w+)/post/$', views.create_chapter, name="wiki_post"),
    url(r'^(?P<category>\w+)/chapter/(?P<id>\d+)/edit/$', views.edit_chapter, name="wiki_edit"),
    url(r'^(?P<category>\w+)/$', views.get_tutorial, name="category"),
    url(r'^(?P<category>\w+)/chapter/(?P<id>\d+)/$', views.get_chapter, name="chapter"),
    # url(r'^search/$', include('haystack.urls'), name="c_search"),
]