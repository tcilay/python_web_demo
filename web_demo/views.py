from django.shortcuts import render
from django.http import *
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


def month_archive(request, year, month):
    pass


def article_detail(request, year, month, article_detail):
    pass
