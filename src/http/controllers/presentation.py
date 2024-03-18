from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Dict


class Presentation(ABC):
    @abstractmethod
    def output(self, data: List[Dict[str, str]]) -> str:
        pass