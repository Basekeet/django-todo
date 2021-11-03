from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response
from django.template import loader
from django.http import Http404

from todos.models import TodoList, Todo

def index(request):
    todolists_list = TodoList.objects.all()
    context = {
        "todolists_list": todolists_list
    }
    return render(request, 'todos/index.html', context)

def detail(request, todolist_id):
    todos_list = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todos/detail.html', {"todos_list":todos_list.todo_set.all(), "todolist_id": todolist_id})

def todo(requse, todolist_id, todo_id):
    return HttpResponse(Todo.objects.get(pk=todo_id))