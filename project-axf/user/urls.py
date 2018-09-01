# -*- coding: utf-8 -*-
__author__ = 'QB'
from django.conf.urls import url
from user import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.login, name='login'),
    # 注册
    url(r'^register/$', views.register, name='register'),
    # 注销
    url(r'^logout/$', views.logout, name='logout'),
    # 检查用户名是否已经存在
    url(r'^checkuser/', views.check_user, name='check_user'),
]
