from flask import jsonify, Blueprint, request
from src.controller.link_find_by_trip_id import LinkFindByTripId
from src.controller.link_registry import LinkRegistry
from src.controller.trip_confirm import TripConfirm
from src.controller.trip_create import TripCreate
from src.controller.trip_find_by_id import TripFindById
from src.model.repository.link_repository import LinkRepository
from src.model.repository.participant_repository import ParticipantRepository
from src.model.repository.trip_repository import TripRepository
from src.model.settings.db_connection_handler import db_connection_handler


trips_routes_bp = Blueprint("trip_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    participant_repository = ParticipantRepository(conn)
    controller = TripCreate(trip_repository, participant_repository)
    response = controller.create_trip(request.json)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip_by_id(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    controller = TripFindById(trip_repository)
    response = controller.find_trip_by_id(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["PATCH"])
def trip_confirm(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    controller = TripConfirm(trip_repository)
    response = controller.trip_confirm(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
def link_registry(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = LinkRepository(conn)
    controller = LinkRegistry(trip_repository)
    response = controller.link_registry(trip_id, request.json)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/links", methods=["GET"])
def find_links_by_trip_id(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = LinkRepository(conn)
    controller = LinkFindByTripId(trip_repository)
    response = controller.find_links_by_trip_id(trip_id)
    return jsonify(response["body"]), response["status_code"]
