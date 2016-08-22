from django.forms import ModelForm

from django.forms.widgets import FileInput
from .models import Topic, Comment


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title',
                  'Description',
                  'book',
                 ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
