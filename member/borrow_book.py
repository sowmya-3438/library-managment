from database import get_connection


def borrow_book(user_id):

    print("\nBORROW BOOK")

    book_id = int(input("Enter book ID: "))
    print("User ID:", user_id)

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:
        # Check whether user exists
        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE user_id = %s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        if user is None:
            print("User not found.")
            return

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

        print("Book:", book[1])

        # Check availability
        if book[2] <= 0:
            print("Book is not available.")
            return

        # Check whether the user currently has this book
        cursor.execute(
            """
            SELECT issue_id
            FROM book_issues
            WHERE book_id = %s
              AND user_id = %s
              AND returned_date IS NULL
            """,
            (book_id, user_id)
        )

        already_issued = cursor.fetchone()

        if already_issued:
            print("You have already borrowed this book.")
            return

        # Create issue record
        cursor.execute(
            """
            INSERT INTO book_issues
            (
                book_id,
                user_id,
                issue_date,
                due_date,
                returned_date,
                issue_status
            )
            VALUES
            (
                %s,
                %s,
                CURDATE(),
                DATE_ADD(CURDATE(), INTERVAL 14 DAY),
                NULL,
                'Issued'
            )
            """,
            (book_id, user_id)
        )

        
        cursor.execute(
            """
            UPDATE books
            SET available_quantity = available_quantity - 1
            WHERE book_id = %s
            """,
            (book_id,)
        )

        connection.commit()

        print("Book borrowed successfully.")
        print("Due date: 14 days from today.")

    except Exception as e:
        connection.rollback()
        print("Error borrowing book:", e)

    finally:
        cursor.close()
        connection.close()
