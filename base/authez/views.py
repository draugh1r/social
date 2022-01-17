from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = 'authez/home.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'authez/register.html'