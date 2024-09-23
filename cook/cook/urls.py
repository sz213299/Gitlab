"""cook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from cook.views import add_cook, delete_cook, get_cookie, add_session, get_session, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cook',add_cook,name='add_cook'),
    path('delete',delete_cook,name='delete_cook'),
    path('get',get_cookie,name='get_cook'),
    path('session',add_session,name='add_session'),
    path('get/se',get_session,name='get_session'),
    path('login',login,name='login')
]
