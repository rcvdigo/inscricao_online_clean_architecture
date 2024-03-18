import mysql.connector
from .export_registration_controller import ExportRegistrationController
from src.application.use_case.export_registration.export_registration import ExportRegistration
from src.infra.repositories.mysql.pdo_registration_repository import PdoRegistrationRepository
from src.infra.adapters.html2_pdf_adapter import Html2PdfAdapter
from src.infra.adapters.report_lab_adapter import ReportLabAdapter
from src.infra.adapters.local_storage import LocalStorage
from src.presentation.export_registration_presenter import ExportRegistrationPresenter
from src.application.contracts.request import Request
from src.application.contracts.response import Response
from src.infra.cli.commands.export_registration_command import ExportRegistrationCommand


def test():

    # Teste Da aplicação via API
    # Use Cases
    load_registration_repository = PdoRegistrationRepository(pdo=mysql.connector)

    # pdf_exporter = Html2PdfAdapter() # SUBSTITUINDO POR OUTRA BIBLIOTECA
    report_lab = ReportLabAdapter()
    storage = LocalStorage()

    export_registration_use_case = ExportRegistration(
        repository=load_registration_repository,
        pdf_exporter=report_lab,
        storage=storage
    )
    
    # Controllers
    export_registration_controller = ExportRegistrationController(
        request=Request,
        response=Response,
        use_case=export_registration_use_case)
    
    # Presenters
    export_registration_presenter = ExportRegistrationPresenter()

    # Response
    response = export_registration_controller.handle(export_registration_presenter)
    print(f"\n\n{response}\n")

    # Teste Da aplicação no CLI

    # Use Cases
    load_registration_repository = PdoRegistrationRepository(pdo=mysql.connector)

    # pdf_exporter = Html2PdfAdapter() # SUBSTITUINDO POR OUTRA BIBLIOTECA
    report_lab = ReportLabAdapter()
    storage = LocalStorage()

    export_registration_use_case = ExportRegistration(
        repository=load_registration_repository,
        pdf_exporter=report_lab,
        storage=storage
    )

    export_registration_command = ExportRegistrationCommand(use_case=export_registration_use_case)

    response = export_registration_command.handle(presentation=export_registration_presenter)
    print(f"\n{response}\n")
