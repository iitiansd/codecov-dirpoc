# services/reporting_service/app.py

class ReportGenerator:
    def __init__(self, service_name: str):
        self.service_name = service_name
        print(f"ReportGenerator initialized for {self.service_name}")

    def generate_summary_report(self, data: list[int]) -> dict:
        """Generates a summary report from a list of numerical data."""
        if not data:
            return {"status": "success", "summary": "No data to process."}

        total = sum(data)
        average = total / len(data)
        
        return {
            "status": "success",
            "service": self.service_name,
            "total_items": len(data),
            "sum": total,
            "average": round(average, 2)
        }

    def generate_detailed_report(self, data: list[dict]) -> list[dict]:
        """Generates a detailed report, adding a status to each item."""
        if not data:
            return []
        
        detailed_report = []
        for i, item in enumerate(data):
            item_copy = item.copy()
            item_copy['report_status'] = 'processed'
            item_copy['report_id'] = f"REPORT-{i+1}"
            detailed_report.append(item_copy)
        return detailed_report

    def get_report_metadata(self) -> dict:
        """Returns metadata about the report service."""
        return {
            "service": self.service_name,
            "author": "Analytics Team",
            "version": "1.0"
        }

# Example usage (usually this would be run by a web server or a task runner)
if __name__ == "__main__":
    generator = ReportGenerator("SalesReporting")
    sales_data = [100, 150, 200, 120, 180]
    summary = generator.generate_summary_report(sales_data)
    print("Summary Report:", summary)

    user_data = [{"user_id": 1, "name": "Alice"}, {"user_id": 2, "name": "Bob"}]
    detailed = generator.generate_detailed_report(user_data)
    print("Detailed Report:", detailed)