from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register),
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),

]