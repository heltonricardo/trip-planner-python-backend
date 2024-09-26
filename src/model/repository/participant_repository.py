from sqlite3 import Connection


class ParticipantRepository:

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create(self, participant_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO participants
                    (id, name, email, trip_id, is_confirmed)
                VALUES
                    (?, ?, ?, ?, ?)
            ''',
            (
                participant_info["id"],
                participant_info["name"],
                participant_info["email"],
                participant_info["trip_id"],
                0,
            )
        )
        self.__conn.commit()

    def exists_by_id(self, participant_id: str) -> bool:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT id
                FROM participants
                WHERE id = ?
            ''',
            (
                participant_id,
            )
        )
        return cursor.fetchone() is not None

    def list_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT id, name, email, is_confirmed
                FROM participants
                WHERE trip_id = ?
            ''',
            (
                trip_id,
            )
        )
        return cursor.fetchall()

    def confirm(self, participant_id) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                SET is_confirmed = 1
                WHERE id = ?
            ''',
            (
                participant_id,
            )
        )
        self.__conn.commit()
