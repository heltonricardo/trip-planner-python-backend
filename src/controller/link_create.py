import uuid


class LinkCreate:
    def __init__(self, link_repository, trip_repository) -> None:
        self.__link_repository = link_repository
        self.__trip_repository = trip_repository

    def link_create(self, body, trip_id) -> dict:
        try:
            trip = self.__trip_repository.trip_find_by_id(trip_id)
            if not trip:
                raise Exception("No trips found",  404)
            id = str(uuid.uuid4())
            link_info = {"id": id, "trip_id": trip_id, **body}
            self.__link_repository.create_link(link_info)
            return {"body": {"id": id}, "status_code": 201}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
