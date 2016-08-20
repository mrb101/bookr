from django.forms import ModelForm

from django.forms.widgets import FileInput
from .models import Topic


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title',
                  'Description',
                  'book',
                 ]
