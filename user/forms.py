#coding:utf-8
from django.contrib.auth  import authenticate
from django import forms
from .models import Subscriber, Department

class Register_Form(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = [
            "username",
            "password",
            "email",
            "full_name",
            "department",
            "contact"
        ]
        labels = {
            "username": "用户名",
            "password": "密码",
            "email": "邮箱",
            "full_name": "姓名",
            "department": "部门",
            "contact": "手机号码"
        }
        help_texts = {
            'username': None,
        }
        widgets = {
            'password': forms.PasswordInput(
                attrs={"class": "form-control", "label": "密码"}
                ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "label": "用户名"}
                ),
            "department": forms.Select(attrs={
                "class": "form-control selectpicker", "id": "", "data-live-search": "true", "label": "部门"
                }),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "label": "email"}
                ),
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "label": "姓名"}
                ),
            "contact": forms.TextInput(
                attrs={"class": "form-control", "label": "手机号码"}
                )
            }


class Login_Form(forms.Form):
    username = forms.CharField(max_length=32, label="用户名")
    password = forms.CharField(widget=forms.PasswordInput, label="密码")

    # def clean(self, *args, **kwargs):
    #     un = self.cleaned_data.get("username")
    #     pw = self.cleaned_data.get("password")
    #     user = authenticate(username=un, password=pw)
    #     if not user:
    #         raise forms.ValidationError("用户不存在")
    #     if not user.check_password(pw):
    #         raise forms.ValidationError("密码错误")
    #     if not user.is_active:
    #         raise forms.ValidationError("用户未激活")
    #     return super(login_form, self).clean(*args, **kwargs)