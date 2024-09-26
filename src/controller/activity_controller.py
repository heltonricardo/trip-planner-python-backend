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
                raise Exception(f"No trips found for trip_id {trip_id}", 404)
            activity_id = str(uuid.uuid4())
            activity_info = {"id": activity_id, "trip_id": trip_id, **body}
            self.__activity_repository.create(activity_info)
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }

    def list_by_trip_id(self, trip_id):
        try:
            search = self.__activity_repository.list_by_trip_id(trip_id)
            if not search:
                raise Exception(
                    f"No activities found for trip_id {trip_id}",
                    404
                )
            activities = [
                {
                    "id": activity[0],
                    "title": activity[1],
                    "occurs_at": activity[2],
                }
                for activity in search
            ]
            return {
                "status_code": 200,
                "body": activities,
            }
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
