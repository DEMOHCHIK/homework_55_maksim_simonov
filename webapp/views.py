from django.shortcuts import render, redirect
from .models import Task


def home(request):
    return render(request, 'home.html')


def task_list(request):
    tasks = Task.objects.all()

    for task in tasks:
        task.status = dict(Task.STATUS_CHOICES)[task.status]

    return render(request, 'task_list.html', {'tasks': tasks})


def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')