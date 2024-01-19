from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category


def get_products(category=None):
    if category is None:
        products = Product.objects.all()
        return products
    products = Product.objects.filter(category=Category.objects.get(name=category))
    return products

def shop(request, category=None):
    products = get_products(category)
    
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {'products': products, 'categories': categories, 'category': category})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/item_detail.html', {'product': product})