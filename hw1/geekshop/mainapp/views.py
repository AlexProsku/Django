import json

from django.shortcuts import render

from mainapp.models import Product, Category

# Create your views here.

def main(request):
    context = {
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)

def products(request):

    context = {
        'links_menu': Category.objects.all()
    }

    return render(request, 'mainapp/products.html', context)

def products_list(request, pk):
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    with open('mainapp/contacts_file.json', 'r', encoding='utf-8') as file:
        contacts_file = json.load(file)

    context = {
        'contacts_file': contacts_file
    }
    return render(request, 'mainapp/contact.html', context)