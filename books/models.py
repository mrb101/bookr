from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.utils.text import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

'''
- Implement Rating
- Implement Tagging
- implement Books in Category Count()
'''

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True



class Publisher(TimeStampModel):
    pass


class Category(TimeStampModel):
    slug = models.CharField(max_length=255, null=False, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("category_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Author(TimeStampModel):
    slug = models.CharField(max_length=255, null=False, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    dob = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)


    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("author_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


def book_cover_path(instance, filename):
    ''' Each user will have a folder to store his books '''
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Book(TimeStampModel):
    slug = models.CharField(max_length=255, null=False, blank=True)
    isbn13 = models.CharField(max_length=10, null=True, blank=True)
    isbn10 = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    edition = models.PositiveSmallIntegerField(null=True, blank=True)
    cover = models.ImageField(upload_to=book_cover_path, blank=True)
    cover_thumbnail = ImageSpecField(source='cover',
                                    processors=[SmartResize(200, 200)],
                                    options={'quality': 60})
    item = models.FileField(upload_to='book_file_path')
    description = models.CharField(max_length=255, null=True, blank=True)
    author = models.ManyToManyField(Author, null=True)
    category = models.ManyToManyField(Category, null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.title)


    def __str__(self):
        return str(self.title)

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("book_detail", kwargs=kwargs)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
