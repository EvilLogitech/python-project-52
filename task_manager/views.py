from django.shortcuts import render
# from gettext import translate as _


def index(request):
    return render(request, 'index.html', context={})
