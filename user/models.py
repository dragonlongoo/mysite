#coding:utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Privilege(models.Model):
    """权限"""
    privilege_code = models.CharField(max_length=8)
    privilege_name = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    """角色"""
    role_code = models.CharField(max_length=8)
    role_name = models.CharField(max_length=16)
    #privileges = models.ManyToManyField(Privilege)
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.role_name

class Department(models.Model):
    """部门"""
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
    #privileges = models.CharField(max_length=32, null=True)
    role = models.CharField(max_length=32, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.set_password(new_password)
    def config_user(self, *args, **kwargs):
        pass
    def get_role(self):
        role = Role.objects.get(role_code=self.role)
        return role
    