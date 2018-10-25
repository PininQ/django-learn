from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from user.models import UserModel, UserTicketModel
from utils.functions import get_ticket
from datetime import datetime, timedelta


def register(request):
    """
    注册
    待实现 => 注册成功可以直接保存该用户 session ，然后重定向到 我的 页面
    """
    data = {
        'title': '注册'
    }
    if request.method == 'GET':
        return render(request, 'user/user_register.html', data)

    if request.method == 'POST':
        username = request.POST.get('username')  # 用户名
        email = request.POST.get('email')  # 用户邮箱
        password = request.POST.get('password')  # 用户密码
        icon = request.FILES.get('icon')  # 用户头像
        # all()验证参数都不为空
        if not all([username, email, password, icon]):
            # 验证不通过, 提示参数不能为空，向页面返回错误信息
            data['msg'] = '请将注册信息填写完整'
            # 返回注册页面
            return render(request, 'user/user_register.html', data)
        # 加密 password
        password = make_password(password)
        # 所有参数都不为空则创建用户
        UserModel.objects.create(username=username,
                                 password=password,
                                 email=email,
                                 icon=icon
                                 )
        # 注册成功，重定向到登录页面
        return HttpResponseRedirect(reverse('user:login'))


def check_user(request):
    '''
    检验用户名是否可用
    '''
    username = request.GET.get("username")
    users = UserModel.objects.filter(username=username)
    data = {
        "msg": "ok",
        "status": "200",
        'desc': '用户名可用'
    }
    if users.exists():
        data['msg'] = "fail"
        data['status'] = '900'
        data['desc'] = "用户已存在"
    return JsonResponse(data)


def login(request):
    """
    登录
    """
    data = {
        'title': '登录'
    }
    if request.method == 'GET':
        # GET请求返回页面
        return render(request, 'user/user_login.html', data)

    if request.method == 'POST':
        # POST请求获取用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证用户是否存在
        user = UserModel.objects.filter(username=username).first()
        if user:
            # 验证密码是否正确
            if check_password(password, user.password):
                # 1. 保存 ticket 在客户端
                # 自定义ticket模块生成ticket并获取
                ticket = get_ticket()
                # 保存返回的HttpResponse对象
                response = HttpResponseRedirect(reverse('axf:mine'))
                # 定义过期时间
                out_time = datetime.now() + timedelta(days=1)
                # 设置返回HttpResponse对象的cookie
                response.set_cookie('ticket', ticket, expires=out_time)
                # 2. 保存ticket到服务端的user_ticket表中
                UserTicketModel.objects.create(user=user,
                                               out_time=out_time,
                                               ticket=ticket)
                # 返回HttpResponse对象
                return response
            else:
                data['msg'] = '密码错误'
                return render(request, 'user/user_login.html', data)
        else:
            data['msg'] = '用户不存在'
            return render(request, 'user/user_login.html', data)


def logout(request):
    """
    注销 删除当前登录的用户的 cookie 中 ticket 的信息
    """
    if request.method == 'GET':
        # 注销，删除当前登录的用户的cookie中的ticket信息
        response = HttpResponseRedirect(reverse('user:login'))
        # 删除返回request的ticket
        response.delete_cookie('ticket')
        return response
