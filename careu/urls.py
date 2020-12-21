from django.urls import path
from . import home_view, views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

#app_name = "careu"


urlpatterns = [
    path('', home_view.home, name='home-base'),
    path("login/", views.login_view, name = "login_view"),
    path("register/", views.register_view, name = "register_view"),
    path("logout/", views.logout_view, name = "logout_view"),
    path("profile/<str:username>/", views.profile_view, name = "profile_view"),

    path('team/', home_view.team, name='team-base'),
    path('journal/', home_view.journal, name='journal-base'),
    path('chat/', home_view.chat, name='chat-base'),

    path('post/', views.home, name = 'journal-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'journal-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'journal-create'),
]
