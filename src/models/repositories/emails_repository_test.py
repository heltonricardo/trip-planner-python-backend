import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_repository import EmailsRepository


db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Interaction with DB")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_repository = EmailsRepository(conn)
    email_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "invite1@event.com",
    }
    emails_repository.registry_email(email_info)


@pytest.mark.skip(reason="Interaction with DB")
def test_find_emails_by_trip_id():
    conn = db_connection_handler.get_connection()
    emails_repository = EmailsRepository(conn)
    emails = emails_repository.find_emails_by_trip_id(trip_id)
    assert isinstance(emails, list)
    assert isinstance(emails[0], tuple)
