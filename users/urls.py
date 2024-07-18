from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    #View SIGNUP
    path(
        route='signup/',
        view=views.view_signup,
        name='signup',
    ),
    #View LOGIN
    path(
        route='login/',
        view=views.view_login,
        name='login',
    ),
    #View LOGOUT
    path(
        route='logout/',
        view=views.view_logout,
        name='logout',
    ),
    #View UPDATE_PROFILE
    path(
        route='update-profile/',
        view=views.view_update_profile,
        name='update_profile',
    ),
]