from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'tasks/home.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('task_list')
        return super().dispatch(request, *args, **kwargs)
class TaskListView(LoginRequiredMixin, ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'deadline']
    success_url = '/tasks/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'status', 'deadline']
    success_url = '/tasks/'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/tasks/'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')