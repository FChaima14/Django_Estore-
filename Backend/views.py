from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product, Customer, Order, OrderItem, ShippingAddress
from django.http import JsonResponse
import json
import datetime
from django.core.paginator import Paginator
from .form import CreateUerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
# Create your views here.

def get_Product_list(request):
    p=Paginator(Product.objects.all(), 4);
    page=request.GET.get('page')
    Pro=p.get_page(page)
    context={
        'products' : Product.objects.all(),
        'pros': Pro,
    }
    #print(context)
    return render(request, 'Backend/Home.html', context)


def search(request):
    q=request.GET['q'];
    items=Product.objects.filter(title__icontains=q).order_by('-id');
    print(items)
    context={
      'pros': items
    }
    return render(request, 'Backend/Home.html', context)

def get_Product_detaill(request, pk):
    print(pk)
    items=Product.objects.get(id=pk)
    context={
      'items': items
    }
    return render(request, 'Backend/detaill.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer;
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all();
    else:
        items=[];
        order={'getItemCart' : 0, 'getTotalCart': 0 , 'shipping': False}
    context={
        'items' :items, 
        'order': order
    }
    return render(request, 'Backend/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer;
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all();
    else:
        items=[];
        order={'getItemCart' : 0, 'getTotalCart': 0, 'shipping': False}
    context={
        'items' :items, 
        'order': order
    }
    return render(request, 'Backend/checkout.html', context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('productId', productId, 'action', action)
    print(request.user.email)
    """create the actio that allow to add the order to cart"""
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order, created=Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created=OrderItem.objects.get_or_create(order=order, product= product)
    if action == 'add':
        orderItem.quantity=(orderItem.quantity) + 1;
    elif action =='remove':
        orderItem.quantity=(orderItem.quantity) - 1;
    orderItem.save();
    if orderItem.quantity <=0:
        orderItem.delete();
    return JsonResponse('item was added' , safe=False);

def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer;
        order, created=Order.objects.get_or_create(customer=customer, complete=False);
        total=float(data['form']['total'])
        order.transaction_id=transaction_id

        if total == float(order.getTotatlCart):
            order.complete=True;

        order.save();

        if order.shipping==True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                adress=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                ZipCode=data['shipping']['zipcode'],
            )
    else:
        print('user b=not logged in ')
    return JsonResponse('order was added', safe=False)

def signIn(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username, password)

        user= authenticate(username=username, password=password);
        if user is not None:
            login(request, user)
            print('user logged')
            return redirect('Product_List');
        else:
            messages.info(request, 'username or password not valid ')
    return render(request, 'Backend/login.html', {})

def signUp(request):
    form= CreateUerForm();
    if request.method =='POST':
        form= CreateUerForm(request.POST)
        if form.is_valid():
            form.save();  
            return redirect('signIn')

    return render(request, 'Backend/register.html', {'form': form})

def signOut(request):
    logout(request);
    return redirect('Product_List');
