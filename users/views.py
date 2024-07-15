from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def dashboard(request):
    return render(request,"dashboard.html")

def create_email(request):
    return render(request,"create_email.html")
