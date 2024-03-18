import os
from pathlib import Path
from src.application.use_case.export_registration.input_boundary import InputBoundary
from src.application.use_case.export_registration.export_registration import ExportRegistration
from src.http.controllers.presentation import Presentation


class ExportRegistrationCommand():
    def __init__(self,
                 use_case: ExportRegistration) -> None:
        self.__use_case = use_case
    
    def handle(self,
               presentation: Presentation
               ) -> str:
        # Obter o caminho da pasta raiz do projeto.
        path = Path(os.path.abspath(''))

        input_boundary = InputBoundary(
            registration_number='40926288890',
            pdf_file_name='xpto-pdf-adapter.pdf',
            path=path / 'storage/registrations'
            )

        output = self.__use_case.handle(input=input_boundary)

        return presentation.output([
            {'fullFileName': output.get_full_file_name}
        ])