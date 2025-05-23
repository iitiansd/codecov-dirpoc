import unittest
from services.email_service.app import EmailService

class TestEmailService(unittest.TestCase):
    def setUp(self):
        self.service = EmailService("noreply@example.com")

    def test_send_email_success(self):
        result = self.service.send_email("user@example.com", "Welcome", "Hello!")
        self.assertEqual(result["from"], "noreply@example.com")
        self.assertEqual(result["to"], "user@example.com")
        self.assertEqual(result["status"], "sent")
