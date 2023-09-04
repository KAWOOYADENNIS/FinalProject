from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#import models to views 
from .models import *

#import forms to views
from .forms import *

#import filters to the views
from .filters import *

#import django decorators
#a decorator is a function being referenced but not called and we use 'at' to reference it.
from django.contrib.auth.decorators import login_required

#import reverse method
from django.urls import reverse


#create views here
def mainpage(request):
    return render(request,'dennis/mainpage.html')

def home_details(request):
    # return render(request,'dennis/home_details.html')
    products = Product.objects.all().order_by('-id')#we are querying the database
#telling the database to get all the products using 'id'
    product_filters = ProductFilter(request.GET,queryset=products)#we search among the products queried above
    products = product_filters.qs 
    return render(request,'dennis/home_details.html',{'products':products, 'product_filters':product_filters})


def about_details(request):
    return render(request,'dennis/about_details.html')



@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id') 
    return render(request,'dennis/receipt.html',{'sales':sales})



@login_required
def issue_item(request,pk):
    issued_item = Product.objects.get(id=pk)
    sales_form = Saleform(request.POST)
    
    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            # here we are keeping track of stock remaining after a sale. 
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity 
            issued_item.save()
            
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            
            return redirect('receipt')
    return render(request,'dennis/issue_item.html',{'sales_form': sales_form})
            
@login_required       
def add_to_stock(request,pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['recieved_quantity'])
            issued_item.total_quantity += added_quantity 
            issued_item.save()
            # to add to the remaining stock, qantity is reduced. 
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home_details')
    return render(request, 'dennis/add_to_stock.html',{'form':form})
            

def receipt_detail(request,receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request,'dennis/receipt_detail.html',{'receipt':receipt})

def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_recieved for items in sales])
    change = sum([items.get_change()for items in sales])
    net = total-change
    return render(request,'dennis/all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})

@login_required
def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'dennis/product_detail.html',{'product':product})
    
    

# Create your views here.
