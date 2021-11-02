from django.db import models


class TodoList(models.Model):
    todolist_name = models.CharField(max_length=200)

    def __str__(self):
        return self.todolist_name


class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text