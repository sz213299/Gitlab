from django.urls import path


from szauth.views import send,login, register

app_name = 'zhiliao'
urlpatterns = [
    path('login', login, name='login'),
    path('reg', register, name='register'),
    path('send',send, name='send')
]
