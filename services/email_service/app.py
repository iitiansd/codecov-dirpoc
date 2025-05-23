class EmailService:
    def __init__(self, sender: str):
        self.sender = sender

    def send_email(self, recipient: str, subject: str, body: str) -> dict:
        """Simulate sending an email."""
        return {
            "from": self.sender,
            "to": recipient,
            "subject": subject,
            "status": "sent"
        }
