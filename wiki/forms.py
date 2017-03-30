#coding:utf-8
from django import forms
from .models import *

class Post_Form(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            "subject",
            "content"
        ]

        widgets={
            "subject": forms.TextInput(attrs={"placeholder": "标题", "class": "form-control"}),
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