from django.urls import path

from movie.views import movie_list, movie_detail

# 指定应用名称
app_name = 'movie'




urlpatterns = [
    path('list',movie_list, name='movie_list'),
    path('detail/<int:movie_id>',movie_detail)
]