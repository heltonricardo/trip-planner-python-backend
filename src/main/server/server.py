from flask import Flask
from src.main.routes.trips_route import trips_routes_bp
from src.main.routes.participants_route import ptcps_routes_bp


app = Flask(__name__)
app.register_blueprint(trips_routes_bp)
app.register_blueprint(ptcps_routes_bp)
