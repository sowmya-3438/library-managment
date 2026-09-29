from database import get_connection


connection = get_connection()

if connection:
    print("MySQL connected successfully!")

    connection.close()
else:
    print("MySQL connection failed.")
