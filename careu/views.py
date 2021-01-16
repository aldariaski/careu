'''module for all logic here'''
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .forms import RegistrationForm, LoginForm
from .models import Post, Profile

#User view
def register_view(request):
    '''register logic'''
    if request.user.is_authenticated:
        return redirect('/')

    context = {
        "register_form" : RegistrationForm
    }

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid(): # pylint: disable=no-else-return
            register_form.save()
            new_user = authenticate(
                username = register_form.cleaned_data['username'],
                password = register_form.cleaned_data['password1']
            )
            new_profile = Profile.objects.create( # pylint: disable=unused-variable,no-member
                user = new_user,
                full_name = new_user.username
            )
            login(request, new_user)

            return redirect("profile_view",username=new_user.username)
        elif register_form.errors:
            context["error"] = register_form.errors
    return render(request, "user/register.html", context)

def validate_username(request):
    '''validate username input'''
    username = request.GET.get('username',None)
    data = {
		'is_exist': User.objects.filter(username__iexact=username).exists(),
        'length': len(username)
    }
    if data['length'] < 8:
        data['error_message'] = 'username too short, input atleast 8 Char'
    elif data['is_exist']:
        data['error_message'] = 'User with that username already exists'
    else:
        data['error_message'] = 'Username available'
    return JsonResponse(data)

def validate_password(request):
    '''validate password input'''
    password1 = request.GET.get('password1',None)
    password2 = request.GET.get('password2',None)
    data = {
		'is_match': password1 == password2,
        'length': len(password1)
    }
    if data['length'] < 8:
        data['error_message'] = 'password too short, input atleast 8 Char'
    elif data['is_match']:
        data['error_message'] = 'Password match'
    else:
        data['error_message'] = 'password do not match'
    return JsonResponse(data)

def logout_view(request):
    '''logout logic'''
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def login_view(request):
    '''login logic'''
    context = {
        "login_form" : LoginForm
    }

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        login_form = LoginForm(data = request.POST)
        if login_form.is_valid(): # pylint: disable=no-else-return
            user = login_form.get_user()
            login(request, user)
            return redirect("profile_view",username=user.username)
        elif login_form.errors:
            context["error"] = "Invalid Username or Password."
    return render(request, "user/login.html", context)

def profile_view(request, username):
    '''profile logic'''
    user = User.objects.get(username = username)
    context = {
        "profile" : Profile.objects.get(user = user) # pylint: disable=no-member
    }
    return render(request, "user/profile.html", context)

#Lainnya

def home(request):
    '''get all post'''
    context = {
        'posts': Post.objects.all() # pylint: disable=no-member
    }
    return render(request, 'home.html', context)

def get_all_post(request): # pylint: disable=unused-argument
    '''get all post'''
    all_post = Post.objects.all() # pylint: disable=no-member
    return HttpResponse(serializers.serialize('json', all_post),
        content_type= "text/json-comment-filtered"
)

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
