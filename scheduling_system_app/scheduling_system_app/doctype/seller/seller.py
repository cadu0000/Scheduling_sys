# Copyright (c) 2025, Carlos Eduardo and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from scheduling_system_app.utils.validators import FieldValidator

class Seller(Document):
    def before_save(self):
        try:
            FieldValidator.validate_email(self.email_address)
            FieldValidator.validate_required_field(self.email_address, "E-mail")
            FieldValidator.validate_required_field(self.phone, "Telefone")
            FieldValidator.validate_brazilian_cellphone(self.phone)
            
        except Exception as e:
            frappe.throw(f"Erro de validação: {e}")


			
			
