import re
from scheduling_system_app.utils.errors import Errors

class FieldValidator:
    @staticmethod
    def validate_email(email: str):
        rgx = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(rgx, email):
            raise Errors.invalid_field("Email address")

    @staticmethod
    def validate_brazilian_cellphone(phone: str):
        phone = re.sub(r'\D', '', phone)
        rgx = r'^(?:\+55)?\d{2}9\d{8}$'
        if not re.match(rgx, phone):
            raise Errors.invalid_field("Phone")

    @staticmethod
    def validate_required_field(value, field_name):
        if not value:
            raise Errors.required_field(field_name)
