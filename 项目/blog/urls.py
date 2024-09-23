import pub

from blog.views import index, blog, publish

from django.urls import path
app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('blog/<int:blog_id>/', blog, name='blog'),
    path('pub',publish,name='pub')
]
