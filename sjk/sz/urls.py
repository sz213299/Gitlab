from django.urls import path

from .views import add_book, query_book, order_view, update_view, delete_view, book_Tag, index
app_name = 'sz'
urlpatterns = [
    path('s', index, name='index'),
    path('book', add_book, name='add_book'),
    path('query', query_book, name='query_book'),
    path('order', order_view, name='order_view'),
    path('update', update_view, name='update_view'),
    path('delete', delete_view, name='delete_view'),
    path('Tag', book_Tag, name='book_Tag')


]