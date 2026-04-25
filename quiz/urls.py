from django.urls import path

from .views import (
    quiz_bitik_add,
    quiz_bitik_delete,
    quiz_index,
    quiz_savol_add,
    quiz_savol_delete,
    quiz_savol_view,
    quiz_savollar,
)

app_name = 'quiz'

urlpatterns = [
    path('', quiz_index, name='index'),
    path('natija/<int:pk>/', quiz_index, name='natija'),
    path('savollar/', quiz_savollar, name='savollar'),
    path('savollar/<int:pk>/', quiz_savollar, name='sinf_savollar'),
    path('savol/add/', quiz_savol_add, name='savol_add'),
    path('savol/<int:pk>/', quiz_savol_view, name='savol_view'),
    path('savol/<int:pk>/delete/', quiz_savol_delete, name='savol_delete'),
    path('bitik/add/', quiz_bitik_add, name='bitik_add'),
    path('bitik/<int:pk>/delete/', quiz_bitik_delete, name='bitik_delete'),
]
