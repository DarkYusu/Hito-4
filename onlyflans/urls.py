"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from web.views import indice, acerca, bienvenido, base1, contacto, success, flan_detalle,add_flan,manage_flan, edit_flan, salir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name='indice'),
    path('welcome/', bienvenido, name='bienvenido'),
    path('about/', acerca, name='acerca'),
    path('base/', base1, name='base'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', success, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', salir, name='logout'),
    path('flan/<slug:slug>/', flan_detalle, name='flan_detalle'),
    path('add_flan/', add_flan, name='add_flan'),
    path('manage_flan/', manage_flan, name='manage_flan'),
    path('edit_flan/<slug:slug>/', edit_flan, name='edit_flan'),
    path('add_flan/', add_flan, name='add_flan'),
]
