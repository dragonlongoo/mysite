 #coding:utf-8
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .tables import pending_order_table, handling_order_table, archived_order_table
from .forms import *

# 创建订单
def Create_Order(request):
    if request.user.is_authenticated():
        order_form = Jianmian_Order_Form(request.POST or None, request.FILES or None)
        if request.method == "POST" and order_form.is_valid():
            order_description = order_form.cleaned_data["order_description"]
            order_image = order_form.cleaned_data["image"]
            order = Jianmian_Order(
                order_type="J",
                created_by=request.user,
                current_tache='C3H',
                order_state="P",
                order_description=order_description,
                image=order_image
            )
            order.save()
            messages.success(request, "创建成功")
            return HttpResponseRedirect(order.get_absolute_url())
        else:
            form = Jianmian_Order_Form()
            context = {
                "form":order_form
            }
            return render(request, "create_order.html", context)
    else:
        return HttpResponse("请先登录")
# 查看工单
def Show_Order(request, baseorder=None, jianmianorder=None):
    context = {
        "order": jianmianorder,
        "base_order": baseorder
    }
    return render(request, "order_page.html", context=context)
# 获取工单
def Fetch_Order(request, id=None):
    jianmianorder = get_object_or_404(Jianmian_Order, id=id)
    jianmianorder.order_state = "H"
    jianmianorder.current_handled_by = request.user.username
    jianmianorder.save()
    messages.success(request, "取单成功")
    return List_Pending_Orders(request)


# 处理工单
def Handle_Order(request, baseorder=None, jianmianorder=None):
    handle_form = Order_Handle_Form(request.POST or None)
    if request.method == "POST" and handle_form.is_valid():
        if request.POST.has_key("finish"):
            jianmianorder.comment = handle_form.cleaned_data["comment"]
            jianmianorder.related_order = handle_form.cleaned_data["related_order"]
            jianmianorder.x_integration_num = handle_form.cleaned_data["x_integration_num"]
            jianmianorder.order_state = "F"
            jianmianorder.current_handled_by = None
            jianmianorder.save()
            return HttpResponseRedirect(jianmianorder.get_absolute_url())

        elif request.POST.has_key("return"):
            jianmianorder.comment = handle_form.cleaned_data["comment"]
            jianmianorder.order_state = "R"
            jianmianorder.current_handled_by = None
            jianmianorder.save()
            return HttpResponseRedirect(jianmianorder.get_absolute_url())

    else:
        context = {
            "order": jianmianorder,
            "base_order": baseorder,
            "form": handle_form
        }
        return render(request, "handle_order.html", context=context)

def List_Pending_Orders(request):
    table = pending_order_table(Jianmian_Order.objects.filter(order_state="P"))
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    context = {
        "table": table
    }
    return render(request, "order_table_page.html", context=context)

def List_Handling_Orders(request):
    table = handling_order_table(
        Jianmian_Order.objects.filter(
            current_handled_by=request.user.username
            ).filter(order_state="H")
        )
    # table.entry = tables.LinkColumn("<a href='/order/jianmian/{{record.id}}/'>fetch</a>")
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    context = {
        "table": table
    }
    return render(request, "order_table_page.html", context=context)

def List_Archived_Orders(request):
    table = archived_order_table(Jianmian_Order.objects.filter(order_state="F"))
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    context = {
        "table": table
    }
    return render(request, "order_table_page.html", context=context)

# 查看或处理工单
def View_Or_Handle_Order(request, id=None):
    if request.user.is_authenticated():
        order = get_object_or_404(Jianmian_Order, id=id)
        base = Base_Order.objects.get(id=order.id)
        username = request.user.username
        if request.user.username == base.current_handled_by and order.order_state != "F":
            return Handle_Order(request, jianmianorder=order, baseorder=base)
        elif request.user.username == base.created_by:
            return Show_Order(request, jianmianorder=order, baseorder=base)
    else:
        return HttpResponse("请先登录")



def order_index(request):
    return render(request, "order_home_page.html")