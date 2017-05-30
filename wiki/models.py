#coding:utf-8
from __future__ import unicode_literals
from django_mysql.models import ListCharField
from django.db import models

# Create your models here.

Choice = (
    ('JT', '集团4G'),
    ("ISALE", "爱销售"),
    ("CRM", "CRM"),
    ("JF", "计费"),
    ("ZY", "资源"),
    ("JH", "激活"),
    ("ITSM", "ITSM"),
    ("DICT", "数据字典")
)

class Content_Type(models.Model):
    type_code = models.CharField(max_length=32)
    type_name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.type_name

class Tutorial_Category(models.Model):
    category_code = models.CharField(max_length=32)
    category_name = models.CharField(max_length=32)
    category_content = models.TextField(null=True)
    def __unicode__(self):
        return self.category_name

class Tutorial(models.Model):
    subject = models.CharField(max_length=32)
    content = models.TextField()
    category = models.CharField(max_length=32)
    def __unicode__(self):
        return self.subject
    def get_absolute_url(self):
        return "/tutorial/%d" % self.id

class Chapter(models.Model):
    class Meta:
        verbose_name = "知识库"
        verbose_name_plural = "知识库"
    tutorial = models.ForeignKey(Tutorial)
    subject = models.CharField(max_length=32)
    content = models.TextField()
    chapter_index = models.IntegerField(null=True)
    def __unicode__(self):
        return self.subject
    def get_absolute_url(self):
        return "/wiki/%s/chapter/%d" % (self.tutorial.category, self.id)

class Section(models.Model):
    chapter = models.ForeignKey(Chapter)
    subject = models.CharField(max_length=32)
    content = models.TextField()
    section_index = models.IntegerField(null=True)
    def __unicode__(self):
        return self.subject
    def get_absolute_url(self):
        return "chapter/section/%d" % self.section_index