# forms.py
# main/forms.py
from django import forms
from django.contrib.auth.models import User
from main.models import UserProfile

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm Password')
    direccion = forms.CharField(max_length=255, required=True)
    telefono = forms.CharField(max_length=15, required=False)
    rol = forms.ChoiceField(choices=UserProfile.roles, required=True, label='Rol')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data
