# -*- coding: utf-8 -*-
__author__ = 'QB'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  # http://127.0.0.1:8000

    url(r'^upload/$', views.upload),
    url(r'^savefile/$', views.savefile),

    url(r'^student/(\d+)/$', views.student),

    url(r'^ajaxstudents/$', views.ajaxstudents),
    url(r'^studentsinfo/$', views.studentsinfo),
    # 富文本
    url(r'^edit/$', views.edit),
    # celery
    url(r'^celery/$', views.celery),
]
