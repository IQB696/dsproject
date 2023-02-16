from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def shop(request):
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')


