from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def baidu(request):
    return render(request, 'baidu.html')


def info(request):
    # 1.普通的变量
    username = '你叫啥名字'
    # 2.字典类型
    book = {'name': "水浒传", 'auther': "施耐庵"}
    # 3.列表
    books = [
        {'name': "水浒传", 'auther': "施耐庵"},
        {'name': "三国演义", 'auther': "罗贯中"}
    ]

    # 4.对象
    class Person:
        def __init__(self, realname):
            self.realname = realname

    context = {
        'username': username,
        'book': book,
        'books': books,
        'person': Person('治疗课堂')

    }
    return render(request, 'info.html', context=context)


def if_view(request):
    age = 90
    return render(request, 'if.html', context={'age': age})


def for_view(request):
    # 列表
    books = [
        {'name': "水浒传", 'auther': "施耐庵"},
        {'name': "三国演义", 'auther': "罗贯中"}
    ]
    # 字典
    person = {'realname': "治疗课堂", 'age': 19, 'height': 190}

    context = {'books': books, 'person': person}

    return render(request, 'for.html', context=context)


def url_view(request):
    return render(request, 'url.html')


def book_view(request, book_id):
    return HttpResponse(f"你访问的图书id是:{book_id}")

def filter_view(request):
    greet="Hello World,   rdtyuijokgfhjklh uioygihu"
    from datetime import datetime
    context = {'greet': greet,'birthday': datetime.now()}
    return render(request,'filter.html',
                  context=context)


def static_view(request):
    return render(request, 'static.html')

def re_view(request):
    context={
        'articles':['小米su7','chatgpt']
    }
    return render(request, 'wz.html', context=context)

