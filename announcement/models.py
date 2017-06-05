#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from user.models import Department
import mistune

# Create your models here.

class Category(models.Model):
    category_code = models.CharField(max_length=8)
    category_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_name

class Notification(models.Model):
    class Meta:
        verbose_name = "公告"
        verbose_name_plural = "公告"
    title = models.CharField(max_length=128)
    category_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.IntegerField()
    outdated = models.BooleanField(default=False)
    content = models.TextField()
    content_html = models.TextField(null=True)
    image = models.FileField(null=True, blank=True)
    department_id = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title

    def get_category(self):
        """获取文章目录"""
        return Category.objects.get(id=self.category_id)

    def get_author(self):
        """获取作者"""
        return User.objects.get(id=self.created_by)

    def get_department(self):
        """获取发表部门"""
        return Department.objects.get(id=self.department_id)

    def get_absolute_url(self):
        return "/board/article/%d" % self.id
    
    def save(self):
        markdown = mistune.Markdown()
        self.content_html = markdown(self.content)
        super(Notification, self).save()