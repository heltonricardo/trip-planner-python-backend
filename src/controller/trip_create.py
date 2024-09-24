import uuid


class TripCreate:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def create_trip(self, body) -> dict:
        try:
            trip_id = str(uuid.uuid4())
            trip_info = {"id": trip_id, **body}
            self.__trip_repository.create_trip(trip_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
