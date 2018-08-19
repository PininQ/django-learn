# -*- coding: utf-8 -*-
__author__ = 'QB'

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