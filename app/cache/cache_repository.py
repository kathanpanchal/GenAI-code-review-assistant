import json

from app.database.postgres import PostgresDB


class CacheRepository:

    def __init__(self):

        self.db = PostgresDB()

        self.connection = self.db.get_connection()

    def get_review_by_hash(self,code_hash):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT review_json
            FROM review_cache
            WHERE code_hash = %s
            """,
            (code_hash,)
        )

        result = cursor.fetchone()

        cursor.close()

        if result:
            return result[0]

        return None
    def increment_hit_count(
        self,
        code_hash
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE review_cache
            SET
                hit_count = hit_count + 1,
                last_accessed = NOW()
            WHERE code_hash = %s
            """,
            (code_hash,)
        )

        self.connection.commit()

        cursor.close()
    def save_review(
        self,
        code_hash,
        review_json
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO review_cache
            (
                code_hash,
                review_json
            )
            VALUES
            (
                %s,
                %s
            )
            ON CONFLICT (code_hash)
            DO NOTHING
            """,
            (
                code_hash,
                json.dumps(review_json)
            )
        )

        self.connection.commit()

        cursor.close()
        