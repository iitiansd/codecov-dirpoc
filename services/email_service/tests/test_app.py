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

    def test_format_subject(self):
        result = self.service.format_subject("Your invoice")
        self.assertEqual(result, "[Notification] Your invoice")

    def test_validate_recipient_valid(self):
        self.assertTrue(self.service.validate_recipient("user@example.com"))

    def test_validate_recipient_invalid(self):
        self.assertFalse(self.service.validate_recipient("userexample.com"))
        self.assertFalse(self.service.validate_recipient("user@com"))

    def test_count_words(self):
        self.assertEqual(self.service.count_words("Hello there!"), 2)
        self.assertEqual(self.service.count_words("  This is a test email. "), 5)

    def test_send(self):
        result = self.service.send("user@example.com", "Welcome")
        assert "Email sent" in result