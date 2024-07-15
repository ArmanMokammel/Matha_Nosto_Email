from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from email_templater.models import Email_Template


# Create your views here.

# Create your views here.
def login_page(request):
  if request.method == 'POST':
       if request.POST.get('login_button'):
            username_ = request.POST.get('username')
            password_ = request.POST.get('password')

            print(username_)
            print(password_)

            user = auth.authenticate(username = username_, password=password_)
            if user is not None:
                 auth.login(request, user)
                 return redirect('note_book_user:dashboard')
            else: 
                 messages.error(request, 'Invalid credentials/User not registered.')
                 return redirect('note_book_user:login_page')
                 

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
     if request.POST.get('sign_up'):
              #clicked sign up button
              username_ = request.POST.get('username')
              password_ = request.POST.get('password')
              confirm_password_ = request.POST.get('confirm_password')

              if password_ == confirm_password_:
                      if User.objects.filter(username = username_).exists():
                           messages.warning(request, 'User already exist')
                           return redirect('note_book_user:signup')
                        
                      else:
                          user = User.objects.create_user(username = username_, password = password_)
                          user.save()
                          messages.success(request, "User created successfully")
                          return redirect('note_book_user:login_page')
              else: 
                  messages.error(request, "Password did not match")
                  return redirect('note_book_user:signup')
            
       
  return render(request, "signup.html")

@login_required
def logout(request):
     auth.logout(request)
     return redirect('note_book_user:login_page')