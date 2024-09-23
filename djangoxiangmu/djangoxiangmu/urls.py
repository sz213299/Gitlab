"""
URL configuration for djangoProject project.

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
from django.urls import path

import students.views

'''
协议：//IP：port/[Path]/[Resource]?[paramsKey=paramValue]&[paramsKey=paramValue]
符合以上格式定义的字符串叫做ULR字符串
https://www.baidu.com/
ftp://localhost
'''
# 定义路径加资源，可以执行对应的方法，重要urls浏览器映射 ,下面这个是接口
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', students.views.LoginView.as_view()),
    # path('user/Login/', students.views.mainview.as_view()),
    path('user/student/', students.views.StudentView.as_view()),

    # path("user/student/",students.views)

]
