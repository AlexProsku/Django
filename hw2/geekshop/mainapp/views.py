import json

from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    links_menu = [
        {'href': 'products_all', 'title': 'все'},
        {'href': 'products_home', 'title': 'дом'},
        {'href': 'products_office', 'title': 'офис'},
        {'href': 'products_modern', 'title': 'модерн'},
        {'href': 'products_classic', 'title': 'классика'},
    ]

    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products.html', context)

def contact(request):
    with open('mainapp/contacts_file.json', 'r', encoding='utf-8') as file:
        contacts_file = json.load(file)

    context = {
        'contacts_file': contacts_file
    }
    return render(request, 'mainapp/contact.html', context)