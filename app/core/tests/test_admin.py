"""
Tests for the Django admin modifications.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):
    """Test the admin site."""

    def setUp(self):
        """Set up the test."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
                email='admin@example.com',
                password='testpass123',
        )
        self.client.force_login(self.admin_user)
