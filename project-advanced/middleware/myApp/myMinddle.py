# -*- coding: utf-8 -*-
__author__ = 'QB'
from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    # 该中间件只能读出来，不能修改
    # 访问 http://127.0.0.1:8000/?abc=1
    def process_request(self, request):
        print("get 参数为：", request.GET.get('abc'))
