from django.shortcuts import render, redirect
from django.http import request
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login



def loginView(request):
    username = request.POST["username"] 
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if not request.user.is_authenticated:
        return redirect('login')

    if user is not None:
        login(request, user)
        
    else:
         return render(request, 'registration/index.html')
        

def signupView(request):
    username = request.POST["username"]
    password = request.POST["password"]

    

def logoutView(request):
    pass

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
     