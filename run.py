# pylint: disable=import-error
from src.server.server import app

if __name__ == "__main__":
    app.run(
        debug=False
        )
