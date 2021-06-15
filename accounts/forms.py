from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Último nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Palavra-passe'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a sua palavra-passe'}),
        }