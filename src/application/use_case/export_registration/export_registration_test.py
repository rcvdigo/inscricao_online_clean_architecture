import os
import mysql.connector
from pathlib import Path
from .export_registration import ExportRegistration
from .input_boundary import InputBoundary
from src.infra.repositories.mysql.pdo_registration_repository import PdoRegistrationRepository
from src.infra.adapters.html2_pdf_adapter import Html2PdfAdapter

def test():

    path = Path(os.path.abspath('src'))

    # Use Cases
    load_registration_repository = PdoRegistrationRepository(pdo=mysql.connector)
    pdf_exporter = Html2PdfAdapter()
    # storage = Storage()

    export_registration_use_case = ExportRegistration(
        repository=load_registration_repository,
        pdf_exporter=pdf_exporter,
        storage=storage
    )

    input_boundary = InputBoundary(registration_number=40926288890,
                                pdf_file_name='xpto',
                                path=path.parent / 'storage')

    output = export_registration_use_case.handle(input=input_boundary)
