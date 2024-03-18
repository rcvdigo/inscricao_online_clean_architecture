from flask import Flask
from src.routes.routes import route_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(blueprint=route_bp)
