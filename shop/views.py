from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Category, Product
from .forms import ProductForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
@login_required
def add_product(request):
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Adminstrators can do this.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.- Please try again')
    else:
        form = ProductForm()  
                
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)        


""" Edit product needs product id """
@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Adminstrators can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

""" Delete product needs product id """
@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Adminstrators can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)   
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('product_admin'))


""" Product Admin """
def product_admin(request):    
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category:
        category = get_object_or_404(Category, category=category)
        products = products.filter(category=category)
    return render(request,
                  'shop/productadmin_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products}) 
