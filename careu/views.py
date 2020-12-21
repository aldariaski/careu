'''module for all logic here'''
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, LoginForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Post, Profile

#User view
def register_view(request):
    if request.user.is_authenticated:
        return redirect("home-base")

    context = {
        "register_form" : RegistrationForm
    }

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            new_user = authenticate(
                username = register_form.cleaned_data['username'],
                password = register_form.cleaned_data['password1']
            )
            new_profile = Profile.objects.create(
                user = new_user,
                full_name = new_user.username
            )
            login(request, new_user)

            return redirect("profile_view",username=new_user.username)
        elif register_form.errors:
            context["error"] = "Please enter valid a name and password."
    
    return render(request, "user/register.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home-base")

def login_view(request):
    context = {
        "login_form" : LoginForm
    }

    if request.user.is_authenticated:
        return redirect("home-base")

    if request.method == "POST":
        login_form = LoginForm(data = request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            print(user.username)
            return redirect("profile_view",username=user.username)
        elif login_form.errors:
            context["error"] = "Invalid Username or Password."
    return render(request, "user/login.html", context)

def profile_view(request, username):
    user = User.objects.get(username = username)
    context = {
        "profile" : Profile.objects.get(user = user)
    }
    return render(request, "user/profile.html", context)

#Lainnya

def home(request):
    '''get all post'''
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

class PostListView(ListView): # pylint: disable=too-many-ancestors
    '''method docstring here'''
    #<app>/<model>_<viewtype>.html
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): # pylint: disable=too-many-ancestors
    '''method docstring here'''
    model = Post

class PostCreateView(CreateView): # pylint: disable=too-many-ancestors
    '''method docstring here'''
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    '''method docstring here'''
    return render(request, 'blog/about.html', {'title': 'About'})
