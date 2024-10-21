from django.urls import path, include
from .views import loginView, signupView

urlpattern = [
    path("accounts/", include("django.contrib.auth.urls")),

    
]