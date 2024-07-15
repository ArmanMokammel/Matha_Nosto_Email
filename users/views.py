from django.http import HttpResponse
from django.shortcuts import render

from email_templater.models import Email_Template

# Create your views here.

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def dashboard(request):
    email_templates = Email_Template.objects.all().order_by('-timestamp')
    context = {
        "email_templates" : email_templates
    }
    return render(request,"dashboard.html", context)

