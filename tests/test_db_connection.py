from app.database.postgres import PostgresDB

db = PostgresDB()

connection = db.get_connection()

print("Database connection successful!")