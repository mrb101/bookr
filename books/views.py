from django.shortcuts import render

from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from .models import Category, Author, Book


''' Category views '''
class CategoryList(ListView):
    model = Category
    tempalte_name = 'categories/list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name= 'category'


class CategoryAdd(CreateView):
    pass


class CategoryUpdate(UpdateView):
    pass


''' Book views '''
class BookList(ListView):
    model = Book
    tempalte_name = 'Books/list.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    tempalte_name = 'Books/detail.html'
    context_object_name = 'book'


class BookAdd(CreateView):
    pass


class BookUpdate(UpdateView):
    pass


class BookReport(View):
    pass


''' Author Views '''
class AuthorList(ListView):
    model = Author
    tempalte_name = 'authors/list.html'
    context_object_name = 'authors'


class AuthorDetail(DetailView):
    model = Author
    tempalte_name = 'authors/detail.html'
    context_object_name = 'author'


class AuthorAdd(CreateView):
    pass


class AuthorUpdate(UpdateView):
    pass

