# -*- coding: utf-8 -*-
__author__ = 'QB'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  # http://127.0.0.1:8000
    url(r'^(\d+)/(\d+)$', views.detail),  # http://127.0.0.1:8000/1000/25
]
