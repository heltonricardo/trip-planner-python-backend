import uuid

from src.model.repository.trip_repository import TripRepository


class TripController:
    def __init__(self, trip_repository: TripRepository) -> None:
        self.__trip_repository = trip_repository

    def create(self, body) -> dict:
        try:
            trip_id = str(uuid.uuid4())
            trip_info = {"id": trip_id, **body}
            self.__trip_repository.create(trip_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }

    def confirm(self, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_by_id(trip_id)
            if not trip:
                raise Exception("No trips found",  404)
            self.__trip_repository.confirm(trip_id)
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }

    def find_by_id(self, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_by_id(trip_id)
            if not trip:
                raise Exception("No trips found",  404)
            return {
                "status_code": 200,
                "body": {
                    "id": trip[0],
                    "destination": trip[1],
                    "start_date": trip[2],
                    "end_date": trip[3],
                    "owner_name": trip[4],
                    "owner_email": trip[5],
                    "status": trip[6],
                }
            }
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
