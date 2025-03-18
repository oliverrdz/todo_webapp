from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.

def home(request):
    return render(request, 'todo/index.html')

def edit_todo(request, id):
    instance = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = FormEditTodo(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved')
        else:
            messages.error(request, form.errors)
    else:
        form = FormEditTodo(instance=instance)
    context = {'form': form}
    return render(request, 'todo/edit_item.html', context)

def list_todo(request):
    todos = Todo.objects.all().order_by('-date').all()
    context = {
        'todos': todos,
    }
    return render(request, 'todo/list_todo.html', context)

def new_todo(request):
    if request.method == 'POST':
        form = FormTodo(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'To do added')
        else:
            messages.error(request, form.errors)
    else:
        form = FormTodo()
    context = {'form': form}
    return render(request, 'todo/new_todo.html', context)