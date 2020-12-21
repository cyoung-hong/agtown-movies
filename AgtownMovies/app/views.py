from django.shortcuts import render
from django.views.generic import ListView

from .models import User

# Create your views here.

class UserList(ListView):
    model = User