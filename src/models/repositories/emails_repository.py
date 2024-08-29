from sqlite3 import Connection


class EmailsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_email(self, email_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO emails
                    (id, trip_id, email)
                VALUES
                    (?, ?, ?)
            ''', (
                email_info["id"],
                email_info["trip_id"],
                email_info["email"],
            )
        )
        self.__conn.commit()

    def find_emails_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM emails
                WHERE trip_id = ?
            ''', (
                trip_id,
            )
        )
        emails = cursor.fetchall()
        return emails
