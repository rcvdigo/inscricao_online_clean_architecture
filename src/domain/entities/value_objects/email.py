class Email:
    def __init__(self, email: str) -> None:
        if not self.__validate_email(email):
            raise Exception("E-mail Inválido!")
        self.email = email

    def __validate_email(self, email: str) -> bool:
        import re
        # Expressão regular para validar o formato do e-mail
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

    def __str__(self) -> str:
        return self.email
