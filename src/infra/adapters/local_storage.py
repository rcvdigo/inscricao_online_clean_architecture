from src.application.contracts.storage import Storage
from typing import Any


class LocalStorage(Storage):

    def store(self,
              file_name: str,
              path: str,
              content: str
              ) -> Any:
        pass
