from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Client, LegalRequest, DocumentAttachment
from .serializers import ClientSerializer, LegalRequestSerializer, DocumentAttachmentSerializer

# Client Views
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# LegalRequest Views
class LegalRequestListCreateView(generics.ListCreateAPIView):
    queryset = LegalRequest.objects.all()
    serializer_class = LegalRequestSerializer

class LegalRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalRequest.objects.all()
    serializer_class = LegalRequestSerializer

# DocumentAttachment Views
class DocumentAttachmentListCreateView(generics.ListCreateAPIView):
    queryset = DocumentAttachment.objects.all()
    serializer_class = DocumentAttachmentSerializer

class DocumentAttachmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentAttachment.objects.all()
    serializer_class = DocumentAttachmentSerializer
