import os
from pathlib import Path
import mysql.connector
from pathlib import Path
from .export_registration import ExportRegistration
from .input_boundary import InputBoundary
from src.infra.repositories.mysql.pdo_registration_repository import PdoRegistrationRepository
from src.infra.adapters.html2_pdf_adapter import Html2PdfAdapter
from src.infra.adapters.local_storage import LocalStorage
from src.domain.entities.registration import Registration


# Class Mock
class MockRegistration(Registration):
    pass

# Data Mock
registration = MockRegistration(name='Ana Silva',
                        email='ana@example.com',
                        birth_date='1990-05-15',
                        registration_number='12345678901',
                        registration_at='2024-03-12 17:34:46')

def test():
    # Obter o caminho da pasta raiz do projeto.
    path = Path(os.path.abspath(''))
    full_path = path.joinpath('storage/registrations')

    # Use Cases
    load_registration_repository = PdoRegistrationRepository(pdo=mysql.connector)
    pdf_exporter = Html2PdfAdapter()
    storage = LocalStorage()
    
    # Content PDF in Bytes
    # content = pdf_exporter.generate(registration=registration)
    
    # # Create Archive PDF in storage/registrations/<archive>.pdf
    # storage.store(file_name='test.pdf',
    #               path=full_path,
    #               content=content)
    
    # regis = load_registration_repository.load_registration_number('123.456.789-10')
    
    # Composers
    # export_registration_use_case = ExportRegistration(
    #     repository=load_registration_repository,
    #     pdf_exporter=pdf_exporter,
    #     storage=storage
    # )

    # input_boundary = InputBoundary(registration_number=40926288890,
    #                             pdf_file_name='xpto',
    #                             path=path / 'storage')

    # output = export_registration_use_case.handle(input=input_boundary)
