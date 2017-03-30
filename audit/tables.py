#coding:utf-8
import django_tables2 as tables
from django_tables2 import A
from .models import *

# 未使用
class pending_order_table (tables.Table):
    id = tables.Column()
    getOrderType = tables.Column(verbose_name="订单类型")
    created_date = tables.Column(verbose_name="创建时间")
    created_by = tables.Column(verbose_name="发起人")
    getOrderState = tables.Column(verbose_name="工单状态")
    getTacheName = tables.Column(verbose_name="当前环节")
    current_handled_by = tables.Column(verbose_name="当前处理人")
    related_order = tables.Column(verbose_name="关联订单")
    entry = tables.TemplateColumn('<a href="/order/jianmian/{{record.id}}/fetch/">取单</a>', verbose_name="取单")
    class Meta:
        model = Jianmian_Order
        fields = (
            "id",
            "getOrderType",
            "created_date",
            "created_by",
            "getOrderState",
            "getTacheName",
            "current_handled_by",
            "related_order",
            "entry"
        )

        attrs = {
            "class": "table table-striped"
            }

class handling_order_table (tables.Table):
    id = tables.Column()
    getOrderType = tables.Column(verbose_name="订单类型")
    created_date = tables.Column(verbose_name="创建时间")
    created_by = tables.Column(verbose_name="发起人")
    getOrderState = tables.Column(verbose_name="工单状态")
    getTacheName = tables.Column(verbose_name="当前环节")
    current_handled_by = tables.Column(verbose_name="当前处理人")
    related_order = tables.Column(verbose_name="关联订单")
    entry = tables.TemplateColumn('<a href="/order/jianmian/{{record.id}}/">处理</a>', verbose_name="处理")
    class Meta:
        model = Jianmian_Order
        fields = (
            "id",
            "getOrderType",
            "created_date",
            "created_by",
            "getOrderState",
            "getTacheName",
            "current_handled_by",
            "related_order",
            "entry"
        )

        attrs = {
            "class": "table table-striped"
            }

class archived_order_table (tables.Table):
    id = tables.Column()
    getOrderType = tables.Column(verbose_name="订单类型")
    created_date = tables.Column(verbose_name="创建时间")
    created_by = tables.Column(verbose_name="发起人")
    getOrderState = tables.Column(verbose_name="工单状态")
    getTacheName = tables.Column(verbose_name="当前环节")
    current_handled_by = tables.Column(verbose_name="当前处理人")
    related_order = tables.Column(verbose_name="关联订单")
    class Meta:
        model = Jianmian_Order
        fields = (
            "id",
            "getOrderType",
            "created_date",
            "created_by",
            "getOrderState",
            "getTacheName",
            "current_handled_by",
            "related_order"
        )

        attrs = {
            "class": "table table-striped"
            }