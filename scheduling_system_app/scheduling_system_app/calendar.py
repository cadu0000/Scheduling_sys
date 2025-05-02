import frappe
from frappe.desk.calendar import get_event_conditions

@frappe.whitelist()
def get_events(start, end, filters=None):
    try:
        conditions = get_event_conditions("Appointment", filters or {})
        
        events = frappe.db.sql(f"""
            SELECT
                name,
                start_date,
                end_date,
                client_name,
                status
            FROM `tabAppointment`
            WHERE (
                (start_date BETWEEN %(start)s AND %(end)s) OR
                (end_date BETWEEN %(start)s AND %(end)s) OR
                (start_date <= %(start)s AND end_date >= %(end)s)
            )
            {conditions}
            ORDER BY start_date
        """, {"start": start, "end": end}, as_dict=True)
        
        return events
        
    except Exception as e:
        frappe.log_error("Falha ao buscar eventos", str(e))
        return []