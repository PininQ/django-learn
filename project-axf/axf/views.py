from django.shortcuts import render


def home(request):
    return render(request, 'axf/home.html')


def market(request):
    return render(request, 'axf/home.html')


def cart(request):
    return render(request, 'axf/home.html')


def mine(request):
    return render(request, 'axf/home.html')
