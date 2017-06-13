#coding:utf-8
from django import forms
from .models import *
from pagedown.widgets import PagedownWidget
from haystack.forms import ModelSearchForm


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
            "attachment"
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
                ),
            # "content": PagedownWidget(),
            # "content": PagedownWidget(attrs={"template": "default.html"}),
            # "image": forms.ClearableFileInput(
            #     attrs={
            #         "multiple": True
            #     }
            # )
            }

CUSTOM_CHOICES = (
    ('annnoucement.Notification', '公告'),
    ('wiki.Chapter', '业务知识'),
)


class CustomModelSearchForm(ModelSearchForm):
    def __init__(self, *args, **kwargs):
        super(CustomModelSearchForm, self).__init__(*args, **kwargs)
        self.fields['models'] = forms.MultipleChoiceField(
            choices=CUSTOM_CHOICES,
            required=False,
            label=('选择搜索范围'),
            widget=forms.CheckboxSelectMultiple
            )