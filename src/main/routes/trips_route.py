from flask import Blueprint, jsonify, request
from src.controller.activity_controller import ActivityController
from src.controller.link_controller import LinkController
from src.controller.participant_controller import ParticipantController
from src.controller.trip_controller import TripController
from src.model.repository.activity_repository import ActivityRepository
from src.model.repository.link_repository import LinkRepository
from src.model.repository.participant_repository import ParticipantRepository
from src.model.repository.trip_repository import TripRepository
from src.model.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trips_routes", __name__)


@trips_routes_bp.route("/trips", methods=["POST"])
def trip_create():
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    trip_controller = TripController(trip_repository)
    response = trip_controller.create(request.json)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def trip_find_by_id(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    trip_controller = TripController(trip_repository)
    response = trip_controller.find_by_id(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["PATCH"])
def trip_confirm(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    trip_controller = TripController(trip_repository)
    response = trip_controller.confirm(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
def link_create(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    trip_repository = TripRepository(conn)
    link_controller = LinkController(link_repository, trip_repository)
    response = link_controller.create(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/links", methods=["GET"])
def link_list_by_trip_id(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    trip_repository = TripRepository(conn)
    link_controller = LinkController(link_repository, trip_repository)
    response = link_controller.list_by_trip_id(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/participants", methods=["POST"])
def participant_create(trip_id):
    conn = db_connection_handler.get_connection()
    ptcp_repository = ParticipantRepository(conn)
    trip_repository = TripRepository(conn)
    ptcp_controller = ParticipantController(ptcp_repository, trip_repository)
    response = ptcp_controller.create(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/participants", methods=["GET"])
def participant_list_by_trip_id(trip_id):
    conn = db_connection_handler.get_connection()
    ptcp_repository = ParticipantRepository(conn)
    trip_repository = TripRepository(conn)
    ptcp_controller = ParticipantController(ptcp_repository, trip_repository)
    response = ptcp_controller.list_by_trip_id(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/activities", methods=["POST"])
def activity_create(trip_id):
    conn = db_connection_handler.get_connection()
    actv_repository = ActivityRepository(conn)
    trip_repository = TripRepository(conn)
    actv_controller = ActivityController(actv_repository, trip_repository)
    response = actv_controller.create(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<trip_id>/activities", methods=["GET"])
def activity_list_by_trip_id(trip_id):
    conn = db_connection_handler.get_connection()
    actv_repository = ActivityRepository(conn)
    trip_repository = TripRepository(conn)
    actv_controller = ActivityController(actv_repository, trip_repository)
    response = actv_controller.list_by_trip_id(trip_id)
    return jsonify(response["body"]), response["status_code"]
