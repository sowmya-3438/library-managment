from database import get_connection


def add_user():

    print("\n ADD USER ")

    full_name = input("Enter full name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (Admin/Librarian/Member): ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO users
        (full_name, username, password, role, email, phone, age, gender)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:

        cursor.execute(
            query,
            (
                full_name,
                username,
                password,
                role,
                email,
                phone,
                age,
                gender
            )
        )

        connection.commit()

        print("User added successfully")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


def view_users():

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            user_id,
            full_name,
            username,
            role,
            email,
            phone,
            age,
            gender
        FROM users
    """

    cursor.execute(query)

    users = cursor.fetchall()

    if not users:
        print("No users found")

    else:

        print("\n USERS ")

        for user in users:

            
            print("ID:", user["user_id"])
            print("Name:", user["full_name"])
            print("Username:", user["username"])
            print("Role:", user["role"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
            print("Age:", user["age"])
            print("Gender:", user["gender"])

    cursor.close()
    connection.close()


def delete_user():

    print("\nDELETE USER")

    user_id = int(input("Enter user ID to delete: "))

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:
        # Check whether user exists
        cursor.execute(
            """
            SELECT user_id, username
            FROM users
            WHERE user_id = %s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        if user is None:
            print("User not found.")
            return

        # Check active/history issue records
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM book_issues
            WHERE user_id = %s
            """,
            (user_id,)
        )

        issue_count = cursor.fetchone()[0]

        if issue_count > 0:
            print("Cannot delete this user.")
            print("This user has book issue records.")
            return

        # Check fines
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM fines
            WHERE user_id = %s
            """,
            (user_id,)
        )

        fine_count = cursor.fetchone()[0]

        if fine_count > 0:
            print("Cannot delete this user.")
            print("This user has fine records.")
            return

        # Delete user
        cursor.execute(
            """
            DELETE FROM users
            WHERE user_id = %s
            """,
            (user_id,)
        )

        connection.commit()

        print("User deleted successfully.")

    except Exception as e:
        connection.rollback()
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
