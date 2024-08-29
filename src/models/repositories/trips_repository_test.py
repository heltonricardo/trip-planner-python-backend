import uuid
import pytest
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Interaction with DB")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    date = datetime.strptime("01-08-2024", "%d-%m-%Y")
    trips_infos = {
        "id": trip_id,
        "destination": "Tokio",
        "start_date": date.isoformat(),
        "end_date": (date + timedelta(days=5)).isoformat(),
        "owner_name": "José das Coves",
        "owner_email": "jose@coves.com"
    }
    trips_repository.create_trip(trips_infos)


@pytest.mark.skip(reason="Interaction with DB")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)


@pytest.mark.skip(reason="Interaction with DB")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_repository.confirm_trip(trip_id)
