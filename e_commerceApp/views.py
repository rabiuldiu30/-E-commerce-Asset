from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login,logout
from django.contrib import messages

def registerPage(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    form = CustomUserForm()
    context={
        'form':form,
        'form_title':'Registration Form',
        'btn':'Register',
    }

    return render(request,'auth_baseForm.html',context)


def loginPage(request):

    if request.method == 'POST':
        form = AuthForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')


    form = AuthForm()
    context={
        'form':form,
        'form_title':'Login Form',
        'btn':'Login',
    }

    return render(request,'auth_baseForm.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def dashboardPage(request):

    product_data = ProductManagementModel.objects.all()
    context = {
        'product_data':product_data
    }

    return render(request,'dashboard.html',context)



#--------------------------------------------------------------------------------------------------

def customerProfilePage(request):
    try:
        user = CustomerProfileModel.objects.get(user=request.user)
    except CustomerProfileModel.DoesNotExist:
        user = CustomerProfileModel.objects.create(user=request.user)


    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
        
    form = CustomerForm(instance=user)
    context = {
        'form':form,
        'form_title':'Customer Profile',
        'btn':'Update',
        'user':user
    }
    return render(request,'baseForm.html',context)


def adminProfilePage(request):
    try:
        user = AdminProfileModel.objects.get(user = request.user)
    except AdminProfileModel.DoesNotExist:
        user = AdminProfileModel.objects.create(user = request.user)

    if request.method == 'POST':
        form = AdminForm(request.POST,request.FILES,instance = user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')


    form = AdminForm(instance = user)
    context = {
        'form':form,
        'form_title':'Admin Profile',
        'btn':'Update',
        'user':user,
    }
    return render(request,'baseForm.html',context)


def categoryAddpage(request):
    
    try:
        user = AdminProfileModel.objects.get(user = request.user)
    except AdminProfileModel.DoesNotExist:
        user = AdminProfileModel.objects.create(user = request.user)
    
    
    if request.user.user_type == "Admin":
        if request.method == "POST":
            form = CategoryForm(request.POST,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = user
                data.save()
                return redirect("dashboard")
    
    form = CategoryForm()
    context = {
        'form':form,
        'form_title':'Add Category',
        'btn':'Add',
    }
    return render(request,'baseForm.html',context)

def productAddPage(request):
    
    try:
        user = AdminProfileModel.objects.get(user = request.user)
    except AdminProfileModel.DoesNotExist:
        user = AdminProfileModel.objects.create(user = request.user)
    
    
    if request.user.user_type == "Admin":
        if request.method == "POST":
            form = ProductManagementForm(request.POST,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = user
                data.save()
                return redirect("dashboard")
    
    form = ProductManagementForm()
    context = {
        'form':form,
        'form_title':'Add Product',
        'btn':'Add',
    }
    return render(request,'baseForm.html',context)

def productOrderPage(request,id):
    product = ProductManagementModel.objects.get(id=id)
    try:
        user = CustomerProfileModel.objects.get(user = request.user)
    except CustomerProfileModel.DoesNotExist:
        user = CustomerProfileModel.objects.create(user = request.user)
    
    
    if request.user.user_type == "Customer":
        if request.method == "POST":
            form = ProductOrderForm(request.POST,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.product = product 
                data.customer = user
                data.save()
                
                return redirect("dashboard")
              
    form = ProductOrderForm()
    context = {
        'form':form,
        'form_title':'Order Product',
        'btn':'Order',
    }
    return render(request,'baseForm.html',context)

def reviewPage(request,id):
    product = ProductManagementModel.objects.get(id=id)
    try:
        user = CustomerProfileModel.objects.get(user = request.user)
    except CustomerProfileModel.DoesNotExist:
        user = CustomerProfileModel.objects.create(user = request.user)
    
    
    if request.user.user_type == "Customer":
        if request.method == "POST":
            form = ReviewForm(request.POST,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.product = product 
                data.customer = user
                data.save()
    
    form = ReviewForm()
    context = {
        'form':form,
        'form_title':'Review Product',
        'btn':'Submit',
    }
    return render(request,'baseForm.html',context)

def viewProductPage(request,id):
    product = ProductManagementModel.objects.get(id=id)
    context = {
        "product":product
    }
    return render(request,'order_product.html',context)



def myOrdersPage(request):
    customer = request.user.customerprofilemodel
    orders = ProductOrderModel.objects.filter(customer=customer)

    return render(request, 'my_orders.html', {'orders': orders})

from django.shortcuts import render
from .models import ProductOrderModel

def allOrdersPage(request):
    orders = ProductOrderModel.objects.all()
    return render(request, 'all_orders.html', {'orders': orders})

from django.db.models import Q


def productListPage(request):
    query = request.GET.get('search', '')  # safe default

    products = ProductManagementModel.objects.all()

    if query:
        products = products.filter(
            Q(product_name__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'dashboard.html', {
        'products': products,
        'query': query
    })
    
