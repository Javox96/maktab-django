from django.urls import path

from .views import main_about, main_index, main_result, main_test

app_name = 'main'

urlpatterns = [
    path('', main_index, name='index'),
    path('about/', main_about, name='about'),
    path('result/', main_result, name='result'),
    path('test/<int:pk>/', main_test, name='test'),
]
