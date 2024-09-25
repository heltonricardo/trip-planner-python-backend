import uuid

from src.model.repository.activity_repository import ActivityRepository
from src.model.repository.trip_repository import TripRepository


class ActivityController:
    def __init__(
        self,
        activity_repository: ActivityRepository,
        trip_repository: TripRepository,
    ) -> None:
        self.__activity_repository = activity_repository
        self.__trip_repository = trip_repository

    def create(self, body, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_by_id(trip_id)
            if not trip:
                raise Exception("No trips found",  404)
            activity_id = str(uuid.uuid4())
            activity_info = {"id": activity_id, "trip_id": trip_id, **body}
            self.__activity_repository.create(activity_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
