from django import views
from django.urls import path
from main.views import contacto, indice, acerca, bienvenido, contact_form

urlpatterns = [
    path('', indice, name='inicio'),
    #path('acerca/', acerca, name='acerca'),
    #path('bienvenido/', bienvenido, name='bienvenido'),
    #path('contacto/', contact_form, name='contacto'),
]