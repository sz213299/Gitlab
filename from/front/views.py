from django.shortcuts import render,HttpResponse
from .form import MessageBoardForm,RegisterForm,ArticleForm
from django.views.decorators.http import require_http_methods
# Create your views here.
# 请求方法  get从服务器获取数据   post向服务器获取数据


def sz(request):
    return HttpResponse("这里是新的界面")
# 装饰器
@require_http_methods(['GET','POST'])
def index(request):
    if request.method == 'GET':
        form = MessageBoardForm()
        return render(request,'index.html',context={'form':form})
    else:
        # 对post请求提交上来的数据，用表单验证是否满足要求
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            return HttpResponse(f"{title},{content},{email}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败")
@require_http_methods(['GET','POST'])
def register(request):
    if request.method == 'GET':
        return render(request,'index1.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            return HttpResponse(f"{telephone}")
        else:
            print(form.errors.get_json_data())  #打印文字
            return HttpResponse('表单验证失败')


@require_http_methods(['GET','POST'])
def artice(request):
    if request.method=='GET':
        return render(request,'article.html')
    else:
        form=ArticleForm(request.POST)
        if form.is_valid():
            # 获取title，con，creat，创建对象，在存储数据库
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            return HttpResponse(f"{title},{content}")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("表单验证失败")

        pass
