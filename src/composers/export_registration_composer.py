# Imports Dependences
import mysql.connector
from flask import request as FlaskRequest

# Imports Infra
from src.infra.adapters.local_storage import LocalStorage
from src.infra.adapters.report_lab_adapter import ReportLabAdapter
from src.infra.repositories.mysql.pdo_registration_repository import PdoRegistrationRepository

# Imports Application
from src.application.use_case.export_registration.export_registration import ExportRegistration
from src.application.contracts.response import Response
from src.application.contracts.request import Request

# Imports Presenters
from src.presentation.export_registration_presenter import ExportRegistrationPresenter

# Imports Controllers
from src.http.controllers.export_registration_controller import ExportRegistrationController


def export_registration_composer():
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
        request=Request(
            headers=FlaskRequest.headers,
            body=FlaskRequest.json,
            query_params=FlaskRequest.args,
            path_params=FlaskRequest.view_args,
            url=FlaskRequest.full_path
        ),
        response=Response,
        use_case=export_registration_use_case)

    # Presenters
    export_registration_presenter = ExportRegistrationPresenter()

    # Response
    response = export_registration_controller.handle(export_registration_presenter)
    return response
