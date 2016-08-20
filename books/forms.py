from django.forms import ModelForm

from django.forms.widgets import FileInput
from .models import Book, Author, Category


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['isbn13',
                  'isbn10',
                  'title',
                  'edition',
                  'cover',
                  'description',
                  'author',
                  'category',
                  'user'
                 ]
        widgets = {
            'cover': FileInput(attrs={'class': 'button'}),
        }

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name','dob','country']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'parent']
