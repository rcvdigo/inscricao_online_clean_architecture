import mysql.connector
from config.app import config
from src.domain.entities.registration import Registration
from src.domain.repositories.load_registration_repository import LoadRegistrationRepository
from src.domain.value_objects.cpf import Cpf
from src.domain.exceptions.registration_not_found_exception import RegistrationNotFoundException


class PdoRegistrationRepository(LoadRegistrationRepository):

    def __init__(self,
                 pdo: mysql.connector
                 ) -> None:
        self.__pdo = pdo
        self.__configdb = config()
        self.__conexao = self.__pdo.connect(
            host=self.__configdb['db']['host'],
            user=self.__configdb['db']['user'],
            password=self.__configdb['db']['password'],
            database=self.__configdb['db']['database']
        )
        self.__cursor = self.__conexao.cursor()

    def load_registration_number(self, cpf: Cpf) -> Registration:
        statement = "SELECT * FROM registrations WHERE registration_number = %s"
        self.__cursor.execute(statement, (str(cpf),))
        
        record = self.__cursor.fetchone()

        if not record:
            raise RegistrationNotFoundException(cpf)

        registration = Registration(
            name=record[0],
            email=record[1],
            registration_number=record[2],
            birth_date=record[3],
            registration_at=record[4]
        )
        
        self.__cursor.close()
        self.__conexao.close()
        return registration
