from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .models import Flan
from .forms import ContactFormModelForm, FlanForm
from django.contrib.auth.decorators import login_required, user_passes_test

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})

def base1(request):
    flanes = Flan.objects.all()
    return render(request, 'base.html', {'flanes': flanes})

def success(request):
    return render(request, 'exito.html', {})

# def contacto(request):
#     if request.method == 'POST':
#         form = ContactFormForm(request.POST)
#         if form.is_valid():
#             contact_form = ContactForm.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/exito')
#     else:
#         form = ContactFormForm()   
#     return render(request, 'contacto.html',{'form':form})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()   
    return render(request, 'contacto.html',{'form':form})

def salir(request):
    logout(request)
    return redirect('/')

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def flan_detalle(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    return render(request, 'flan_detalle.html', {'flan': flan})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def add_flan(request):
    if request.method == 'POST':
        form = FlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar
    else:
        form = FlanForm()
    return render(request, 'add_flan.html', {'form': form})