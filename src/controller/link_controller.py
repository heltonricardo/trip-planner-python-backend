import uuid

from src.model.repository.link_repository import LinkRepository
from src.model.repository.trip_repository import TripRepository


class LinkController:
    def __init__(
            self,
            link_repository: LinkRepository,
            trip_repository: TripRepository
    ) -> None:
        self.__link_repository = link_repository
        self.__trip_repository = trip_repository

    def create(self, body, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_by_id(trip_id)
            if not trip:
                raise Exception("No trips found",  404)
            id = str(uuid.uuid4())
            link_info = {"id": id, "trip_id": trip_id, **body}
            self.__link_repository.create(link_info)
            return {"body": {"id": id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }

    def list_by_trip_id(self, trip_id):
        try:
            search = self.__link_repository.list_by_trip_id(trip_id)
            if not search:
                raise Exception(f"No links found for trip_id {trip_id}",  404)
            links = [
                {
                    "id": link[0],
                    "url": link[1],
                    "title": link[2]
                }
                for link in search
            ]
            return {
                "status_code": 200,
                "body": links,
            }
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
