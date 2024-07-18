from operator import truediv
from users.models import Profile
from payments.models import Order
from .models import Guitar, Model, Brand, Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from .utils import get_favs

# Create your views here.
def index(request):
    guitars = Guitar.objects.order_by('id_guitar')
    models = Model.objects.order_by('id_model')
    brands  = Brand.objects.order_by('id_brand')
    if not request.user.is_authenticated:
        context = {
            'list_guitars': guitars,
            'list_models': models,
            'list_brands': brands,
            'cartItems': 0,
        }
        return render(request, 'guitars/index.html', context)
    else:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context = {
            'authenticated': True,
            'list_guitars': guitars,
            'list_models': models,
            'list_brands': brands,
            'cartItems': order.get_cart_items,
        }
        return render(request, 'guitars/index.html', context)

def detail_guitar(request, id_guitar):
    guitar = Guitar.objects.get(id_guitar=id_guitar)
    if not request.user.is_authenticated:
        context = {
            'guitar': guitar,
            'cartItems': 0,
        }
        return render(request, 'guitars/detail_guitar.html', context)
    else:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context = {
            'guitar': guitar,
            'cartItems': order.get_cart_items,
        }
        return render(request, 'guitars/detail_guitar.html', context)
    

@login_required(login_url='/users/login/')
def favorites(request):
    user = request.user
    myprofile = Profile.objects.get(user=user)
    try:
        if len(request.COOKIES.get('fav')) > 0:
            dict_fav_guitars = get_favs(request.COOKIES.get('fav').strip())
            for fav_guitar in dict_fav_guitars.items():
                if (fav_guitar[1] == "true"):
                    myprofile.addFavorite(fav_guitar[0])
                elif(fav_guitar[1] == "false"):
                    myprofile.removeFavorite(fav_guitar[0])
            myprofile.save()
    except:
        raise Exception("Error in Favorites View")

    customer = request.user.customer
    fav_guitars = []
    for favs in myprofile.getFavorites():
        fav_guitars.append(Guitar.objects.get(pk=favs))
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {
        'fav_guitars': fav_guitars,
        'cartItems': order.get_cart_items,
        'error': "There are no guitars in your Favorite list"
    }
    return render(request, 'guitars/favorite.html', context)