**主要笔记**

## Django 中间件

### 概述

一个轻量级、底层的插件，可以介入 Django 的请求和响应

### 本质

一个 Python 类

### 方法
- `__init__` 不需要传递参数，服务器响应第一个请求的时候自动调用，用于确认是否启用中间件。

- process_request(self, request) 在执行视图之前被调用（分配 url 匹配视图之前），每个请求都会调用，返回 None 或者 HttpResponse 对象

- process_view(self, view_func, view_args, view_kwargs) 调用视图之前执行，每个请求都会调用，返回 None 或者 HttpResponse 对象

- process_template_response(self, request, response)
    - 在视图执行结束后调用，每个请求都会调用，返回 None 或者 HttpResponse 对象。
    - 使用 render

- process_response(self, request, response) 所有的响应返回浏览器之前调用，每个请求都会调用，返回 None 或者 HttpResponse 对象

- process_exception(self, request, exception) 当时图抛出异常时调用，返回 HttpResponse 对象

工程目录下 setting.py 文件中提供的中间件：
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
### 执行位置

中间件各方法执行位置
![中间件各方法执行位置](https://raw.githubusercontent.com/qinbin52qiul/MarkdownPhotos/master/django-learn/%E4%B8%AD%E9%97%B4%E4%BB%B6%E5%90%84%E6%96%B9%E6%B3%95%E6%89%A7%E8%A1%8C%E4%BD%8D%E7%BD%AE.png)

### 自定义中间件

工程目录下 middleware 目录下创建 myApp 目录

创建一个 python 文件
```python
from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):
    # 该中间件只能读出来，不能修改
    def process_request(self, request):
        print("get 参数为：", request.GET.get('abc'))
```
使用自定义中间件，配置 setting.py 

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.myApp.myMinddle.MyMiddle' # 添加自定义中间件
]
```
## Ajax 请求问题

 Ajax 请求，在谷歌浏览器里的控制台没有返回数据，还一直显示着历史的 console.log("I am Bin Qin") ，暂时不知道怎么回事，先记录一下，

 ![谷歌浏览器Ajax返回数据结果](https://raw.githubusercontent.com/qinbin52qiul/MarkdownPhotos/master/django-learn/%E8%B0%B7%E6%AD%8C%E6%B5%8F%E8%A7%88%E5%99%A8Ajax%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%9C.png)
 
 在火狐浏览器返回了数据。
 
 ![火狐浏览器Ajax返回数据结果](https://raw.githubusercontent.com/qinbin52qiul/MarkdownPhotos/master/django-learn/%E7%81%AB%E7%8B%90%E6%B5%8F%E8%A7%88%E5%99%A8Ajax%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%9C.png)


谷歌浏览器的 Ajax 请求可以返回数据了，一直点击 `Clear console` 就可以突然显示数据了😁。如下图：

 ![clear console](https://raw.githubusercontent.com/qinbin52qiul/MarkdownPhotos/master/django-learn/clear%20console.png)
 
 谷歌浏览器的 Ajax 请求可以返回数据

 ![谷歌浏览器的Ajax请求可以返回数据](https://raw.githubusercontent.com/qinbin52qiul/MarkdownPhotos/master/django-learn/%E8%B0%B7%E6%AD%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E7%9A%84Ajax%E8%AF%B7%E6%B1%82%E5%8F%AF%E4%BB%A5%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE.png)
 
 ## Celery - 分布式任务队列
 
 文档：http://docs.jinkan.org/docs/celery/
 
 ### 问题
 
 - 用户发起 request，并且要等待 response 返回。但是在视图中有一些耗时的操作，导致用户可能会等待很长时间才能接收到 response，这样用户体验很差
 
 - 网站每隔一段时间都要同步一次数据，但是 HTTP 请求是需要触发的
 
 ### 解决
 
 - 将耗时的操作放到 celery 中执行
 
 - 使用 celery 定时执行
 
 ### Celery 概述
 
 - 任务 task：本质是一个 Python 函数，将耗时操作封装成一个函数
 - 队列 queue：将要执行的任务放到队列中
 - 工人 worker：负责执行对列中的任务
 - 代理 broker：负责调度，在部署环境中使用 redis
 
### Celery 相应包的安装
 
```python
pip install celery
pip install celery-with-redis
pip install django-celery
```

### 配置 setting.py 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
    'tinymce',  # 富文本
    'djcelery',  # 配置 djcelery
]
...
...
...
# celery
import djcelery
djcelery.setup_loader()  # 初始化队列
BROKER_URL = 'redis://:123456@127.0.0.1:6379/0'  # redis 代理配置
CELERY_IMPORTS = ('myApp.task')  # 任务配置
```
### 在应用目录下创建 task.py 文件
 
### 执行迁移生成 celery 所需的数据库表
 
 python manage.py migrate
 
 ![celery](https://raw.githubusercontent.com/qinbin52qiul/MarkdownPhotos/master/django-learn/celery.png)
 
### 在工程目录下的 project 目录下创建 celery.py 文件

celery.py 内容：
```python
from __future__ import absolute_import
# 使用绝对包含路径
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whthas_home.settings')
# 设置django运行时需要的环境变量

app = Celery('portal')  # 传入的应该是项目名称

app.config_from_object('django.conf:settings')
# 读取django 的配置信息，使用 'CELERY_' 开头的即为celery的配置

app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)  # 自动发现在installed apps中包含的task（需要在tasks.py中定义）这样就不用手动的在CELERY_IMPORTS中添加设置

@app.task(bind=True)  # dumps its own request information
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```

### 在工程目录下的 project 目录下的 `__init__.py` 文件中添加

```python
from .celery import app as celery_app
```
 
##总结
 
 很多时候明明没有写错，但是结果一直不对，这个时候就需要多刷新页面，多清楚缓存和 cookie，多重启 Django 服务器，多试试其他浏览器是否能正常显示，
 然后再确认以下是否是自己写错了，自己写错了一般会有报错信息，但是前面那种情况一般没有报错信息可以查看。