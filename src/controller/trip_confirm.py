class TripConfirm:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository

    def trip_confirm(self, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("No trip found",  404)
            self.__trip_repository.confirm_trip(trip_id)
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "status_code": exception.args[1] or 400,
                "body": {"error": exception.args[0] or "Unknown error"},
            }
