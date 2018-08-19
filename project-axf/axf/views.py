from django.shortcuts import render


def home(request):
    return render(request, 'axf/home.html', {"title": "主页"})


def market(request):
    return render(request, 'axf/market.html', {"title": "闪送超市"})


def cart(request):
    return render(request, 'axf/cart.html', {"title": "购物车"})


def mine(request):
    return render(request, 'axf/mine.html', {"title": "我的"})
