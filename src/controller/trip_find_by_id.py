class TripFindById:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def trip_find_by_id(self, trip_id) -> dict:
        try:
            trip = self.__trip_repository.trip_find_by_id(trip_id)
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
