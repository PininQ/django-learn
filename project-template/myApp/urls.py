# -*- coding: utf-8 -*-
__author__ = 'QB'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  # http://127.0.0.1:8000

    url(r'^students/$', views.students),
    url(r'^good/(\d+)/$', views.good, name='good'),

    url(r'^main/$', views.main),
    url(r'^detail/$', views.detail),


    url(r'^posttest/$', views.posttest, name='showinfo'),
    url(r'^showinfo/$', views.showinfo, name='showinfo'),
    # 验证码
    url(r'^verifycode/$', views.verifycode, name='verifycode'),
    url(r'^verifyresult/$', views.verifyresult, name='verifyresult'),
    url(r'^verifycodecheck/$', views.verifycodecheck, name='verifycodecheck'),
]
