import os
from pathlib import Path
from src.application.contracts.request import Request
from src.application.contracts.response import Response
from src.application.use_case.export_registration.export_registration import ExportRegistration
from src.application.use_case.export_registration.input_boundary import InputBoundary
from src.http.controllers.presentation import Presentation


class ExportRegistrationController():
    def __init__(self,
                 request: Request,
                 response: Response,
                 use_case: ExportRegistration
                 ) -> None:
        self.__request = request
        self.__response = response
        self.__use_case = use_case

    def handle(self, presentation: Presentation) -> Response:
        # Obter o caminho da pasta raiz do projeto.
        path = Path(os.path.abspath(''))

        input_boundary = InputBoundary(
            registration_number=self.__request.body['registration_number'],
            pdf_file_name=f'{self.__request.body['pdf_file_name']}.pdf',
            path=path / 'storage/registrations'
            )

        output = self.__use_case.handle(input=input_boundary)

        self.__request.body['presentation'] = presentation.output([
            {'fullFileName': output.get_full_file_name}
            ])

        self.__response.headers = self.__request.headers
        self.__response.body = self.__request.body
        self.__response.status_code = 200

        return self.__response
    