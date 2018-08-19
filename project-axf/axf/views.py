from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from axf.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods


def home(request):
    '''
    首页视图函数
    '''
    if request.method == 'GET':
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'title': '首页',
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainbuys': mainbuys,
            'mainshops': mainshops,
            'mainshows': mainshows,
        }
        return render(request, 'axf/home.html', data)


def market(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('axf:market_params', args=('104749', '0', '0')))


def user_market(request, typeid, cid, sid):
    """
    :param request:
    :param typeid: 分类id
    :param cid: 子类id
    :param sid: 排序id
    """
    foodtypes = FoodType.objects.all()
    # 获取某分类下的商品
    if cid == '0':
        goods = Goods.objects.filter(categoryid=typeid)
    else:
        goods = Goods.objects.filter(categoryid=typeid, childcid=cid)
    data = {
        'foodtypes': foodtypes,
        'goods': goods,
        'typeid': typeid,
        'cid': cid,
    }
    return render(request, 'axf/market.html', data)


def cart(request):
    return render(request, 'axf/cart.html', {"title": "购物车"})


def mine(request):
    return render(request, 'axf/mine.html', {"title": "我的"})
