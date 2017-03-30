#coding:utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Post_Form
from .models import Tutorial, Chapter, Section
# Create your views here.

@login_required
def get_home_page(request):
    return render(request, "wiki_home_page.html")

@login_required
def get_tutorial(request, category=None):
    _tutorial = Tutorial.objects.get(category=category)
    _chapters = Chapter.objects.filter(tutorial=_tutorial)
    context = {
        "chapters": _chapters,
        "tutorial": _tutorial
    }
    return render(request, "tutorial_page.html", context)

@login_required
def get_chapter(request, category, id):
    _tutorial = Tutorial.objects.get(category=category)
    _chapter = Chapter.objects.get(tutorial=_tutorial, id=id)
    _chapters = Chapter.objects.filter(tutorial=_tutorial)
    _sections = Section.objects.filter(chapter=_chapter)
    context = {
        "tutorial": _tutorial,
        "chapters": _chapters,
        "chapter": _chapter,
        "sections": _sections
    }
    return render(request, "chapter_page.html", context)

@login_required
def create_chapter(request, category=None):
    if request.user.is_authenticated():
        _tutorial = Tutorial.objects.get(category=category)
        _postform = Post_Form(request.POST or None)
        if request.method == "POST" and _postform.is_valid():
            _subject = _postform.cleaned_data["subject"]
            _content = _postform.cleaned_data["content"]
            new_chapter = Chapter(tutorial=_tutorial, subject=_subject, content=_content)
            new_chapter.save()
            return HttpResponseRedirect(new_chapter.get_absolute_url())
        else:
            blank_postform = Post_Form
            context = {
                "form":blank_postform
            }
            return render(request, "wiki_post_page.html", context)
    else:
        return HttpResponse("请先登录")

@login_required
def edit_chapter(request, category=None, id=None):
    if request.user.is_authenticated():
        _tutorial = Tutorial.objects.get(category=category)
        _chapter = Chapter.objects.get(tutorial=_tutorial, id=id)
        _postform = Post_Form(request.POST or None, instance=_chapter)
        if request.method == "POST" and _postform.is_valid():
            _chapter._subject = _postform.cleaned_data["subject"]
            _chapter._content = _postform.cleaned_data["content"]
            _chapter.save()
            return HttpResponseRedirect(_chapter.get_absolute_url())
        else:
            context = {
                "form":_postform
                }
            return render(request, "wiki_post_page.html", context)
    else:
        return HttpResponse("请先登录")