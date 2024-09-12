class LinkFindByTripId:
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def find_links_by_trip_id(self, trip_id):
        try:
            search = self.__links_repository.find_links_by_trip_id(trip_id)
            if not search:
                raise Exception(f"No links found for trip_id {trip_id}",  404)
            links = [
                {
                    "id": link[0],
                    "url": link[2],
                    "title": link[3]
                }
                for link in search
            ]
            return {
                "status_code": 200,
                "body": {"links": links},
            }
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {
                    "error": "Bad Request",
                    "message": exception.args[0] or "Unknown error"
                },
            }
