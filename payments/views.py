from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from .models import * 
from .utils import cartData
from guitars.models import Guitar
from .forms import form_shipping_information
from django.contrib.auth.decorators import login_required
# Create your views here.

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'payments/cart.html', context)

def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    
    if request.method == 'POST':
        form = form_shipping_information(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                customer = request.user.customer
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                cartItems = order.get_cart_items
            else:
                customer = Customer(user=None)
                customer.name = form.cleaned_data['name']
                customer.email = form.cleaned_data['email']
                customer.payment_method = form.cleaned_data['payment_method']
                customer.save()
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                for myitem in items:
                    myproduct = OrderItem(product=myitem['product'], order=order, quantity=myitem['quantity'])
                pass
            form.save_data(customer,order)
            return redirect('guitars:index')
        else:
            return render(request, 'payments/checkout.html', {'form':form,'cartItems':cartItems})
    else:
        form = form_shipping_information()
        return render(request, 'payments/checkout.html', {'form':form,'cartItems':cartItems})

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	customer = request.user.customer
	product = Guitar.objects.get(id_guitar=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

@login_required
def history_order(request):
    customer = request.user.customer
    history_order = Order.objects.filter(customer=customer)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {
        'history_order': history_order,
        'cartItems': order.get_cart_items,
        'error': "There are no guitars in your Favorite list"
    }
    customer = request.user.customer
    
    return render(request, 'payments/history_order.html', context)