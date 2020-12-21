from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        "class" : "form-control mb-3",
        "placeholder" : "Username"
    }))

    password1 = forms.CharField(label="Password", widget=forms.TextInput(attrs={
        "class" : "form-control mb-3 ",
        "placeholder" : "Password",
        "type" : "password"
    }))

    password2 = forms.CharField(label="Konfirmasi password", widget=forms.TextInput(attrs={
        "class" : "form-control mb-3",
        "placeholder" : "Konfirmasi password",
        "type" : "password"
    }))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        "class" : "form-control mb-3",
        "placeholder" : "Username"
    }))

    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={
        "class" : "form-control mb-3",
        "placeholder" : "Password",
        "type" : "password"
    }))

    class Meta:
        fields = "__all__"



