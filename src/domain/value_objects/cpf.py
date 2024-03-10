import re


class Cpf:
    def __init__(self, cpf: str) -> None:
        if not self.__validate_cpf(cpf):
            raise Exception("Cpf inválido!!!")
        self.cpf = cpf

    def __validate_cpf(self, cpf: str) -> bool:
        # Remove caracteres não numéricos do CPF
        cpf = re.sub(r'[^0-9]', '', cpf)

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        if resto < 2:
            digito_verificador1 = 0
        else:
            digito_verificador1 = 11 - resto

        # Verifica o primeiro dígito verificador
        if int(cpf[9]) != digito_verificador1:
            return False

        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        if resto < 2:
            digito_verificador2 = 0
        else:
            digito_verificador2 = 11 - resto

        # Verifica o segundo dígito verificador
        if int(cpf[10]) != digito_verificador2:
            return False
        
        return True

    def __str__(self) -> str:
        return re.sub(r'[^0-9]', '', self.cpf)
