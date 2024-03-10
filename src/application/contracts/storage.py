from abc import ABC
from abc import abstractmethod
from typing import Any


class Storage(ABC):
    @abstractmethod
    def store(self,
              file_name: str,
              path: str,
              content: str
              ) -> Any:
        pass
