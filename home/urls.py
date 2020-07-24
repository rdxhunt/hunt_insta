from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [

    path('',views.index,name='index'),

    path('login_form', views.login_form,name='login_form'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),


    path('registration_form', views.registration_form,name='registration_form'),
    path('registration', views.registration,name='registration'),



    path('hunt_redirect', views.hunt_redirect, name='hunt_redirect'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('change_r_url', views.change_r_url, name='change_r_url'),
    re_path('\d{4}',views.hunt_page,name="huntpage")
]

