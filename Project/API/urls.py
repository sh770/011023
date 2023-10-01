from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('alllist/', views.getAllList, name='alllist'),
    path('one/<int:id>', views.getOneTodo, name='one'),
    path('put/<int:id>', views.putTodo, name='edit'),
    path('del/<int:id>', views.delTodo, name='del'),
    path('add/', views.postTodo, name='add todo')
]

