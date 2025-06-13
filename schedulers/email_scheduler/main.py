import datetime

class EmailJob:
    def __init__(self, recipient: str, subject: str):
        self.recipient = recipient
        self.subject = subject
        self.created_at = datetime.datetime.now()

    def get_metadata(self) -> dict:
        return {
            "recipient": self.recipient,
            "subject": self.subject,
            "created_at": self.created_at.isoformat()
        }
