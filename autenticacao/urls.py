from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from autenticacao.forms import AuthenticationFormCustomizado

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=AuthenticationFormCustomizado), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
