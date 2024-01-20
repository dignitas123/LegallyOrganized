from django.urls import path
from .views import (
    ClientListCreateView,
    ClientDetailView,
    LegalRequestListCreateView,
    LegalRequestDetailView,
    DocumentAttachmentListCreateView,
    DocumentAttachmentDetailView,
)

urlpatterns = [
    # Client URLs
    path('api/clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('api/clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),

    # LegalRequest URLs
    path('api/legal-requests', LegalRequestListCreateView.as_view(), name='legal-request-list-create'),
    path('api/legal-requests/<int:pk>/', LegalRequestDetailView.as_view(), name='legal-request-detail'),

    # DocumentAttachment URLs
    path('api/document-attachments/', DocumentAttachmentListCreateView.as_view(), name='document-attachment-list-create'),
    path('api/document-attachments/<int:pk>/', DocumentAttachmentDetailView.as_view(), name='document-attachment-detail'),
]
