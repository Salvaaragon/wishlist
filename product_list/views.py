from django.shortcuts import render
from .models import ProductList, ProductType

# Create your views here.

def index(request):

    productlist = ProductList.objects.filter(owner = request.user)
    return render(request, 'product_list/lists.html', 
        {'products_lists': productlist , 'title': 'Listas de productos'})

def get_product_list(request, pk):
    list = ProductList.objects.get(pk = pk)
    products = list.products.all()
    return render(request, 'product_list/product_list.html', 
        {'list': list, 'products': products, 'title': list.name})

def new_product_list(request):
    product_types = ProductType.objects.all()
    return render(request, 'product_list/form_product_list.html', 
        {'product_types': product_types, 'title': 'Nueva lista'})