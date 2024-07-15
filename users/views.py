from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from email_templater.models import Email_Template

# Create your views here.
def login(request):
  if request.method == 'POST':
       if request.POST.get('Log-in'):
            username_ = request.POST.get('username')
            password_ = request.POST.get('password')

            user = auth.authenticate(username = username_, password=password_)
            if user is not None:
                 auth.login(request, user)
                 return redirect('users:dashboard')
            else: 
                 messages.error(request, 'Invalid credentials/User not registered.')
                 return redirect('users:login')
                 

  return render(request, "login.html")

@login_required
def dashboard(request):
    email_templates = Email_Template.objects.all().order_by('-timestamp')
    context = {
        "email_templates" : email_templates
    }
    return render(request,"dashboard.html", context)


def signup(request):
  if request.method == "POST":
     print(request.POST)
     if request.POST.get('Sign-Up'):
          #clicked sign up button
          username_ = request.POST.get('username')
          password_ = request.POST.get('password')
          confirm_password_ = request.POST.get('confirm_password')

          if password_ == confirm_password_:
               if User.objects.filter(username = username_).exists():
                    messages.warning(request, 'User already exist')
                    return redirect('users:signup')
               
               else:
                    user = User.objects.create_user(username = username_, password = password_)
                    user.save()
                    messages.success(request, "User created successfully")
                    return redirect('users:login')
          else: 
               messages.error(request, "Password did not match")
               return redirect('users:signup')
            
       
  return render(request, "signup.html")

@login_required
def logout(request):
     auth.logout(request)
     return redirect('users:login')