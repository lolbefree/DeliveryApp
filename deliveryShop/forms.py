from django import forms
from .models import Basket
from django.contrib.auth.forms import AuthenticationForm


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['goods']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Користувач')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')