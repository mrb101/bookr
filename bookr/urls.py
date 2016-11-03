"""bookr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from main import views as main_views
from books import views as books_views
from discussions import views as topics_views
from tags import views as tags_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, name="login"),
    url(r'^logout/', auth_views.logout, name="logout"),

    url(r'^$', main_views.Home.as_view(), name='home'),
    url(r'^about/$', main_views.About.as_view(), name='about'),
    url(r'^contact$', main_views.Contact.as_view(), name='contact'),

    url(r'^categories/$', books_views.CategoryList.as_view(), name="categories_list"),
    url(r'^categories/add/$', books_views.CategoryAdd.as_view(), name="category_add"),
    url(r'^categories/(?P<slug>[-\w]+)/update/$',books_views.CategoryUpdate.as_view(), name="category_update"),
    url(r'^categories/(?P<slug>[-\w]+)/$', books_views.CategoryDetail.as_view(), name="category_detail"),

    url(r'^books/$', books_views.BookList.as_view(), name="books_list"),
    url(r'^books/add/$', books_views.BookAdd.as_view(), name="book_add"),
    url(r'^books/(?P<slug>[-\w]+)/update/$',books_views.BookUpdate.as_view(), name="book_update"),
    url(r'^books/(?P<slug>[-\w]+)/report', books_views.BookReport.as_view(), name="book_report"),
    url(r'^books/(?P<slug>[-\w]+)/$', books_views.BookDetail.as_view(), name="book_detail"),

    url(r'^topics/$', topics_views.TopicList.as_view(), name="topics_list"),
    url(r'^topics/add/$', topics_views.TopicAdd.as_view(), name="topic_add"),
    url(r'^topics/(?P<slug>[-\w]+)/update/$',topics_views.TopicUpdate.as_view(), name="topic_update"),
    url(r'^topics/(?P<slug>[-\w]+)/report/$', topics_views.TopicReport.as_view(), name="topic_report"),
    url(r'^topics/(?P<slug>[-\w]+)/$', topics_views.TopicDetail.as_view(), name="topic_detail"),
    url(r'^topics/(?P<slug>[-\w]+)/add/$', topics_views.add_comment, name="add_comment"),


    url(r'^tags/(?P<slug>[-\w]+)/$', tags_views.TagDetail.as_view(), name="tag_detail"),
]

# Some extra setup for debug mode
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
