#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    category_code = models.CharField(max_length=8)
    category_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_name

class Notification(models.Model):
    title = models.CharField(max_length=128)
    category_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.IntegerField()
    outdated = models.BooleanField(default=False)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def get_category(self):
        return Category.objects.get(id=self.category_id)
    
    def get_author(self):
        return User.objects.get(id=self.created_by)

    def get_absolute_url(self):
        return "/board/article/%d" % self.id