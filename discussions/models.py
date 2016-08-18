from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from books.model import Book

from django.core.urlresolvers import reverse
from django.utils.text import slugify



class Topic(models.Model):
    slug = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    Description = models.CharField(max_length=255, null=True, blank=True)
    book = models.ForeignKey(Book, related_names='topics', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.title)

    def __str__(self):
        return str(self.titlea)

    @property
    def get_absolute_url(self):
        kwargs = {self.slug}
        return reverse("top_details", kwargs=kwargs)
