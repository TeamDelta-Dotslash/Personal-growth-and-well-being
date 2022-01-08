from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration/', views.registration, name="reg"),
    path('login/',views.user_login, name= "login" ),
    path('logout/',views.user_logout, name= "logout" ),
]
