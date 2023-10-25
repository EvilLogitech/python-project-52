from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={})


def login(request):
    return render(request, 'base.html', context={})


def logout(request):
    return render(request, 'base.html', context={})