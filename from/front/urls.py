from django.urls import path

from front.views import index, register, sz, artice

urlpatterns = [
    # path('', index, name='index'),
    path('register',register, name='register'),
    path('artice',artice,name='artice')

]
