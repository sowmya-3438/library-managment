from database import get_connection


def return_book(user_id):

    print("\nRETURN BOOK")

    book_id = int(input("Enter book ID: "))

    print("User ID:", user_id)

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:
        # Find the active issue for this user and book
        cursor.execute(
            """
            SELECT issue_id, due_date
            FROM book_issues
            WHERE book_id = %s
              AND user_id = %s
              AND returned_date IS NULL
              AND issue_status = 'Issued'
            """,
            (book_id, user_id)
        )

        issue = cursor.fetchone()

        if issue is None:
            print("No active issue found for this book.")
            return

        issue_id = issue[0]
        due_date = issue[1]

        # Update issue record
        cursor.execute(
            """
            UPDATE book_issues
            SET
                returned_date = CURDATE(),
                issue_status = 'Returned'
            WHERE issue_id = %s
            """,
            (issue_id,)
        )

        # Increase available quantity
        cursor.execute(
            """
            UPDATE books
            SET available_quantity = available_quantity + 1
            WHERE book_id = %s
            """,
            (book_id,)
        )

        connection.commit()

        print("Book returned successfully.")
        print("Due date:", due_date)
        print("Returned date: Today")

    except Exception as e:
        connection.rollback()
        print("Error returning book:", e)

    finally:
        cursor.close()
        connection.close()
