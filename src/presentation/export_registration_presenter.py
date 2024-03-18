import json
from typing import Dict, List
from src.http.controllers.presentation import Presentation


class ExportRegistrationPresenter(Presentation):
    def __init__(self) -> None:
        super().__init__()

    def output(self, data: List[Dict[str, str]]) -> str:
        return json.dumps(data)
