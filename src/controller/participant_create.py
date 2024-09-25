import uuid


class ParticipantCreate:
    def __init__(self, trip_repository, participant_repository) -> None:
        self.__trip_repository = trip_repository
        self.__participant_repository = participant_repository

    def create_participant(self, body, trip_id) -> dict:
        try:
            trip = self.__trip_repository.trip_find_by_id(trip_id)
            if not trip:
                raise Exception("No trips found",  404)
            ptcp_id = str(uuid.uuid4())
            ptcp_info = {"id": ptcp_id, "trip_id": trip_id, **body}
            self.__participant_repository.create_participant(ptcp_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
