权限 用户网点名称 分公司

审批领导必填

附件数量限制为一个

费用减免（审批领导，需求标题 关于xxx的费用减免审批单，附件数量限制为1）

个性化业务审批（文本框）

工单池，取单

超链接 颜色修改

统一模板文件

用户模型，权限

注册

归档工单模型（表）

如何实现知识库结构能够随意调整，章、节、段落等顺序能随意调整顺序


drop table wiki_category;
drop table wiki_content;
drop table wiki_content_type;
drop table wiki_zy_chapter;
drop table wiki_zy_section;
drop table wiki_zy_tutorial;

c = Content_Type(type_code="YWZS", type_name="业务知识")
c.save()

c = Tutorial_Category(category_code="crm", category_name="CRM")
c.save()
c = Tutorial_Category(category_code="iSale", category_name="爱销售")
c.save()
c = Tutorial_Category(category_code="jt", category_name="集团")
c.save()
c = Tutorial_Category(category_code="jf", category_name="计费")
c.save()
c = Tutorial_Category(category_code="zy", category_name="资源")
c.save()
c = Tutorial_Category(category_code="jh", category_name="激活")
c.save()

Tutorial

t = Tutorial(subject="CRM",category="crm")
t.save()
t = Tutorial(subject="爱销售",category="iSale")
t.save()
t = Tutorial(subject="集团",category="jt")
t.save()
t = Tutorial(subject="计费",category="jf")
t.save()
t = Tutorial(subject="资源",category="zy")
t.save()
t = Tutorial(subject="激活",category="jh")
t.save()


<div class="page-header">
            <a href="{% url 'wiki_post' tutorial.category %}">
                <button type="button" class="btn btn-default btn-sm">编辑教程</button>
            </a>
            <a href="{% url 'wiki_post' tutorial.category %}">
                <button type="button" class="btn btn-success btn-sm">新增章节</button>
            </a>
            
        </div>
            <h4>{{tutorial.subject}}</h4>
        <ul>
            {% for c in chapters %}
            <li class="list-unstyled">
                <a href="{% url 'chapter' tutorial.category c.id %}">{{c.subject}}</a>
            </li>
            {% endfor %}
        </ul>

from audit.models import *
os = order_state(state_code='I',state_name='发起')
os.save()
os = order_state(state_code='P', state_name='待接单')
os.save()
os = order_state(state_code='H', state_name='处理中')
os.save()
os = order_state(state_code='F', state_name='完成')
os.save()
os = order_state(state_code='S', state_name='已提交')
os.save()
os = order_state(state_code='R', state_name='退单')
os.save()
ot = order_type(type_code='J', type_name='减免单')
ot.save()
os = order_state(state_code='C', state_name='取消')
os.save()
ota = order_tache(tache_code='I', tache_name='拟稿人发起')
ota.save()
ota = order_tache(tache_code='C3H', tache_name='市级处理')
ota.save()
ota = order_tache(tache_code='IAP', tache_name='拟稿人确认')
ota.save()
oa = order_action(action_type='S', action_name='提交')
os.save()
oa = order_action(action_type='R', action_name='退单')
oa.save()
oa = order_action(action_type='C', action_name='撤单')
oa.save()
oa = order_action(action_type='F', action_name='完成')
oa.save()
