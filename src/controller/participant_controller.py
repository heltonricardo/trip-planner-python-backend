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
                raise Exception("No trips found",  404)
            ptcp_id = str(uuid.uuid4())
            ptcp_info = {"id": ptcp_id, "trip_id": trip_id, **body}
            self.__participant_repository.create(ptcp_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
