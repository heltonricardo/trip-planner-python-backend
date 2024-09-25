class LinkFindByTripId:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository

    def link_find_by_trip_id(self, trip_id):
        try:
            search = self.__link_repository.link_find_by_trip_id(trip_id)
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
