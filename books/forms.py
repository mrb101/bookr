from django import forms
from django.forms import ModelForm
from .validators import MimeTypeValidator

from django.forms.widgets import FileInput
from .models import Book, Author, Category


class BookForm(ModelForm):
    item = forms.FileField(validators=[MimeTypeValidator('application/pdf')],
                           help_text="Only PDF files allowed"
                          )
    class Meta:
        model = Book
        fields = ['isbn13',
                  'isbn10',
                  'title',
                  'edition',
                  'cover',
                  'item',
                  'description',
                  'author',
                  'category',
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
