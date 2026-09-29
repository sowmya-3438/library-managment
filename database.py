import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="library_management"
        )

        return connection

    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None
