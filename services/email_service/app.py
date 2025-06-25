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

    def extract_recipient_domain(self, recipient: str) -> str:
        """Return the domain part of an email address, e.g. 'example.com'."""
        if not self.validate_recipient(recipient):
            raise ValueError(f"Invalid recipient: {recipient!r}")
        # split only on the first "@"
        return recipient.split("@", 1)[1]