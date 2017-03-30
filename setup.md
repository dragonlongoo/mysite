# 更新
1. sudo apt-get update

# 软件与组件准备
1. 安装vscode
2. 安装python 2.7(ubuntu 自带)
3. 安装git  
sudo apt-get install git
4. 安装pip  
sudo apt install python-pip  
sudo pip install --upgrade pip
5. 安装django==1.10  
sudo pip install django==1.10
6. 安装 django-tables2  
sudo pip isntall django-tables2
7. 安装 six  
sudo pip install six
8. 安装 django-mysql  
sudo pip install django-mysql  
sudo apt-get install python-mysqldb
sudo apt-get install mysql-client-core-5.7
sudo mariadb-client-core-10.0
9. 安装 pillow  
sudo pip install pillow

# 安装nginx
1. sudo apt-get install nginx
2. 修改default端口  
cd /etc/nginx/site-enabled
sudo vi default  
listen 80 修改为目标端口 8088或者其他  
service nginx restart
3. 

# 安装uwsgi
1. sudo pip install uwsgi
2. 在django项目的根目录下创建test.py文件，添加源码如下：
```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello World"] # python2
    #return [b"Hello World"] # python3
```
然后，Run uWSGI:
```
uwsgi --http :8000 --wsgi-file test.py
```

# 数据库安装/配置
1. sudo apt install mysql-server
2. sudo vi /etc/mysql/my.cnf    
[client]  
default-character-set=utf8mb4  
[mysql]  
default-character-set=utf8mb4  
[mysqld]  
character-set-server=utf8mb4

# 代码调整
1. 将user从mysite.settings中注册app中注释掉
2. 在mysite.url中将user注释
3. 部署时将announcement.category_id的定义注释掉
4. 删除app中的migrations文件夹  
sudo rm -r migrations
5. 重新迁移  
sudo python manage.py makemigrations announcement, etc...
# user
```python
from user.models import Department
d = Department(department_name = 'IT支撑中心', area_code='HU', area_name='湖州市分公司')
d.save()
d = Department(department_name = '市场部', area_code='HU', area_name='湖州市分公司')
d.save()
d = Department(department_name = '渠道运营部', area_code='HU', area_name='湖州市分公司')
d.save()
d = Department(department_name = '财务部', area_code='HU', area_name='湖州市分公司')
d.save()
d = Department(department_name = '吴兴区销售部', area_code='WX', area_name='吴兴区分公司')
d.save()
d = Department(department_name = '南浔区销售部', area_code='NX', area_name='南浔区分公司')
d.save()
```
# announcement
```
from announcement.models import Category
c = Category(category_code="SMZ", category_name="实名制")
c.save()
c = Category(category_code="YYSL", category_name="营业受理")
c.save()
c = Category(category_code="CPZF", category_name="产品资费")
c.save()
c = Category(category_code="PZKT", category_name="配置开通")
c.save()
c = Category(category_code="WXZW", category_name="外线装维")
c.save()
c = Category(category_code="ZHGL", category_name="综合管理")
c.save()
```
# audit
```python
from audit.models import *
os = Order_State(state_code='I',state_name='发起')
os.save()
os = Order_State(state_code='P', state_name='待接单')
os.save()
os = Order_State(state_code='H', state_name='处理中')
os.save()
os = Order_State(state_code='F', state_name='完成')
os.save()
os = Order_State(state_code='S', state_name='已提交')
os.save()
os = Order_State(state_code='R', state_name='退单')
os.save()
ot = Order_Type(type_code='J', type_name='减免单')
ot.save()
os = Order_State(state_code='C', state_name='取消')
os.save()
ota = Order_Tache(tache_code='I', tache_name='拟稿人发起')
ota.save()
ota = Order_Tache(tache_code='C3H', tache_name='市级处理')
ota.save()
ota = Order_Tache(tache_code='IAP', tache_name='拟稿人确认')
ota.save()
oa = Order_Action(action_type='S', action_name='提交')
os.save()
oa = Order_Action(action_type='R', action_name='退单')
oa.save()
oa = Order_Action(action_type='C', action_name='撤单')
oa.save()
oa = Order_Action(action_type='F', action_name='完成')
oa.save()
```
# Tutorial
```python
from wiki.models import *
tc = Tutorial_Category(category_code="JT",category_name="集团4G",category_content="")
tc.save()
tc = Tutorial_Category(category_code="ISALE",category_name="爱销售",category_content="")
tc.save()
tc = Tutorial_Category(category_code="CRM",category_name="CRM",category_content="")
tc.save()
tc = Tutorial_Category(category_code="JF",category_name="计费",category_content="")
tc.save()
tc = Tutorial_Category(category_code="ZY",category_name="资源",category_content="")
tc.save()
tc = Tutorial_Category(category_code="JH",category_name="激活",category_content="")
tc.save()
tc = Tutorial_Category(category_code="ITM",category_name="ITSM",category_content="")
tc.save()
tc = Tutorial_Category(category_code="DICT",category_name="数据字典",category_content="")
tc.save()

t = Tutorial(subject="集团4G业务知识教程",content="集团4G业务知识教程",category="JT")
t.save()
t = Tutorial(subject="爱销售业务知识教程",content="爱销售业务知识教程",category="ISALE")
t.save()
t = Tutorial(subject="CRM",content="CRM业务知识教程",category="CRM")
t.save()
t = Tutorial(subject="计费知识教程",content="计费知识教程",category="JF")
t.save()
t = Tutorial(subject="资源业务知识教程",content="资源业务知识教程",category="ZY")
t.save()
t = Tutorial(subject="激活业务知识教程",content="激活业务知识教程",category="JH")
t.save()
t = Tutorial(subject="ITSM业务知识教程",content="ITSM业务知识教程",category="ITM")
t.save()
t = Tutorial(subject="数据字典业务知识教程",content="数据字典业务知识教程",category="DICT")
t.save()

```