"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib import admin
from mysite import views
from announcement.views import show_home_page

urlpatterns = [
    # url(r'^$', views.user_landing, name="landing_page"),
    url(r'^$', show_home_page, name="board_index"),
    url(r'^admin/', admin.site.urls, name="admin_page"),
    url(r'^signin/', views.get_home_page, name="user_page"),
    url(r'^board/', include('announcement.urls')),
    url(r'^order/', include('audit.urls')),
    url(r'^wiki/', include('wiki.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^search/', include('haystack.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
