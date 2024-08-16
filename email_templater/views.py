from django.shortcuts import redirect, render

from Matha_Nosto_Email import settings
from email_templater.email_handler import EmailHandler
from email_templater.models import Document_File, Email_Template

# Create your views here.

def create_email(request):
    if request.method == 'POST':
        if request.POST.get('submit_email'):
            title = request.POST.get('title')
            description = request.POST.get('description')
            template_type = request.POST.get('template_type')
         
         

            task_link_title = request.POST.get('task_link_title')
            task_link = request.POST.get('task_link')
            external_links = {}
            external_links[task_link_title] = task_link
            external_links[task_link_title+"_1"] = task_link
            email_recipients = {}
            if request.POST.getlist('email_addresses[]'):
                recipients = request.POST.getlist('email_addresses[]')
                for email_recipient in recipients:
                    email_recipients[email_recipient] = ""

            email_template = Email_Template.objects.create(subject=title, description=description, template_type=template_type, external_links=external_links, email_recipients=email_recipients )
           
            email_template.save()
           
            attachments = None
            email_attachments = []
            if request.FILES.get('attachments'):
                attachments = request.FILES.getlist('attachments')
                for attachment in attachments:
                    email_attachments.append(Document_File.objects.create(email_template=email_template, document=attachment))

            EmailHandler.send_emails(request, email_template, email_attachments)

            return redirect('users:dashboard')



    return render(request,"create_email.html")

def email_template(request, template_id):
   template = Email_Template.objects.get(id=template_id)
   attachments = Document_File.objects.filter(email_template=template)
   context = {
       "template": template,
       "attachments": attachments,
       "media_url": settings.MEDIA_URL
   }
   if template.template_type == 'event':
        return render(request, "email_template.html", context)
   elif template.template_type == 'task':
       return render(request, "task_template.html", context)
    

