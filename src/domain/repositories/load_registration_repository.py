from abc import ABC
from abc import abstractmethod
from src.domain.value_objects.cpf import Cpf
from src.domain.entities.registration import Registration


class LoadRegistrationRepository(ABC):
   
    @abstractmethod
    def load_registration_number(self, cpf: Cpf) -> Registration:
        pass
