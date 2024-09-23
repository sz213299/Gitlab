from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
在url中携带参数
1.通过查询字符串(query string): https//www.baidu.com/s?
2.在path中携带：http://127.0.0.1:8000/book/2

'''


def book_detail(request):
    # request.GET={"id":3}
    request.GET.get('id')  # 没有会返回none
    book_id = request.GET.get('id')
    name = request.GET.get('name')

    return HttpResponse(f"你查找的图书id是:{book_id},图书名字是:{name}")


def book_list(request, book_id):
    return HttpResponse(f"你查找色图书是:{book_id}")


def book_str(request, book_id):
    return HttpResponse(f"图是是:{book_id}")

# 空格 下划线
def book_slug(request, book_id):
    return HttpResponse(f"图书是:{book_id}")


# 可以传/
def book_path(request, book_id):
    return HttpResponse(f"图书是:{book_id}")