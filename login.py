from database import get_connection


def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            user_id,
            full_name,
            username,
            role
        FROM users
        WHERE username = %s
        AND password = %s
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:

        print("\nLogin successful")
        print("Welcome", user["full_name"])

        return user

    print("\nInvalid username or password")

    return None