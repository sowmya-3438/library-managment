from database import get_connection
from datetime import date, timedelta


def issue_book():

    print("\n ISSUE BOOK ")

    book_id = input("Enter book ID: ")
    user_id = input("Enter user ID: ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Check whether book exists
        cursor.execute(
            """
            SELECT book_id, book_name, available_quantity
            FROM books
            WHERE book_id = %s
            """,
            (book_id,)
        )

        book = cursor.fetchone()

        if book is None:
            print("Book not found.")
            return

        book_id_db, book_name, available_quantity = book

        # Check book availability
        if available_quantity <= 0:
            print("Book is not available.")
            return

        # Check whether user exists
        cursor.execute(
            """
            SELECT user_id, full_name, role
            FROM users
            WHERE user_id = %s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        if user is None:
            print("User not found.")
            return

        # Check if this user already has this book issued
        cursor.execute(
            """
            SELECT issue_id
            FROM book_issues
            WHERE book_id = %s
              AND user_id = %s
              AND issue_status <> 'Returned'
            """,
            (book_id, user_id)
        )

        existing_issue = cursor.fetchone()

        if existing_issue:
            print("This book is already issued to this user.")
            return

        # Dates
        issue_date = date.today()
        due_date = issue_date + timedelta(days=14)

        # Insert into book_issues
        query = """
            INSERT INTO book_issues
            (
                book_id,
                user_id,
                issue_date,
                due_date,
                issue_status
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                book_id,
                user_id,
                issue_date,
                due_date,
                "Issued"
            )
        )

        # Decrease available quantity
        cursor.execute(
            """
            UPDATE books
            SET available_quantity = available_quantity - 1
            WHERE book_id = %s
            AND available_quantity > 0
            """,
            (book_id,)
        )

        connection.commit()

        print("\nBook issued successfully.")
        print("Book       :", book_name)
        print("User       :", user[1])
        print("Issue Date :", issue_date)
        print("Due Date   :", due_date)

    except Exception as e:

        connection.rollback()

        print("Error issuing book:", e)

    finally:

        cursor.close()
        connection.close()
