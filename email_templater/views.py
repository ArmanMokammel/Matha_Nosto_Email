from django.shortcuts import render

# Create your views here.

def create_email(request):
    return render(request,"create_email.html")
