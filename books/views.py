from django.core.urlresolvers import reverse

from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from django.contrib.contenttypes.models import ContentType

from .models import Category, Author, Book
from .forms import CategoryForm, AuthorForm, BookForm

from tags.models import Tag

''' Category views '''
class CategoryList(ListView):
    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name= 'category'


class CategoryAdd(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categories/form.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('category_detail', kwargs={'slug': self.object.slug})


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'categories/form.html'
    form_class = CategoryForm
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('category_detail', kwargs={'slug': self.object.slug})

''' Book views '''
class BookList(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail.html'
    context_object_name = 'book'

    def get_context_data(self, *args, **kwargs):
        context = super(BookDetail, self).get_context_data(*args, **kwargs)
        model = ContentType.objects.get_for_model(Book)
        tags = Tag.objects.filter(content_type=model, object_id=self.object.id)
        context['tags'] = tags
        return context


class BookAdd(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/form.html'
    form_class = BookForm
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super(BookAdd, self).form_valid(form)


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/form.html'
    form_class = BookForm
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'slug': self.object.slug})


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


class AuthorAdd(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'authors/form.html'
    form_class = AuthorForm


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'authors/form.html'
    form_class = AuthorForm
    context_object_name = 'form'
    success_url = '/authors/'
