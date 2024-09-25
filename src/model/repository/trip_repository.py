from sqlite3 import Connection


class TripRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def trip_create(self, trip_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO trips (
                    id,
                    destination,
                    start_date,
                    end_date,
                    owner_name,
                    owner_email,
                    status
                )
                VALUES
                    (?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                trip_info["id"],
                trip_info["destination"],
                trip_info["start_date"],
                trip_info["end_date"],
                trip_info["owner_name"],
                trip_info["owner_email"],
                0,
            )
        )
        self.__conn.commit()

    def trip_find_by_id(self, trip_id: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM trips
                WHERE id = ?
            ''',
            (
                trip_id,
            )
        )
        trip = cursor.fetchone()
        return trip

    def confirm_trip(self, trip_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE trips
                    SET status = 1
                WHERE id = ?
            ''',
            (
                trip_id,
            )
        )
        self.__conn.commit()
