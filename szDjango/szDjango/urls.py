"""
URL configuration for szDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import HttpResponse
from book.views import book_detail, book_list, book_str, book_slug, book_path
from django.conf import settings
from django.conf.urls.static import static
# url与视图映射
# s/(url) --->视图函数 进行映射
# 视图函数
# def index(request):
#     print(reverse("movie:movie_list"))
#     # print(reverse("book_detail"))
#     # reverse("book_path",kwargs={"book_id":1})
#     return HttpResponse("欢迎你刚回来")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('book', book_detail, name='book_detail'),
    #     http://127.0.0.1:8000/book/1,指定参数类型，会出现404，在视图函数中得到就是整型，就则默认就是str
    path('book/<int:book_id>', book_list),
    path('book/str/<int:book_id>', book_str),
    path('book/slug/<slug:book_id>', book_slug),
    path('book/path/<path:book_id>', book_path, name='book_path'),

    path('movie/', include('movie.urls')),
    path('home/', include('home.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
