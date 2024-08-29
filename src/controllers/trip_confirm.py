class TripConfirm:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository

    def trip_confirm(self, trip_id) -> dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("No trip found",  404)
            self.__trips_repository.confirm_trip(trip_id)
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {
                    "error": "Bad Request",
                    "message": exception.args[0] or "Unknown error"
                },
            }
