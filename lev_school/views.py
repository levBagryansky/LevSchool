from django.shortcuts import render
from django.core.cache import cache
# from . import terms_work


def home(request):
    return render(request, "home.html")
