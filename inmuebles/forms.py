from django.forms import ModelForm
from main.models import Inmueble
from django import forms

class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        exclude = []  # Puedes listar los campos a excluir si es necesario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_baños': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.TextInput(attrs={'class': 'form-control'}),
            'precios': forms.NumberInput(attrs={'class': 'form-control'}),
            'precios_ufs': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
