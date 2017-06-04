#coding:utf-8
import django_tables2 as tables
from django_tables2 import A
from user.models import Subscriber, Privilege, Role, Department

class user_table(tables.Table):
    class Meta:
        model = Subscriber
        fields = [
            "id",
            "username",
            "full_name",
            "contact",
            "email",
            "department",
            "role",
            "created_date"
        ]
        attrs = {
        "class": "paleblue"
        }
    id = tables.Column(verbose_name="ID")
    username = tables.Column(verbose_name="用户名")
    full_name = tables.Column(verbose_name="姓名")
    contact = tables.Column(verbose_name="联系方式")
    email = tables.Column(verbose_name="邮件")
    department = tables.Column(verbose_name="部门")
    role = tables.Column(verbose_name="角色")
    created_date = tables.Column(verbose_name="创建时间")
    entry = tables.TemplateColumn('<a href="/user/{{user.id}}/config/">修改</a>', verbose_name="操作")

class Privilege_Table(tables.Table):
    class Meta:
        model = Privilege
        fields = [
            
        ]