from datetime import date
from src.domain.value_objects.email import Email
from src.domain.value_objects.cpf import Cpf


class Registration:
    def __init__(self,
                 name: str,
                 email: Email,
                 birth_date: date,
                 registration_number: Cpf,
                 registration_at: date
                 ) -> None:
        self.__name = name
        self.__email = email
        self.__registration_number = registration_number
        self.__registration_at = registration_at
        self.__birth_date = birth_date

    @property
    def get_name(self) -> str:
        return self.__name
    
    @property
    def set_name(self, value: str) -> None:
        self.__name = value

    @property
    def get_email(self) -> Email:
        return self.__email
    
    @property
    def set_email(self, value: Email) -> None:
        self.__email = value

    @property
    def get_registration_number(self) -> Cpf:
        return self.__registration_number
    
    @property
    def set_registration_number(self, value: Cpf) -> None:
        self.__registration_number = value

    @property
    def get_registration_at(self) -> str:
        return self.__registration_at
    
    @property
    def set_registration_at(self, value: str) -> None:
        self.__registration_at = value

    @property
    def get_birth_date(self) -> str:
        return self.__birth_date
    
    @property
    def set_birth_date(self, value: str) -> None:
        self.__birth_date = value
