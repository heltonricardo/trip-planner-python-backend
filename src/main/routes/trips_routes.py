from flask import jsonify, Blueprint, request
from src.controllers.trip_create import TripCreate
from src.controllers.trip_find_by_id import TripFindById
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_repository import EmailsRepository
from src.models.settings.db_connection_handler import db_connection_handler


trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsRepository(conn)
    controller = TripCreate(trips_repository, emails_repository)
    response = controller.create_trip(request.json)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip_by_id(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFindById(trips_repository)
    response = controller.find_trip_by_id(trip_id)
    return jsonify(response["body"]), response["status_code"]
