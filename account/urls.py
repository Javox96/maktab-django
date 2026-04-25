from django.urls import path

from .views import account_login, account_logout, account_regist

app_name = 'account'

urlpatterns = [
    path('regist/', account_regist, name='regist'),
    path('login/', account_login, name='login'),
    path('logout/', account_logout, name='logout'),
]
