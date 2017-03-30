#coding:utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Privilege(models.Model):
    privilege_code = models.CharField(max_length=8)
    privilege_name = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    role_code = models.CharField(max_length=8)
    role_name = models.CharField(max_length=16)
    privileges = models.ManyToManyField(Privilege)
    created_date = models.DateTimeField(auto_now_add=True)

class Department(models.Model):
    department_name = models.CharField(max_length=32)
    area_code = models.CharField(max_length=32)
    area_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.department_name

class Subscriber(User):
    full_name = models.CharField(max_length=32, null=True)
    contact = models.CharField(max_length=32)
    department = models.ForeignKey(Department)
    is_expert = models.BooleanField(default=False)
    privileges = models.ManyToManyField(Privilege, null=True)
    roles = models.ManyToManyField(Role)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.set_password(new_password)
    def config_user(self, *args, **kwargs):
        pass