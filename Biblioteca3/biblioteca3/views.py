from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class VistaHome(TemplateView):
    template_name = 'biblioteca/home.html'
