from django.forms import ModelForm

from django.forms.widgets import Textarea
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
        widgets = {
            'body': Textarea(attrs={
                'class': 'comment',
                'cols': '40', 'rows': '3'
            }),
        }
