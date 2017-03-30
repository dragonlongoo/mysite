#coding:utf-8
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    #部署时将category_id的定义注释掉
    category_id = forms.ChoiceField(
     choices=[(c.id, c.category_name) for c in Category.objects.all()]
    )
    class Meta:
        model = Notification
        fields = [
            "title",
            "content",
            "category_id",
            "image"
        ]
        widgets={
            "category_id": forms.Select(attrs={'class': 'form-control'}),
            "title": forms.TextInput(attrs={"placeholder": "标题", "class": "form-control"}),
            "content": forms.Textarea(
                attrs={
                    "name": "content",
                    "data-provide": "markdown",
                    "data-iconlibrary": "fa",
                    "rows": "10",
                    "id": "editor"
                    }
                )
            }
