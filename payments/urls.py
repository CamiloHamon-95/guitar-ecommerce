from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path(
        route='cart/',
        view=views.cart,
        name='cart'
    ),
    path(
        route='checkout/',
        view=views.checkout,
        name='checkout'
    ),
    path(
        route='update_item/',
        view=views.updateItem,
        name='update_item'
    ),
    path(
        route='history/',
        view=views.history_order,
        name='history'
    ),
]