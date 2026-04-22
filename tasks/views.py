from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'deadline']
    success_url = '/'