from rest_framework import serializers
from .models import Client, LegalRequest, DocumentAttachment

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class LegalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalRequest
        fields = '__all__'

class DocumentAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAttachment
        fields = '__all__'
