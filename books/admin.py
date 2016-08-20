from django.contrib import admin

from imagekit.admin import AdminThumbnail

from .models import Category, Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='cover_thumbnail')

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
