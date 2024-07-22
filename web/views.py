from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .models import Flan
from .forms import ContactFormModelForm, FlanForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

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
    return redirect('/welcome/')

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
            return redirect('/')  # Redirige a la página de inicio después de guardar
    else:
        form = FlanForm()
    return render(request, 'add_flan.html', {'form': form})

@user_passes_test(is_admin)
def manage_flan(request):
    flanes = Flan.objects.all()

    if request.method == 'POST':
        if 'delete' in request.POST:
            flan_id = request.POST.get('delete')
            flan = get_object_or_404(Flan, id=flan_id)
            flan.delete()
            messages.success(request, 'Flan eliminado con éxito.')
            return redirect('manage_flan')
    
    return render(request, 'manage_flan.html', {'flanes': flanes})

@user_passes_test(is_admin)
def edit_flan(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    
    if request.method == 'POST':
        form = FlanForm(request.POST, instance=flan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flan actualizado con éxito.')
            return redirect('manage_flan')
    else:
        form = FlanForm(instance=flan)
    
    return render(request, 'edit_flan.html', {'form': form, 'flan': flan})