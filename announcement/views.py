#coding:utf-8
from django.shortcuts import render,HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import *
from .forms import *
from mysite import settings
# Create your views here.

def show_home_page(request):
    if request.user.is_authenticated():
        _notifications = Notification.objects.all()
        _role = request.user.subscriber.role
        context = {
                "notifications": _notifications,
                "role": _role
            }
        return render(request, "board_home_page.html", context)
    else:
        return HttpResponse("请先登录")

def show_notifications(request, notification=None, notifications=None):
    _editable = False
    _role = request.user.subscriber.role
    if notification:
        if request.user.id == notification.created_by:
            _editable = True
            context = {
                "notifications": notifications,
                "notification": notification,
                "editable": _editable,
                "role": _role
            }
            return render(request, "notification_page.html", context)
        else:
            context = {
                "notifications": notifications,
                "notification": notification,
                "role": _role
            }
            return render(request, "notification_page.html", context)
    else:
        context = {
            "notifications": notifications,
            "role": _role
        }
        return render(request, "board_home_page.html", context)


def create_notification(request):
    if request.user.is_authenticated():
        postform = PostForm(request.POST or None, request.FILES or None)
        if request.method == "POST" and postform.is_valid():
            image = postform.cleaned_data["image"]
            category_id = postform.cleaned_data["category_id"]
            title = postform.cleaned_data["title"]
            content = postform.cleaned_data["content"]
            notification = Notification(
                category_id=category_id,
                created_by=request.user.id,
                content=content,
                title=title,
                image=image
            )
            notification.save()
            return HttpResponseRedirect(notification.get_absolute_url())
        else:
            blank_postform = PostForm
            context = {
                "form":blank_postform
            }
            return render(request, "handle_notification.html", context)
    else:
        return HttpResponse("请先登录")


def edit_notification(request, notificationid=None):
    _notification = get_object_or_404(Notification, id=notificationid)
    _postform = PostForm(request.POST or None, instance=_notification)
    if request.method == "POST" and _postform.is_valid():
        if _postform.is_valid():
            instance = _postform.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            return HttpResponse("failed")
    else:
        context = {
            "form": _postform
        }
        return render(request, "handle_notification.html", context=context)


def view_or_handle_notification(request, notificationid=None, categoryid=None):
    if request.user.is_authenticated():
        if notificationid:
            _notification = get_object_or_404(Notification, id=notificationid)
            _notifications = Notification.objects.filter(category_id=_notification.category_id)
            return show_notifications(request, notification=_notification, notifications=_notifications)
        elif categoryid:
            # _category = Category.objects.get(id=categoryid)
            _notifications = Notification.objects.filter(category_id=categoryid)
            return show_notifications(request, notifications=_notifications)
        else:
            return create_notification(request)
    else:
        return HttpResponse("请先登录")
