from flask import Blueprint, jsonify
from src.controller.participant_controller import ParticipantController
from src.model.repository.participant_repository import ParticipantRepository
from src.model.repository.trip_repository import TripRepository
from src.model.settings.db_connection_handler import db_connection_handler

ptcps_routes_bp = Blueprint("participants_routes", __name__)


@ptcps_routes_bp.route("/participants/<ptcp_id>/confirm", methods=["GET"])
def participant_confirm(ptcp_id):
    conn = db_connection_handler.get_connection()
    ptcp_repository = ParticipantRepository(conn)
    trip_repository = TripRepository(conn)
    ptcp_controller = ParticipantController(ptcp_repository, trip_repository)
    response = ptcp_controller.confirm(ptcp_id)
    return jsonify(response["body"]), response["status_code"]
