from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'home.html', {'tasks': tasks, 'form': form})
