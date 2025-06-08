from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:pk>/edit/', views.todo_update, name='todo_update'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),

]
