#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Order_State(models.Model):
    state_code = models.CharField(max_length=4)
    state_name = models.CharField(max_length=8)

    def __unicode__(self):
        return self.state_name

class Order_Type(models.Model):
    type_code = models.CharField(max_length=4)
    type_name = models.CharField(max_length=8)

class Order_Tache(models.Model):
    tache_code = models.CharField(max_length=4)
    tache_name = models.CharField(max_length=8)

class Order_Action(models.Model):
    action_type = models.CharField(max_length=4)
    action_name = models.CharField(max_length=8)

class Base_Order(models.Model):
    order_number = models.CharField(max_length=32)
    order_subject = models.CharField(max_length=32)
    order_type = models.CharField(max_length=4)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=32)
    current_tache = models.CharField(max_length=4)
    current_handled_by = models.CharField(max_length=32, null=True)

    def getTacheName(self):
        if Order_Tache.objects.get(tache_code=self.current_tache):
            return Order_Tache.objects.get(tache_code=self.current_tache).tache_name
        else:
            return "无当前环节"
    def getOrderType(self):
        order_type = Order_Type.objects.get(type_code=self.order_type)
        return order_type.type_name
    def getCurrentHandledBy(self):
        return User.objects.get(username=self.current_handled_by).username
    def getCreatedBy(self):
        return User.objects.get(username=self.created_by).username

class Jianmian_Order(Base_Order):
    order_state = models.CharField(max_length=4)
    order_description = models.TextField()
    image = models.FileField(null=True, blank=True)
    related_order = models.CharField(max_length=32)
    x_integration_num = models.CharField(max_length=32)
    approved_by = models.CharField(max_length=32)
    comment = models.CharField(max_length=140)
    def getOrderState(self):
        return Order_State.objects.get(state_code=self.order_state).state_name

    def handle_order(self, related_order, x_integration_num, action, comment=None):
        if action == "R":
            self.order_state = "I"
            # self.related_order = related_order
            self.x_integration_num = x_integration_num
            self.comment = comment
            self.save()
            return self.get_absolute_url()
        else:
            self.order_state = "F"
            self.related_order = related_order
            self.x_integration_num = x_integration_num
            self.comment = "处理完成"
            self.save()
            return self.get_absolute_url()

    def fetch_order(self, user):
        if self.order_state == "S":
            self.order_state = "P"
            self.current_handled_by = user
            self.current_tache = "C3H"
            self.save()

    def get_absolute_url(self):
        return "/order/jianmian/%d" % self.id