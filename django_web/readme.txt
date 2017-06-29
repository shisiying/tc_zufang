#一、生产环境的搭建以及项目的配置
安装python2.7
安装pip
安装django
安装mongoengine
#编程软件
pycharm社区版
#创建方法
先在cmd中创建一个目录，比如在f盘中创建一个Django_web的项目
#创建项目
django-admin startproject 项目名字
#创建项目模块app
进入到项目目录
python manage.py startapp datashow
#使用pycharm进行开发
使用file导入项目所在文件夹

#二、页面的编写与设计
#UI框架
Semantic-U
#UI重点
模板的套用
模板继承
django模板标签语言

#三、django数据的获取以及使用方法
#models模块的重点

#views的重点

#urls路由的配置
在views.py中编写函数
def test(request):
    return render(request,'base.html')
在urls.py中引入模块函数，并且分配路由
from datashow.views import test
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', test),
]
启动服务器，就可以看到自已的页面了
启动服务器的方法是
在文件目录中执行python manage.py runserver

#四、settings的配置
1.当生成app模块的时候，需要在
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'datashow'#这里就是我们新建的模块
]
2.设置template文件的目录
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"template")],#这里设置我们的模板目录
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
3.静态文件css和js文件的引入
在django_web下新建static文件夹
然后在settings中新增
STATICFILES_DIRS=(os.path.join(BASE_DIR,"static"))
当我们在页面引入这个文件夹的时候只需使用{% load static %}就可以使用static这个文件夹的路径了
