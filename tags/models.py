from django.db import models

from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class Tag(TimeStampModel):
    tag = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255, null=False, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return str(self.tag)

    def __str__(self):
        return str(self.tag)

    @property
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse("tag_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.tag)
        super(Tag, self).save(*args, **kwargs)
