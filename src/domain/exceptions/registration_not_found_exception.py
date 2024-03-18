from src.domain.value_objects.cpf import Cpf


class RegistrationNotFoundException(Exception):
    def __init__(self, cpf: Cpf):
        self.cpf = cpf
        super().__init__(f"CPF: {self.cpf} não encontrado na base de dados!")
