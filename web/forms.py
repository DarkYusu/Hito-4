from django import forms
from django.forms import ModelForm
from web.models import ContactForm
from .models import Flan
# class ContactFormForm(forms.Form):
#     customer_email = forms.EmailField(label='Correo')
#     customer_name = forms.CharField(max_length=64, label='nombre')
#     message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
        
class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name', 'description', 'image_url', 'is_private', 'precio']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'image_url': 'URL de la Imagen',
            'is_private': '¿Privado?',
            'precio': 'Precio (CLP)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_private': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }