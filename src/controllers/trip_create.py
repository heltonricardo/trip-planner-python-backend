import uuid


class TripCreate:
    def __init__(self, trips_repository, participants_repository) -> None:
        self.__trips_repository = trips_repository
        self.__participants_repository = participants_repository

    def create_trip(self, body) -> dict:
        try:
            trip_id = str(uuid.uuid4())
            trip_info = {"id": trip_id, **body}
            self.__trips_repository.create_trip(trip_info)
            participants = body.get("participants") or []
            for participant in participants:
                participant_id = str(uuid.uuid4())
                self.__participants_repository.registry_participant({
                    "id": participant_id,
                    "name": participant["name"],
                    "email": participant["email"],
                    "trip_id": trip_id,
                })
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
