#coding:utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import loginForm, registerForm

def user_landing(request):
    if request.user.is_authenticated():
        if request.user.username == "admin":
            return HttpResponseRedirect(reverse("admin_page"))
        else:
            # return HttpResponseRedirect(reverse("user_page"))
            return HttpResponseRedirect(reverse("board_index"))
    else:
        return HttpResponseRedirect(reverse("login"))

def get_home_page(request):
    return render(request, "user_home_page.html")