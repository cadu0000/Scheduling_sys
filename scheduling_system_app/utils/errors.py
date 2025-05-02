class Errors:
    @staticmethod
    def required_field(field_name: str) -> ValueError:
        return ValueError(f"É necessário preencher o campo {field_name}.")

    @staticmethod
    def invalid_field(field_name: str) -> ValueError:
        return ValueError(f"{field_name} inválido.")
    
    @staticmethod
    def invalid_schedule(seller_name: str) -> ValueError:
        return ValueError(f"O vendedor {seller_name} já possui um compromisso agendado nesse horário.")
