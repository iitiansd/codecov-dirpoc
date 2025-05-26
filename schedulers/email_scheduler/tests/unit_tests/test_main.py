import unittest
from schedulers.email_scheduler.main import EmailJob

class TestEmailJob(unittest.TestCase):
    def test_get_metadata_fields(self):
        job = EmailJob("user@example.com", "Monthly Report")
        metadata = job.get_metadata()
        self.assertEqual(metadata["recipient"], "user@example.com")
        self.assertEqual(metadata["subject"], "Monthly Report")
        self.assertIn("created_at", metadata)
