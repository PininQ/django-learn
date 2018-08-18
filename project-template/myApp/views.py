from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades, Students


# 定义视图
def index(request):
    # return HttpResponse("my is a good man")
    student = Students.objects.get(pk=1)
    return render(request, 'myApp/index.html', {
        "stu": student,
        "list": ["qinbin", "qiuqiu", "dada"],
        "num": 10,
        "test": False,

    })


def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {"students": studentsList})


def good(request, id):
    # http://127.0.0.1:8000/qinbin/good/13124/
    return render(request, 'myApp/good.html', {"id": id})


def main(request):
    # http://127.0.0.1:8000/qinbin/main/
    return render(request, 'myApp/main.html')


def detail(request):
    # http://127.0.0.1:8000/qinbin/detail/
    return render(request, 'myApp/detail.html')


def posttest(request):
    return render(request, 'myApp/posttest.html')


def showinfo(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    return render(request, 'myApp/showinfo.html', {
        "username": name,
        "password": pwd
    })


# 生成验证码
def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 40
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的 point() 函数绘制噪点
    for i in range(0, 200):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = '0123456789aijklmbcfEFGHIJKLMghnoRSdeTUpqrstuvwxyzABCDNOPQVWXYZ'
    # 随机选取 4 个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('../fonts/msyhl.ttc', 25)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制 4 个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入 session，用于做进一步验证
    request.session['verify'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为 png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME 类型为图片 png
    return HttpResponse(buf.getvalue(), 'image/png')


def verifyresult(request):
    return render(request,'myApp/verifyresult.html')


from django.http import HttpResponseRedirect
def verifycodecheck(request):
    code1 = request.POST.get("verifycode").upper()
    code2 = request.session["verify"].upper()
    if code1 == code2:
        return HttpResponse("<h1 style='color:green;'>验证成功！</h1>")
    return HttpResponse("<h1 style='color:red;'>验证失败！</h1>")