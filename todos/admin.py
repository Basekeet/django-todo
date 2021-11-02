from django.contrib import admin
from todos.models import TodoList, Todo

admin.site.register(TodoList)
admin.site.register(Todo)
