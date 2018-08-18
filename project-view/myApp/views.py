from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades, Students


# 定义视图
def index(request):
    # 访问地址：http://127.0.0.1:8000/bin/
    return HttpResponse("qinbin is a good man!")
    # return HttpResponse("my is a good man")


def attribles(request):
    # 访问地址：http://127.0.0.1:8000/bin/attribles/
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")


# 获取get传递的数据，GET 属性浏览器传递给服务器的数据
def get1(request):
    # 访问地址：http://127.0.0.1:8000/bin/get1?a=1&b=2&c=3
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)


def get2(request):
    # 访问地址：http://127.0.0.1:8000/bin/get2?a=1&a=2&c=3
    # 同一个参数有多个值
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + " " + a2 + " " + c)


# POST
def register(request):
    # http://127.0.0.1:8000/bin/register/
    return render(request, 'myApp/register.html')


# request
def success(request):
    # http://127.0.0.1:8000/bin/register/success/
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("post success.")


# response
def showresponse(request):
    # http://127.0.0.1:8000/bin/showresponse/
    res = HttpResponse(b'good')
    # res.content = b'good'
    print(res.content)  # 返回的内容
    print(res.charset)  # 编码格式
    print(res.status_code)  # 响应状态码，常见200、304、404、400
    # print(res.cookies)  # 返回cookies
    return res


# cookietest
def cookietest(request):
    # http://127.0.0.1:8000/bin/cookietest/
    res = HttpResponse()
    # 设置 cookie 的方法，set_cookie(key,value='',max_age=None,expires=None,domain=None)
    # cookie = res.set_cookie("qinbin","good")
    # 获取 cookie
    cookie = request.COOKIES
    res.write("<h1>" + cookie["qinbin"] + "</h1>")
    # 删除 cookie 的方法 delete_cookie(key)
    return res


# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def redirect1(request):
    # http://127.0.0.1:8000/bin/redirect1/
    # 使用 HttpResponseRedirect 的方式
    # return HttpResponseRedirect("/bin/redirect2")
    # 使用 redirect 的方式
    return redirect('/bin/redirect2')


def redirect2(request):
    return HttpResponse("<h1>该页面是重定向之后的页面</h1>")


# session
def main(request):
    # http://127.0.0.1:8000/bin/showmain/
    # 取出 session
    username = request.session.get('name')
    if username is None:
        username = '游客'
    print(username)
    return render(request, 'myApp/main.html', {'username': username})


def login(request):
    return render(request, 'myApp/login.html')


# 在这里踩坑了，login.html 的 POST 提交路径
def showmain(request):
    print("========")
    username = request.POST.get('username')
    print("username = ", username)
    # 存储 session
    request.session['name'] = username
    # 设置 session 10s 后过期，默认半个月，0 是关闭浏览器时就失效，None 是永不过期
    # request.session.set_expiry(10)
    return redirect('/bin/main/')


from django.contrib.auth import logout
def quit(request):
    # 清除 session，以下三种方式
    logout(request)  # 推荐
    # request.session.clear()
    # request.session.flush()
    return redirect('/bin/main/')


# redis 存储 session
def set_session(request):
    # 保存 session 数据
    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存session数据成功')


def get_session(request):
    # 获取 session 数据
    username = request.session.get('username')
    verify_code = request.session.get('verify_code')
    text = 'username=%s, verify_code=%s' % (username, verify_code)
    return HttpResponse(text)