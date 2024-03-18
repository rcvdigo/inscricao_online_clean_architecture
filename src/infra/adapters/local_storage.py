import os
from typing import Any
from src.application.contracts.storage import Storage


class LocalStorage(Storage):

    def store(self,
              file_name: str,
              path: str,
              content: bytes
              ) -> Any:
        with open(os.path.join(path, file_name), 'wb') as file:
            file.write(content)
