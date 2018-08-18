# -*- coding: utf-8 -*-
__author__ = 'QB'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  # http://127.0.0.1:8000
    url(r'^attribles/$', views.attribles),  # http://127.0.0.1:8000/attribles/

    # get
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),

    # post
    url(r'^register/$', views.register),

    # request
    url(r'^success/$', views.success),

    # response
    url(r'^showresponse/$', views.showresponse),

    # cookie
    url(r'^cookietest/$', views.cookietest),

    # redirect
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),

    # session
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^quit/$', views.quit),
    url(r'^showmain/$', views.showmain),

    url(r'^set_session$', views.set_session),           # 保存session数据
    url(r'^get_session$', views.get_session),           # 获取session数据
]
