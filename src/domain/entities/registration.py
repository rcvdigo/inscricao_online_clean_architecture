from datetime import date
from src.domain.entities.value_objects.email import Email
from src.domain.entities.value_objects.cpf import Cpf


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
    def name(self) -> str:
        return self.__name
    
    @property
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def email(self) -> Email:
        return self.__email
    
    @property
    def email(self, value: Email) -> None:
        self.__email = value

    @property
    def registration_number(self) -> Cpf:
        return self.__registration_number
    
    @property
    def registration_number(self, value: Cpf) -> None:
        self.__registration_number = value

    @property
    def registration_at(self) -> str:
        return self.__registration_at
    
    @property
    def registration_at(self, value: str) -> None:
        self.__registration_at = value

    @property
    def birth_date(self) -> str:
        return self.__birth_date
    
    @property
    def birth_date(self, value: str) -> None:
        self.__birth_date = value
