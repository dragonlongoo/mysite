import views
from django.conf.urls import url, include
from haystack import urls
urlpatterns = [
    url(r'^index/$', views.show_home_page, name="board_index"),
    url(
        r'^article/(?P<notificationid>\d+)/$',
        views.view_or_handle_notification,
        name="notification"
        ),
    # url(r'^category/$', views)
    url(
        r'^category/(?P<categoryid>\d+)/$',
        views.view_or_handle_notification,
        name="notification_category"
        ),
    url(
        r'^article/(?P<notificationid>\d+)/edit/$',
        views.edit_notification,
        name="notification_edit"
        ),
    url(r'^create/$', views.create_notification, name="notification_create"),
    # url(r'^search/$', include('haystack.urls'), name="n_search"),
    url(r'^test/$', views.test, name="test"),
]