from django.shortcuts import render, HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum,F,Q
from .models import Book, BookOrder, Publisher, Author


# Create your views here.

def avg_view(request):
    result = Book.objects.aggregate(Avg('price'))
    print(result)
    return HttpResponse('成功')


def count_view(request):
    result = Book.objects.aggregate(book_count=Count('id'))
    print(result)
    return HttpResponse('成功')


def mai_view(request):
    result = Author.objects.aggregate(max_age=Max('age'), min_age=Min('age'))
    print(result)
    return HttpResponse('成功')


def sum_view(request):
    result = Book.objects.annotate(total=Sum('bookorder__price')).values('name', 'total')
    print(result)
    return HttpResponse('成功')

def F_view(request):
    request=Book.objects.update(price=F('price')-0.99)
    print(request)
    return HttpResponse('成功')

def Q_view(request):
    request=Book.objects.filter(Q(price__gte=89)|Q(price__gte=89))
    for i in request:
        print(i.name,i.price)
    return HttpResponse('成功')

