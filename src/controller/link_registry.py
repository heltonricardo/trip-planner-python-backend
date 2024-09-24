import uuid


class LinkRegistry:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def link_registry(self, trip_id, body) -> dict:
        try:
            id = str(uuid.uuid4())
            link_info = {"id": id, "trip_id": trip_id, **body}
            self.__link_repository.registry_link(link_info)
            return {"body": {"id": id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
