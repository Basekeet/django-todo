
from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from todos.models import TodoList, Todo

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todolists_list'

    def get_queryset(self):
        return TodoList.objects.all()

def detail(request, todolist_id):
    todos_list = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todos/detail.html', {'todos_list':todos_list.todo_set.all(), 'todolist_id': todolist_id})

def todo(requse, todolist_id, todo_id):
    return HttpResponse(Todo.objects.get(pk=todo_id))

def create_todolist(request):
    try:
        todolist = TodoList(todolist_name=request.POST['todolist_name'])
    except KeyError:
        return HttpResponseRedirect(reverse('todos:index'))
    if todolist.todolist_name:
        todolist.save()
    return HttpResponseRedirect(reverse('todos:index'))

def create_todo(request, todolist_id):
    try:
        todolist = TodoList.objects.get(pk=todolist_id)
        todolist.todo_set.create(todo_text=request.POST['todo_text'])
    except KeyError:
        return HttpResponseRedirect(reverse('todos:detail', args=(todolist_id,)))
    return HttpResponseRedirect(reverse('todos:detail', args=(todolist_id,)))