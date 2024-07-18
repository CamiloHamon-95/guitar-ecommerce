import json
from math import prod
from .models import *
from guitars.models import Guitar

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('Ya esta en la vista CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0}
	cartItems = order['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			cartItems += cart[i]['quantity']

			product = Guitar.objects.get(pk=i)
			total = (product.price * cart[i]['quantity'])

			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']
	
			item = {
				'id':product.id_guitar,
				'product': product,
    			'quantity':cart[i]['quantity'],
       			'get_total':total,
			}
			items.append(item)
		except:
			raise Exception("Hubo un Error en el tratamiento de COOKIES para el carrito de compras")

	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}
