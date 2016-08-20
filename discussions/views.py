from django.shortcuts import render

from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from .models import Topic
from .forms import TopicForm


class TopicList(ListView):
    model = Topic
    template_name = 'discussions/list.html'
    context_object_name = 'topics'


class TopicDetail(DetailView):
    model = Topic
    template_name = 'discussions/detail.html'
    context_object_name= 'topic'


class TopicAdd(CreateView):
    model = Topic
    template_name = 'discussions/form.html'
    form_class = TopicForm

class TopicUpdate(UpdateView):
    model = Topic
    template_name = 'discussions/form.html'
    form_class = TopicForm


class TopicReport(View):
    pass
