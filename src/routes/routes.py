import json
from flask import Blueprint
from src.composers.export_registration_composer import export_registration_composer


# Apelidando o @app para @route_bp
route_bp = Blueprint("routes", __name__)

@route_bp.route('/', methods=['POST'])
def index():
    response = export_registration_composer()
    response.body['presentation'] = json.loads(response.body['presentation'])
    return response.body, response.status_code
