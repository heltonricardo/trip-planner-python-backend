import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository


db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Interaction with DB")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    link_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "https://www.trivago.com/",
        "title": "Hotel",
    }
    links_repository.registry_link(link_info)


@pytest.mark.skip(reason="Interaction with DB")
def test_find_links_from_trip_id():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    links = links_repository.find_links_by_trip_id(trip_id)
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
