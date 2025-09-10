class Documentation:
    VALID = {"NOT_STARTED", "IN_PROGRESS", "COMPLETED"}

    def __init__(self, doc_id, title, link, status="NOT_STARTED"):
        self.doc_id = doc_id
        self.title = title
        self.link = link
        self.status = status.upper() if status else "NOT_STARTED"
        if status not in self.VALID:
            self.status = "NOT_STARTED"

    def to_dict(self):
        return {
                "doc_id": self.doc_id,
                "title": self.title,
                "link": self.link,
                "status": self.status
                }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
                data.get("doc_id", ""),
                data.get("title", ""),
                data.get("link", ""),
                data.get("status", "NOT_STARTED")
                )

    def update_status(self, status):
        status = status.upper()
        if status not in ["NOT_STARTED", "IN_PROGRESS", "COMPLETED"]:
            print("❌ Invalid status. Must be NOT_STARTED, IN_PROGRESS, or COMPLETED.")
            return
        self.status = status
        print(f"✅ Status updated to {self.status}")

    def __str__(self):
        return f"{self.title} ({self.status}) → {self.link}"
