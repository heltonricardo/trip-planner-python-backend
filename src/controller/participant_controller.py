import uuid

from src.model.repository.participant_repository import ParticipantRepository
from src.model.repository.trip_repository import TripRepository


class ParticipantController:
    def __init__(
            self,
            participant_repository: ParticipantRepository,
            trip_repository: TripRepository,
    ) -> None:
        self.__participant_repository = participant_repository
        self.__trip_repository = trip_repository

    def create(self, body, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_by_id(trip_id)
            if not trip:
                raise Exception(f"No trips found for trip_id {trip_id}", 404)
            ptcp_id = str(uuid.uuid4())
            ptcp_info = {"id": ptcp_id, "trip_id": trip_id, **body}
            self.__participant_repository.create(ptcp_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }

    def confirm(self, ptcp_id) -> dict:
        try:
            exists = self.__participant_repository.exists_by_id(ptcp_id)
            if not exists:
                raise Exception(
                        f"No participants found for participant_id {ptcp_id}",
                        404
                    )
            self.__participant_repository.confirm(ptcp_id)
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }

    def list_by_trip_id(self, trip_id):
        try:
            search = self.__participant_repository.list_by_trip_id(trip_id)
            if not search:
                raise Exception(
                    f"No participants found for trip_id {trip_id}",
                    404
                )
            participants = [
                {
                    "id": participant[0],
                    "name": participant[1],
                    "email": participant[2],
                    "is_confirmed": participant[3],
                }
                for participant in search
            ]
            return {
                "status_code": 200,
                "body": participants,
            }
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
