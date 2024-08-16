from django.db import models

# Create your models here.
class Email_Template(models.Model):
  subject = models.CharField(null=False, blank=False, max_length=150)
  description = models.TextField(null=True, blank=True)
  contains_attachment = models.BooleanField(null=False, blank=False, default=False)
  timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  external_links=models.JSONField(null=True, blank=True, default=dict) 
  email_recipients=models.JSONField(null=True, blank=True, default=dict) 
  template_type = models.CharField(null=False, blank=False, max_length=60)

  class Meta:
    verbose_name = 'Email Template'
    
  def __str__(self):
    return str(self.pk)
  
# class Image_File(models.Model):
#   email_template = models.ForeignKey(Email_Template, null=False, blank=False, on_delete=models.CASCADE)
#   image = models.ImageField(null=False, blank=False, upload_to='EmailPictures/')
  
#   class Meta: 
#     verbose_name = 'Image File'
    
#   def __str__(self):
#     return str(self.pk)
  

class Document_File(models.Model): 
  email_template = models.ForeignKey(Email_Template, null=False, blank=False, on_delete=models.CASCADE)
  document = models.FileField(null=False, blank=False, upload_to='EmailDocuments/')
  
  class Meta: 
    verbose_name = 'Attachment'
    
  def __str__(self):
    return str(self.pk)
