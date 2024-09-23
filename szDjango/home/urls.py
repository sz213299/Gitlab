from django.urls import path

from home.views import index, baidu, info, if_view, for_view, url_view, book_view, filter_view, static_view, re_view

# 指定应用名称
app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('baidu', baidu, name='baidu'),
    path('info', info, name='info'),
    path('if', if_view, name='if'),
    path('for', for_view, name='for'),
    path('url', url_view, name='url'),
    path('book/<book_id>',book_view, name='book'),
    path('filter',filter_view, name='filter'),
    path('sta',static_view,name='static'),
    path('wz',re_view,name='wz')
]
