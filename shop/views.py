from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import ProductForm 

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

# Manage Products (Admin Only)

def add_product(request):
    form = ProductForm()
        
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)        

