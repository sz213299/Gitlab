from django.shortcuts import HttpResponse, render
from django.views.decorators.http import require_http_methods

def add_cook(request):
    response = HttpResponse("设置cook")
    max_age = 60 * 60 * 24 * 30
    response.set_cookie('username', 'zhiliao', max_age=max_age)
    return response


def delete_cook(request):
    response = HttpResponse("删除cook")
    response.delete_cookie('username')
    return response


def get_cookie(request):
    for key, value in request.GET.items():
        print(key, value)
    # username=request.COOKIES.get('username')
    # print(username)
    return HttpResponse('get_cookie')

def add_session(request):
    request.session['user_id']='zhiliao'
    # request.session.set_expiry(0)
    return HttpResponse('add_session')

def get_session(request):
    username=request.session.get('user_id')
    print(username)
    return HttpResponse('get_session')



@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print(request.POST)
        print(request.COOKIES)
        return HttpResponse('登录成功')
