import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.order_index, name="order_index"),
    url(r'jianmian/(?P<id>\d+)/fetch/$', views.Fetch_Order, name="fetch_order"),
    url(r'^pending/$', views.List_Pending_Orders, name="order_pending"),
    url(r'^handling/$', views.List_Handling_Orders, name="order_feched"),
    url(r'^archived/$', views.List_Archived_Orders, name="order_archived"),
    url(r'^jianmian/(?P<id>\d+)/$', views.View_Or_Handle_Order, name="order_jianmian"),
    url(r'^jianmian/create/$', views.Create_Order, name="order_create"),
]