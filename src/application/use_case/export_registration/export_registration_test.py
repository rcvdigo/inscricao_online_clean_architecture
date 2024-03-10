import os
from pathlib import Path
from datetime import date
from .export_registration import ExportRegistration
from src.application.use_case.export_registration.input_boundary import InputBoundary
from src.domain.repositories.load_registration_repository import LoadRegistrationRepository
from src.application.contracts.export_registration_pdf_exporter import PdfExporter
from src.application.contracts.storage import Storage
from src.domain.value_objects.cpf import Cpf
from src.domain.entities.registration import Registration


# class MockUseCase(LoadRegistrationRepository):
    
#     def __init__(self) -> None:
#         pass

#     def load_registration_number(self, cpf: Cpf) -> Registration:
#         pass

def test():

    path = Path(os.path.abspath('src'))

    # Entities
    registration = Registration(
        name='Rodrigo',
        email='rcvdigo@gmail.com',
        birth_date=date.today(),
        registration_number='40926288890',
        registration_at=date.today()
    )

    # Use Cases
    load_registration_repository = LoadRegistrationRepository()
    pdf_exporter = PdfExporter()
    storage = Storage()

    export_registration_use_case = ExportRegistration(
        repository=load_registration_repository,
        pdf_exporter=pdf_exporter,
        storage=storage
    )

    input_boundary = InputBoundary(registration_number=40926288890,
                                pdf_file_name='xpto',
                                path=path.parent / 'storage')

    output = export_registration_use_case.handle(input=input_boundary)
