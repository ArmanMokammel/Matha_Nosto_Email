from django.urls import path

from email_templater import views

app_name = 'email_templater'

urlpatterns = [
    path('email/create_email/', views.create_email, name='create_email'),

    path('email/email_template/<int:template_id>', views.email_template, name='email_template'),
   
    
]