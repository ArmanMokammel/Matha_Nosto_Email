from django.urls import path

from email_templater import views

app_name = 'email_templater'

urlpatterns = [
    path('email/create_email/', views.create_email, name='create_email'),
]