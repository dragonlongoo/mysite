 #coding:utf-8
from django import forms
from django.forms import ModelChoiceField, Form
from .models import *

class Jianmian_Order_Form(forms.ModelForm):
    class Meta:
        model = Jianmian_Order
        fields = [
            "order_description",
            "approved_by",
            "image"
        ]
        widgets={
            'order_description': forms.Textarea(attrs={"class": "form-control", "rows": "5"}),
            "approved_by": forms.TextInput(attrs={"class": "form-control"}),
            }


class Order_Handle_Form(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "3", "placeholder": "请填写意见"})
        )
    related_order = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    x_integration_num = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))