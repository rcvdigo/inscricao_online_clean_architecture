from abc import ABC
from abc import abstractmethod
from src.domain.entities.registration import Registration

class ExportRegistrationPdfExporter(ABC):

    @abstractmethod
    def generate(self,
                 registration: Registration
                 ) -> bytes:
        pass
