'''module forms'''
from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    '''form registrasi dengan 3 fields'''
    username = forms.CharField(required=True,label="Username",min_length=8, widget=forms.TextInput(attrs={
        "class" : "form-control",
        "id": "username_id",
        "placeholder" : "Username"
    }))

    password1 = forms.CharField(label="Password", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Password",
        "id": "password1",
        "type" : "password"
    }))

    password2 = forms.CharField(label="Konfirmasi password", widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "Konfirmasi password",
        "id": "password2",
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
        fields = ["username", "password"]
