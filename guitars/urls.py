from django.urls import path
from . import views

app_name = 'guitars'

urlpatterns = [
    path(
        route='',
        view=views.index,
        name='index',
    ),
    path(
        route='guitar/<int:id_guitar>/',
        view=views.detail_guitar,
        name='detail_guitar',
    ),
    path(
        route='guitar/favorites/',
        view=views.favorites,
        name='favorites',
    ),
]