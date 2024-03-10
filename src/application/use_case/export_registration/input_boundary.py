class InputBoundary:
    def __init__(self,
                 registration_number: str,
                 pdf_file_name: str,
                 path: str) -> None:
        self.__registration_number = registration_number
        self.__pdf_file_name = pdf_file_name
        self.__path = path

    @property
    def registration_number(self) -> str:
        return self.__registration_number

    @property
    def pdf_file_name(self) -> str:
        return self.__pdf_file_name

    @property
    def path(self) -> str:
        return self.__path
