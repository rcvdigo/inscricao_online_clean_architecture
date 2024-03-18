# Representando os dados de resposta
class Response:

    def __init__(
            self,
            body,
            headers,
            status_code,
        ) -> None:
        self.headers=headers
        self.status_code=status_code
        self.body=body
