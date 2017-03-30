 #coding:utf-8
from django import forms
from django.contrib.auth  import authenticate

class loginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)

    def clean(self, *args, **kwargs):
        un = self.cleaned_data.get("username")
        pw = self.cleaned_data.get("password")
        user = authenticate(username=un, password=pw)
        if not user:
            raise forms.ValidationError("用户不存在")
        if not user.check_password(pw):
            raise forms.ValidationError("密码错误")
        if not user.is_active:
            raise forms.ValidationError("用户未激活")
        return super(loginForm, self).clean(*args, **kwargs)

class registerForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=128)

