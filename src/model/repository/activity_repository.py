from sqlite3 import Connection


class ActivityRepository:

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create(self, activity_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO activities
                    (id, title, occurs_at, trip_id)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (
                activity_info["id"],
                activity_info["title"],
                activity_info["occurs_at"],
                activity_info["trip_id"],
            )
        )
        self.__conn.commit()

    def list_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT id, title, occurs_at
                FROM activities
                WHERE trip_id = ?
            ''',
            (
                trip_id,
            )
        )
        return cursor.fetchall()
