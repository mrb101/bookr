from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from books.models import Book

from django.core.urlresolvers import reverse
from django.utils.text import slugify


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class Topic(TimeStampModel):
    slug = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    Description = models.CharField(max_length=255, null=True, blank=True)
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("topic_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)


class Comment(TimeStampModel):
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    body = models.TextField()

    def __unicode__(self):
        return str(self.body)

    def __str__(self):
        return str(self.body)

