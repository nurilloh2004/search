import imp
from unicodedata import name
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'



def search_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        name = Products.objects.filter(name_contains = searched)
        return render(request, 'search.html', {'searched' : searched}, {'name' : name})
    else:
        return render(request, 'index.html', {} )