from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from .models import Topic


class TopicList(ListView):
    model = Topic
    tempalte_name = 'topics/list.html'
    context_object_name = 'topics'


class TopicDetail(DetailView):
    model = Topic
    template_name = 'topics/detail.html'
    context_object_name= 'topic'


class TopicCrate(CreateView):
    pass


class TopicUpdate(UpdateView):
    pass


