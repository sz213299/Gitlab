

from django.shortcuts import HttpResponse
from django.db import connection

from sz.models import Book, Tag


def index1(request):
    return HttpResponse("这是主页")
# Create your views here.
def index(request):
    # 获取游标对象
    cursor = connection.cursor()
    # sql语句
    cursor.execute("select * from book")
    # 获取数据
    book = cursor.fetchall()
    # 遍历数据
    for i in book:
        print(i)
    return HttpResponse("查找成功")


def add_book(request):
    book=Book(name='三国演义',author='罗贯中',price=100)
    # book = Book(name='水浒传', author='施耐庵', price=109)
    book.save()
    return HttpResponse("读书插入成功")

def query_book(request):
    # books=Book.objects.all()
    # book=Book.objects.filter(name="三国演义")
    # for i in book:
    #     print(i.name,i.author,i.price,i.pub_time)
    try:
        book=Book.objects.get(name='三国演义')
        print(book.name)
        return HttpResponse("查找成功")
    except:
        print("图书不存在")
        return HttpResponse("查找失败")

def order_view(request):
    # books=Book.objects.order_by('-pub_time')
    books = Book.objects.all()
    for book in books:

        print(book.name)
    return HttpResponse("排序成功")


def update_view(request):
    book=Book.objects.first()
    book.name='西游记'
    book.save()
    print(book.name)
    return HttpResponse("修改成功")

def delete_view(request):
    book=Book.objects.get(name='西游记')
    book.delete()
    return HttpResponse("删除成功")

def book_Tag(request):
    tag=Tag()
    tag.save()
    return HttpResponse("插入成功")
