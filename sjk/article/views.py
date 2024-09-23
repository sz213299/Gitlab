from datetime import datetime

from django.shortcuts import render, HttpResponse

import article
from article.models import User, Article


# Create your views here.

def article_test(request):
    article = Article.objects.first()
    return HttpResponse(article.author.name)

    # user=User(name='admin',password='123456')
    # user.save()
    # article=Article(title="这是我s的课堂",content='xxxx',author=user)
    # article.save()
    # return HttpResponse("XXXXX")


def one_to_many(request):
    user = User.objects.first()
    articles = user.article_set.all()  # .filter(title__icontains='的')过滤
    for article in articles:
        print(article.title)
    return HttpResponse("成功")


'''
id__exact=1
title__iexact 不区分大小写
contains 大小写敏感判断是否包含了某个数据  title不要忘记
contains 忽略大小写
in 
gt >
lt<

'''


def query1(request):
    # article = Article.objects.filter(id__exact=1)
    article = Article.objects.filter(title__iexact='这是我的课堂Sz')
    #     查询结果
    print(article.query)  # 执行代码
    print(article)
    return HttpResponse("成功")


def query2(request):
    article = Article.objects.filter(title__icontains='sz')
    print(article.query)  # 执行代码
    print(article)
    return HttpResponse("成功")


def query3(request):
    article = Article.objects.filter(id__in=[1, 2, 3])
    print(article.query)  # 执行代码
    print(article)
    return HttpResponse("成功")


def query4(request):
    start_date = datetime(year=2024, month=6, day=3)
    end_date = datetime(year=2024, month=6, day=4)
    article = Article.objects.filter(pubtime__time__range=(start_date, end_date))
    print(article.query)  # 执行代码
    print(article)
    return HttpResponse("成功")



def query5(request):
    # 查找标题中包含Sz用户
    user=User.objects.filter(article__title__icontains='sz')
    print(user.query)
    print(user)
    return HttpResponse("成功")



