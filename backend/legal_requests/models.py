from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class LegalRequest(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    case_description = models.TextField()
    case_type = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

class DocumentAttachment(models.Model):
    legal_request = models.ForeignKey(LegalRequest, related_name='attachments', on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
