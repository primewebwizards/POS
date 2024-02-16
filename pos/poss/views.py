from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def dashbord(request):
    return render(request, 'dashbord.html')

def invoicing(request):
    
    return render(request, 'invoicing.html')


def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        code = request.POST['code']
        photo = request.FILES.get('image')
        cost = request.POST['cost']
        quantity = request.POST['quantity']
        
        if Product.objects.filter(name=name).exists():
            print("product already exist")
            return redirect('add_product')
        if Product.objects.filter(code=code).exists():
            print("enter a unique code")
            return redirect('add_product')
        else:
            product = Product.objects.create(name=name, code=code, photo=photo, cost=cost, quantity=quantity)
            product.save()
            return redirect('add_product')
        
    else:
        return render(request, 'add_product.html')
        
        

def inventory(request):
    products = Product.objects.all()
    return render(request, 'inventory.html', {'products': products})