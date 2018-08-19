from django.shortcuts import render
from .models import Wheel, Nav,Mustbuy


def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()
    return render(request, 'axf/home.html', {
        "title": "主页",
        "wheelsList": wheelsList,
        "navList": navList,
        "mustbuyList": mustbuyList,
    })


def market(request):
    return render(request, 'axf/market.html', {"title": "闪送超市"})


def cart(request):
    return render(request, 'axf/cart.html', {"title": "购物车"})


def mine(request):
    return render(request, 'axf/mine.html', {"title": "我的"})
