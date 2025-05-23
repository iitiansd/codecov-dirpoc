# services/reporting_service/tests/test_app.py
import unittest
from services.reporting_service.app import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ReportGenerator("TestService")

    def test_generate_summary_report_with_data(self):
        data = [10, 20, 30, 40]
        expected_summary = {
            "status": "success",
            "service": "TestService",
            "total_items": 4,
            "sum": 100,
            "average": 25.0
        }
        self.assertEqual(self.generator.generate_summary_report(data), expected_summary)

    def test_generate_summary_report_empty_data(self):
        data = []
        expected_summary = {"status": "success", "summary": "No data to process."}
        self.assertEqual(self.generator.generate_summary_report(data), expected_summary)

    def test_generate_detailed_report_with_data(self):
        data = [{"item": "A"}, {"item": "B"}]
        expected_detailed = [
            {"item": "A", "report_status": "processed", "report_id": "REPORT-1"},
            {"item": "B", "report_status": "processed", "report_id": "REPORT-2"}
        ]
        self.assertEqual(self.generator.generate_detailed_report(data), expected_detailed)

    def test_generate_detailed_report_empty_data(self):
        data = []
        expected_detailed = []
        self.assertEqual(self.generator.generate_detailed_report(data), expected_detailed)