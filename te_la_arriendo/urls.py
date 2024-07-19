"""
URL configuration for te_la_arriendo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main.views import change_password, edit_user, home, solo_arrendadores, solo_arrendatarios, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/change-pass/', change_password, name='change_password'),
    path('edit-user/', edit_user, name='edit_user'),
    path('arrendadores/', solo_arrendadores, name='solo_arrendadores'),
    path('arrendatarios/', solo_arrendatarios, name='solo_arrendatarios'),
]