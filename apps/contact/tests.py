from unittest.mock import patch
from django.test import TestCase
from .models import Lead
class ContactTests(TestCase):
    @patch("apps.contact.tasks.notify_new_lead.delay")
    def test_lead_saved_and_notification_queued(self,delay):
        r=self.client.post("/contact/submit/",{"name":"Test User","email":"test@example.com","company":"Example","phone":"123","message":"Hello"})
        self.assertEqual(r.status_code,200)
        self.assertTrue(r.json()["success"])
        self.assertEqual(Lead.objects.count(),1)
        delay.assert_called_once()
    def test_invalid_contact_is_rejected(self):
        r=self.client.post("/contact/submit/",{"name":"","email":"bad","message":""})
        self.assertEqual(r.status_code,400)
        self.assertEqual(Lead.objects.count(),0)
