from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import *

# Create your views here.

def home(request):
    return HttpResponse('Todo home')

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