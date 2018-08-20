from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from axf.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods


def home(request):
    """
    首页视图函数
    """
    if request.method == 'GET':
        # 查询数据
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        # 组织数据
        data = {
            'title': '首页',
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainbuys': mainbuys,
            'mainshops': mainshops,
            'mainshows': mainshows,
        }
        # 携带数据渲染页面
        return render(request, 'axf/home.html', data)


def market(request):
    """
    闪购超市
    """
    if request.method == 'GET':
        # 重定向到market_params方法所对应的路由
        return HttpResponseRedirect(reverse('axf:market_params', args=('104749', '0', '0')))


def user_market(request, typeid, cid, sid):
    """
    闪购详情
    :param request:
    :param typeid: 分类id
    :param cid: 子类id
    :param sid: 排序id
    """
    # 查询所有食品类型
    foodtypes = FoodType.objects.all()
    # 根据分类查询到对应的所有商品
    if cid == '0':
        goods = Goods.objects.filter(categoryid=typeid)
    # typeid 和 categoryid   并且是一对多的一个关系
    else:
        goods = Goods.objects.filter(categoryid=typeid, childcid=cid)

    # 重新组装全部分类的参数
    # 组装结果为[['全部分类','0'], ['酒类':13550], ['饮用水':15431]]
    foodtypes_current = foodtypes.filter(typeid=typeid).first()
    if foodtypes_current:
        childtypes = foodtypes_current.childtypenames
        childtypenames = childtypes.split('#')
        child_list = []
        for childtypename in childtypenames:
            child_type_info = childtypename.split(':')
            child_list.append(child_type_info)

    # 将商品按指定顺序排序
    if sid == '0':
        pass
    if sid == '1':
        goods = goods.order_by('productnum')
    if sid == '2':
        goods = goods.order_by('-price')
    if sid == '3':
        goods = goods.order_by('price')

    # 组织数据
    data = {
        'foodtypes': foodtypes,
        'goods': goods,
        'typeid': typeid,
        'child_list': child_list,
        'cid': cid,
    }
    # 传递数据给页面并渲染
    return render(request, 'axf/market.html', data)


def cart(request):
    """
    购物车
    """
    return render(request, 'axf/cart.html', {"title": "购物车"})


def mine(request):
    """
    我的
    """
    if request.method == 'GET':
        data = {
            "title": "我的"
        }
    return render(request, 'axf/mine.html', data)
