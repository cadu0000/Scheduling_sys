# Copyright (c) 2025, Carlos Eduardo and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import throw
from scheduling_system_app.utils.scheduler import AppointmentScheduler

class Appointment(Document):
    def before_save(self):
        if not self.start_date or not self.duration or not self.seller:
            return

        try:
            scheduler = AppointmentScheduler(
                seller=self.seller,
                start=self.start_date,
                duration=self.duration,
                docname=self.name
            )

            self.end_date = scheduler.get_end_datetime()
            scheduler.has_conflict()
                
        except Exception as e:
            throw(f"Erro ao validar agendamento: {e}.")
