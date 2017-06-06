#coding:utf-8
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import *
from .forms import *
from mysite import settings
# Create your views here.

def show_home_page(request):
    _role = None
    _notifications = Notification.objects.all()
    _user = None
    if request.user.is_authenticated():
        _role = request.user.subscriber.role
        _user = request.user
    context = {
        "notifications": _notifications,
        "role": _role,
        "user": _user
        }
    return render(request, "article_list.html", context)

def show_notifications(request, notification=None, notifications=None, category=None):
    _editable = False
    _role = None
    _user = None
    if request.user.is_authenticated():
        _role = request.user.subscriber.role
        _user = request.user
    if notification:
        if request.user.id == notification.created_by:
            _editable = True
            context = {
                # "notifications": notifications,
                "notification": notification,
                "editable": _editable,
                "role": _role,
                "user": _user
            }
            return render(request, "article.html", context)
        else:
            context = {
                "notifications": notifications,
                "notification": notification,
                "role": _role,
                "user": _user
            }
            return render(request, "article.html", context)
    else:
        context = {
            "category": category,
            "notifications": notifications,
            "role": _role,
            "user": _user
        }
        return render(request, "article_list.html", context)


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
                image=image,
                department_id=request.user.subscriber.department.id
            )
            notification.save()
            return HttpResponseRedirect(notification.get_absolute_url())
        else:
            blank_postform = PostForm
            context = {
                "form":blank_postform
            }
            return render(request, "article_post.html", context)
    else:
        return HttpResponse("请先登录")


def edit_notification(request, notificationid=None):
    _notification = get_object_or_404(Notification, id=notificationid)
    _postform = PostForm(request.POST or None, request.FILES or None, instance=_notification)
    if request.method == "POST" and _postform.is_valid():
        instance = _postform.save(commit=False)
        instance.save()
        return HttpResponseRedirect(_notification.get_absolute_url())
        # return HttpResponseRedirect(instance.get_absolute_url())
    else:
        context = {
            "form": _postform
        }
        return render(request, "article_post.html", context=context)


def view_or_handle_notification(request, notificationid=None, categoryid=None):
    _notification = None
    _notifications = None
    #查看单篇文章且未登录
    if notificationid and not request.user.is_authenticated():
        _notification = get_object_or_404(Notification, id=int(notificationid))
        #文章目录ID=8为部门私有文章，未登录不允许查看
        if _notification.category_id == 7:
            context = {
                "categoryid": _notification.category_id
            }
            return render(request, "error.html", context=context)
        #文章目录ID为9为个人私有文章，未登录不允许查看
        elif _notification.category_id == 8:
            context = {
                "categoryid": _notification.category_id
            }
            return render(request, "error.html", context=context)
        #公共文章
        else:
            # _notifications = Notification.objects.filter(category_id=_notification.category_id)
            return show_notifications(request, notification=_notification, notifications=_notifications)
    # 查看单篇文章且用户已登录
    elif notificationid and request.user.is_authenticated():
        _notification = get_object_or_404(Notification, id=int(notificationid))
        #文章目录ID=8为部门私有文章，非作者部门成员不允许查看
        if _notification.category_id == 7:
            if _notification.get_department() != request.user.subscriber.department:
                context = {
                    "categoryid": _notification.category_id
                }
                return render(request, "error.html", context=context)
            else:
                return show_notifications(request, notification=_notification, notifications=_notifications)
        #文章目录ID=9为个人私有文章，非作者不允许查看
        elif _notification.category_id == 8:
            if _notification.get_author() != request.user:
                context = {
                    "categoryid": _notification.category_id
                }
                return render(request, "error.html", context=context)
            else:
                return show_notifications(request, notification=_notification, notifications=_notifications)
        else:
            #公共文章
            return show_notifications(request, notification=_notification, notifications=_notifications)
    #查看目录且未登录
    elif categoryid and not request.user.is_authenticated():
        _category = Category.objects.get(id=categoryid)
        #文章目录ID=8为部门私有目录，未登录不允许查看
        if int(categoryid) == 7:
            context = {
                "categoryid": _notification.category_id
            }
            return render(request, "error.html", context=context)
        #文章目录ID为9为个人私有目录，未登录不允许查看
        elif int(categoryid) == 8:
            context = {
                "categoryid": _notification.category_id
            }
            return render(request, "error.html", context=context)
        else:
            print "line 163"
            _notifications = Notification.objects.filter(category_id=int(categoryid))
            return show_notifications(request, notifications=_notifications, category=_category)
    #查看目录且用户已登录
    elif categoryid and request.user.is_authenticated():
        _category = Category.objects.get(id=int(categoryid))
        if int(categoryid) == 7:
            _notifications = Notification.objects.filter(
                category_id=int(categoryid), department_id=request.user.subscriber.department_id)
            return show_notifications(request, notifications=_notifications, category=_category)
        elif int(categoryid) == 8:
            _notifications = Notification.objects.filter(
                category_id=categoryid, created_by=request.user.id)
            return show_notifications(request, notifications=_notifications, category=_category)
        else:
            _notifications = Notification.objects.filter(category_id=int(categoryid))
            return show_notifications(request, notifications=_notifications, category=_category)
    else:
        context = {
            "message":"未在文章或目录"
        }
        return render(request, "error.html", context=context)