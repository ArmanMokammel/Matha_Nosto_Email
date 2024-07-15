from django.contrib import admin
from .models import Email_Template, Document_File

# Register your models here.
@admin.register(Email_Template) 
class Email_Template(admin.ModelAdmin):
  list_display = [
    'id',
    'subject',
    'contains_attachment',
    'timestamp'
  ]

@admin.register(Document_File) 
class Document_File(admin.ModelAdmin):
  list_display = [
    'id',
    'email_template',
    'document'
  ]


