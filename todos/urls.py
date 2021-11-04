from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todolist_id>/', views.detail, name='detail'),
    path('<int:todolist_id>/<int:todo_id>/', views.todo, name='todo'),
    path('create_todolist', views.create_todolist, name='create_todolist'),
    path('create_todo/<int:todolist_id>/', views.create_todo, name='create_todo')
]