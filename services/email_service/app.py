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

    def format_subject(self, subject: str) -> str:
        """Prefix subject with tag."""
        return f"[Notification] {subject}"

    def validate_recipient(self, recipient: str) -> bool:
        """Very basic email validation."""
        return "@" in recipient and "." in recipient.split("@")[-1]

    def count_words(self, message: str) -> int:
        """Count the number of words in the email body."""
        return len(message.strip().split())