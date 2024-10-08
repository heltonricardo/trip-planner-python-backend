from sqlite3 import Connection


class LinkRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create(self, link_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, url, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                link_info["id"],
                link_info["trip_id"],
                link_info["url"],
                link_info["title"],
            )
        )
        self.__conn.commit()

    def list_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT id, url, title
                FROM links
                WHERE trip_id = ?
            ''',
            (
                trip_id,
            )
        )
        links = cursor.fetchall()
        return links
