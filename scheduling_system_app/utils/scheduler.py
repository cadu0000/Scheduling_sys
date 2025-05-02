from frappe.utils import get_datetime
from datetime import timedelta
import frappe
from scheduling_system_app.utils.errors import Errors

class AppointmentScheduler:
    def __init__(self, seller: str, start: str, duration: str, docname: str = None):
        self.seller = seller
        self.start = get_datetime(start)
        self.duration = self.parse_duration(duration)
        self.end = self.start + self.duration
        self.docname = docname  

    def parse_duration(self, duration_str: str) -> timedelta:
        parts = duration_str.strip().split(":")
        if not 1 <= len(parts) <= 3:
            raise Errors.invalid_field("duration")

        parts = [int(p) for p in parts]
        while len(parts) < 3:
            parts.append(0)

        return timedelta(hours=parts[0], minutes=parts[1], seconds=parts[2])

    def has_conflict(self):
        filters = {
            "seller": self.seller,
            "start_date": ["<", self.end],
            "end_date": [">", self.start],
        }
        if self.docname:
            filters["name"] = ["!=", self.docname]

        if bool(frappe.db.exists("Appointment", filters)):
            raise Errors.invalid_schedule(filters["seller"])

    def get_end_datetime(self) -> str:
        return self.end
