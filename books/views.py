from django.shortcuts import render

from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from .models import Category, Author, Book
from .forms import CategoryForm, AuthorForm, BookForm


''' Category views '''
class CategoryList(ListView):
    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name= 'category'


class CategoryAdd(CreateView):
    model = Category
    template_name = 'categories/form.html'
    form_class = CategoryForm


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'categories/form.html'
    form_class = CategoryForm
    context_object_name = 'form'
    success_url = '/categories/'


''' Book views '''
class BookList(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail.html'
    context_object_name = 'book'


class BookAdd(CreateView):
    model = Book
    template_name = 'books/form.html'
    form_class = BookForm
    context_object_name = 'form'
    success_url = '/books/'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super(BookAdd, self).form_valid(form)


class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/form.html'
    form_class = BookForm
    context_object_name = 'form'
    success_url = '/books/'


class BookReport(View):
    pass


''' Author Views '''
class AuthorList(ListView):
    model = Author
    template_name = 'authors/list.html'
    context_object_name = 'authors'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'authors/detail.html'
    context_object_name = 'author'


class AuthorAdd(CreateView):
    model = Author
    template_name = 'authors/form.html'
    form_class = AuthorForm


class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'authors/form.html'
    form_class = AuthorForm
    context_object_name = 'form'
    success_url = '/authors/'

