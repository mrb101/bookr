from django.shortcuts import render

from django.views.generic import DetailView

from .models import Tag


class TagDetail(DetailView):
    pass
