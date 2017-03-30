#coding:utf-8
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import Register_Form, Login_Form
from .models import Subscriber

def user_register(request):
    register_form = Register_Form(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data["username"]
        email = register_form.cleaned_data["email"]
        password = register_form.cleaned_data["password"]
        full_name = register_form.cleaned_data["full_name"]
        department = register_form.cleaned_data["department"]
        contact = register_form.cleaned_data["contact"]
        subscriber = Subscriber(
            username=username,
            password=password,
            email=email,
            full_name=full_name,
            department=department,
            contact=contact
            )
        subscriber.save()
        subscriber.set_password(password)
        subscriber.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        context = {
            "register_form": register_form
            }
        return render(request, "user_register.html", context=context)

def user_login(request):
    login_form = Login_Form(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data["username"]
        password = login_form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.username == "admin":
                # ci入口不对admin开放
                return HttpResponse("admin请使用其他url登录")
            else:
                # 其他账号登录后进入普通界面
                return HttpResponseRedirect(reverse("user_page"))
        else:
            return HttpResponse("账号或密码错")
    else:
        print "not valid"
        context = {
            "loginform": login_form
        }
        return render(request, "user_login.html", context=context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))