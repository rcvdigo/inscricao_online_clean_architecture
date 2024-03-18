class OutputBoundary:
    def __init__(self, full_file_name: str):
        self.__full_file_name = full_file_name

    @property
    def get_full_file_name(self) -> str:
        return self.__full_file_name

    # def __init__(self, values):
    #     self.__name = values.get('name', '')
    #     self.__email = values.get('email', '')
    #     self.__birth_date = values.get('birth_date', '')
    #     self.__registration_number = values.get('registration_number', '')
    #     self.__registration_at = values.get('registration_at', '')
        
    # @property
    # def name(self) -> str:
    #     return self.__name

    # @property
    # def email(self) -> str:
    #     return self.__email

    # @property
    # def birth_date(self) -> str:
    #     return self.__birth_date

    # @property
    # def registration_number(self) -> str:
    #     return self.__registration_number

    # @property
    # def registration_at(self) -> str:
    #     return self.__registration_at
