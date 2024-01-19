from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, LegalRequest, DocumentAttachment

admin.site.register(Client)
admin.site.register(LegalRequest)
admin.site.register(DocumentAttachment)
