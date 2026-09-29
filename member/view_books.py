from database import get_connection


def view_books():

    print("\n AVAILABLE BOOKS ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        query = """
            SELECT *
            FROM books
        """

        cursor.execute(query)

        books = cursor.fetchall()

        if not books:
            print("No books available.")
        else:
            print("\n BOOK LIST ")

            for book in books:
                print(book)

    except Exception as e:
        print("Error viewing books:", e)

    finally:
        cursor.close()
        connection.close()
