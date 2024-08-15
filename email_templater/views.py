from django.shortcuts import redirect, render

from email_templater.models import Email_Template

# Create your views here.

def create_email(request):
    if request.method == 'POST':
        if request.POST.get('submit_email'):
            title = request.POST.get('title')
            description = request.POST.get('description')

            email_template = Email_Template.objects.create(subject=title, description=description)
            email_template.save()

            return redirect('email_templater:email_template')



    return render(request,"create_email.html")

def email_template(request):
   

    return render(request, "email_template.html")

def task_template(request):
   

    return render(request, "task_template.html")

