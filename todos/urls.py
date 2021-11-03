from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todolist_id>/', views.detail, name='detail'),
    path('<int:todolist_id>/<int:todo_id>/', views.todo, name='todo')
]