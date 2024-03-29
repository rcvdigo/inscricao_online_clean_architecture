import os
from .input_boundary import InputBoundary
from .output_boundary import OutputBoundary

# Class Imports Domain
from src.domain.value_objects.cpf import Cpf
from src.domain.repositories.load_registration_repository import LoadRegistrationRepository

# Class Imports Application/Contracts
from src.application.contracts.export_registration_pdf_exporter import ExportRegistrationPdfExporter
from src.application.contracts.storage import Storage


class ExportRegistration:

    def __init__(self,
                 repository: LoadRegistrationRepository,
                 pdf_exporter: ExportRegistrationPdfExporter,
                 storage: Storage) -> None:
        self.__repository = repository
        self.__pdf_exporter = pdf_exporter
        self.__storage = storage

    def handle(self, input: InputBoundary) -> OutputBoundary:
        cpf = Cpf(input.registration_number)

        registration = self.__repository.load_registration_number(
            cpf=cpf
        )

        file_content = self.__pdf_exporter.generate(
            registration=registration
        )

        self.__storage.store(
            file_name=input.pdf_file_name,
            path=input.path,
            content=file_content
        )
        
        full_file_name = os.path.join(input.path, input.pdf_file_name)
        return OutputBoundary(full_file_name)
