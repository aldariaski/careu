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
        return redirect("")

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
    return redirect("")

def login_view(request):
    context = {
        "login_form" : LoginForm
    }

    if request.user.is_authenticated:
        return redirect("")

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

from .home_model import BadMentalHealth, Symptoms, CareUTeam

def homehome(request):
    '''to render home view with all object correspond'''
    data1 = BadMentalHealth("Bipolar Disorder","Mental Disorder that causes unusual shifts in mood",'careu/bipolar.png',Symptoms.bipolar_name1,Symptoms.bipolar_desc1) # pylint: disable=line-too-long
    data2 = BadMentalHealth("Stress","feeling of emotional or physical tension.",'careu/stress.png',Symptoms.stress_name1,Symptoms.stress_desc1) # pylint: disable=line-too-long
    data3 = BadMentalHealth("Anxiety","feeling of fear or apprehension about what's to come.",'careu/anxiety.png','Panic','feelings of danger, panic, or dread') # pylint: disable=line-too-long
    data4 = BadMentalHealth("dementia","deterioration in memory, thinking, behaviour and the ability to perform everyday activities.",'careu/dementia.png','Memory loss','Memory loss, which is usually noticed by a spouse or someone else') # pylint: disable=line-too-long
    data5 = BadMentalHealth("insomnia","have difficulty falling asleep, or staying asleep as long as desired.",'careu/insomnia.png','Tiredness','Daytime tiredness or sleepiness.') # pylint: disable=line-too-long
    data6 = BadMentalHealth("schizophrenia","extremely disordered thinking and behavior that impairs daily functioning.",'careu/schizophrenia.png','Hallucinations','These usually involve seeing or hearing things that don`t exist.') # pylint: disable=line-too-long
    data = [data1,data2,data3,data4,data5,data6]
    context = {
        'data': data,
        "username" : "Anonim" if not request.user.is_authenticated else request.user.username
    }
    return render(request, 'home2.html',context)

def team(request):
    '''team careu'''
    data1 = CareUTeam("M. Fauzi Ridwan", 1906351070, "https://www.linkedin.com/in/muhamad-fauzi-ridwan-199260172/", "careu/fauzi.png")
    data2 = CareUTeam("Kirene Naomi", 1906353473, "", "-")
    data3 = CareUTeam("Yusuf Fakhri", 1906351096, "https://www.linkedin.com/in/ysfakhrialdrian/", "-")
    data4 = CareUTeam("Jesika Avonia", 1906398686, "", "-")
    data = [data1,data2,data3,data4]
    context = {
        'data':data
    }
    return render(request, 'team.html', context)

def journal(request):
    '''journa'''
    return render(request, 'journal.html')

def chat(request):
    '''chat'''
    return render(request, 'chat.html')

