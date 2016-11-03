from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.core import serializers

from django.core.urlresolvers import reverse

from django.views.generic import (View,
                                  TemplateView,
                                  CreateView,
                                  DetailView,
                                  UpdateView
                                 )
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from .models import Topic, Comment
from .forms import TopicForm, CommentForm


class TopicList(ListView):
    model = Topic
    template_name = 'discussions/list.html'
    context_object_name = 'topics'


class TopicDetail(FormMixin, DetailView):
    model = Topic
    form_class = CommentForm
    template_name = 'discussions/detail.html'
    context_object_name= 'topic'

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['from'] = self.get_form()
        return context


def add_comment(request, slug):
    if request.method == 'POST':
        user_name = request.user.username
        #user = serializers.serialize('json', )
        topic = Topic.objects.get(slug=slug)
        user = request.user
        comment = Comment()
        comment.user = request.user
        comment.topic = topic
        comment.body = request.POST.get('comment')
        comment.save()
        return HttpResponse(json.dumps({
            'type': 'S01',
            'msg': 'Comment has been added',
            'comment': request.POST.get('comment'),
            'user': user_name
        }))
    return HttpResponse(json.drumps({
        'type': 'E01',
        'msg': 'Faild'
    }))


class TopicComment(SingleObjectMixin, FormView):
    """
    post: check if the user is authenticated and holds the current object
    gets_success_url: user the object to redirect after successful post
    for_Valid: adds the current user and the object to the form before commiting
    """
    model = Topic
    template_name = 'discussions/detail.html'
    form_class = CommentForm
    redirect_field_name = 'next'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/?next=%s' % request.path)
        self.object = self.get_object()
        return super(TopicComment, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('topic_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.topic = self.get_object()
        comment.save()
        return super(TopicComment, self).form_valid(form)


class TopicAdd(LoginRequiredMixin, CreateView):
    model = Topic
    from_class = TopicForm
    template_name = 'discussions/form.html'
    success_url = '/topics/'
    fields = ['title', 'Description', 'book']

    def form_valid(self, form):
        """
        if the form is valid, save the associated model.
        """
        topic = form.save(commit=False)
        topic.user = self.request.user
        topic.save()
        return super(TopicAdd, self).form_valid(form)


class TopicUpdate(LoginRequiredMixin, UpdateView):
    model = Topic
    template_name = 'discussions/form.html'
    form_class = TopicForm


class TopicReport(View):
    pass
