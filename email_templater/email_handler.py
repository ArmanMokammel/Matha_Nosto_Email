from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from Matha_Nosto_Email import settings

class EmailHandler:

    def send_emails(request, email_template, attachments):
        merge_data = {
            'template': email_template,
            'attachments': attachments,
            'media_url': settings.MEDIA_URL,
            'host': request.META['HTTP_HOST']
        }
        html_body = render_to_string("email_template.html", merge_data)

        message = EmailMultiAlternatives(
        subject='Django HTML Email',
        # body="mail testing",
        from_email=settings.EMAIL_HOST_USER,
        to=['armanmokammel@gmail.com']
        )
        message.attach_alternative(html_body, "text/html")
        message.send(fail_silently=False)