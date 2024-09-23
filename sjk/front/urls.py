from django.urls import path

from front.views import avg_view, count_view, mai_view, sum_view, F_view, Q_view

app_name = 'front'
urlpatterns = [
    path('avg', avg_view, name='avg'),
    path('count', count_view, name='count'),
    path('mai', mai_view, name='mai'),
    path('sum',sum_view,name='sum_view'),
    path('F',F_view, name='F_view'),
    path('Q',Q_view, name='Q_view')

]
