from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Grades, Students


# 定义视图
def index(request):
    # return HttpResponse("my is a good man")
    return render(request, 'myApp/index.html')


# 上传文件
def upload(request):
    return render(request, 'myApp/upload.html')


# 保存文件
import os
from django.conf import settings
def savefile(request):
    if request.method == "POST":
        f = request.FILES['file']
        # 文件保存路径（服务器端）
        filePath = os.path.join(settings.MDEIA_ROOT, f.name)
        with open(filePath, 'wb') as fp:
            for each in f.chunks():
                fp.write(each)
        return HttpResponse("<h1 style='color:green;'>上传成功！</h1>")
    else:
        return HttpResponse("<h1 style='color:red;'>上传失败！</h1>")


# 分页
from .models import Students
from django.core.paginator import Paginator
def student(request, pageid):
    # 所有学生列表
    allList = Students.objects.all()
    paginator = Paginator(allList, 6)
    page = paginator.page(pageid)
    return render(request, 'myApp/student.html', {"students": page})


def ajaxstudents(request):
    return render(request, 'myApp/ajaxstudents.html')


from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.objects.all()
    # liststus = [stu.sname for stu in stus]
    liststus = []
    for stu in stus:
        liststus.append([stu.sname, stu.sage])
    return JsonResponse({"data": liststus})


def edit(request):
    return render(request, 'myApp/edit.html')

import time
def celery(request):
    print("good")
    time.sleep(5)  # 模拟耗时操作
    print("nice")
    return render(request, 'myApp/celery.html')