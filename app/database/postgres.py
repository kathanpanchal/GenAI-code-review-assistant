import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


class PostgresDB:

    def __init__(self):

        self.connection = psycopg2.connect(
            host="localhost",
            database="genai_code_reviewer",
            user="postgres",
            password=os.getenv("POSTGRES_PASSWORD"),
            port="5432"
        )

    def get_connection(self):
        return self.connection