from sqlite3 import Connection


class ParticipantsRepository:

    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT INTO participants
                    (id, name, email, trip_id)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (
                participant_info["id"],
                participant_info["name"],
                participant_info["email"],
                participant_info["trip_id"],
            )
        )
        self.__conn.commit()

    def find_participant_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT id, name, email, is_confirmed
                FROM participants
                WHERE trip_id = ?
            ''',
            (
                trip_id
            )
        )
        return cursor.fetchall()
