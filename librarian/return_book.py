from database import get_connection


def return_book():

    print("\nRETURN BOOK ")

    book_id = input("Enter book ID: ")
    user_id = input("Enter user ID: ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Check whether the book was issued
        cursor.execute("""
            SELECT *
            FROM issued_books
            WHERE book_id = %s AND user_id = %s
        """, (book_id, user_id))

        issued = cursor.fetchone()

        if issued is None:
            print("No issued book record found.")
            return

        # Add record to returned_books
        cursor.execute("""
            INSERT INTO returned_books
            (book_id, user_id)
            VALUES (%s, %s)
        """, (book_id, user_id))

        # Remove the book from issued_books
        cursor.execute("""
            DELETE FROM issued_books
            WHERE book_id = %s AND user_id = %s
        """, (book_id, user_id))

        connection.commit()

        print("Book returned successfully.")

    except Exception as e:
        connection.rollback()
        print("Error returning book:", e)

    finally:
        cursor.close()
        connection.close()
