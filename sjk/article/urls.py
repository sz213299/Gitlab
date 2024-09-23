from django.urls import path

from article.views import article_test, one_to_many, query1, query2, query3, query4, query5

app_name = 'article'
urlpatterns = [
    path('test', article_test, name='article_test'),
    path('one',one_to_many, name='one_to_many'),
    path('query1', query1, name='query1'),
    path('query2', query2, name='query2'),
    path('query3', query3, name='query3'),
    path('query4', query4, name='query4'),
    path('query5', query5, name='query5')

]
