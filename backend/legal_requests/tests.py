from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Client, LegalRequest, DocumentAttachment
from django.utils import timezone

class ClientModelTest(TestCase):
    def test_create_client(self):
        client = Client.objects.create(name="John Doe", email="john@example.com", phone="1234567890")
        self.assertEqual(client.name, "John Doe")
        self.assertEqual(client.email, "john@example.com")
        self.assertEqual(client.phone, "1234567890")

class LegalRequestModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="John Doe", email="john@example.com", phone="1234567890")

    def test_create_legal_request(self):
        legal_request = LegalRequest.objects.create(
            client=self.client,
            case_description="Test Case Description",
            case_type="Test Case Type",
            submission_date=timezone.now(),
            status="open"
        )
        self.assertEqual(legal_request.client, self.client)
        self.assertEqual(legal_request.case_description, "Test Case Description")
        self.assertEqual(legal_request.case_type, "Test Case Type")
        self.assertEqual(legal_request.status, "open")

from django.urls import reverse

class LegalRequestViewTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="John Doe", email="john@example.com", phone="1234567890")
        self.legal_request = LegalRequest.objects.create(
            client=self.client,
            case_description="Test Case Description",
            case_type="Test Case Type",
            submission_date=timezone.now(),
            status="open"
        )

    def test_view_legal_requests(self):
        response = self.client.get(reverse('legal_requests:view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Case Description")

    # Add more tests for POST requests, form submissions, etc.
