from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 定义视图
def index(request):
    return HttpResponse("my is a good man")


def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))
