from django.shortcuts import render

from django.views.generic import TemplateView



class Home(TemplateView):
    template_name = 'main/home.html'



class About(TemplateView):
    template_name = 'main/about.html'


class Contact(TemplateView):
    template_name = 'main/contact.html'
