import uuid


class TripCreate:
    def __init__(self, trips_repository, emails_repository) -> None:
        self.__trips_repository = trips_repository
        self.__emails_repository = emails_repository

    def create_trip(self, body) -> dict:
        try:
            trip_id = str(uuid.uuid4())
            emails = body.get("emails") or []
            trip_info = {"id": trip_id, **body}
            self.__trips_repository.create_trip(trip_info)
            for email in emails:
                email_id = str(uuid.uuid4())
                self.__emails_repository.registry_email({
                    "id": email_id,
                    "trip_id": trip_id,
                    "email": email,
                })
            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
