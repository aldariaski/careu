'''module forms'''
from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    '''form registrasi dengan 3 fields'''
    username = forms.CharField(required=True,label="Username", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Username"
    }))

    password1 = forms.CharField(label="Password", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Password",
        "type" : "password"
    }))

    password2 = forms.CharField(label="Konfirmasi password", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Konfirmasi password",
        "type" : "password"
    }))

    class Meta:# pylint: disable=too-few-public-methods
        '''meta'''
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    '''login form 2 fields'''
    username = forms.CharField(required = True, label="Username", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Username",
        "type": "text"
    }))

    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Password",
        "type" : "password"
    }))

    class Meta:# pylint: disable=too-few-public-methods
        '''meta'''
        model = User
        fields = ["username", "password"]
