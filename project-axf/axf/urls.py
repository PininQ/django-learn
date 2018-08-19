# -*- coding: utf-8 -*-
__author__ = 'QB'

from django.conf.urls import url
from axf import views
urlpatterns = [
    # 首页
    url(r'^home/$', views.home, name='home'),
    # 个人中心
    url(r'^mine/$', views.mine, name='mine'),
    # 闪购超市
    url(r'^market/$', views.market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.user_market, name='market_params'),

    # 购物车页面
    url(r'^cart/$', views.cart, name='cart'),
]