import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()


def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    date = datetime.strptime("01-08-2024", "%d-%m-%Y")

    trips_infos = {
        "id": str(uuid.uuid4()),
        "destination": "Tokio",
        "start_date": date,
        "end_date": date + timedelta(days=5),
        "owner_name": "José das Coves",
        "owner_email": "jose@coves.com"
    }

    trips_repository.create_trip(trips_infos)
