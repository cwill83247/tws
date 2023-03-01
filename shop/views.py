from django.shortcuts import render, get_object_or_404
from .models import Category, Product 

# Create your views here.

# List of All Products
def product_list(request):    #passingin category so can filter
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category:
        category = get_object_or_404(Category, category=category)
        products = products.filter(category=category)
    return render(request,
                  'shop/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products}) 


# Product Details 
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)                 
    context = {                                                                 
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)                
