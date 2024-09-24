class TripFindById:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository

    def find_trip_by_id(self, trip_id) -> dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("No trip found",  404)
            return {
                "status_code": 200,
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "start_date": trip[2],
                        "end_date": trip[3],
                        "owner_name": trip[4],
                        "owner_email": trip[5],
                        "status": trip[6],
                    },
                },
            }
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {
                    "error": "Bad Request",
                    "message": exception.args[0] or "Unknown error"
                },
            }
